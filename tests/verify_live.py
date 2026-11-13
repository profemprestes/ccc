"""
Empirical verification script for Envíos DosRuedas production environment.
Tests all assertions made in INFORME_AUDITORIA_ENVIOS_DOSRUEDAS.md against live https://www.enviosdosruedas.com/.
"""

import sys
import ssl
import socket
import json
import re
import hashlib
from datetime import datetime
import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener_noredirect = urllib.request.build_opener(NoRedirect)
opener_redirect = urllib.request.build_opener()

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def probe_url(url, follow_redirects=False):
    opener = opener_redirect if follow_redirects else opener_noredirect
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with opener.open(req, timeout=15) as resp:
            body = resp.read()
            return {
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers),
                "body_len": len(body),
                "body_sample": body[:1000].decode('utf-8', errors='replace'),
                "body_full": body
            }
    except urllib.error.HTTPError as e:
        body = e.read() if hasattr(e, 'read') else b""
        return {
            "url": url,
            "status": e.code,
            "headers": dict(e.headers),
            "body_len": len(body),
            "body_sample": body[:1000].decode('utf-8', errors='replace'),
            "body_full": body
        }
    except Exception as exc:
        return {
            "url": url,
            "status": None,
            "error": str(exc)
        }

def get_title_and_h1(html_bytes):
    text = html_bytes.decode('utf-8', errors='replace')
    title_match = re.search(r'<title[^>]*>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else None
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.IGNORECASE | re.DOTALL)
    if h1_match:
        # Strip internal tags
        h1_raw = h1_match.group(1)
        h1 = re.sub(r'<[^>]+>', ' ', h1_raw)
        h1 = re.sub(r'\s+', ' ', h1).strip()
    else:
        h1 = None
    return title, h1

def main():
    print("=" * 80)
    print("LIVE PRODUCTION EMPIRICAL VERIFICATION HARNESS")
    print("Target: https://www.enviosdosruedas.com/")
    print(f"Timestamp: {datetime.now(datetime.timezone.utc).isoformat()}")
    print("=" * 80)

    results = {}

    # 1. DNS & SSL verification
    print("\n--- 1. DNS & SSL / TLS VERIFICATION ---")
    hostname = "www.enviosdosruedas.com"
    apex = "enviosdosruedas.com"

    # DNS
    try:
        ip_list_www = socket.gethostbyname_ex(hostname)[2]
        print(f"DNS {hostname}: {ip_list_www}")
    except Exception as e:
        ip_list_www = str(e)
        print(f"DNS {hostname} Error: {e}")

    try:
        ip_list_apex = socket.gethostbyname_ex(apex)[2]
        print(f"DNS {apex}: {ip_list_apex}")
    except Exception as e:
        ip_list_apex = str(e)
        print(f"DNS {apex} Error: {e}")

    # SSL Cert
    ctx = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            tls_version = ssock.version()

    ssl_info = {
        "subject": cert.get("subject"),
        "issuer": cert.get("issuer"),
        "notBefore": cert.get("notBefore"),
        "notAfter": cert.get("notAfter"),
        "subjectAltName": cert.get("subjectAltName"),
        "cipher": cipher,
        "tls_version": tls_version
    }
    print(f"TLS Version: {tls_version}")
    print(f"Cipher: {cipher}")
    print(f"Issuer: {cert.get('issuer')}")
    print(f"Validity: {cert.get('notBefore')} -> {cert.get('notAfter')}")
    print(f"SANs: {cert.get('subjectAltName')}")
    results["ssl"] = ssl_info

    # 2. Key Target URLs (Requirement 1, 2, 3)
    print("\n--- 2. PROBING KEY TARGET URLS ---")
    urls_to_test = [
        "https://www.enviosdosruedas.com/terminos-y-condiciones/",
        "https://www.enviosdosruedas.com/terminos-y-condiciones",
        "https://www.enviosdosruedas.com/cobertura/",
        "https://www.enviosdosruedas.com/cobertura",
        "https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/",
        "https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata",
        "https://www.enviosdosruedas.com/servicios/",
        "https://www.enviosdosruedas.com/servicios",
        "https://www.enviosdosruedas.com/servicios/envios-flex/",
        "https://www.enviosdosruedas.com/servicios/envios-flex",
        "https://www.enviosdosruedas.com/servicios/enviosflex/",
        "https://www.enviosdosruedas.com/servicios/enviosflex",
        "https://www.enviosdosruedas.com/",
        "https://enviosdosruedas.com"
    ]

    url_results = {}
    for url in urls_to_test:
        raw_probe = probe_url(url, follow_redirects=False)
        followed_probe = probe_url(url, follow_redirects=True) if raw_probe.get("status") in (301, 302, 307, 308) else raw_probe
        
        title, h1 = (None, None)
        if followed_probe.get("body_full"):
            title, h1 = get_title_and_h1(followed_probe["body_full"])

        loc_header = raw_probe.get("headers", {}).get("Location") or raw_probe.get("headers", {}).get("location")
        server_header = raw_probe.get("headers", {}).get("Server") or raw_probe.get("headers", {}).get("server")
        x_vercel_id = raw_probe.get("headers", {}).get("X-Vercel-Id") or raw_probe.get("headers", {}).get("x-vercel-id")
        x_vercel_cache = raw_probe.get("headers", {}).get("X-Vercel-Cache") or raw_probe.get("headers", {}).get("x-vercel-cache")
        x_prerender = raw_probe.get("headers", {}).get("X-Nextjs-Prerender") or raw_probe.get("headers", {}).get("x-nextjs-prerender")

        info = {
            "initial_status": raw_probe.get("status"),
            "initial_location": loc_header,
            "final_status": followed_probe.get("status"),
            "content_length": followed_probe.get("body_len"),
            "title": title,
            "h1": h1,
            "server": server_header,
            "x_vercel_id": x_vercel_id,
            "x_vercel_cache": x_vercel_cache,
            "x_nextjs_prerender": x_prerender,
            "headers": raw_probe.get("headers")
        }
        url_results[url] = info
        print(f"URL: {url}")
        print(f"  Initial Status: {info['initial_status']} | Location: {info['initial_location']}")
        print(f"  Final Status: {info['final_status']} | Len: {info['content_length']} bytes")
        print(f"  Title: {info['title']}")
        print(f"  H1: {info['h1']}")
        print(f"  Vercel Id: {info['x_vercel_id']} | Cache: {info['x_vercel_cache']} | Prerender: {info['x_nextjs_prerender']}")

    results["urls"] = url_results

    # 3. Sitemap.xml Verification (Requirement 4)
    print("\n--- 3. SITEMAP.XML INSPECTION ---")
    sitemap_url = "https://www.enviosdosruedas.com/sitemap.xml"
    sm_probe = probe_url(sitemap_url, follow_redirects=True)
    print(f"Sitemap status: {sm_probe['status']}, len: {sm_probe['body_len']}")

    sitemap_entries = []
    if sm_probe.get("body_full"):
        try:
            root = ET.fromstring(sm_probe["body_full"])
            # namespaces
            ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for url_elem in root.findall('ns:url', ns):
                loc = url_elem.find('ns:loc', ns)
                if loc is not None and loc.text:
                    sitemap_entries.append(loc.text.strip())
        except Exception as e:
            print(f"Error parsing sitemap XML: {e}")

    print(f"Total entries in sitemap.xml: {len(sitemap_entries)}")
    sitemap_test_results = []
    for loc in sitemap_entries:
        probe = probe_url(loc, follow_redirects=False)
        has_slash = loc.endswith('/')
        status = probe.get("status")
        loc_header = probe.get("headers", {}).get("Location") or probe.get("headers", {}).get("location")
        sitemap_test_results.append({
            "loc": loc,
            "has_trailing_slash": has_slash,
            "status": status,
            "redirect_location": loc_header
        })
        print(f"  Loc: {loc} | TrailingSlash: {has_slash} | Status: {status} | Target: {loc_header}")

    results["sitemap"] = {
        "url": sitemap_url,
        "entry_count": len(sitemap_entries),
        "entries": sitemap_test_results
    }

    # 4. Check specific sitemap URLs mentioned in report:
    # /servicios/plan-emprendedores and /servicios/envios-contrareembolso
    print("\n--- 4. SPECIAL SITEMAP URL REDIRECTS ---")
    special_urls = [
        "https://www.enviosdosruedas.com/servicios/plan-emprendedores",
        "https://www.enviosdosruedas.com/servicios/plan-emprendedores/",
        "https://www.enviosdosruedas.com/servicios/envios-contrareembolso",
        "https://www.enviosdosruedas.com/servicios/envios-contrareembolso/"
    ]
    special_results = {}
    for su in special_urls:
        p_raw = probe_url(su, follow_redirects=False)
        p_fol = probe_url(su, follow_redirects=True)
        loc_h = p_raw.get("headers", {}).get("Location") or p_raw.get("headers", {}).get("location")
        special_results[su] = {
            "initial_status": p_raw.get("status"),
            "location": loc_h,
            "final_status": p_fol.get("status"),
            "final_len": p_fol.get("body_len")
        }
        print(f"Special: {su} -> Status {p_raw.get('status')} -> {loc_h} (Final: {p_fol.get('status')})")
    results["special_sitemap_urls"] = special_results

    # 5. Security Headers on Homepage
    print("\n--- 5. SECURITY HEADERS VERIFICATION ---")
    hp_headers = url_results.get("https://www.enviosdosruedas.com/", {}).get("headers", {})
    sec_headers = {
        "strict-transport-security": hp_headers.get("Strict-Transport-Security") or hp_headers.get("strict-transport-security"),
        "x-frame-options": hp_headers.get("X-Frame-Options") or hp_headers.get("x-frame-options"),
        "x-content-type-options": hp_headers.get("X-Content-Type-Options") or hp_headers.get("x-content-type-options"),
        "content-security-policy": hp_headers.get("Content-Security-Policy") or hp_headers.get("content-security-policy"),
        "server": hp_headers.get("Server") or hp_headers.get("server"),
        "x-vercel-cache": hp_headers.get("X-Vercel-Cache") or hp_headers.get("x-vercel-cache"),
        "x-nextjs-prerender": hp_headers.get("X-Nextjs-Prerender") or hp_headers.get("x-nextjs-prerender"),
    }
    for k, v in sec_headers.items():
        print(f"  {k}: {v}")
    results["security_headers"] = sec_headers

    # 6. Robots.txt
    print("\n--- 6. ROBOTS.TXT ---")
    robots_probe = probe_url("https://www.enviosdosruedas.com/robots.txt", follow_redirects=True)
    print(f"Robots status: {robots_probe['status']}")
    print(f"Robots content:\n{robots_probe.get('body_sample')}")
    results["robots_txt"] = robots_probe.get("body_sample")

    # 7. Compare local terminos-y-condiciones.html and logistica-dosruedas.html SHA-256
    print("\n--- 7. LOCAL FILE COMPARISON (TERMINOS VS LOGISTICA) ---")
    local_terminos_path = r"d:\repositorios\ccc\envios\terminos-y-condiciones.html"
    local_logistica_path = r"d:\repositorios\ccc\envios\logistica-dosruedas.html"

    def file_hash(p):
        h = hashlib.sha256()
        with open(p, "rb") as f:
            h.update(f.read())
        return h.hexdigest().upper()

    try:
        h_term = file_hash(local_terminos_path)
        h_logi = file_hash(local_logistica_path)
        print(f"Local terminos-y-condiciones.html SHA-256: {h_term}")
        print(f"Local logistica-dosruedas.html    SHA-256: {h_logi}")
        print(f"Binary identical? {h_term == h_logi}")
        results["local_hashes"] = {
            "terminos": h_term,
            "logistica": h_logi,
            "identical": h_term == h_logi
        }
    except Exception as e:
        print(f"Local file hash error: {e}")

    # Output JSON summary to stdout
    print("\n" + "=" * 80)
    print("EMPIRICAL TEST SUMMARY (JSON)")
    print("=" * 80)
    # Save test results to a temp/structured location or print
    clean_results = {}
    for k, v in results.items():
        if k == "urls":
            clean_urls = {}
            for u, uv in v.items():
                c_uv = dict(uv)
                c_uv.pop("headers", None) # drop verbose dict
                clean_urls[u] = c_uv
            clean_results[k] = clean_urls
        else:
            clean_results[k] = v
    print(json.dumps(clean_results, indent=2, default=str))

if __name__ == "__main__":
    main()

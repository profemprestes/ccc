import os
import sys
import re
import json
import ssl
import socket
import urllib.request
import urllib.parse
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

BASE_URL = "https://www.enviosdosruedas.com"
STATE_DIR = r"d:\repositorios\ccc\.agents\teamwork\explorer_survey_live"
REPO_ROOT = r"d:\repositorios\ccc"

# Disable proxy inside python by removing proxy env vars for local requests if needed
for k in ['http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)

def fetch_url(url, follow_redirects=True, timeout=15):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    
    chain = []
    current_url = url
    
    class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    if not follow_redirects:
        opener = urllib.request.build_opener(NoRedirectHandler)
    else:
        opener = urllib.request.build_opener()

    try:
        response = opener.open(req, timeout=timeout)
        content = response.read()
        return {
            'status': response.getcode(),
            'final_url': response.geturl(),
            'headers': dict(response.info()),
            'content': content.decode('utf-8', errors='replace'),
            'error': None
        }
    except urllib.error.HTTPError as e:
        content = e.read() if e.fp else b''
        return {
            'status': e.code,
            'final_url': e.geturl() if hasattr(e, 'geturl') else url,
            'headers': dict(e.headers) if e.headers else {},
            'content': content.decode('utf-8', errors='replace'),
            'error': f"HTTPError {e.code}: {e.reason}"
        }
    except Exception as e:
        return {
            'status': 0,
            'final_url': url,
            'headers': {},
            'content': '',
            'error': str(e)
        }

def get_ssl_info(hostname="www.enviosdosruedas.com", port=443):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()
                return {
                    'subject': dict(x[0] for x in cert.get('subject', ())),
                    'issuer': dict(x[0] for x in cert.get('issuer', ())),
                    'notBefore': cert.get('notBefore'),
                    'notAfter': cert.get('notAfter'),
                    'san': [x[1] for x in cert.get('subjectAltName', ()) if x[0] == 'DNS'],
                    'cipher': cipher,
                    'version': version
                }
    except Exception as e:
        return {'error': str(e)}

def parse_html_elements(html, url_context):
    data = {}
    
    # Title
    m = re.search(r'(?si)<title>(.*?)</title>', html)
    data['title'] = m.group(1).strip() if m else ''
    
    # Meta description
    m = re.search(r'(?si)<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html)
    data['description'] = m.group(1).strip() if m else ''
    
    # Canonical
    m = re.search(r'(?si)<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html)
    data['canonical'] = m.group(1).strip() if m else ''
    
    # H1
    h1_matches = re.findall(r'(?si)<h1[^>]*>(.*?)</h1>', html)
    clean_h1s = [re.sub(r'<[^>]+>', ' ', h).strip() for h1 in h1_matches for h in [h1]]
    data['h1'] = ' | '.join(clean_h1s) if clean_h1s else ''
    
    # WhatsApp links
    wa_matches = re.findall(r'(?si)href=["\'](https?://(?:api\.whatsapp\.com|wa\.me)/[^"\']*)["\']', html)
    parsed_wa = []
    for wa in wa_matches:
        parsed = urllib.parse.urlparse(wa)
        q = urllib.parse.parse_qs(parsed.query)
        text = q.get('text', [''])[0]
        phone = q.get('phone', [''])[0]
        if not phone and 'wa.me' in parsed.netloc:
            phone = parsed.path.strip('/')
        parsed_wa.append({'raw': wa, 'phone': phone, 'text': text})
    data['whatsapp_links'] = parsed_wa
    
    # Tel links
    tel_matches = re.findall(r'(?si)href=["\'](tel:[^"\']*)["\']', html)
    data['tel_links'] = list(set(tel_matches))
    
    # Mailto links
    mail_matches = re.findall(r'(?si)href=["\'](mailto:[^"\']*)["\']', html)
    data['mail_links'] = list(set(mail_matches))
    
    # Internal links
    all_links = re.findall(r'(?si)<a\s+[^>]*href=["\']([^"\']*)["\']', html)
    internal = []
    external = []
    for l in all_links:
        if l.startswith('#') or l.startswith('javascript:'):
            continue
        if l.startswith('tel:') or l.startswith('mailto:'):
            continue
        if 'whatsapp.com' in l or 'wa.me' in l:
            continue
        if l.startswith('/') or 'enviosdosruedas.com' in l:
            internal.append(l)
        else:
            external.append(l)
    data['internal_links'] = sorted(list(set(internal)))
    data['external_links'] = sorted(list(set(external)))
    
    # Forms
    form_matches = re.findall(r'(?si)<form([^>]*)>(.*?)</form>', html)
    forms = []
    for fattr, fbody in form_matches:
        inputs = re.findall(r'(?si)<(?:input|select|textarea)[^>]*name=["\']([^"\']*)["\']', fbody)
        buttons = re.findall(r'(?si)<button[^>]*>(.*?)</button>', fbody)
        clean_buttons = [re.sub(r'<[^>]+>', '', b).strip() for b in buttons]
        m_action = re.search(r'action=["\']([^"\']*)["\']', fattr)
        m_method = re.search(r'method=["\']([^"\']*)["\']', fattr)
        forms.append({
            'action': m_action.group(1) if m_action else '',
            'method': m_method.group(1) if m_method else '',
            'inputs': inputs,
            'buttons': clean_buttons
        })
    data['forms'] = forms
    
    # Images
    img_matches = re.findall(r'(?si)<img\s+[^>]*src=["\']([^"\']*)["\'][^>]*>', html)
    data['images'] = sorted(list(set(img_matches)))
    
    # Scripts
    scripts = re.findall(r'(?si)<script\s+[^>]*src=["\']([^"\']*)["\']', html)
    data['scripts'] = scripts

    return data

def main():
    print("1. Testing SSL...")
    ssl_info = get_ssl_info()
    
    print("2. Fetching robots.txt and sitemap.xml...")
    robots_res = fetch_url(f"{BASE_URL}/robots.txt")
    sitemap_res = fetch_url(f"{BASE_URL}/sitemap.xml")
    
    sitemap_urls = []
    if sitemap_res['status'] == 200:
        try:
            root = ET.fromstring(sitemap_res['content'])
            ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for loc in root.findall('.//ns:loc', ns):
                sitemap_urls.append(loc.text.strip())
        except Exception as e:
            print("Error parsing sitemap XML:", e)
            
    print(f"Found {len(sitemap_urls)} URLs in sitemap.")
    
    # Define complete test list
    additional_urls = [
        f"{BASE_URL}/",
        f"{BASE_URL}/servicios/",
        f"{BASE_URL}/revisar/",
        f"{BASE_URL}/admin/",
        f"{BASE_URL}/api/",
        f"{BASE_URL}/servicios/envios-flex/",
        f"{BASE_URL}/no-existe-404-test"
    ]
    all_test_urls = sorted(list(set(sitemap_urls + additional_urls)))
    
    # Test each URL with both follow_redirects=False (to see 308/301/307) and follow_redirects=True (to see final page)
    url_results = {}
    print(f"3. Auditing {len(all_test_urls)} URLs...")
    for u in all_test_urls:
        print(f"  Testing {u}...")
        no_redir = fetch_url(u, follow_redirects=False)
        with_redir = fetch_url(u, follow_redirects=True)
        
        parsed_data = {}
        if with_redir['status'] == 200:
            parsed_data = parse_html_elements(with_redir['content'], u)
            
        url_results[u] = {
            'initial_status': no_redir['status'],
            'redirect_location': no_redir['headers'].get('Location', no_redir['headers'].get('location')),
            'final_status': with_redir['status'],
            'final_url': with_redir['final_url'],
            'content_length': len(with_redir['content']),
            'headers': {k: v for k, v in with_redir['headers'].items() if k.lower() in [
                'server', 'x-matched-path', 'x-nextjs-prerender', 'x-vercel-cache', 'content-security-policy', 'strict-transport-security'
            ]},
            'parsed': parsed_data
        }

    # 4. Local files inventory
    print("4. Inspecting local files in envios/...")
    envios_dir = os.path.join(REPO_ROOT, "envios")
    local_files_data = {}
    if os.path.exists(envios_dir):
        for f in os.listdir(envios_dir):
            if f.endswith('.html'):
                fpath = os.path.join(envios_dir, f)
                with open(fpath, 'r', encoding='utf-8', errors='replace') as fp:
                    fcontent = fp.read()
                local_files_data[f] = {
                    'size': os.path.getsize(fpath),
                    'parsed': parse_html_elements(fcontent, f)
                }

    # 5. Public assets inventory
    print("5. Inspecting public/ assets...")
    public_dir = os.path.join(REPO_ROOT, "public")
    public_assets = []
    if os.path.exists(public_dir):
        for root, dirs, files in os.walk(public_dir):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), REPO_ROOT).replace('\\', '/')
                public_assets.append({
                    'rel_path': rel_path,
                    'size': os.path.getsize(os.path.join(root, file))
                })

    out_file = os.path.join(STATE_DIR, "audit_full_data.json")
    full_data = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'ssl_info': ssl_info,
        'robots_txt': robots_res['content'],
        'sitemap_urls': sitemap_urls,
        'url_results': url_results,
        'local_files': local_files_data,
        'public_assets_count': len(public_assets),
        'public_assets': public_assets
    }
    
    with open(out_file, 'w', encoding='utf-8') as fp:
        json.dump(full_data, fp, indent=2, ensure_ascii=False)
        
    print(f"Audit completed! Saved full data to {out_file}")

if __name__ == '__main__':
    main()

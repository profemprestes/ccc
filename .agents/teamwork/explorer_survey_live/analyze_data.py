import os
import json

data_file = r"d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\audit_full_data.json"
with open(data_file, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

print("="*60)
print("1. SSL INFO")
print("="*60)
ssl_info = data.get('ssl_info', {})
print("Issuer:", ssl_info.get('issuer'))
print("Subject:", ssl_info.get('subject'))
print("Valid From:", ssl_info.get('notBefore'))
print("Valid To:", ssl_info.get('notAfter'))
print("SAN:", ssl_info.get('san'))
print("TLS Version:", ssl_info.get('version'), "Cipher:", ssl_info.get('cipher', [None])[0])

print("\n" + "="*60)
print("2. URL STATUS & REDIRECTS")
print("="*60)
url_results = data.get('url_results', {})
for u, r in sorted(url_results.items()):
    init_s = r.get('initial_status')
    fin_s = r.get('final_status')
    redir = r.get('redirect_location')
    fin_u = r.get('final_url')
    sz = r.get('content_length')
    matched = r.get('headers', {}).get('x-matched-path', 'N/A')
    print(f"{u:55} | Init:{init_s:3} -> Fin:{fin_s:3} | Sz:{sz:6} | Matched:{matched:25} | Redir:{redir}")

print("\n" + "="*60)
print("3. LIVE PAGES PARSED METADATA")
print("="*60)
for u, r in sorted(url_results.items()):
    if r.get('final_status') == 200:
        p = r.get('parsed', {})
        print(f"\nURL: {u}")
        print(f"  Title: {p.get('title')}")
        print(f"  H1: {p.get('h1')}")
        print(f"  Canonical: {p.get('canonical')}")
        print(f"  Desc: {p.get('description')[:80]}...")
        print(f"  WhatsApp ({len(p.get('whatsapp_links', []))} links): {[w['text'] for w in p.get('whatsapp_links', [])[:3]]}")
        print(f"  Tel: {p.get('tel_links')}")
        print(f"  Mail: {p.get('mail_links')}")
        print(f"  Forms ({len(p.get('forms', []))}): {p.get('forms')}")

print("\n" + "="*60)
print("4. LOCAL ENVIOS/ FILES INVENTORY")
print("="*60)
local_files = data.get('local_files', {})
for f, info in sorted(local_files.items()):
    p = info.get('parsed', {})
    print(f"\nFile: {f} ({info.get('size')} bytes)")
    print(f"  Title: {p.get('title')}")
    print(f"  H1: {p.get('h1')}")
    print(f"  Canonical: {p.get('canonical')}")
    print(f"  WhatsApp ({len(p.get('whatsapp_links', []))}): {[w['text'] for w in p.get('whatsapp_links', [])[:2]]}")
    print(f"  Forms ({len(p.get('forms', []))}): {p.get('forms')}")

print("\n" + "="*60)
print("5. PUBLIC ASSETS SUMMARY")
print("="*60)
print(f"Total public assets found: {data.get('public_assets_count')}")
for a in data.get('public_assets', [])[:20]:
    print(f"  {a['rel_path']} ({a['size']} bytes)")

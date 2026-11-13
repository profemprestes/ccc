import os
import json
import re
import urllib.parse

BASE_URL = "https://www.enviosdosruedas.com"

data_file = r"d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\audit_full_data.json"
with open(data_file, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

url_results = data['url_results']
local_files = data['local_files']

print("="*70)
print("A. LIVE-ONLY PAGES (NOT IN REPOSITORY ENVIOS/)")
print("="*70)
live_only = [
    'https://www.enviosdosruedas.com/cobertura',
    'https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata',
    'https://www.enviosdosruedas.com/servicios/'
]
for u in live_only:
    r = url_results.get(u, {})
    p = r.get('parsed', {})
    print(f"\nURL: {u}")
    print(f"  Title: {p.get('title')}")
    print(f"  H1: {p.get('h1')}")
    print(f"  Canonical: {p.get('canonical')}")
    print(f"  Description: {p.get('description')}")
    print(f"  Size: {r.get('content_length')} bytes")
    print(f"  WhatsApp count: {len(p.get('whatsapp_links', []))}")
    print(f"  Internal links count: {len(p.get('internal_links', []))}")

print("\n" + "="*70)
print("B. LIVE REAL 'TERMINOS Y CONDICIONES' VS LOCAL")
print("="*70)
live_tc = url_results.get('https://www.enviosdosruedas.com/terminos-y-condiciones', {}).get('parsed', {})
local_tc = local_files.get('terminos-y-condiciones.html', {}).get('parsed', {})
print(f"LIVE /terminos-y-condiciones/:")
print(f"  Title: {live_tc.get('title')}")
print(f"  H1: {live_tc.get('h1')}")
print(f"  Canonical: {live_tc.get('canonical')}")
print(f"\nLOCAL terminos-y-condiciones.html:")
print(f"  Title: {local_tc.get('title')}")
print(f"  H1: {local_tc.get('h1')}")
print(f"  Canonical: {local_tc.get('canonical')}")
print(f"  CRITICAL BUG: Local file is an EXACT duplicate of logistica-dosruedas.html!")

print("\n" + "="*70)
print("C. LOCAL 'html.html' VS 'home.html'")
print("="*70)
h_home = local_files.get('home.html', {})
h_html = local_files.get('html.html', {})
print(f"home.html size: {h_home.get('size')} bytes")
print(f"html.html size: {h_html.get('size')} bytes")
print(f"home.html Title: {h_home.get('parsed', {}).get('title')}")
print(f"html.html Title: {h_html.get('parsed', {}).get('title')}")
print(f"home.html H1: {h_home.get('parsed', {}).get('h1')}")
print(f"html.html H1: {h_html.get('parsed', {}).get('h1')}")

# What is the difference between home.html and html.html?
with open(r"d:\repositorios\ccc\envios\home.html", 'r', encoding='utf-8', errors='replace') as f1:
    c1 = f1.read()
with open(r"d:\repositorios\ccc\envios\html.html", 'r', encoding='utf-8', errors='replace') as f2:
    c2 = f2.read()
print(f"Difference in length: {len(c2) - len(c1)} characters")
# Check if html.html contains extra sections or unminified code
print(f"c1 script count: {len(re.findall(r'<script', c1))} vs c2 script count: {len(re.findall(r'<script', c2))}")
print(f"c1 style count: {len(re.findall(r'<style', c1))} vs c2 style count: {len(re.findall(r'<style', c2))}")

print("\n" + "="*70)
print("D. WHATSAPP AUDIT (PHONE NUMBERS & MESSAGES)")
print("="*70)
all_wa_numbers = set()
all_wa_messages = set()
page_wa_summary = []
for u, r in sorted(url_results.items()):
    if r.get('final_status') == 200:
        p = r.get('parsed', {})
        for w in p.get('whatsapp_links', []):
            raw = w.get('raw', '')
            phone = w.get('phone', '')
            text = urllib.parse.unquote(w.get('text', ''))
            all_wa_numbers.add(phone)
            all_wa_messages.add(text)
            page_wa_summary.append((u.replace(BASE_URL, '') or '/', phone, text[:60]))

print(f"Unique WhatsApp numbers found across site: {all_wa_numbers}")
print(f"Total WhatsApp message variants: {len(all_wa_messages)}")
print("Sample message mappings:")
for path, ph, txt in page_wa_summary[:15]:
    print(f"  {path:35} | Phone:{ph:15} | Text: {txt}")

print("\n" + "="*70)
print("E. INTERACTIVE FORMS AUDIT")
print("="*70)
for u, r in sorted(url_results.items()):
    if r.get('final_status') == 200:
        p = r.get('parsed', {})
        forms = p.get('forms', [])
        if forms:
            print(f"\nURL: {u.replace(BASE_URL, '')}")
            for idx, f in enumerate(forms):
                print(f"  Form #{idx+1}: Action='{f.get('action')}' Method='{f.get('method')}'")
                print(f"    Inputs ({len(f.get('inputs', []))}): {f.get('inputs')}")
                print(f"    Buttons: {f.get('buttons')}")

print("\n" + "="*70)
print("F. PHONE, EMAIL & SOCIAL MEDIA AUDIT")
print("="*70)
all_tel = set()
all_mail = set()
all_ig = set()
all_fb = set()
for u, r in sorted(url_results.items()):
    if r.get('final_status') == 200:
        p = r.get('parsed', {})
        for t in p.get('tel_links', []): all_tel.add(t)
        for m in p.get('mail_links', []): all_mail.add(m)
        for ext in p.get('external_links', []):
            if 'instagram.com' in ext: all_ig.add(ext)
            if 'facebook.com' in ext: all_fb.add(ext)

print(f"Tel links: {all_tel}")
print(f"Mail links: {all_mail}")
print(f"Instagram links: {all_ig}")
print(f"Facebook links: {all_fb}")

import json
import urllib.parse
import re

with open(r"d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\audit_full_data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print("="*70)
print("WHATSAPP LINKS ACROSS ALL LIVE PAGES")
print("="*70)
wa_details = {}
for url, res in data['url_results'].items():
    if res['final_status'] == 200:
        p = res.get('parsed', {})
        w_links = p.get('whatsapp_links', [])
        path = url.replace('https://www.enviosdosruedas.com', '') or '/'
        wa_details[path] = []
        for w in w_links:
            raw = w['raw']
            wa_details[path].append(raw)

for path, links in sorted(wa_details.items()):
    print(f"\nPath: {path} ({len(links)} WhatsApp links)")
    unique_links = list(set(links))
    for l in unique_links:
        parsed = urllib.parse.urlparse(l)
        q = urllib.parse.parse_qs(parsed.query)
        txt = q.get('text', ['<NO TEXT>'])[0]
        print(f"  - Netloc: {parsed.netloc} | Path: {parsed.path} | Query: text='{txt}'")

print("\n" + "="*70)
print("COTIZAR PAGE INTERACTIVITY ANALYSIS")
print("="*70)
cotizar_html = data['url_results'].get('https://www.enviosdosruedas.com/cotizar', {}).get('parsed', {})
# let's inspect the scripts and interactive elements of cotizar
import urllib.request
req = urllib.request.Request('https://www.enviosdosruedas.com/cotizar/', headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')

# Look for JavaScript logic related to calculation
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
print(f"Inline scripts in /cotizar/: {len(scripts)}")
for idx, s in enumerate(scripts):
    if len(s.strip()) > 0 and 'function' in s or 'calc' in s or 'tarifa' in s or 'price' in s:
        print(f"Script #{idx+1} excerpt: {s.strip()[:300]}...")

# Look for form or input fields in /cotizar/
inputs = re.findall(r'<input[^>]*>', content)
selects = re.findall(r'<select[^>]*>.*?</select>', content, re.DOTALL)
buttons = re.findall(r'<button[^>]*>.*?</button>', content, re.DOTALL)

print(f"Inputs in /cotizar/: {len(inputs)}")
for inp in inputs:
    print(f"  {inp}")
print(f"Selects in /cotizar/: {len(selects)}")
for sel in selects:
    name = re.search(r'name=["\']([^"\']*)["\']', sel)
    opts = re.findall(r'<option[^>]*>(.*?)</option>', sel)
    print(f"  Select name={name.group(1) if name else 'N/A'}: Options={opts}")
print(f"Buttons in /cotizar/: {len(buttons)}")
for btn in buttons:
    clean_b = re.sub(r'<[^>]+>', '', btn).strip()
    print(f"  Button: '{clean_b}'")

print("\n" + "="*70)
print("LOGISTICA DOSRUEDAS TRACKING ANALYSIS")
print("="*70)
req = urllib.request.Request('https://www.enviosdosruedas.com/logistica-dosruedas/', headers={'User-Agent': 'Mozilla/5.0'})
log_content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
log_inputs = re.findall(r'<input[^>]*>', log_content)
log_buttons = re.findall(r'<button[^>]*>.*?</button>', log_content, re.DOTALL)
print(f"Inputs in /logistica-dosruedas/: {len(log_inputs)}")
for inp in log_inputs:
    print(f"  {inp}")
print(f"Buttons in /logistica-dosruedas/: {len(log_buttons)}")
for btn in log_buttons:
    clean_b = re.sub(r'<[^>]+>', '', btn).strip()
    print(f"  Button: '{clean_b}'")

# Check if there is an external portal link
external_log = re.findall(r'href=["\'](https?://[^"\']*)["\']', log_content)
print("External links on /logistica-dosruedas/:", set(external_log))

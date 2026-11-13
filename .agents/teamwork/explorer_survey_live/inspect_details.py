import os
import json
import re
import difflib

# 1. Compare home.html vs html.html
with open(r"d:\repositorios\ccc\envios\home.html", 'r', encoding='utf-8', errors='replace') as f1:
    home_lines = f1.readlines()
with open(r"d:\repositorios\ccc\envios\html.html", 'r', encoding='utf-8', errors='replace') as f2:
    html_lines = f2.readlines()

print(f"home.html line count: {len(home_lines)}")
print(f"html.html line count: {len(html_lines)}")

# Let's see what is extra in html.html
diff = list(difflib.unified_diff(home_lines[:200], html_lines[:200], fromfile='home.html', tofile='html.html'))
print("First diffs (head):", ''.join(diff[:30]))

# Search for unique sections or elements in html.html
home_set = set(line.strip() for line in home_lines if len(line.strip()) > 30)
html_set = set(line.strip() for line in html_lines if len(line.strip()) > 30)
only_html = [l for l in html_lines if len(l.strip()) > 30 and l.strip() not in home_set]
print(f"Lines only in html.html: {len(only_html)}")
print("Sample lines unique to html.html:")
for l in only_html[:10]:
    print("  +", l.strip()[:100])

# 2. Inspect real live terminos-y-condiciones text
data_file = r"d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\audit_full_data.json"
with open(data_file, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

u_tc = data['url_results'].get('https://www.enviosdosruedas.com/terminos-y-condiciones', {})
# let's extract sections from the live terminos y condiciones
import urllib.request
req = urllib.request.Request("https://www.enviosdosruedas.com/terminos-y-condiciones/", headers={'User-Agent': 'Mozilla/5.0'})
try:
    content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    # extract paragraphs or h2/h3
    h2s = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content)
    clean_h2s = [re.sub(r'<[^>]+>', '', h).strip() for h2 in h2s]
    print("\nLive Términos y Condiciones Headings:")
    for h in clean_h2s:
        print("  -", h)
except Exception as e:
    print("Error fetching TC:", e)

# 3. Inspect /cotizar on live: extract pricing and zones
try:
    req = urllib.request.Request("https://www.enviosdosruedas.com/cotizar/", headers={'User-Agent': 'Mozilla/5.0'})
    cotizar_html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    # Find pricing mentions ($...)
    prices = re.findall(r'\$\s*[\d\.\,]+', cotizar_html)
    print("\nPricing mentions on /cotizar/:", set(prices))
    # Find zone mentions
    zones = re.findall(r'(Zona\s+[A-Z0-9]+|Tarifa\s+[A-Za-z]+|Express|LowCost|Flex)', cotizar_html, re.I)
    print("Zone/Service keywords on /cotizar/:", set(zones))
except Exception as e:
    print("Error fetching cotizar:", e)

# 4. Inspect /cobertura on live: extract zones and pricing
try:
    req = urllib.request.Request("https://www.enviosdosruedas.com/cobertura/", headers={'User-Agent': 'Mozilla/5.0'})
    cobertura_html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    prices_cob = re.findall(r'\$\s*[\d\.\,]+', cobertura_html)
    print("\nPricing mentions on /cobertura/:", set(prices_cob))
    h2s_cob = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', cobertura_html)
    print("Headings on /cobertura/:", [re.sub(r'<[^>]+>', '', h).strip() for h2 in h2s_cob])
except Exception as e:
    print("Error fetching cobertura:", e)

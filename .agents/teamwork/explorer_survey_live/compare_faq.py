import urllib.request
import re

with open(r'd:\repositorios\ccc\envios\nosotrospreguntas-frecuentes.html', 'r', encoding='utf-8', errors='replace') as fp:
    local_faq = fp.read()

req = urllib.request.Request('https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/', headers={'User-Agent': 'Mozilla/5.0'})
live_faq = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')

print("LOCAL FAQ ACCORDIONS / HEADINGS:")
local_qs = re.findall(r'<button[^>]*>(.*?)</button>', local_faq, re.DOTALL)
for q in [re.sub(r'<[^>]+>', '', x).strip() for x in local_qs if len(x.strip()) > 15]:
    print("  -", q)

print("\nLIVE FAQ ACCORDIONS / HEADINGS:")
live_qs = re.findall(r'<button[^>]*>(.*?)</button>', live_faq, re.DOTALL)
for q in [re.sub(r'<[^>]+>', '', x).strip() for x in live_qs if len(x.strip()) > 15]:
    print("  -", q)

# Check where the prices are on live FAQ
print("\nLive FAQ text matching prices:")
for match in re.finditer(r'([^.]{0,80}\$\s*[\d\.\,]+[^.]{0,80})', live_faq):
    snippet = re.sub(r'<[^>]+>', ' ', match.group(1)).strip()
    if not snippet.startswith('1:"') and not 'self.__next_f' in snippet:
        print("  *", snippet)

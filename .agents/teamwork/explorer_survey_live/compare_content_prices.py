import os
import re

pairs = [
    ('Express', r'd:\repositorios\ccc\envios\serviciosenvios-express.html', 'https://www.enviosdosruedas.com/servicios/envios-express/'),
    ('LowCost', r'd:\repositorios\ccc\envios\serviciosenvios-lowcost.html', 'https://www.enviosdosruedas.com/servicios/envios-lowcost/'),
    ('Flex', r'd:\repositorios\ccc\envios\serviciosenviosflex.html', 'https://www.enviosdosruedas.com/servicios/enviosflex/'),
    ('Cotizar', r'd:\repositorios\ccc\envios\cotizar.html', 'https://www.enviosdosruedas.com/cotizar/'),
    ('FAQ', r'd:\repositorios\ccc\envios\nosotrospreguntas-frecuentes.html', 'https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/')
]

import urllib.request

for label, lpath, live_url in pairs:
    print(f"\n=== COMPARING {label} ===")
    with open(lpath, 'r', encoding='utf-8', errors='replace') as fp:
        local_html = fp.read()
    
    req = urllib.request.Request(live_url, headers={'User-Agent': 'Mozilla/5.0'})
    live_html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    
    local_prices = sorted(list(set(re.findall(r'\$\s*[\d\.\,]+', local_html))))
    live_prices = sorted(list(set(re.findall(r'\$\s*[\d\.\,]+', live_html))))
    
    print(f"Local prices ({len(local_prices)}): {local_prices}")
    print(f"Live prices  ({len(live_prices)}): {live_prices}")
    
    # Check if there are price differences
    diff_local = set(local_prices) - set(live_prices)
    diff_live = set(live_prices) - set(local_prices)
    if diff_local or diff_live:
        print(f"  Prices ONLY in local: {diff_local}")
        print(f"  Prices ONLY in live:  {diff_live}")
    else:
        print("  Prices match 100% between local snapshot and live page!")

import json
import re
import urllib.parse

with open(r"d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\audit_full_data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print("="*80)
print("PRICING, SCHEDULES, ZONES & CUT-OFF TIMES ON LIVE PAGES")
print("="*80)

# We have the content for pages or can fetch key pages
urls_to_check = [
    ('/', 'https://www.enviosdosruedas.com/'),
    ('/servicios/envios-express', 'https://www.enviosdosruedas.com/servicios/envios-express/'),
    ('/servicios/envios-lowcost', 'https://www.enviosdosruedas.com/servicios/envios-lowcost/'),
    ('/servicios/enviosflex', 'https://www.enviosdosruedas.com/servicios/enviosflex/'),
    ('/servicios/deposito-fulfillment', 'https://www.enviosdosruedas.com/servicios/deposito-fulfillment/'),
    ('/servicios/empresas-cuenta-corriente', 'https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente/'),
    ('/cotizar', 'https://www.enviosdosruedas.com/cotizar/'),
    ('/cobertura', 'https://www.enviosdosruedas.com/cobertura/'),
    ('/mardelivery', 'https://www.enviosdosruedas.com/mardelivery/'),
    ('/guias/envios-flex-mar-del-plata', 'https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/'),
    ('/nosotros/preguntas-frecuentes', 'https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/')
]

import urllib.request

for slug, u in urls_to_check:
    print(f"\n--- PAGE: {slug} ({u}) ---")
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        
        # Prices
        prices = sorted(list(set(re.findall(r'\$\s*[\d\.\,]+', html))))
        print(f"Prices detected: {prices}")
        
        # Horarios / cut-off
        schedules = set(re.findall(r'\b\d{1,2}(?::\d{2})?\s*(?:hs|horas|am|pm)\b', html, re.I))
        print(f"Schedules/Hours detected: {schedules}")
        
        # Zones
        zones = set(re.findall(r'(?:Zona\s+[1-4]|Zona\s+[A-D]|Tarifa\s+[A-Za-z]+|Radio\s+[A-Za-z0-9]+)', html, re.I))
        print(f"Zones detected: {zones}")
        
    except Exception as e:
        print(f"Error fetching {u}: {e}")

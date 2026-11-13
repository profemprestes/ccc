import os
import re

envios_dir = r"d:\repositorios\ccc\envios"
results = []

for f in sorted(os.listdir(envios_dir)):
    if f.endswith('.html'):
        fpath = os.path.join(envios_dir, f)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as fp:
            content = fp.read()
        
        sd_count = len(re.findall(r'data-sd-id', content))
        bis_count = len(re.findall(r'bis_skin_checked', content))
        font_refs = len(re.findall(r'\.\./public/fuentes', content))
        next_refs = len(re.findall(r'/_next/static', content))
        results.append({
            'file': f,
            'size': os.path.getsize(fpath),
            'sd_count': sd_count,
            'bis_count': bis_count,
            'font_local_refs': font_refs,
            'next_static_refs': next_refs
        })

print(f"{'File':38} | {'Size':8} | {'sd-id':5} | {'bis':5} | {'local fonts':11} | {'_next refs':10}")
print("-" * 88)
for r in results:
    print(f"{r['file']:38} | {r['size']:8} | {r['sd_count']:5} | {r['bis_count']:5} | {r['font_local_refs']:11} | {r['next_static_refs']:10}")

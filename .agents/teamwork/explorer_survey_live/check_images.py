import os
import re

envios_dir = r"d:\repositorios\ccc\envios"
all_imgs = set()
file_imgs = {}

for f in sorted(os.listdir(envios_dir)):
    if f.endswith('.html'):
        fpath = os.path.join(envios_dir, f)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as fp:
            content = fp.read()
        imgs = re.findall(r'<img[^>]*src=["\']([^"\']*)["\']', content)
        file_imgs[f] = imgs
        for s in imgs:
            all_imgs.add(s)

print(f"Total unique img src in envios/*.html: {len(all_imgs)}")
print("Image paths found:")
for s in sorted(all_imgs):
    # Check if exists locally
    local_target = s
    if s.startswith('/'):
        local_target = os.path.join(r"d:\repositorios\ccc\public", s.lstrip('/'))
    elif s.startswith('../public/'):
        local_target = os.path.join(r"d:\repositorios\ccc", s.replace('../', ''))
    exists = os.path.exists(local_target)
    print(f"  {s:50} -> Exists in repo? {exists}")

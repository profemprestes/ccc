import urllib.request
import re

req = urllib.request.Request('https://www.enviosdosruedas.com/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
imgs = re.findall(r'<img[^>]*src=["\']([^"\']*)["\']', html)
print('Live Homepage image sources:')
for s in sorted(set(imgs)):
    print('  ', s)

# Also check other live pages
for sub in ['/cotizar/', '/servicios/enviosflex/', '/cobertura/', '/mardelivery/']:
    req2 = urllib.request.Request('https://www.enviosdosruedas.com' + sub, headers={'User-Agent': 'Mozilla/5.0'})
    html2 = urllib.request.urlopen(req2, timeout=10).read().decode('utf-8')
    imgs2 = re.findall(r'<img[^>]*src=["\']([^"\']*)["\']', html2)
    print(f'\nLive {sub} image sources:')
    for s in sorted(set(imgs2)):
        print('  ', s)

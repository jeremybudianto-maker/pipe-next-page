from pathlib import Path
import base64
import json

root = Path(__file__).parent
assets = root / 'assets'
html = (root / 'template.html').read_text()
art = {}
for key in ['hero', 'artist', 'team', 'history', 'oracle', 'dayoff']:
    art[key] = 'data:image/webp;base64,' + base64.b64encode((assets / (key + '.webp')).read_bytes()).decode()
html = html.replace('{{ASSET_MANIFEST}}', json.dumps(art, separators=(',', ':')))
font = base64.b64encode((assets / 'inter-latin-400-700.woff2').read_bytes()).decode()
html = html.replace('/*EMBED_FONTS*/', "@font-face{font-family:Inter;font-style:normal;font-weight:400 700;font-display:swap;src:url(data:font/woff2;base64," + font + ") format('woff2')}")
license_text = (assets / 'inter-OFL.txt').read_text()
html = html.replace('</head>', '<!-- Embedded font license\n' + license_text + '\n-->\n</head>')
assert '{{' not in html
(root / 'dist' / 'index.html').write_text(html)
print(f'Built self-contained presentation: {len(html):,} bytes')

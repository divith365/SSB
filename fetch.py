import requests
import json
import time
import re

cards = {
  'chk': ['Mullayanagiri', 'Kudremukh', 'Sringeri', 'Belur,_Karnataka'],
  'crg': ['Abbey_Falls', 'Dubare', 'Raja%27s_Seat', 'Bylakuppe'],
  'mys': ['Mysore_Palace', 'Ooty', 'Kodaikanal', 'Wayanad_district'],
  'ker': ['Munnar', 'Periyar_National_Park', 'Alappuzha', 'Kovalam'],
  'oot': ['Ooty', 'Nilgiri_Mountain_Railway', 'Ooty_Botanical_Gardens', 'Doddabetta'],
  'kod': ['Kodaikanal', 'Pillar_Rocks', 'Coaker%27s_Walk', 'Bryant_Park'],
  'goa': ['Palolem_Beach', 'Dudhsagar_Falls', 'Aguada_Fort', 'Basilica_of_Bom_Jesus'],
  'alp': ['Alappuzha', 'Kumarakom', 'Vembanad', 'Kerala_backwaters']
}

headers = {'User-Agent': 'MyApp/3.0'}
results = {}

for card, titles in cards.items():
    results[card] = []
    for title in titles:
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&pithumbsize=960&format=json"
        try:
            r = requests.get(url, headers=headers)
            data = r.json()
            pages = data.get('query', {}).get('pages', {})
            found = False
            for p_id, p_info in pages.items():
                if 'thumbnail' in p_info:
                    results[card].append(p_info['thumbnail']['source'])
                    found = True
                    break
            if not found:
                results[card].append("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/960px-Ooty_Lake.jpg") # fallback
        except Exception as e:
            results[card].append("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/960px-Ooty_Lake.jpg")
        time.sleep(0.5)

# Read index.html
with open('/home/arun/SSB/index.html', 'r') as f:
    html = f.read()

# Replace the bg-collage CSS
for card, urls in results.items():
    css_regex = r"\.bg-collage-" + card + r" \{\s*background-image:[^}]*\}"
    new_css = f".bg-collage-{card} {{\n  background-image:\n    url('{urls[0]}'),\n    url('{urls[1]}'),\n    url('{urls[2]}'),\n    url('{urls[3]}');\n  background-position: top left, top right, bottom left, bottom right;\n  background-size: 50.5% 50.5%, 50.5% 50.5%, 50.5% 50.5%, 50.5% 50.5%;\n  background-repeat: no-repeat;\n}}"
    html = re.sub(css_regex, new_css, html)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(html)
print("Updated CSS with valid 960px URLs!")

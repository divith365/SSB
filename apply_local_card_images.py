import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Wikimedia URLs with local image paths for the cards
replacements = [
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tirumala_090615.jpg/800px-Tirumala_090615.jpg", "images/piligrim.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Munnar_hill_station.jpg/800px-Munnar_hill_station.jpg", "images/hill.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Varkala_beach_from_above.jpg/800px-Varkala_beach_from_above.jpg", "images/honey.jpeg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Palolem_Beach_Goa.jpg/800px-Palolem_Beach_Goa.jpg", "images/beach.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alappuzha_Boat_Beauty_W.jpg/800px-Alappuzha_Boat_Beauty_W.jpg", "images/houseboat.webp"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/800px-Mysore_Palace_Morning.jpg", "images/city.jpeg")
]

for old_url, new_img in replacements:
    html = html.replace(old_url, new_img)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

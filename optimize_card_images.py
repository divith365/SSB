import os
import requests
import re
from PIL import Image
from io import BytesIO

# The 6 image URLs used in the cat-cards
urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tirumala_090615.jpg/800px-Tirumala_090615.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Munnar_hill_station.jpg/800px-Munnar_hill_station.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Varkala_beach_from_above.jpg/800px-Varkala_beach_from_above.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Palolem_Beach_Goa.jpg/800px-Palolem_Beach_Goa.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alappuzha_Boat_Beauty_W.jpg/800px-Alappuzha_Boat_Beauty_W.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/800px-Mysore_Palace_Morning.jpg"
]

os.makedirs('/home/arun/SSB/images/cards', exist_ok=True)

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for i, url in enumerate(urls, 1):
    print(f"Downloading {url}...")
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        webp_filename = f'cat_img_{i}.webp'
        webp_path = os.path.join('/home/arun/SSB/images/cards', webp_filename)
        
        # Save as optimized webp
        img.save(webp_path, 'WEBP', quality=75)
        print(f"Saved {webp_path}")
        
        # Replace the URL in HTML
        html = html.replace(url, f'images/cards/{webp_filename}')
    else:
        print(f"Failed to download {url}")

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

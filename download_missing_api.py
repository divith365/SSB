import os
import requests
from PIL import Image
from io import BytesIO

queries = [
    ("Golden_Temple", "images/hero/north_3.webp"),
    ("Boutique_hotel", "images/hero/hotel_deluxe.webp"),
    ("Resort_hotel", "images/hero/hotel_super_deluxe.webp")
]

headers = {'User-Agent': 'CoolBot/1.0'}

for q, target in queries:
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={q}"
    res = requests.get(url, headers=headers).json()
    pages = res['query']['pages']
    page_id = list(pages.keys())[0]
    
    if page_id != "-1" and 'original' in pages[page_id]:
        img_url = pages[page_id]['original']['source']
        print(f"Downloading {img_url} for {q}")
        r = requests.get(img_url, headers=headers)
        if r.status_code == 200:
            img = Image.open(BytesIO(r.content))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            img.save(target, 'WEBP', quality=80)
            print(f"Saved {target}")
        else:
            print(f"Failed to download image data for {q}")
    else:
        print(f"No original image found for {q}")

import requests
from PIL import Image
from io import BytesIO

urls = [
    ("https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200", "images/hero/hotel_deluxe.webp"),
    ("https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200", "images/hero/hotel_super_deluxe.webp")
]

headers = {'User-Agent': 'Mozilla/5.0'}

for url, target in urls:
    print(f"Downloading {url}")
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        img = Image.open(BytesIO(r.content))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
        img.save(target, 'WEBP', quality=80)
        print(f"Saved {target}")
    else:
        print(f"Failed {r.status_code}")

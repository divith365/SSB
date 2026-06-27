import os
import requests
from PIL import Image
from io import BytesIO

urls = [
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Golden_Temple%2C_Amritsar%2C_Punjab%2C_India.jpg/1200px-Golden_Temple%2C_Amritsar%2C_Punjab%2C_India.jpg", "images/hero/north_3.webp"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Hotel-room-renaissance-columbus-ohio.jpg/1200px-Hotel-room-renaissance-columbus-ohio.jpg", "images/hero/hotel_deluxe.webp"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Luxury_hotel_room.jpg/1200px-Luxury_hotel_room.jpg", "images/hero/hotel_super_deluxe.webp")
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
        print(f"Failed to download {url}: {r.status_code}")

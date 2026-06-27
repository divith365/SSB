import os
import requests
from PIL import Image
from io import BytesIO

urls = [
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Taj_Mahal_%28Edited%29.jpeg/1200px-Taj_Mahal_%28Edited%29.jpeg", "images/hero/north_1.webp"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Hawa_Mahal_2006.jpg/1200px-Hawa_Mahal_2006.jpg", "images/hero/north_2.webp"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Golden_Temple_at_night_%28Amritsar%29.jpg/1200px-Golden_Temple_at_night_%28Amritsar%29.jpg", "images/hero/north_3.webp"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Qutb_Minar_in_the_monsoons_2017.jpg/1200px-Qutb_Minar_in_the_monsoons_2017.jpg", "images/hero/north_4.webp")
]

headers = {'User-Agent': 'CoolBot/1.0'}

for url, target_path in urls:
    print(f"Downloading {url}...")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        image.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
        image.save(target_path, 'WEBP', quality=80)
        print(f"Saved {target_path}")
    else:
        print(f"Failed {url}, status {response.status_code}")

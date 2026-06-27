import os
import re
import time
import requests
import hashlib
from PIL import Image
from io import BytesIO

# Make sure the images directory exists
os.makedirs('images/optimized', exist_ok=True)

with open('index.html', 'r') as f:
    content = f.read()

# Find all wikimedia urls
urls = set(re.findall(r'(https://upload\.wikimedia\.org/[^\s\'")]+)', content))

print(f"Found {len(urls)} unique external URLs.")

headers = {
    'User-Agent': 'CoolBot/1.0 (contact: test@example.com)'
}

for url in urls:
    try:
        url_clean = url.strip()
        # Create a clean filename hash
        url_hash = hashlib.md5(url_clean.encode()).hexdigest()[:10]
        # Try to extract the original filename
        filename = url_clean.split('/')[-1]
        filename = re.sub(r'^\d+px-', '', filename) # remove 960px- prefix if any
        base_name = os.path.splitext(filename)[0]
        
        local_path = f"images/optimized/{base_name}_{url_hash}.webp"
        
        if os.path.exists(local_path):
            print(f"Already downloaded {local_path}")
            content = content.replace(url, local_path)
            continue
            
        print(f"Downloading {url_clean}...")
        
        # Retry loop
        for attempt in range(3):
            response = requests.get(url_clean, headers=headers, timeout=10)
            if response.status_code == 429:
                print("Rate limited, sleeping 5 seconds...")
                time.sleep(5)
            else:
                break
                
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            # Convert to RGB if needed
            if image.mode in ('RGBA', 'P', 'LA'):
                background = Image.new('RGB', image.size, (255, 255, 255))
                if image.mode == 'RGBA' or image.mode == 'LA':
                    background.paste(image, mask=image.split()[-1])
                else:
                    background.paste(image)
                image = background
            elif image.mode != 'RGB':
                image = image.convert('RGB')
                
            # Resize
            max_size = (1200, 1200)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save
            image.save(local_path, 'WEBP', quality=80)
            
            # Replace in content
            content = content.replace(url, local_path)
            print(f"Successfully optimized and replaced {url_clean} -> {local_path}")
        else:
            print(f"Failed to download {url_clean}: Status {response.status_code}")
            
        time.sleep(1) # Be nice to wikipedia
            
    except Exception as e:
        print(f"Error processing {url}: {e}")

with open('index.html', 'w') as f:
    f.write(content)

print("Done replacing URLs!")

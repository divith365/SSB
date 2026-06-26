import os
import glob
from PIL import Image
import re

# 1. Create directory
os.makedirs('images/hero', exist_ok=True)

# 2. Find and process all 1-18 images
image_files = []
for ext in ('*.jpg', '*.jpeg', '*.png', '*.webp'):
    image_files.extend(glob.glob(ext))

# Filter only those that look like numbers (1 to 18)
hero_images = []
for f in image_files:
    basename = os.path.splitext(f)[0]
    if basename.isdigit():
        hero_images.append((int(basename), f))

hero_images.sort() # sort by number

html_slides = []
for num, filepath in hero_images:
    try:
        with Image.open(filepath) as img:
            # Resize logic (max width 1920)
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
            MAX_WIDTH = 1920
            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_size = (MAX_WIDTH, int(img.height * ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            out_path = f'images/hero/slide_{num}.webp'
            img.save(out_path, 'WEBP', quality=80)
            
            # Create HTML string
            active_class = ' active' if num == 1 else ''
            # For titles we can just put "S.S.B. Package & Holidays"
            html_slides.append(f'    <div class="bg-slide{active_class}" style="background-image: url(\'{out_path}\');" data-title="Incredible India"></div>')
            
            # Remove original
            os.remove(filepath)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace inner HTML of hero-bg-fader
new_fader_html = f'''  <div class="hero-bg-fader" id="heroBgFader">
{chr(10).join(html_slides)}
  </div>'''

# regex to replace the content of heroBgFader
html = re.sub(r'<div class="hero-bg-fader" id="heroBgFader">.*?</div>\n  <div class="hero-overlay">', new_fader_html + '\n  <div class="hero-overlay">', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import os
import re

old_wikimedia_slides = '''    <div class="bg-slide active" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/1920px-Mysore_Palace_Morning.jpg');" data-title="Mysore Palace"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Jog_Falls_05092016.jpg/1920px-Jog_Falls_05092016.jpg');" data-title="Jog Falls"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Murudeshwar_Full_view.jpg/1920px-Murudeshwar_Full_view.jpg'); background-position: top center;" data-title="Murudeshwara"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Entrance_of_Mysore_Zoo.jpg/1920px-Entrance_of_Mysore_Zoo.jpg');" data-title="Mysore Zoo"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tirumala_090615.jpg/1920px-Tirumala_090615.jpg');" data-title="Tirupati Balaji"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alappuzha_Boat_Beauty_W.jpg/1920px-Alappuzha_Boat_Beauty_W.jpg');" data-title="Alleppey Backwaters"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/An_aerial_view_of_Madurai_city_from_atop_of_Meenakshi_Amman_temple.jpg/1920px-An_aerial_view_of_Madurai_city_from_atop_of_Meenakshi_Amman_temple.jpg');" data-title="Madurai Meenakshi Temple"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Boathouse_%287063399547%29.jpg/1920px-Boathouse_%287063399547%29.jpg');" data-title="Kerala Houseboats"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Varkala_beach_from_above.jpg/1920px-Varkala_beach_from_above.jpg');" data-title="Varkala Cliff Beach"></div>'''

# Generate html for slides 4 through 18
new_local_slides = []
for i in range(4, 19):
    new_local_slides.append(f'    <div class="bg-slide" style="background-image: url(\'images/hero/slide_{i}.webp\');" data-title="Incredible India"></div>')

all_slides = old_wikimedia_slides + '\n' + '\n'.join(new_local_slides)

new_fader_html = f'''  <div class="hero-bg-fader" id="heroBgFader">
{all_slides}
  </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove slides 1, 2, 3
for i in range(1, 4):
    path = f'images/hero/slide_{i}.webp'
    if os.path.exists(path):
        os.remove(path)

# Replace the inner html of heroBgFader
html = re.sub(r'<div class="hero-bg-fader" id="heroBgFader">.*?</div>\n  <div class="hero-overlay">', new_fader_html + '\n  <div class="hero-overlay">', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_slides = '''    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tirumala_090615.jpg/1920px-Tirumala_090615.jpg');" data-title="Tirupati Balaji"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Munnar_Overview.jpg/1920px-Munnar_Overview.jpg');" data-title="Munnar, Kerala"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alappuzha_Boat_Beauty_W.jpg/1920px-Alappuzha_Boat_Beauty_W.jpg');" data-title="Alleppey Backwaters"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Ooty_lake.jpg/1920px-Ooty_lake.jpg');" data-title="Ooty Lake"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Boating_in_Kodaikanal_Lake_with_Mist.jpg/1920px-Boating_in_Kodaikanal_Lake_with_Mist.jpg');" data-title="Kodaikanal"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/An_aerial_view_of_Madurai_city_from_atop_of_Meenakshi_Amman_temple.jpg/1920px-An_aerial_view_of_Madurai_city_from_atop_of_Meenakshi_Amman_temple.jpg');" data-title="Madurai Meenakshi Temple"></div>
  </div>'''

html = html.replace('  </div>\n  <div class="hero-overlay"></div>', new_slides + '\n  <div class="hero-overlay"></div>')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

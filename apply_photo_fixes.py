import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Murudeshwara Cut off (it's currently: background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Murudeshwar_Full_view.jpg/1920px-Murudeshwar_Full_view.jpg');")
murudeshwara_old = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Murudeshwar_Full_view.jpg/1920px-Murudeshwar_Full_view.jpg');"
murudeshwara_new = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Murudeshwar_Full_view.jpg/1920px-Murudeshwar_Full_view.jpg'); background-position: center 20%;"
html = html.replace(murudeshwara_old, murudeshwara_new)

# 2. Fix Kanyakumari Bridge (was Unsplash generic photo) -> Use Vivekananda Rock
kanyakumari_old = "background-image: url('https://images.unsplash.com/photo-1592345279419-959d784e8aad?w=1600&q=80');"
kanyakumari_new = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Vivekananda_Rock_Memorial%2C_Kanyakumari.jpg/1920px-Vivekananda_Rock_Memorial%2C_Kanyakumari.jpg');"
html = html.replace(kanyakumari_old, kanyakumari_new)

# 3. Add Pamban Bridge for Rameswaram (replace the old Rameswaram Temple photo)
rameswaram_old = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Ramanathaswamy_temple7.JPG/1920px-Ramanathaswamy_temple7.JPG'); background-position: top center;"
rameswaram_new = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Pamban_Bridge_Train_Passing.jpg/1920px-Pamban_Bridge_Train_Passing.jpg'); background-position: center;"
html = html.replace(rameswaram_old, rameswaram_new)
html = html.replace('data-title="Rameshwaram Temple"', 'data-title="Pamban Bridge, Rameshwaram"')

# 4. Dhanushkodi recent photo
dhanushkodi_old = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Final_Dhanush_002.jpg/1920px-Final_Dhanush_002.jpg');"
dhanushkodi_new = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Road_to_Arichal_Munai.jpg/1920px-Road_to_Arichal_Munai.jpg');"
html = html.replace(dhanushkodi_old, dhanushkodi_new)

# 5. Add more Ooty and Kerala photos at the end of the list
new_slides = '''    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/4/41/NMR_train_at_Ketti_05-02-26_75.jpeg');" data-title="Ooty Toy Train"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Boathouse_%287063399547%29.jpg/1920px-Boathouse_%287063399547%29.jpg');" data-title="Kerala Houseboats"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Varkala_beach_from_above.jpg/1920px-Varkala_beach_from_above.jpg');" data-title="Varkala Cliff Beach"></div>
  </div>'''

if 'data-title="Mullayanagiri"></div>\n  </div>' in html:
    html = html.replace('data-title="Mullayanagiri"></div>\n  </div>', 'data-title="Mullayanagiri"></div>\n' + new_slides)
else:
    # Just insert it before closing hero-bg-fader
    html = html.replace('  </div>\n  <div class="hero-overlay"></div>', new_slides + '\n  <div class="hero-overlay"></div>')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

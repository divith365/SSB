import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove slide 10 (slide_4.webp) and slide 16 (slide_10.webp)
slide_10 = '''    <div class="bg-slide" style="background-image: url('images/hero/slide_4.webp');" data-title="Incredible India"></div>\n'''
slide_16 = '''    <div class="bg-slide" style="background-image: url('images/hero/slide_10.webp');" data-title="Incredible India"></div>\n'''

html = html.replace(slide_10, '')
html = html.replace(slide_16, '')

# 2. Add contain to slide 23 (slide_17.webp)
slide_23_old = '''<div class="bg-slide" style="background-image: url('images/hero/slide_17.webp');" data-title="Incredible India"></div>'''
slide_23_new = '''<div class="bg-slide" style="background-image: url('images/hero/slide_17.webp'); background-size: contain; background-repeat: no-repeat;" data-title="Incredible India"></div>'''
html = html.replace(slide_23_old, slide_23_new)

# 3. Remove light effect from overlay
old_overlay = '''background: linear-gradient(to bottom,rgba(26,18,8,0.65) 0%,rgba(26,18,8,0.3) 60%,rgba(253,248,240,1) 100%);'''
new_overlay = '''background: linear-gradient(to bottom, rgba(26,18,8,0.65) 0%, rgba(26,18,8,0.3) 100%);'''
html = html.replace(old_overlay, new_overlay)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Revert the inline CSS on slide_17.webp
slide_17_old = '''<div class="bg-slide" style="background-image: url('images/hero/slide_17.webp'); background-size: contain; background-repeat: no-repeat;" data-title="Incredible India"></div>'''
slide_17_new = '''<div class="bg-slide" style="background-image: url('images/hero/slide_17.webp');" data-title="Incredible India"></div>'''

html = html.replace(slide_17_old, slide_17_new)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

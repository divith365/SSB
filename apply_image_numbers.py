import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
old_css = ".place-name-overlay { position: absolute; top: 120px; right: 40px; z-index: 3; color: rgba(255,255,255,0.8); font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; transition: opacity 1s ease; font-family: 'Inter', sans-serif; display: flex; align-items: center; gap: 8px; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 20px; backdrop-filter: blur(4px); }"
new_css = ".place-name-overlay { position: absolute; bottom: 40px; right: 40px; z-index: 3; color: rgba(255,255,255,0.8); font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; transition: opacity 1s ease; font-family: 'Inter', sans-serif; display: flex; align-items: center; gap: 8px; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 20px; backdrop-filter: blur(4px); }"
if old_css in html:
    html = html.replace(old_css, new_css)
else:
    print("Warning: CSS not found exactly.")

# 2. Update HTML default state
old_html = '<div class="place-name-overlay" id="placeNameOverlay">&#128205; Mysore Palace</div>'
new_html = '<div class="place-name-overlay" id="placeNameOverlay">Image 1</div>'
if old_html in html:
    html = html.replace(old_html, new_html)

# 3. Update JS logic
old_js = "placeName.innerHTML = '&#128205; ' + slides[currentSlide].getAttribute('data-title');"
new_js = "placeName.innerHTML = 'Image ' + (currentSlide + 1);"
if old_js in html:
    html = html.replace(old_js, new_js)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

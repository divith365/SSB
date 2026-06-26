import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the typo
html = html.replace('    <div class="bg-slide" sty\n', '')

# Append new locations
new_locations = '''    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Annapoorneshwari_Temple%2C_Horanadu.jpg/1920px-Annapoorneshwari_Temple%2C_Horanadu.jpg');" data-title="Horanadu"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/2/2a/Vidyashankara_Temple_at_Shringeri.jpg');" data-title="Sringeri"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Kodachadri.JPG/1920px-Kodachadri.JPG');" data-title="Kodachadri"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/en/3/3a/Chikmagalur_city_on_the_foothills_of_western_ghats.jpg');" data-title="Mullayanagiri"></div>
  </div>'''

html = html.replace('  </div>\n  <div class="hero-overlay"></div>', new_locations + '\n  <div class="hero-overlay"></div>')

# Fix footer
footer_regex = r'<div style="text-align: center; margin-bottom: 20px;">\s*<h3[^>]*>S\.S\.B\. Package & Holidays</h3>\s*<p[^>]*>ಎಸ್\.ಎಸ್\.ಬಿ\. ಪ್ಯಾಕೇಜ್ & ಹಾಲಿಡೇಸ್</p>\s*</div>\s*<div style="text-align: center; margin-bottom: 24px;">\s*<h4[^>]*>Contact</h4>'
if re.search(footer_regex, html):
    html = re.sub(footer_regex, '<div style="text-align: center; margin-bottom: 24px;">', html)
else:
    # Manual fallback if regex fails
    old_footer_exact = '''    <div style="text-align: center; margin-bottom: 20px;">
      <h3 style="margin: 0; color: #FFF; font-size: 20px; letter-spacing: 1px;">S.S.B. Package &amp; Holidays</h3>
      <p style="margin: 5px 0 0; color: #FFD580; font-size: 14px;">ಎಸ್.ಎಸ್.ಬಿ. ಪ್ಯಾಕೇಜ್ &amp; ಹಾಲಿಡೇಸ್</p>
    </div>
    
    <div style="text-align: center; margin-bottom: 24px;">
      <h4 style="margin: 0 0 16px; color: #FFF; font-size: 16px; text-transform: uppercase; letter-spacing: 2px; opacity: 0.8;">Contact</h4>'''
    if old_footer_exact in html:
        html = html.replace(old_footer_exact, '    <div style="text-align: center; margin-bottom: 24px;">')


with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

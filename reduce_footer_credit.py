import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add base .footer-credit CSS
base_css = '''
  .footer-credit { width:100%; text-align:center; margin-top:16px; font-weight:700; font-size:14px; letter-spacing:0.5px; background: linear-gradient(90deg, #FF6B00, #9B4DCA); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  @media(max-width:900px) {'''
html = html.replace('@media(max-width:900px) {', base_css)

# 2. Add mobile .footer-credit CSS inside the @media block
mobile_css = '''
    /* Loader */
    .footer-credit { font-size: 7px; margin-top: 12px; }'''
html = html.replace('/* Loader */', mobile_css)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Desktop overrides
html = html.replace('width:86px; height:86px;', 'width:73px; height:73px;')
html = html.replace('font-size:32px;', 'font-size:27px;')

old_header_pad = '''  header {
    background: linear-gradient(135deg, #FFF9F0 0%, #FFFDF8 40%, #FFF5E6 100%);
    padding: 16px 40px;'''
new_header_pad = '''  header {
    background: linear-gradient(135deg, #FFF9F0 0%, #FFFDF8 40%, #FFF5E6 100%);
    padding: 12px 40px;'''
html = html.replace(old_header_pad, new_header_pad)

# Mobile overrides
old_mobile_pad = '''    /* Header */
    header { padding:12px 18px; }
    nav { display:none; }
    .hamburger { display:flex; }
    .logo-flip-wrap { width:60px; height:60px; }
    .logo-text h1 { font-size:15px; padding-bottom: 4px; }'''
new_mobile_pad = '''    /* Header */
    header { padding:8px 18px; }
    nav { display:none; }
    .hamburger { display:flex; }
    .logo-flip-wrap { width:51px; height:51px; }
    .logo-text h1 { font-size:13px; padding-bottom: 4px; }'''
html = html.replace(old_mobile_pad, new_mobile_pad)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

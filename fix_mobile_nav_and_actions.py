import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move mobile-floating-actions to the right
html = html.replace('.mobile-floating-actions {\n    position: fixed; bottom: 20px; left: 16px; display: none;', 
                    '.mobile-floating-actions {\n    position: fixed; bottom: 20px; right: 16px; display: none;')

# 2. Fix .mobile-nav horizontal scrolling
old_nav_css = '''  .mobile-nav {
    display:none; position:fixed; inset:0; top:0;
    background:rgba(26,18,8,0.97);
    z-index:150; flex-direction:column;
    align-items:center; justify-content:center; gap:14px;
    backdrop-filter:blur(8px);
  }'''

new_nav_css = '''  .mobile-nav {
    display:none; position:fixed; top:0; left:0; width:100%; height:100vh;
    background:rgba(26,18,8,0.97);
    z-index:150; flex-direction:column;
    align-items:center; justify-content:center; gap:14px;
    backdrop-filter:blur(8px);
    overflow-x:hidden;
    box-sizing:border-box;
  }'''

html = html.replace(old_nav_css, new_nav_css)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

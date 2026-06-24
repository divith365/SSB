import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Nav links size and underline
html = html.replace(
    '  nav a { text-decoration:none; color:var(--text); font-size:14px; font-weight:500; transition:color 0.2s; white-space:nowrap; }',
    '  nav a { text-decoration:none; color:var(--text); font-size:16px; font-weight:600; transition:all 0.3s ease; white-space:nowrap; position: relative; }\n  nav a::after { content:""; position:absolute; width:0; height:2px; bottom:-4px; left:0; background-color:var(--saffron); transition:width 0.3s ease; }'
)
html = html.replace(
    '  nav a:hover { color:var(--saffron); }',
    '  nav a:hover { color:var(--saffron); }\n  nav a:hover::after { width:100%; }'
)

# 2. Language Toggle size reduction
lang_old = '''  /* LANGUAGE TOGGLE */
  .lang-toggle {
    display: flex; gap: 4px; border-radius: 40px;
    overflow: hidden;
    border: 2px solid rgba(0,0,0,0.15);
    background: #e0e0e0;
    padding: 4px;
    flex-shrink: 0;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
  }
  .lang-btn {
    padding: 8px 18px; font-size: 14px; font-weight: 800;
    cursor: pointer; border: none; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-family: 'Inter','Noto Sans Kannada', sans-serif;
    background: transparent; color: #555;
    letter-spacing: 0.5px;
    border-radius: 30px;
  }'''

lang_new = '''  /* LANGUAGE TOGGLE */
  .lang-toggle {
    display: flex; gap: 2px; border-radius: 40px;
    overflow: hidden;
    border: 1px solid rgba(0,0,0,0.15);
    background: #e0e0e0;
    padding: 2px;
    flex-shrink: 0;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
  }
  .lang-btn {
    padding: 4px 10px; font-size: 11px; font-weight: 800;
    cursor: pointer; border: none; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-family: 'Inter','Noto Sans Kannada', sans-serif;
    background: transparent; color: #555;
    letter-spacing: 0.5px;
    border-radius: 30px;
  }'''

html = html.replace(lang_old, lang_new)

# 3. Footer padding CSS reduction
html = html.replace(
    'footer { background:var(--dark); color:white; padding:44px 40px 20px; }',
    'footer { background:var(--dark); color:white; padding:24px 40px 16px; }'
)
html = html.replace(
    '.footer-top { display:flex; justify-content:space-between; flex-wrap:wrap; gap:36px; margin-bottom:36px; }',
    '.footer-top { display:flex; justify-content:space-between; flex-wrap:wrap; gap:20px; margin-bottom:24px; }'
)
# Also mobile footer padding
html = html.replace(
    '    footer { padding:32px 16px 16px; }',
    '    footer { padding:24px 16px 16px; }'
)

# 4. Footer HTML updates
old_footer_brand = '''    <div class="footer-brand">
      <h3 data-t="brand_name">S.S.B. Package & Holidays</h3>
      <p data-t="footer_brand_p" style="font-size: 0.8em; opacity: 0.85; line-height: 1.6;">Shirdi Sai Baba Package & Holidays | Nandan Cabs &bull; Authorised by Govt. of Karnataka, Dept. of Tourism &bull; Serving travellers from Bangalore since decades.</p>
    </div>'''
new_footer_brand = '''    <div class="footer-brand">
      <h3 data-t="brand_name">S.S.B. Package & Holidays</h3>
    </div>'''
html = html.replace(old_footer_brand, new_footer_brand)

old_footer_links = '''    <div class="footer-links">
      <h4 data-t="footer_contact_h">Contact</h4>
      <ul>
        <li><a href="tel:9880782128">📞 9880782128</a></li>
        <li><a href="tel:9886859280">📞 9886859280</a></li>
        <li><a href="mailto:sada@ssbholidays.com">✉️ sada@ssbholidays.com</a></li>
        <li><a href="#">🌐 www.ssbholidays.com</a></li>
      </ul>
    </div>'''
new_footer_links = '''    <div class="footer-links">
      <h4 data-t="footer_contact_h">Contact</h4>
      <ul style="display: flex; flex-direction: column; gap: 8px;">
        <li style="display: flex; gap: 12px; align-items: center;"><a href="tel:9880782128">📞 9880782128</a> <span style="opacity: 0.3;">|</span> <a href="tel:9886859280">📞 9886859280</a></li>
        <li style="display: flex; gap: 12px; align-items: center;"><a href="mailto:sada@ssbholidays.com">✉️ sada@ssbholidays.com</a> <span style="opacity: 0.3;">|</span> <a href="#">🌐 www.ssbholidays.com</a></li>
      </ul>
    </div>'''
html = html.replace(old_footer_links, new_footer_links)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

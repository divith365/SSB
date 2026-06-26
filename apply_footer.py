import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS changes
css_old = '.footer-top { display:flex; justify-content:space-between; flex-wrap:wrap; gap:20px; margin-bottom:24px; }'
css_new = '''  .footer-top { display:flex; flex-direction:column; align-items:center; gap:20px; margin-bottom:24px; text-align:center; }
  .phone-link { font-size: 24px !important; font-weight: 800; color: var(--saffron) !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; display: inline-block; opacity: 1 !important; text-decoration: none; }
  .phone-link:hover { color: var(--gold) !important; transform: scale(1.1) translateY(-2px); text-shadow: 0 4px 12px rgba(232,114,42,0.4); }
  .email-link { font-size: 15px !important; color: #ccc !important; transition: all 0.3s ease !important; opacity: 1 !important; text-decoration: none; }
  .email-link:hover { color: white !important; }'''
html = html.replace(css_old, css_new)

# HTML changes
html_old = '''    <div class="footer-links">
      <h4 data-t="footer_contact_h">Contact</h4>
      <ul style="display: flex; flex-direction: column; gap: 8px;">
        <li style="display: flex; gap: 12px; align-items: center;"><a href="tel:9880782128">📞 9880782128</a> <span style="opacity: 0.3;">|</span> <a href="tel:9886859280">📞 9886859280</a></li>
        <li style="display: flex; gap: 12px; align-items: center;"><a href="mailto:sada@ssbholidays.com">✉️ sada@ssbholidays.com</a> <span style="opacity: 0.3;">|</span> <a href="#">🌐 www.ssbholidays.com</a></li>
      </ul>
    </div>'''

html_new = '''    <div class="footer-links" style="width:100%; display:flex; flex-direction:column; align-items:center;">
      <h4 data-t="footer_contact_h" style="font-size:16px;">Contact</h4>
      <ul style="display: flex; flex-direction: column; gap: 12px; align-items: center; padding:0;">
        <li style="display: flex; gap: 16px; align-items: center; justify-content: center; margin-bottom:0;">
          <a href="tel:9880782128" class="phone-link">📞 9880782128</a> 
          <span style="opacity: 0.2; font-size:20px;">|</span> 
          <a href="tel:9886859280" class="phone-link">📞 9886859280</a>
        </li>
        <li style="display: flex; gap: 16px; align-items: center; justify-content: center; margin-bottom:0;">
          <a href="mailto:sada@ssbholidays.com" class="email-link">✉️ sada@ssbholidays.com</a> 
          <span style="opacity: 0.2;">|</span> 
          <a href="https://www.ssbholidays.com" class="email-link">🌐 www.ssbholidays.com</a>
        </li>
      </ul>
    </div>'''

html = html.replace(html_old, html_new)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

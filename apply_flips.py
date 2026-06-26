import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS update
old_css = '''  .why-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; list-style: none; padding: 0; max-width: 800px; margin: 0 auto; }
  .why-list li { font-size: 18px; color: #333; font-weight: 600; display: flex; align-items: center; gap: 12px; padding: 15px 20px; background: #fdf8f0; border-radius: 10px; border: 1px solid #f0e6d2; box-shadow: 0 4px 10px rgba(0,0,0,0.02); transition: transform 0.3s ease; }
  .why-list li:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(220,105,0,0.1); }
  .why-list .tick { color: #DC6900; font-size: 20px; }'''

new_css = '''  .flip-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto; padding: 0 20px; }
  .flip-btn { background: transparent; perspective: 1000px; height: 65px; cursor: pointer; }
  .flip-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s cubic-bezier(0.4, 0.2, 0.2, 1); transform-style: preserve-3d; }
  .flip-btn:hover .flip-inner { transform: rotateY(180deg); }
  .flip-front, .flip-back { position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; border-radius: 35px; }
  .flip-front { background: #fdf8f0; color: #DC6900; border: 2px solid #DC6900; }
  .flip-back { background: linear-gradient(135deg, #DC6900, #ff8c20); color: #FFF; transform: rotateY(180deg); box-shadow: 0 10px 20px rgba(220,105,0,0.3); border: 2px solid transparent; }'''

if old_css in html:
    html = html.replace(old_css, new_css)
else:
    print("Warning: old CSS not found.")

# HTML update
old_html = '''  <ul class="why-list">
    <li><span class="tick">✔️</span> <span data-t="why1_h">Govt. Authorised</span></li>
    <li><span class="tick">✔️</span> <span data-t="why2_h">Luxury Coaches</span></li>
    <li><span class="tick">✔️</span> <span data-t="why3_h">Hotel Options</span></li>
    <li><span class="tick">✔️</span> <span data-t="why4_h">Expert Guides</span></li>
    <li><span class="tick">✔️</span> <span data-t="why5_h">All Inclusive</span></li>
    <li><span class="tick">✔️</span> <span data-t="why6_h">24/7 Support</span></li>
  </ul>'''

new_html = '''  <div class="flip-grid">
    <div class="flip-btn">
      <div class="flip-inner">
        <div class="flip-front"><span data-t="why1_h">Govt. Authorised</span></div>
        <div class="flip-back">Govt. Authorised</div>
      </div>
    </div>
    <div class="flip-btn">
      <div class="flip-inner">
        <div class="flip-front"><span data-t="why2_h">Luxury Coaches</span></div>
        <div class="flip-back">Luxury Coaches</div>
      </div>
    </div>
    <div class="flip-btn">
      <div class="flip-inner">
        <div class="flip-front"><span data-t="why3_h">Hotel Options</span></div>
        <div class="flip-back">Hotel Options</div>
      </div>
    </div>
    <div class="flip-btn">
      <div class="flip-inner">
        <div class="flip-front"><span data-t="why4_h">Expert Guides</span></div>
        <div class="flip-back">Expert Guides</div>
      </div>
    </div>
    <div class="flip-btn">
      <div class="flip-inner">
        <div class="flip-front"><span data-t="why5_h">All Inclusive</span></div>
        <div class="flip-back">All Inclusive</div>
      </div>
    </div>
    <div class="flip-btn">
      <div class="flip-inner">
        <div class="flip-front"><span data-t="why6_h">24/7 Support</span></div>
        <div class="flip-back">24/7 Support</div>
      </div>
    </div>
  </div>'''

if old_html in html:
    html = html.replace(old_html, new_html)
else:
    print("Warning: old HTML not found.")


with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

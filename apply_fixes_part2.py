import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert flip-grid CSS right before CONTACT CSS
flip_css = '''  /* FLIP BUTTONS */
  .flip-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto; padding: 0 20px; }
  .flip-btn { background: transparent; perspective: 1000px; height: 65px; cursor: pointer; }
  .flip-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s cubic-bezier(0.4, 0.2, 0.2, 1); transform-style: preserve-3d; }
  .flip-btn:hover .flip-inner { transform: rotateY(180deg); }
  .flip-front, .flip-back { position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; border-radius: 35px; }
  .flip-front { background: var(--cream); color: var(--deep-saffron); border: 2px solid var(--deep-saffron); }
  .flip-back { background: linear-gradient(135deg, var(--saffron), var(--deep-saffron)); color: #FFF; transform: rotateY(180deg); box-shadow: 0 10px 20px rgba(220,105,0,0.3); border: 2px solid transparent; }

'''

if '.flip-grid {' not in html:
    html = html.replace('  /* CONTACT */', flip_css + '  /* CONTACT */')

# 2. Update Testimonial CSS
old_testi_css = '''  /* TESTIMONIALS */
  .testimonials { padding: 80px 40px; background: #f9f5eb; }
  .testi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }
  .testi-card { background: #FFF; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); position: relative; }
  .testi-card::before { content: '”'; position: absolute; top: 10px; right: 20px; font-size: 80px; color: #f0e6d2; font-family: serif; line-height: 1; }
  .testi-text { font-size: 16px; color: #555; line-height: 1.6; margin-bottom: 20px; font-style: italic; position: relative; z-index: 1; }
  .testi-author { font-weight: 700; color: #1a1208; font-size: 16px; display: flex; align-items: center; gap: 10px; }
  .testi-author::before { content: ''; width: 30px; height: 2px; background: #DC6900; display: inline-block; }
  .testi-rating { color: #FFD580; margin-bottom: 10px; font-size: 14px; letter-spacing: 2px; }'''

new_testi_css = '''  /* TESTIMONIALS */
  .testimonials { padding: 80px 0; background: var(--cream); overflow: hidden; position: relative; }
  .testi-track { display: flex; width: max-content; animation: scrollLeft 25s linear infinite; gap: 30px; padding: 0 20px; }
  .testi-track:hover { animation-play-state: paused; }
  @keyframes scrollLeft {
    0% { transform: translateX(0); }
    100% { transform: translateX(calc(-50% - 15px)); }
  }
  .testi-card { background: #FFF; width: 350px; padding: 35px 30px; border-radius: 40px 0 40px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.05); position: relative; flex-shrink: 0; border: 1px solid rgba(220,105,0,0.1); }
  .testi-card::before { content: '”'; position: absolute; top: 10px; right: 25px; font-size: 90px; color: rgba(220,105,0,0.08); font-family: 'Playfair Display', serif; line-height: 1; }
  .testi-text { font-size: 15px; color: var(--muted); line-height: 1.7; margin-bottom: 25px; font-style: italic; position: relative; z-index: 1; }
  .testi-author { font-weight: 700; color: var(--dark); font-size: 15px; display: flex; align-items: center; gap: 12px; }
  .testi-author::before { content: ''; width: 30px; height: 2px; background: var(--saffron); display: inline-block; }
  .testi-rating { color: var(--saffron); margin-bottom: 15px; font-size: 16px; letter-spacing: 3px; }'''

if old_testi_css in html:
    html = html.replace(old_testi_css, new_testi_css)
else:
    # Just in case we didn't inject old_testi_css properly earlier, let's inject it via replacement of /* CONTACT */
    if '.testi-track {' not in html:
        html = html.replace('  /* CONTACT */', new_testi_css + '\n  /* CONTACT */')

# 3. Update Testimonial HTML Structure
old_testi_html = '''  <div class="testi-grid">
    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"Sadanand was extremely humble and helpful throughout our entire trip. The Tirupathi darshan was completely seamless and stress-free. Highly recommended!"</p>
      <div class="testi-author">Rajesh Kumar</div>
    </div>
    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"Excellent service from S.S.B. Holidays! The luxury coaches were very comfortable and our local guide was incredibly knowledgeable. Will definitely book again."</p>
      <div class="testi-author">Priya Menon</div>
    </div>
    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"A truly blessed and well-organized journey. Sadanand and his team ensured our hotel accommodations were top notch and the 24/7 support gave us great peace of mind."</p>
      <div class="testi-author">Ananya T.</div>
    </div>
  </div>'''

cards_content = '''    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"Sadanand was extremely humble and helpful throughout our entire trip. The Tirupathi darshan was completely seamless and stress-free. Highly recommended!"</p>
      <div class="testi-author">Rajesh Kumar</div>
    </div>
    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"Excellent service from S.S.B. Holidays! The luxury coaches were very comfortable and our local guide was incredibly knowledgeable. Will definitely book again."</p>
      <div class="testi-author">Priya Menon</div>
    </div>
    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"A truly blessed and well-organized journey. Sadanand and his team ensured our hotel accommodations were top notch and the 24/7 support gave us great peace of mind."</p>
      <div class="testi-author">Ananya T.</div>
    </div>
    <div class="testi-card">
      <div class="testi-rating">★★★★★</div>
      <p class="testi-text">"The hill station tour was beyond my expectations. Perfectly coordinated with no hidden costs. Truly all-inclusive as promised!"</p>
      <div class="testi-author">Mohit S.</div>
    </div>'''

new_testi_html = f'''  <div class="testi-track">
{cards_content}
{cards_content}
  </div>'''

if old_testi_html in html:
    html = html.replace(old_testi_html, new_testi_html)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

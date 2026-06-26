import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for why-us list and testimonials
css_updates = '''  .why-us { background:#FFF; }
  .why-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; list-style: none; padding: 0; max-width: 800px; margin: 0 auto; }
  .why-list li { font-size: 18px; color: #333; font-weight: 600; display: flex; align-items: center; gap: 12px; padding: 15px 20px; background: #fdf8f0; border-radius: 10px; border: 1px solid #f0e6d2; box-shadow: 0 4px 10px rgba(0,0,0,0.02); transition: transform 0.3s ease; }
  .why-list li:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(220,105,0,0.1); }
  .why-list .tick { color: #DC6900; font-size: 20px; }

  /* TESTIMONIALS */
  .testimonials { padding: 80px 40px; background: #f9f5eb; }
  .testi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }
  .testi-card { background: #FFF; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); position: relative; }
  .testi-card::before { content: '”'; position: absolute; top: 10px; right: 20px; font-size: 80px; color: #f0e6d2; font-family: serif; line-height: 1; }
  .testi-text { font-size: 16px; color: #555; line-height: 1.6; margin-bottom: 20px; font-style: italic; position: relative; z-index: 1; }
  .testi-author { font-weight: 700; color: #1a1208; font-size: 16px; display: flex; align-items: center; gap: 10px; }
  .testi-author::before { content: ''; width: 30px; height: 2px; background: #DC6900; display: inline-block; }
  .testi-rating { color: #FFD580; margin-bottom: 10px; font-size: 14px; letter-spacing: 2px; }'''

if '.why-list {' not in html:
    html = html.replace('.why-us { background:#FFF; }', css_updates)
elif '.testi-grid {' not in html:
    # Append to existing .why-list if we already modified why-us in a previous thought logic but here we are clean
    pass

# 2. Update HTML for Why Us
why_us_old = '''  <div class="why-grid">
    <div class="why-card"><span class="why-icon">🏛️</span><h3 data-t="why1_h">Govt. Authorised</h3><p data-t="why1_p">Officially authorised by the Government of Karnataka, Department of Tourism. Travel with complete trust and confidence.</p></div>
    <div class="why-card"><span class="why-icon">🚌</span><h3 data-t="why2_h">Luxury Coaches</h3><p data-t="why2_p">Travel in comfort with our luxury 2×2 push-back seat coaches and Mini Luxury Coaches for a relaxed journey.</p></div>
    <div class="why-card"><span class="why-icon">🏨</span><h3 data-t="why3_h">Hotel Options</h3><p data-t="why3_p">Choose from Deluxe, Super Deluxe, Star, Luxury, Home Stay or Resort to suit your budget and preference.</p></div>
    <div class="why-card"><span class="why-icon">🧭</span><h3 data-t="why4_h">Expert Guides</h3><p data-t="why4_p">Knowledgeable local guides at every destination ensure you don't miss any important sight or story.</p></div>
    <div class="why-card"><span class="why-icon">📋</span><h3 data-t="why5_h">All Inclusive</h3><p data-t="why5_p">Hotel accommodation, entrance fees, and guide charges included in most packages. No hidden surprises.</p></div>
    <div class="why-card"><span class="why-icon">📞</span><h3 data-t="why6_h">24/7 Support</h3><p data-t="why6_p">Multiple contact numbers ensure we're always reachable for any assistance during your journey.</p></div>
  </div>'''

why_us_new = '''  <ul class="why-list">
    <li><span class="tick">✔️</span> <span data-t="why1_h">Govt. Authorised</span></li>
    <li><span class="tick">✔️</span> <span data-t="why2_h">Luxury Coaches</span></li>
    <li><span class="tick">✔️</span> <span data-t="why3_h">Hotel Options</span></li>
    <li><span class="tick">✔️</span> <span data-t="why4_h">Expert Guides</span></li>
    <li><span class="tick">✔️</span> <span data-t="why5_h">All Inclusive</span></li>
    <li><span class="tick">✔️</span> <span data-t="why6_h">24/7 Support</span></li>
  </ul>'''

if why_us_old in html:
    html = html.replace(why_us_old, why_us_new)

# 3. Add Testimonials Section
testimonials_section = '''</section>

<!-- TESTIMONIALS -->
<section class="testimonials" id="testimonials">
  <div class="section-title">
    <span class="eyebrow">Happy Travellers</span>
    <h2>What Our Customers Say</h2>
    <div class="divider"></div>
  </div>
  <div class="testi-grid">
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
  </div>
</section>

<!-- CONTACT -->'''

html = html.replace('</section>\n\n<!-- CONTACT -->', testimonials_section)


with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

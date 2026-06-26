import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
old_css = '''  .cat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:18px; max-width:1100px; margin:0 auto; }
  .cat-card { background:var(--cream); border-radius:16px; padding:26px 18px; text-align:center; cursor:pointer; transition:all 0.25s; border:2px solid transparent; }
  .cat-card:hover { border-color:var(--saffron); transform:translateY(-4px); box-shadow:0 8px 24px rgba(232,114,42,0.15); }
  .cat-icon { font-size:32px; display:block; margin-bottom:12px; }
  .cat-card h3 { font-size:14px; font-weight:600; color:var(--dark); margin-bottom:4px; }
  .cat-card p { font-size:12px; color:var(--muted); }'''

new_css = '''  .cat-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:30px; max-width:1200px; margin:0 auto; }
  .cat-card { 
    border-radius: 20px; padding: 30px 24px; text-align: left; cursor: pointer; 
    transition: all 0.4s ease; border: none; height: 280px; position: relative; overflow: hidden;
    display: flex; flex-direction: column; justify-content: flex-end;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1); background: #000;
  }
  .cat-bg {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background-size: cover; background-position: center;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); z-index: 1;
  }
  .cat-overlay {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(to top, rgba(26,18,8,0.95) 0%, rgba(26,18,8,0.1) 100%);
    z-index: 2; transition: opacity 0.4s ease; opacity: 1;
  }
  .cat-overlay-hover {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(to top, rgba(220,105,0,0.95) 0%, rgba(220,105,0,0.2) 100%);
    z-index: 3; transition: opacity 0.4s ease; opacity: 0;
  }
  .cat-card:hover .cat-bg { transform: scale(1.1); }
  .cat-card:hover .cat-overlay { opacity: 0; }
  .cat-card:hover .cat-overlay-hover { opacity: 1; }
  .cat-card:hover { transform:translateY(-5px); box-shadow:0 15px 35px rgba(232,114,42,0.3); }
  .cat-content { position: relative; z-index: 4; color: white; }
  .cat-icon { font-size:36px; display:block; margin-bottom:15px; }
  .cat-card h3 { font-size:22px; font-weight:700; color:white; margin-bottom:6px; }
  .cat-card h3 span { color:rgba(255,255,255,0.85) !important; font-size:14px !important; }
  .cat-card p { font-size:14px; color:rgba(255,255,255,0.9); line-height:1.5; }'''

html = html.replace(old_css, new_css)

# Update Mobile CSS
old_mobile = '.cat-grid { grid-template-columns:repeat(2,1fr); gap:12px; }'
new_mobile = '.cat-grid { grid-template-columns:repeat(1,1fr); gap:20px; }'
html = html.replace(old_mobile, new_mobile)

# 2. Update HTML Structure
old_html = '''  <div class="cat-grid">
    <div class="cat-card"><span class="cat-icon">🛕</span><h3 style="line-height:1.4;">ಯಾತ್ರಾ ಪ್ರವಾಸ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Pilgrimage Tours</span></h3><p data-t="cat1_p">Tirupathi, Shirdi, Rameshwaram & more</p></div>
    <div class="cat-card"><span class="cat-icon">🏔️</span><h3 style="line-height:1.4;">ಗಿರಿಧಾಮ ಪ್ರವಾಸ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Hill Station Tours</span></h3><p data-t="cat2_p">Ooty, Kodai, Munnar, Coorg, Coonur</p></div>
    <div class="cat-card"><span class="cat-icon">💑</span><h3 style="line-height:1.4;">ಹನಿಮೂನ್ ಸ್ಪೆಷಲ್<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Honeymoon Special</span></h3><p data-t="cat3_p">Romantic packages for newlyweds</p></div>
    <div class="cat-card"><span class="cat-icon">🏖️</span><h3 style="line-height:1.4;">ಬೀಚ್ ಪ್ಯಾಕೇಜ್<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Beach Packages</span></h3><p data-t="cat4_p">Goa, Pondicherry, Kanyakumari, Kovalam</p></div>
    <div class="cat-card"><span class="cat-icon">🚢</span><h3 style="line-height:1.4;">ಹೌಸ್‌ಬೋಟ್ ಪ್ರವಾಸ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Houseboat Tours</span></h3><p data-t="cat5_p">Alleppey & Kumarakom backwaters</p></div>
    <div class="cat-card"><span class="cat-icon">🏙️</span><h3 style="line-height:1.4;">ನಗರ ದರ್ಶನ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">City Sightseeing</span></h3><p data-t="cat6_p">Bangalore, Mysore day tours</p></div>
  </div>'''

new_html = '''  <div class="cat-grid">
    <div class="cat-card">
      <div class="cat-bg" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tirumala_090615.jpg/800px-Tirumala_090615.jpg');"></div>
      <div class="cat-overlay"></div><div class="cat-overlay-hover"></div>
      <div class="cat-content">
        <span class="cat-icon">🛕</span>
        <h3 style="line-height:1.4;">ಯಾತ್ರಾ ಪ್ರವಾಸ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Pilgrimage Tours</span></h3>
        <p data-t="cat1_p">Tirupathi, Shirdi, Rameshwaram & more</p>
      </div>
    </div>
    <div class="cat-card">
      <div class="cat-bg" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Munnar_hill_station.jpg/800px-Munnar_hill_station.jpg');"></div>
      <div class="cat-overlay"></div><div class="cat-overlay-hover"></div>
      <div class="cat-content">
        <span class="cat-icon">🏔️</span>
        <h3 style="line-height:1.4;">ಗಿರಿಧಾಮ ಪ್ರವಾಸ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Hill Station Tours</span></h3>
        <p data-t="cat2_p">Ooty, Kodai, Munnar, Coorg, Coonur</p>
      </div>
    </div>
    <div class="cat-card">
      <div class="cat-bg" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Varkala_beach_from_above.jpg/800px-Varkala_beach_from_above.jpg');"></div>
      <div class="cat-overlay"></div><div class="cat-overlay-hover"></div>
      <div class="cat-content">
        <span class="cat-icon">💑</span>
        <h3 style="line-height:1.4;">ಹನಿಮೂನ್ ಸ್ಪೆಷಲ್<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Honeymoon Special</span></h3>
        <p data-t="cat3_p">Romantic packages for newlyweds</p>
      </div>
    </div>
    <div class="cat-card">
      <div class="cat-bg" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Palolem_Beach_Goa.jpg/800px-Palolem_Beach_Goa.jpg');"></div>
      <div class="cat-overlay"></div><div class="cat-overlay-hover"></div>
      <div class="cat-content">
        <span class="cat-icon">🏖️</span>
        <h3 style="line-height:1.4;">ಬೀಚ್ ಪ್ಯಾಕೇಜ್<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Beach Packages</span></h3>
        <p data-t="cat4_p">Goa, Pondicherry, Kanyakumari, Kovalam</p>
      </div>
    </div>
    <div class="cat-card">
      <div class="cat-bg" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Alappuzha_Boat_Beauty_W.jpg/800px-Alappuzha_Boat_Beauty_W.jpg');"></div>
      <div class="cat-overlay"></div><div class="cat-overlay-hover"></div>
      <div class="cat-content">
        <span class="cat-icon">🚢</span>
        <h3 style="line-height:1.4;">ಹೌಸ್‌ಬೋಟ್ ಪ್ರವಾಸ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">Houseboat Tours</span></h3>
        <p data-t="cat5_p">Alleppey & Kumarakom backwaters</p>
      </div>
    </div>
    <div class="cat-card">
      <div class="cat-bg" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/800px-Mysore_Palace_Morning.jpg');"></div>
      <div class="cat-overlay"></div><div class="cat-overlay-hover"></div>
      <div class="cat-content">
        <span class="cat-icon">🏙️</span>
        <h3 style="line-height:1.4;">ನಗರ ದರ್ಶನ<br><span style="font-size:0.8em; color:var(--muted); font-family:'Playfair Display',serif;">City Sightseeing</span></h3>
        <p data-t="cat6_p">Bangalore, Mysore day tours</p>
      </div>
    </div>
  </div>'''

html = html.replace(old_html, new_html)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

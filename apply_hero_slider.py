import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_old = ".hero { min-height:92vh; background:linear-gradient(to bottom,rgba(26,18,8,0.65) 0%,rgba(26,18,8,0.3) 60%,rgba(253,248,240,1) 100%), url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&q=80') center/cover no-repeat; display:flex; align-items:flex-start; padding:100px 40px 40px; position:relative; }"
css_new = '''  .hero { min-height:92vh; display:flex; align-items:flex-start; padding:100px 40px 40px; position:relative; overflow: hidden; background: #000; }
  .hero-bg-slider { position: absolute; top:0; left:0; height: 100%; display:flex; z-index: 0; animation: heroSlide 40s linear infinite; }
  .hero-bg-slide { width: 100vw; height: 100%; object-fit: cover; flex-shrink: 0; }
  .hero-overlay { position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 1; background: linear-gradient(to bottom,rgba(26,18,8,0.65) 0%,rgba(26,18,8,0.3) 60%,rgba(253,248,240,1) 100%); pointer-events: none; }
  .hero-content, .hero-stats { z-index: 2; position: relative; }
  @keyframes heroSlide {
    0% { transform: translateX(0); }
    100% { transform: translateX(calc(-100vw * 4)); }
  }'''

html = html.replace(css_old, css_new)

html_old = '''<div class="hero">
  <div class="hero-content reveal-left">'''
html_new = '''<div class="hero">
  <div class="hero-bg-slider">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/1920px-Mysore_Palace_Morning.jpg" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Jog_Falls_05092016.jpg/1920px-Jog_Falls_05092016.jpg" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Vivekananda_Rock_Memorial%2C_Kanyakumari.jpg/1920px-Vivekananda_Rock_Memorial%2C_Kanyakumari.jpg" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Ramanathaswamy_temple7.JPG/1920px-Ramanathaswamy_temple7.JPG" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/1920px-Mysore_Palace_Morning.jpg" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Jog_Falls_05092016.jpg/1920px-Jog_Falls_05092016.jpg" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Vivekananda_Rock_Memorial%2C_Kanyakumari.jpg/1920px-Vivekananda_Rock_Memorial%2C_Kanyakumari.jpg" class="hero-bg-slide">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Ramanathaswamy_temple7.JPG/1920px-Ramanathaswamy_temple7.JPG" class="hero-bg-slide">
  </div>
  <div class="hero-overlay"></div>
  <div class="hero-content reveal-left">'''
html = html.replace(html_old, html_new)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

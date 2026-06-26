import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS for the new fading slider
css_old = '''  .hero { min-height:92vh; display:flex; align-items:flex-start; padding:100px 40px 40px; position:relative; overflow: hidden; background: #000; }
  .hero-bg-slider { position: absolute; top:0; left:0; height: 100%; display:flex; z-index: 0; animation: heroSlide 40s linear infinite; }
  .hero-bg-slide { width: 100vw; height: 100%; object-fit: cover; flex-shrink: 0; }
  .hero-overlay { position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 1; background: linear-gradient(to bottom,rgba(26,18,8,0.65) 0%,rgba(26,18,8,0.3) 60%,rgba(253,248,240,1) 100%); pointer-events: none; }
  .hero-content, .hero-stats { z-index: 2; position: relative; }
  @keyframes heroSlide {
    0% { transform: translateX(0); }
    100% { transform: translateX(calc(-100vw * 4)); }
  }'''

css_new = '''  .hero { min-height:92vh; display:flex; align-items:flex-start; padding:100px 40px 40px; position:relative; overflow: hidden; background: #000; }
  .hero-bg-fader { position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 0; }
  .bg-slide { position: absolute; top:0; left:0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 2s ease-in-out; transform: scale(1.05); }
  .bg-slide.active { opacity: 1; transform: scale(1); transition: opacity 2s ease-in-out, transform 8s linear; }
  .hero-overlay { position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 1; background: linear-gradient(to bottom,rgba(26,18,8,0.65) 0%,rgba(26,18,8,0.3) 60%,rgba(253,248,240,1) 100%); pointer-events: none; }
  .hero-content, .hero-stats { z-index: 2; position: relative; }
  .place-name-overlay { position: absolute; bottom: 30px; left: 40px; z-index: 3; color: rgba(255,255,255,0.7); font-size: 13px; font-weight: 600; letter-spacing: 3px; text-transform: uppercase; transition: opacity 1s ease; font-family: 'Inter', sans-serif; display: flex; align-items: center; gap: 8px; }
  .place-name-overlay::before { content: ''; display: inline-block; width: 20px; height: 1px; background: rgba(255,255,255,0.7); }'''

html = html.replace(css_old, css_new)

# 2. Update HTML
html_old = '''<div class="hero">
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
  <div class="hero-overlay"></div>'''

html_new = '''<div class="hero">
  <div class="hero-bg-fader" id="heroBgFader">
    <div class="bg-slide active" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Mysore_Palace_Morning.jpg/1920px-Mysore_Palace_Morning.jpg');" data-title="Mysore Palace"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Jog_Falls_05092016.jpg/1920px-Jog_Falls_05092016.jpg');" data-title="Jog Falls"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Thiruvalluvar_Statue_at_Kanyakumari_02.jpg/1920px-Thiruvalluvar_Statue_at_Kanyakumari_02.jpg');" data-title="Kanyakumari"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Ramanathaswamy_temple7.JPG/1920px-Ramanathaswamy_temple7.JPG'); background-position: top center;" data-title="Rameshwaram Temple"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Final_Dhanush_002.jpg/1920px-Final_Dhanush_002.jpg');" data-title="Dhanushkodi Beach"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Shiva_Statue_Murdeshwara_Temple.jpg/1920px-Shiva_Statue_Murdeshwara_Temple.jpg');" data-title="Murudeshwara"></div>
    <div class="bg-slide" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Entrance_of_Mysore_Zoo.jpg/1920px-Entrance_of_Mysore_Zoo.jpg');" data-title="Mysore Zoo"></div>
  </div>
  <div class="hero-overlay"></div>
  <div class="place-name-overlay" id="placeNameOverlay">Mysore Palace</div>'''

html = html.replace(html_old, html_new)

# 3. Update JS Logic (Injecting before Accordion Logic)
js_insert = '''
// HERO BG FADER LOGIC
(function() {
  const slides = document.querySelectorAll('.bg-slide');
  const placeName = document.getElementById('placeNameOverlay');
  if(!slides.length || !placeName) return;
  let currentSlide = 0;
  setInterval(() => {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
    placeName.style.opacity = '0';
    setTimeout(() => {
      placeName.textContent = slides[currentSlide].getAttribute('data-title');
      placeName.style.opacity = '1';
    }, 1000); // Wait for fade out to change text
  }, 6000); // 6 seconds per slide
})();

// SLIDER & ACCORDION LOGIC
'''
html = html.replace('// SLIDER & ACCORDION LOGIC', js_insert.strip() + '\n')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for dots
css_new = '''  .place-name-overlay { position: absolute; top: 120px; right: 40px; z-index: 3; color: rgba(255,255,255,0.8); font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; transition: opacity 1s ease; font-family: 'Inter', sans-serif; display: flex; align-items: center; gap: 8px; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 20px; backdrop-filter: blur(4px); }
  .hero-dots { position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); display: flex; gap: 10px; z-index: 3; }
  .hero-dot { width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.4); cursor: pointer; transition: all 0.3s; }
  .hero-dot.active { background: white; transform: scale(1.3); }'''

if '.hero-dots {' not in html:
    html = html.replace(".place-name-overlay { position: absolute; top: 120px; right: 40px; z-index: 3; color: rgba(255,255,255,0.8); font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; transition: opacity 1s ease; font-family: 'Inter', sans-serif; display: flex; align-items: center; gap: 8px; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 20px; backdrop-filter: blur(4px); }", css_new)

# 2. Add HTML for dots container
html_new = '''  <div class="place-name-overlay" id="placeNameOverlay">&#128205; Mysore Palace</div>
  <div class="hero-dots" id="heroDots"></div>'''

if 'id="heroDots"' not in html:
    html = html.replace('  <div class="place-name-overlay" id="placeNameOverlay">&#128205; Mysore Palace</div>', html_new)

# 3. Update JS Logic
js_old = '''// HERO BG FADER LOGIC
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
      placeName.innerHTML = '&#128205; ' + slides[currentSlide].getAttribute('data-title');
      placeName.style.opacity = '1';
    }, 1000); // Wait for fade out to change text
  }, 6000); // 6 seconds per slide
})();'''

js_new = '''// HERO BG FADER LOGIC
(function() {
  const slides = document.querySelectorAll('.bg-slide');
  const placeName = document.getElementById('placeNameOverlay');
  const dotsContainer = document.getElementById('heroDots');
  if(!slides.length || !placeName || !dotsContainer) return;
  
  let currentSlide = 0;
  let timer;

  // Generate dots
  slides.forEach((_, idx) => {
    const dot = document.createElement('div');
    dot.className = 'hero-dot' + (idx === 0 ? ' active' : '');
    dot.addEventListener('click', () => {
      goToSlide(idx);
      resetTimer();
    });
    dotsContainer.appendChild(dot);
  });
  const dots = document.querySelectorAll('.hero-dot');

  function goToSlide(idx) {
    slides[currentSlide].classList.remove('active');
    dots[currentSlide].classList.remove('active');
    currentSlide = idx;
    slides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');
    
    placeName.style.opacity = '0';
    setTimeout(() => {
      placeName.innerHTML = '&#128205; ' + slides[currentSlide].getAttribute('data-title');
      placeName.style.opacity = '1';
    }, 1000);
  }

  function resetTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
      let nextSlide = (currentSlide + 1) % slides.length;
      goToSlide(nextSlide);
    }, 6000);
  }

  resetTimer();
})();'''

html = html.replace(js_old, js_new)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

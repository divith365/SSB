import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for arrows
css_new = '''  .hero-nav { position: absolute; top: 50%; transform: translateY(-50%); z-index: 3; background: rgba(0,0,0,0.3); color: white; border: none; font-size: 24px; padding: 15px 12px; cursor: pointer; backdrop-filter: blur(4px); transition: all 0.3s; }
  .hero-nav:hover { background: rgba(0,0,0,0.6); transform: translateY(-50%) scale(1.1); }
  .prev-slide { left: 10px; border-radius: 0 5px 5px 0; }
  .next-slide { right: 10px; border-radius: 5px 0 0 5px; }
  @media (max-width: 768px) {
    .hero-nav { padding: 10px 8px; font-size: 18px; }
  }
'''

if '.hero-nav {' not in html:
    html = html.replace('.hero-dots {', css_new + '  .hero-dots {')

# 2. Add HTML for arrows
html_arrows = '''  <div class="hero-dots" id="heroDots"></div>
  <button class="hero-nav prev-slide" id="heroPrev">&#10094;</button>
  <button class="hero-nav next-slide" id="heroNext">&#10095;</button>'''

if 'id="heroPrev"' not in html:
    html = html.replace('  <div class="hero-dots" id="heroDots"></div>', html_arrows)

# 3. Update JS Logic
js_old = '''// HERO BG FADER LOGIC
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

js_new = '''// HERO BG FADER LOGIC
(function() {
  const slides = document.querySelectorAll('.bg-slide');
  const placeName = document.getElementById('placeNameOverlay');
  const dotsContainer = document.getElementById('heroDots');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  
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
    if (idx < 0) idx = slides.length - 1;
    if (idx >= slides.length) idx = 0;
    
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

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      goToSlide(currentSlide - 1);
      resetTimer();
    });
  }
  
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      goToSlide(currentSlide + 1);
      resetTimer();
    });
  }

  function resetTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
      goToSlide(currentSlide + 1);
    }, 6000);
  }

  resetTimer();
})();'''

if js_old in html:
    html = html.replace(js_old, js_new)
else:
    print("Warning: old JS not found. Manual replacement might be needed.")

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

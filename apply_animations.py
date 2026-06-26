import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS UPDATES
css_tours_old = r'\.tours-grid\s*\{\s*display:grid;\s*grid-template-columns:repeat\(auto-fit,minmax\(310px,1fr\)\);\s*gap:24px;\s*max-width:1200px;\s*margin:0 auto;\s*\}'
css_tours_new = '''/* TOUR SLIDER CSS */
.tours-slider-wrapper {
  max-width: 1200px; margin: 0 auto; overflow: hidden; position: relative; padding-bottom: 20px;
}
.tours-slider-track {
  display: flex; gap: 24px; width: max-content; will-change: transform;
}
.tours-slider-track .tour-card {
  width: 320px; flex-shrink: 0; cursor: pointer;
}
.tours-slider-dots {
  display: flex; justify-content: center; gap: 8px; margin-top: 24px; flex-wrap: wrap;
}
.tour-dot {
  width: 10px; height: 10px; border-radius: 50%; background: rgba(0,0,0,0.15); cursor: pointer; transition: all 0.3s;
}
.tour-dot.active {
  background: var(--saffron); transform: scale(1.3);
}
@media (max-width:768px) {
  .tours-slider-track .tour-card { width: 280px; }
}
'''
html = re.sub(css_tours_old, css_tours_new, html)

css_dest_old = r'\.dest-grid\s*\{.*?\}.*?\.dest-card\s*p\s*\{.*?\}'
css_dest_new = '''/* DESTINATIONS ACCORDION GRID */
.dest-accordion { display: flex; gap: 12px; max-width: 1200px; margin: 0 auto; height: 400px; padding: 10px; }
.dest-panel {
  flex: 1; border-radius: 20px; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  color: white; overflow: hidden; transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
  position: relative; cursor: pointer; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  display: flex; flex-direction: column;
}
.dest-panel-content { position: relative; z-index: 2; padding: 20px; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; }
.dest-panel-icon { font-size: 28px; margin-bottom: auto; transition: transform 0.3s; }
.dest-panel h3 {
  font-size: 16px; color: white; margin: 0; white-space: nowrap; writing-mode: vertical-rl;
  transform: rotate(180deg); transition: all 0.5s ease; letter-spacing: 1px;
}
.dest-panel-details { opacity: 0; max-height: 0; transition: opacity 0.3s ease, max-height 0.3s ease; overflow: hidden; }
.dest-panel-details p { font-size: 14px; color: rgba(255,255,255,0.8); line-height: 1.6; margin-top: 10px; white-space: normal; }

.dest-panel:hover, .dest-panel.active { flex: 4; border-color: var(--saffron); box-shadow: 0 0 20px rgba(232, 114, 42, 0.4); }
.dest-panel:hover h3, .dest-panel.active h3 {
  writing-mode: horizontal-tb; transform: none; font-size: 20px; color: var(--saffron);
  white-space: normal; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 8px;
}
.dest-panel:hover .dest-panel-details, .dest-panel.active .dest-panel-details { opacity: 1; max-height: 200px; }
.dest-panel:hover .dest-panel-icon, .dest-panel.active .dest-panel-icon { transform: scale(1.2); margin-bottom: 10px; }

@media (max-width: 768px) {
  .dest-accordion { flex-direction: column; height: auto; }
  .dest-panel { min-height: 80px; }
  .dest-panel h3 { writing-mode: horizontal-tb; transform: none; }
  .dest-panel-icon { position: absolute; right: 20px; top: 20px; margin: 0; }
}
'''
html = re.sub(css_dest_old, css_dest_new, html, flags=re.DOTALL)

# Remove media query rules for old grids
html = re.sub(r'\.tours-grid\s*\{\s*grid-template-columns:1fr;\s*\}', '', html)
html = re.sub(r'\.dest-grid\s*\{\s*grid-template-columns:1fr;\s*\}', '', html)

# 2. HTML UPDATES
html = html.replace('<div class="tours-grid">', '<div class="tours-slider-wrapper" id="toursSliderWrapper"><div class="tours-slider-track" id="toursSliderTrack">')
html = html.replace('<!-- DESTINATIONS -->', '</div><div class="tours-slider-dots" id="toursSliderDots"></div></div>\n<!-- DESTINATIONS -->')

dest_grid_match = re.search(r'<div class="dest-grid">(.*?)</div>\s*</section>', html, re.DOTALL)
if dest_grid_match:
    old_dest_inner = dest_grid_match.group(1)
    new_dest_inner = ''
    cards = re.findall(r'<div class="dest-card"><h3>(.*?) (.*?)</h3><p>(.*?)</p></div>', old_dest_inner)
    for icon, title, desc in cards:
        new_dest_inner += f'''
    <div class="dest-panel">
      <div class="dest-panel-content">
        <div class="dest-panel-icon">{icon}</div>
        <h3>{title}</h3>
        <div class="dest-panel-details"><p>{desc}</p></div>
      </div>
    </div>'''
    html = html.replace('<div class="dest-grid">' + old_dest_inner + '</div>', '<div class="dest-accordion" id="destAccordion">' + new_dest_inner + '\n  </div>')


# 3. JS UPDATES
js_code = '''
// SLIDER & ACCORDION LOGIC
(function() {
  // Slider
  const track = document.getElementById('toursSliderTrack');
  const wrapper = document.getElementById('toursSliderWrapper');
  const dotsContainer = document.getElementById('toursSliderDots');
  if(track && wrapper && dotsContainer) {
    const cards = Array.from(track.querySelectorAll('.tour-card'));
    // Duplicate cards for infinite loop
    cards.forEach(card => track.appendChild(card.cloneNode(true)));
    
    // Create dots
    cards.forEach((_, i) => {
      let dot = document.createElement('div');
      dot.className = 'tour-dot' + (i===0?' active':'');
      dotsContainer.appendChild(dot);
    });
    const dots = dotsContainer.querySelectorAll('.tour-dot');

    let currentX = 0;
    let isPaused = false;
    let speed = 1; // scroll speed
    
    function animate() {
      if(!isPaused) {
        currentX -= speed;
        const cardWidth = cards[0].offsetWidth + 24; 
        const maxScroll = cardWidth * cards.length;
        
        if(Math.abs(currentX) >= maxScroll) {
          currentX = 0;
        }
        track.style.transform = `translateX(${currentX}px)`;

        // Update dot
        let activeIndex = Math.floor(Math.abs(currentX) / cardWidth) % cards.length;
        dots.forEach(d => d.classList.remove('active'));
        if(dots[activeIndex]) dots[activeIndex].classList.add('active');
      }
      requestAnimationFrame(animate);
    }
    
    wrapper.addEventListener('mouseenter', () => isPaused = true);
    wrapper.addEventListener('mouseleave', () => isPaused = false);
    wrapper.addEventListener('touchstart', () => isPaused = true, {passive:true});
    wrapper.addEventListener('touchend', () => isPaused = false);
    wrapper.addEventListener('click', () => isPaused = !isPaused);
    
    animate();
  }

  // Accordion Mobile Support (Active State Toggle)
  document.querySelectorAll('.dest-panel').forEach(panel => {
    panel.addEventListener('click', () => {
      document.querySelectorAll('.dest-panel').forEach(p => p.classList.remove('active'));
      panel.classList.add('active');
    });
  });
})();
'''
html = html.replace('// ── MAIN APP JS ──', js_code + '\n// ── MAIN APP JS ──')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

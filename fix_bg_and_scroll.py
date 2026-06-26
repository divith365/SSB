with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix opacity of gradients so bg images are visible
html = html.replace('linear-gradient(to right, rgba(15,15,25,0.9), rgba(15,15,25,0.85))',
                    'linear-gradient(to right, rgba(15,15,25,0.7), rgba(15,15,25,0.4))')
html = html.replace('linear-gradient(to right, rgba(232,114,42,0.25), rgba(15,15,25,0.8))',
                    'linear-gradient(to right, rgba(232,114,42,0.4), rgba(15,15,25,0.3))')
html = html.replace('linear-gradient(135deg, rgba(232,114,42,0.4) 0%, rgba(15,15,25,0.7) 100%)',
                    'linear-gradient(135deg, rgba(232,114,42,0.6) 0%, rgba(15,15,25,0.2) 100%)')

# 2. Add scroll reveal to the tour explorer items instead of tour-card
old_js = """  document.querySelectorAll('.tour-card').forEach((el, i) => {
    el.classList.add('reveal');
    el.style.transitionDelay = (i * 100) + 'ms';
  });"""
new_js = """  document.querySelectorAll('.tex-menu-item').forEach((el, i) => {
    el.classList.add('reveal-scale');
    el.style.transitionDelay = ((i % 5) * 80) + 'ms';
  });
  document.querySelectorAll('.tex-panel').forEach((el, i) => {
    el.classList.add('reveal-right');
  });"""
html = html.replace(old_js, new_js)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixes applied.")

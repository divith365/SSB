import sys

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

# Add class to the badge
old_div = """<div style="position:absolute;top:45px;left:15px;background:rgba(0,0,0,0.6);color:rgba(255,255,255,0.9);padding:4px 10px;border-radius:6px;font-size:11px;font-weight:600;font-family:'Inter',sans-serif;border:1px solid rgba(255,255,255,0.2);z-index:10;backdrop-filter:blur(4px);letter-spacing:0.5px;">N - Nights | D - Days</div>"""
new_div = """<div class="nd-badge" style="position:absolute;top:45px;left:15px;background:rgba(0,0,0,0.6);color:rgba(255,255,255,0.9);padding:4px 10px;border-radius:6px;font-size:11px;font-weight:600;font-family:'Inter',sans-serif;border:1px solid rgba(255,255,255,0.2);z-index:10;backdrop-filter:blur(4px);letter-spacing:0.5px;">N - Nights | D - Days</div>"""
content = content.replace(old_div, new_div)

# Add CSS for mobile to hide .nd-badge
old_css = """@media (max-width: 768px) {"""
new_css = """@media (max-width: 768px) {
  .nd-badge { display: none !important; }"""
content = content.replace(old_css, new_css)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)

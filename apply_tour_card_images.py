import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS Update: remove the default gradient from .tour-img
html = html.replace('.tour-img { height:160px; background:linear-gradient(135deg,var(--saffron),var(--gold)); position:relative; display:flex; align-items:center; justify-content:center; font-size:48px; }',
                    '.tour-img { height:160px; background-color: #222; position:relative; display:flex; align-items:center; justify-content:center; font-size:48px; background-size: cover !important; background-position: center !important; }')
html = html.replace('.tour-card.featured .tour-img { background:linear-gradient(135deg,#1B6CA8,#0D4A7A); }', '')
html = html.replace('.tour-card.honeymoon .tour-img { background:linear-gradient(135deg,#C0392B,#922B21); }', '')
html = html.replace('.tour-card.beach .tour-img { background:linear-gradient(135deg,#1A8A5A,#0F6040); }', '')

# Replace specific tour-img divs with styled ones
replacements = [
    ('<div class="tour-img">🏙️<span class="tour-badge" data-t="tour_badge_local">Local</span><span class="tour-num">Tour #1</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/city.jpeg\');">🏙️<span class="tour-badge" data-t="tour_badge_local">Local</span><span class="tour-num">Tour #1</span></div>'),
     
    ('<div class="tour-img">🏰<span class="tour-badge" data-t="tour_badge_daytr">Day Tour</span><span class="tour-num">Tour #2</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/hero/slide_4.webp\');">🏰<span class="tour-badge" data-t="tour_badge_daytr">Day Tour</span><span class="tour-num">Tour #2</span></div>'),
     
    ('<div class="tour-img">💑<span class="tour-badge" data-t="tour_badge_honey">Honeymoon Special</span><span class="tour-num">Tour #3</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/honey.jpeg\');">💑<span class="tour-badge" data-t="tour_badge_honey">Honeymoon Special</span><span class="tour-num">Tour #3</span></div>'),
     
    ('<div class="tour-img">🌿<span class="tour-badge" data-t="tour_badge_hill">Hill Station</span><span class="tour-num">Tour #4</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/hill.jpg\');">🌿<span class="tour-badge" data-t="tour_badge_hill">Hill Station</span><span class="tour-num">Tour #4</span></div>'),
     
    ('<div class="tour-img">⛰️<span class="tour-badge" data-t="tour_badge_pop">Popular</span><span class="tour-num">Tour #5</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/hero/slide_5.webp\');">⛰️<span class="tour-badge" data-t="tour_badge_pop">Popular</span><span class="tour-num">Tour #5</span></div>'),
     
    ('<div class="tour-img">🌲<span class="tour-badge" data-t="tour_badge_nat">Nature</span><span class="tour-num">Tour #6</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/hero/slide_6.webp\');">🌲<span class="tour-badge" data-t="tour_badge_nat">Nature</span><span class="tour-num">Tour #6</span></div>'),
     
    ('<div class="tour-img">🛕<span class="tour-badge" data-t="tour_badge_best">Best Seller</span><span class="tour-num">Tour #7</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/piligrim.jpg\');">🛕<span class="tour-badge" data-t="tour_badge_best">Best Seller</span><span class="tour-num">Tour #7</span></div>'),
     
    ('<div class="tour-img">🍃<span class="tour-badge" data-t="tour_badge_kerala">Kerala</span><span class="tour-num">Tour #8</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/hero/slide_7.webp\');">🍃<span class="tour-badge" data-t="tour_badge_kerala">Kerala</span><span class="tour-num">Tour #8</span></div>'),
     
    ('<div class="tour-img">🏖️<span class="tour-badge" data-t="tour_badge_beach">Beach Special</span><span class="tour-num">Tour #9</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/beach.jpg\');">🏖️<span class="tour-badge" data-t="tour_badge_beach">Beach Special</span><span class="tour-num">Tour #9</span></div>'),
     
    ('<div class="tour-img">🗺️<span class="tour-badge" data-t="tour_badge_mega">Mega Tour</span><span class="tour-num">Tour #10</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/hero/slide_8.webp\');">🗺️<span class="tour-badge" data-t="tour_badge_mega">Mega Tour</span><span class="tour-num">Tour #10</span></div>'),
     
    ('<div class="tour-img">🚢<span class="tour-badge" data-t="tour_badge_hboat">Houseboat</span><span class="tour-num">Tour #11</span></div>',
     '<div class="tour-img" style="background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.7)), url(\'images/houseboat.webp\');">🚢<span class="tour-badge" data-t="tour_badge_hboat">Houseboat</span><span class="tour-num">Tour #11</span></div>')
]

for old_tag, new_tag in replacements:
    html = html.replace(old_tag, new_tag)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

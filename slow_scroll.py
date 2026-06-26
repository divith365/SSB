with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Slow down CSS reveal animations
html = html.replace('transition: opacity 0.7s ease, transform 0.7s ease;', 'transition: opacity 1.4s ease, transform 1.4s ease;')
html = html.replace('transition: opacity: 0.7s ease, transform 0.7s ease;', 'transition: opacity 1.4s ease, transform 1.4s ease;')
html = html.replace('transition: opacity 0.65s ease, transform 0.65s ease;', 'transition: opacity 1.4s ease, transform 1.4s ease;')

# Slow down JS delays
html = html.replace('el.style.transitionDelay = (i * 80) + \'ms\';', 'el.style.transitionDelay = (i * 150) + \'ms\';')
html = html.replace('el.style.transitionDelay = ((i % 5) * 80) + \'ms\';', 'el.style.transitionDelay = ((i % 5) * 150) + \'ms\';')
html = html.replace('el.style.transitionDelay = (i * 70) + \'ms\';', 'el.style.transitionDelay = (i * 120) + \'ms\';')
html = html.replace('el.style.transitionDelay = (i * 90) + \'ms\';', 'el.style.transitionDelay = (i * 160) + \'ms\';')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Scroll reveal slow down applied.")

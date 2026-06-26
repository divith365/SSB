import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add transition to header
old_header_css = '''  header {
    background: linear-gradient(135deg, #FFF9F0 0%, #FFFDF8 40%, #FFF5E6 100%);
    padding: 16px 40px;
    display: flex; align-items: center; justify-content: space-between;
    box-shadow: 0 2px 20px rgba(232,114,42,0.12);
    position: sticky; top: 0; z-index: 100;
    overflow: hidden; gap: 16px;
  }'''
new_header_css = '''  header {
    background: linear-gradient(135deg, #FFF9F0 0%, #FFFDF8 40%, #FFF5E6 100%);
    padding: 16px 40px;
    display: flex; align-items: center; justify-content: space-between;
    box-shadow: 0 2px 20px rgba(232,114,42,0.12);
    position: sticky; top: 0; z-index: 100;
    overflow: hidden; gap: 16px;
    transition: transform 0.4s ease, padding 0.4s ease;
  }
  header.header-hidden { transform: translateY(-100%); }
  header.header-shrink { padding: 8px 40px; }
  header.header-shrink .logo-flip-wrap { width: 50px; height: 50px; }
  header.header-shrink .logo-flip-inner-h { width: 50px; height: 50px; }
  header.header-shrink .logo-text h1 { font-size: 20px; }
  header.header-shrink .logo-text .sub-name { font-size: 11px; }'''

if old_header_css in html:
    html = html.replace(old_header_css, new_header_css)

# Add JS logic for scroll at the very end of the file before </body>
scroll_js = '''
<script>
  let lastScrollY = window.scrollY;
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
      header.classList.add('header-shrink');
      if (window.scrollY > lastScrollY) {
        // Scrolling down
        header.classList.add('header-hidden');
      } else {
        // Scrolling up
        header.classList.remove('header-hidden');
      }
    } else {
      header.classList.remove('header-shrink');
      header.classList.remove('header-hidden');
    }
    lastScrollY = window.scrollY;
  });
</script>
</body>'''

html = html.replace('</body>', scroll_js)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

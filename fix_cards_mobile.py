import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for .tex-menu-item to support background images
old_css = """.tex-menu-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px 20px;
  margin: 6px 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  position: relative;
  user-select: none;
  background: rgba(255,255,255,0.04);
}"""

new_css = """.tex-menu-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px 20px;
  margin: 6px 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  position: relative;
  user-select: none;
  background-color: #111;
  background-image: linear-gradient(to right, rgba(15,15,25,0.9), rgba(15,15,25,0.85)), var(--bg-img, none);
  background-size: cover;
  background-position: center;
  overflow: hidden;
}"""
html = html.replace(old_css, new_css)

hover_css = """.tex-menu-item:hover {
  background: rgba(255,255,255,0.08);
  border-color: rgba(232,114,42,0.4);
  transform: translateX(4px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}"""
new_hover = """.tex-menu-item:hover {
  background-image: linear-gradient(to right, rgba(232,114,42,0.25), rgba(15,15,25,0.8)), var(--bg-img, none);
  border-color: rgba(232,114,42,0.6);
  transform: translateX(4px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}"""
html = html.replace(hover_css, new_hover)

active_css = """.tex-menu-item.tex-active {
  background: linear-gradient(135deg, rgba(232,114,42,0.2) 0%, rgba(232,114,42,0.08) 100%);
  border-color: rgba(232,114,42,0.6);
  box-shadow: 0 4px 24px rgba(232,114,42,0.2), inset 0 1px 0 rgba(255,255,255,0.05);
  transform: translateX(4px);
}"""
new_active = """.tex-menu-item.tex-active {
  background-image: linear-gradient(135deg, rgba(232,114,42,0.4) 0%, rgba(15,15,25,0.7) 100%), var(--bg-img, none);
  border-color: var(--saffron);
  box-shadow: 0 4px 24px rgba(232,114,42,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
  transform: translateX(4px);
}"""
html = html.replace(active_css, new_active)

# Update Mobile CSS
old_mobile = ".tex-left { width: 100%; border-right: none; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 16px 0; flex-direction: row; flex-wrap: wrap; overflow-x: auto; }"
new_mobile = ".tex-left { width: 100%; border-right: none; border-bottom: 1px solid rgba(255,255,255,0.06); padding: 16px 0; display: flex; flex-direction: row; flex-wrap: nowrap; overflow-x: auto; overflow-y: hidden; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n  .tex-left::-webkit-scrollbar { display: none; }\n  .tex-menu-item { flex: 0 0 85%; max-width: 300px; margin: 0 8px; }"
html = html.replace(old_mobile, new_mobile)

# Inject background images into the HTML tags
images = {
    'pkg-blr': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Vidhana_Soudha_Bangalore_India.jpg/800px-Vidhana_Soudha_Bangalore_India.jpg",
    'pkg-cab': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Halebeedu_DSW.jpg/800px-Halebeedu_DSW.jpg",
    'pkg-chk': "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Mullayanagiri_Peak.jpg/800px-Mullayanagiri_Peak.jpg",
    'pkg-crg': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Abbey_Falls_Kodagu.jpg/800px-Abbey_Falls_Kodagu.jpg",
    'pkg-mys': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Mysore_Palace_Morning.jpg/800px-Mysore_Palace_Morning.jpg",
    'pkg-ker': "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Munnar_hillstation.jpg/800px-Munnar_hillstation.jpg",
    'pkg-oot': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/800px-Ooty_Lake.jpg",
    'pkg-kod': "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Kodaikanal_Lake.jpg/800px-Kodaikanal_Lake.jpg",
    'pkg-goa': "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Palolem_Beach_Goa_India.jpg/800px-Palolem_Beach_Goa_India.jpg",
    'pkg-alp': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Alleppey_Houseboat.jpg/800px-Alleppey_Houseboat.jpg"
}

for pkg, img in images.items():
    pattern = r'(<div class="tex-menu-item[^"]*" onclick="selectTexPackage\(this,\s*\'{}\'\)")>'.format(pkg)
    html = re.sub(pattern, r'\1 style="--bg-img: url(\'' + img + r'\');">', html)

# Add smooth scroll fix for a href elements starting with #
smooth_scroll_js = """
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if(targetId.length > 1) {
          const target = document.querySelector(targetId);
          if(target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            if (window.closeMobileNav) closeMobileNav();
          }
      }
    });
  });
"""
if smooth_scroll_js not in html:
    html = html.replace('// --- Floating Action Animation ---', smooth_scroll_js + '\n// --- Floating Action Animation ---')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Changes applied!")

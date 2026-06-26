import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix body overflow
html = html.replace('body { font-family:\'Inter\',\'Noto Sans Kannada\',sans-serif; background:var(--cream); color:var(--text); overflow-x:hidden; }', 
                    'html, body { max-width: 100vw; overflow-x: hidden; }\n  body { font-family:\'Inter\',\'Noto Sans Kannada\',sans-serif; background:var(--cream); color:var(--text); overflow-x:hidden; }')

# 2. Replace mobile nav CSS
old_nav_css = '''  .mobile-nav {
    display:none; position:fixed; top:0; left:0; width:100%; height:100vh;
    background:rgba(26,18,8,0.97);
    z-index:150; flex-direction:column;
    align-items:center; justify-content:center; gap:14px;
    backdrop-filter:blur(8px);
    overflow-x:hidden;
    box-sizing:border-box;
  }
  .mobile-nav.open { display:flex; animation:fadeInDown 0.3s ease; }
  @keyframes fadeInDown { from{opacity:0;transform:translateY(-20px)} to{opacity:1;transform:translateY(0)} }
  .mobile-nav a {
    text-decoration:none; color:white; font-size:12px; font-weight:600;
    font-family:'Playfair Display',serif;
    transition:color 0.2s;
    padding:4px 0;
  }
  .mobile-nav a:hover { color:var(--gold); }
  .mobile-nav .call-btn { background:var(--saffron); color:white!important; padding:8px 20px; border-radius:8px; font-size:11px!important; }
  .mobile-nav-close { position:absolute; top:24px; right:24px; font-size:27px; color:white; cursor:pointer; background:none; border:none; line-height:1; }'''

new_nav_css = '''  .mobile-nav {
    display:none; position:fixed; top:70px; right:16px; width:220px; height:auto;
    background:rgba(255,255,255,0.98);
    z-index:150; flex-direction:column;
    align-items:flex-start; justify-content:flex-start; gap:8px;
    border-radius:12px; padding:16px;
    box-shadow:0 8px 32px rgba(0,0,0,0.15);
    border:1px solid rgba(0,0,0,0.05);
  }
  .mobile-nav.open { display:flex; animation:fadeInDown 0.2s ease; }
  @keyframes fadeInDown { from{opacity:0;transform:translateY(-10px)} to{opacity:1;transform:translateY(0)} }
  .mobile-nav a {
    text-decoration:none; color:var(--text); font-size:14px; font-weight:600;
    font-family:'Inter',sans-serif;
    transition:color 0.2s;
    padding:8px 0; width:100%; border-bottom:1px solid rgba(0,0,0,0.05);
  }
  .mobile-nav a:last-child { border-bottom:none; }
  .mobile-nav a:hover { color:var(--saffron); }
  .mobile-nav .call-btn { background:var(--saffron); color:white!important; padding:10px; border-radius:8px; font-size:13px!important; text-align:center; margin-top:8px; border-bottom:none; }
  .mobile-nav-close { display:none; }'''

html = html.replace(old_nav_css, new_nav_css)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

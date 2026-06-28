import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Move <button> inside <div class="tex-panel-hero">
pattern = r'(<button [^>]*onclick="document\.getElementById\(\'texModalOverlay[^>]+\>.*?&times;</button>)\s*(<div class="tex-panel-hero[^>]*>)'
content = re.sub(pattern, r'\2\n            \1', content)

# 2. Update .tex-tab-coin CSS from top to bottom
content = re.sub(
    r'top:\s*15px;\s*left:\s*15px;\s*bottom:\s*auto;\s*right:\s*auto;',
    r'bottom: 15px;\n  left: 15px;\n  top: auto;\n  right: auto;',
    content
)

# 3. Update the close button inline style
content = re.sub(
    r'style="position: absolute; top: 15px; right: 15px;',
    r'style="position: absolute; bottom: 15px; right: 15px; top: auto;',
    content
)

# 4. Update the CSS block overrides (.tex-panel > button -> .tex-panel-hero > button)
content = re.sub(
    r'\.tex-panel > button \{ top: \d+px !important; right: \d+px !important;',
    r'.tex-panel-hero > button { bottom: 15px !important; right: 15px !important; top: auto !important;',
    content
)

# 5. Fix JS to show '#1a' instead of '1a'
content = re.sub(r'coin\.textContent=\'(\d+[a-z])\';', r"coin.textContent='#\1';", content)

# 6. Fix HTML hardcoded '1a', '2a', etc. in .tex-tab-coin
# Example: <div class="tex-tab-coin coin-1a" id="blr-coin">1a</div> -> #1a
content = re.sub(r'(<div class="tex-tab-coin[^>]*>)(\d+[a-z])(</div>)', r'\1#\2\3', content)

# 7. Update mobile padding to shift space to bottom
content = re.sub(
    r'padding: 55px 16px 12px !important;',
    r'padding: 24px 16px 60px !important;',
    content
)

# 8. Update global padding to shift space to bottom
content = re.sub(
    r'padding: 32px 24px 16px;',
    r'padding: 24px 24px 60px;',
    content
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Update completed.")

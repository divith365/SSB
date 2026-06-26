import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Base CSS update to inherit colors for a tags
html = html.replace('.footer-credit { width:100%;', '.footer-credit a { color: inherit; text-decoration: none; }\n  .footer-credit a:hover { text-decoration: underline; }\n  .footer-credit { width:100%;')

# Mobile CSS update (increase font size by ~30% from 7px to 9.5px)
html = html.replace('.footer-credit { font-size: 7px; margin-top: 12px; }',
                    '.footer-credit { font-size: 9.5px; margin-top: 12px; }')

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove tour-includes lines
content = re.sub(r'\n\s*<div class="tour-includes">.*?</div\s*>', '', content)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

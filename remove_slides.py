import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove specific slides
titles_to_remove = [
    '"Pamban Bridge, Rameshwaram"',
    '"Kanyakumari"',
    '"Dhanushkodi Beach"'
]

lines = html.splitlines()
new_lines = []
for line in lines:
    should_remove = False
    for title in titles_to_remove:
        if f'data-title={title}' in line:
            should_remove = True
            break
    
    if not should_remove:
        new_lines.append(line)

html = '\n'.join(new_lines)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

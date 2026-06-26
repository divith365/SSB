import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove specific slides
titles_to_remove = [
    '"Munnar, Kerala"',
    '"Ooty Lake"',
    '"Kodaikanal"',
    '"Horanadu"',
    '"Sringeri"',
    '"Kodachadri"',
    '"Mullayanagiri"',
    '"Ooty Toy Train"'
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

# 2. Adjust Murudeshwara
murudeshwara_old = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Murudeshwar_Full_view.jpg/1920px-Murudeshwar_Full_view.jpg'); background-position: center 20%;"
murudeshwara_new = "background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Murudeshwar_Full_view.jpg/1920px-Murudeshwar_Full_view.jpg'); background-position: top center;"
html = html.replace(murudeshwara_old, murudeshwara_new)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

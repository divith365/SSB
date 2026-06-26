import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken line
broken_line = "    <div class=\"bg-slide\" style=\"background-image: url('https://upload.wi\n"
if broken_line in html:
    html = html.replace(broken_line, "")

# Also, there might be another broken line from earlier diff
broken_line_2 = "    <div class=\"bg-slide\" sty\n"
if broken_line_2 in html:
    html = html.replace(broken_line_2, "")
    
# check for exact broken strings
html = re.sub(r'^\s*<div class="bg-slide" style="background-image: url\(\'https://upload\.wi\s*$', '', html, flags=re.MULTILINE)
html = re.sub(r'^\s*<div class="bg-slide" sty\s*$', '', html, flags=re.MULTILINE)


with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

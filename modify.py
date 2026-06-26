import re

with open('/home/arun/SSB/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove tour-footer
pattern_footer = r'\n\s*<div class="tour-footer">\s*<div>.*?</div>\s*<a href="#contact".*?</a>\s*</div>'
content = re.sub(pattern_footer, '', content, flags=re.DOTALL)

# Renumber Tour #
counter = 1
def replace_tour_num(match):
    global counter
    res = f'<span class="tour-num">Tour #{counter}</span>'
    counter += 1
    return res

content = re.sub(r'<span class="tour-num">Tour #\d+</span>', replace_tour_num, content)

with open('/home/arun/SSB/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

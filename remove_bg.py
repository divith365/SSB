import sys
import re

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

# Remove the inline background-image styles from the tour-explorer divs
# Example: style="background-image: url('...');"
pattern = r'(<div class="tour-explorer"[^>]+?)\s*style="background-image:\s*url\([^)]+\);"'
new_content = re.sub(pattern, r'\1', content)

# Check if there are other variations of background-image inline styles
pattern2 = r'(<div class="tour-explorer"[^>]+?)\s*style=\'background-image:\s*url\([^)]+\);\''
new_content = re.sub(pattern2, r'\1', new_content)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(new_content)

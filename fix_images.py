import sys
import re

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

# Fix broken image links that were repeated placeholders
broken_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ooty_Lake.jpg/960px-Ooty_Lake.jpg"
valid_urls = [
    "images/hero/slide_5.webp",
    "images/hero/slide_6.webp",
    "images/hero/slide_7.webp",
    "images/hero/slide_8.webp",
    "images/hero/slide_9.webp",
    "images/hero/slide_11.webp"
]

# We need to replace occurrences of broken_url with different valid URLs
def replacer(match):
    replacer.counter += 1
    # Pick a valid url circularly
    idx = replacer.counter % len(valid_urls)
    return valid_urls[idx]

replacer.counter = 0

content = re.sub(re.escape(broken_url), replacer, content)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(content)

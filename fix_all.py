import re

with open('/home/arun/SSB/index.html', 'r') as f:
    content = f.read()

valid_images = [
    "images/hero/slide_4.webp", "images/hero/slide_5.webp",
    "images/hero/slide_6.webp", "images/hero/slide_7.webp",
    "images/hero/slide_8.webp", "images/hero/slide_9.webp",
    "images/hero/slide_11.webp", "images/hero/slide_12.webp",
    "images/hero/slide_13.webp", "images/hero/slide_14.webp",
    "images/hero/slide_15.webp", "images/hero/slide_16.webp",
    "images/hero/slide_17.webp", "images/hero/slide_18.webp",
    "images/beach.jpg", "images/city.jpeg", "images/hill.jpg",
    "images/honey.jpeg", "images/houseboat.webp", "images/piligrim.jpg"
]

def replacer(match):
    replacer.counter += 1
    idx = replacer.counter % len(valid_images)
    return f"url('{valid_images[idx]}')"

replacer.counter = 0

# Replace any url('...') that contains wikimedia or optimized
# Note: we need to handle both single and double quotes, or no quotes, but the code uses single quotes mostly
pattern = r"url\(['\"]?(https://upload\.wikimedia\.org/[^'\"]+|images/optimized/[^'\"]+)['\"]?\)"

new_content = re.sub(pattern, replacer, content)

with open('/home/arun/SSB/index.html', 'w') as f:
    f.write(new_content)

print("Replaced all broken links.")

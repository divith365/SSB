from PIL import Image, ImageDraw
import sys

img_path = "/home/arun/.gemini/antigravity/brain/1040c929-406a-4e3e-aceb-677fc95e2b1c/media__1782498908338.jpg"
try:
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    print(f"Size: {w}x{h}")

    # Create a circular mask
    # The inner circle appears to be about 65% of the total radius
    # We will crop an inner square and mask it as a circle
    cx, cy = w // 2, h // 2
    r = int(min(w, h) * 0.35)  # 70% of half-width

    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)

    img.putalpha(mask)
    cropped = img.crop((cx - r, cy - r, cx + r, cy + r))

    out_path = "/home/arun/SSB/images/sai_center.png"
    cropped.save(out_path)
    print("Saved cropped image to", out_path)
except Exception as e:
    print("Error:", e)

import os
import glob
from PIL import Image, ImageEnhance

image_dir = 'images/hero'
webp_files = glob.glob(os.path.join(image_dir, '*.webp'))

for file_path in webp_files:
    try:
        with Image.open(file_path) as img:
            # 1. Enhance Color (Saturation)
            color_enhancer = ImageEnhance.Color(img)
            img = color_enhancer.enhance(1.3) # 30% more colorful
            
            # 2. Enhance Contrast
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(1.15) # 15% more contrast
            
            # 3. Enhance Brightness slightly
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(1.05) # 5% brighter
            
            # Save back to the same file
            img.save(file_path, 'WEBP', quality=85)
            print(f"Enhanced {file_path}")
    except Exception as e:
        print(f"Failed to enhance {file_path}: {e}")

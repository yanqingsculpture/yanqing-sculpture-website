"""Compress all JPG images to WebP format, max 1200px wide, quality 80."""
import os
from PIL import Image

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
MAX_SIZE = 1200
QUALITY = 80

total_before = 0
total_after = 0
count = 0

for fname in sorted(os.listdir(IMG_DIR)):
    if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        fpath = os.path.join(IMG_DIR, fname)
        before = os.path.getsize(fpath)
        
        img = Image.open(fpath).convert('RGB')
        w, h = img.size
        
        # Resize if wider than MAX_SIZE
        if w > MAX_SIZE:
            ratio = MAX_SIZE / w
            new_size = (MAX_SIZE, int(h * ratio))
            img = img.resize(new_size, Image.LANCZOS)
            w, h = new_size
        
        # Save as WebP
        webp_name = os.path.splitext(fname)[0] + '.webp'
        webp_path = os.path.join(IMG_DIR, webp_name)
        img.save(webp_path, 'WEBP', quality=QUALITY)
        
        after = os.path.getsize(webp_path)
        total_before += before
        total_after += after
        count += 1
        
        pct = (1 - after / before) * 100
        print(f"{fname:30s} {before/1024:>8.1f}KB -> {after/1024:>8.1f}KB  (-{pct:.0f}%)")

print(f"\n总压缩: {total_before/1024/1024:.1f}MB -> {total_after/1024/1024:.1f}MB  (节省 {(1-total_after/total_before)*100:.0f}%)")
print(f"处理 {count} 张图片完成!")

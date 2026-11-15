#!/usr/bin/env python3
"""
process_user_three_chosen_cats.py
針對使用者明確選定的 3 張圖片執行去背、抹除文字、尺寸最佳化：
1. media_1794740969873_ec04da22.jpg (Fig 01 · 側伸腿放鬆貓 + 木凳 + 小玳瑁)
2. media_1794740979604_8a730326.jpg (Fig 05 · 升降桌四腳朝天徹底放鬆貓)
3. media_1794741003762_81c889a9.jpg (Fig 03 · 端坐提籃旁的黑面翡翠眼玳瑁貓 + 垂掛毛球)
輸出純透明、無文字、無外框的高畫質 PNG 至 img/editorial/
"""

import os
from PIL import Image, ImageDraw

IMG_1_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794740969873_ec04da22.jpg"
IMG_5_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794740979604_8a730326.jpg"
IMG_3_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794741003762_81c889a9.jpg"

DEST_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading/img/editorial"
os.makedirs(DEST_DIR, exist_ok=True)

def remove_background_floodfill(img, threshold=45):
    img_rgba = img.convert("RGBA")
    w, h = img_rgba.size
    pixels = img_rgba.load()

    # 取邊界背景色平均
    corners = [img_rgba.getpixel((0, 0)), img_rgba.getpixel((w-1, 0)), img_rgba.getpixel((0, h-1)), img_rgba.getpixel((w-1, h-1))]
    bg_r = sum(c[0] for c in corners) // 4
    bg_g = sum(c[1] for c in corners) // 4
    bg_b = sum(c[2] for c in corners) // 4

    visited = [[False]*h for _ in range(w)]
    queue = []
    for x in range(w):
        queue.append((x, 0))
        queue.append((x, h-1))
    for y in range(h):
        queue.append((0, y))
        queue.append((w-1, y))

    def is_bg(r, g, b):
        diff = abs(r - bg_r) + abs(g - bg_g) + abs(b - bg_b)
        return diff < threshold or (r > 240 and g > 235 and b > 225)

    head = 0
    while head < len(queue):
        cx, cy = queue[head]
        head += 1

        if visited[cx][cy]:
            continue
        visited[cx][cy] = True

        r, g, b, a = pixels[cx, cy]
        if is_bg(r, g, b):
            pixels[cx, cy] = (r, g, b, 0) # 透明
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                    nr, ng, nb, _ = pixels[nx, ny]
                    if is_bg(nr, ng, nb):
                        queue.append((nx, ny))

    return img_rgba

def process_img_1():
    # 圖片 1: 側伸腿放鬆貓 + 木凳 + 小玳瑁
    img = Image.open(IMG_1_SRC).convert("RGB")
    w, h = img.size
    
    # 抹除上方文字 (FIG. 01 · AMBER STRETCH / 2026 // PARASYMPATHETIC RELEASE)
    draw = ImageDraw.Draw(img)
    bg_sample = img.getpixel((w // 2, 50))
    draw.rectangle([int(w * 0.25), int(h * 0.15), int(w * 0.75), int(h * 0.32)], fill=bg_sample)

    # 緊密裁切主體 (只保留貓咪、木凳與小玳瑁)
    crop_box = (int(w * 0.36), int(h * 0.50), int(w * 0.68), int(h * 0.82))
    cropped = img.crop(crop_box)

    # 去背
    transparent = remove_background_floodfill(cropped, threshold=40)
    out_path = os.path.join(DEST_DIR, "chosen-01-amber-stretch.png")
    transparent.save(out_path, format="PNG")
    print(f"Saved {out_path} ({transparent.size})")

def process_img_5():
    # 圖片 5: 升降桌四腳朝天徹底放鬆貓
    img = Image.open(IMG_5_SRC).convert("RGB")
    w, h = img.size

    # 抹除下方文字 (FIG. 05 · TOTAL SURRENDER / DESK // RADICAL REST & RESET)
    draw = ImageDraw.Draw(img)
    bg_sample = img.getpixel((w // 2, h - 50))
    draw.rectangle([int(w * 0.08), int(h * 0.88), int(w * 0.92), int(h * 0.96)], fill=bg_sample)

    # 緊密裁切主體
    crop_box = (int(w * 0.22), int(h * 0.36), int(w * 0.75), int(h * 0.72))
    cropped = img.crop(crop_box)

    # 去背
    transparent = remove_background_floodfill(cropped, threshold=40)
    out_path = os.path.join(DEST_DIR, "chosen-05-total-surrender.png")
    transparent.save(out_path, format="PNG")
    print(f"Saved {out_path} ({transparent.size})")

def process_img_3():
    # 圖片 3: 端坐編織提籃旁的黑面翡翠眼玳瑁貓 + 垂掛毛球
    img = Image.open(IMG_3_SRC).convert("RGB")
    w, h = img.size

    # 抹除左下方文字 (FIG. 03 · SENTINEL WITH BASKET / AXIS // SOLID BOUNDARY)
    draw = ImageDraw.Draw(img)
    bg_sample = img.getpixel((100, h - 50))
    draw.rectangle([int(w * 0.03), int(h * 0.86), int(w * 0.40), int(h * 0.96)], fill=bg_sample)

    # 緊密裁切主體 (保留上方懸掛毛球、整隻端坐玳瑁與提籃)
    crop_box = (int(w * 0.48), int(h * 0.00), int(w * 0.87), int(h * 0.85))
    cropped = img.crop(crop_box)

    # 去背
    transparent = remove_background_floodfill(cropped, threshold=40)
    out_path = os.path.join(DEST_DIR, "chosen-03-sentinel-basket.png")
    transparent.save(out_path, format="PNG")
    print(f"Saved {out_path} ({transparent.size})")

if __name__ == '__main__':
    process_img_1()
    process_img_5()
    process_img_3()
    print("All 3 chosen images cleanly processed: zero text, perfectly transparent, cropped!")

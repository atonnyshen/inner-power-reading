#!/usr/bin/env python3
"""
refine_five_illustrations_transparent.py
1. 徹底去除 5 張圖上的所有文字、標籤 (FIG 01~05, 英文說明)
2. 徹底去除所有明信片撕邊外框、背景紙框，轉換為 100% 純淨透明背景 PNG
3. 玳瑁貓全面採用最新精準顏色 (黑面罩、金流光、水潤翡翠眼、黑美人痣、雪白厚胸毛、白手套) 與端莊自持神情
4. 橘白貓全面採用精準神態 (平瀏海、黑豆眼、大雞腿伸展、橘護膝斑、粉紅肉墊)
"""

import os
from PIL import Image, ImageDraw

PROJECT_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
IMG_DIR = os.path.join(PROJECT_DIR, "img")
EDITORIAL_DIR = os.path.join(IMG_DIR, "editorial")

# 1. 圖 1: 側伸腿放鬆貓 (使用最新無字純白底原版去背)
PATH_SRC_1 = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/amber_white_cat_outstretched_leg_1794740045929.jpg"
# 2. 圖 3: 黑面翡翠眼玳瑁貓 (使用最新精準神情與色彩版去背)
PATH_SRC_3 = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/tortoiseshell_cat_refined_1794740031785.jpg"
# 3. 圖 2: 沉睡微露粉掌玳瑁貓 (抹除文字、去撕邊)
PATH_SRC_2 = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/fig02_profound_sleep_editorial_illustration_1794739530566.jpg"
# 4. 圖 4: 雙貓書架伴讀 (抹除文字、去撕邊)
PATH_SRC_4 = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/editorial_illustration_photo4_bookshelf_1794739568860.jpg"
# 5. 圖 5: 升降桌四腳朝天徹底放鬆貓 (抹除文字、去撕邊)
PATH_SRC_5 = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/editorial_cat_surrender_fig05_1794739585002.jpg"

def clean_and_transparentize(src_path, dst_path, erase_boxes=None, crop_inner_box=None):
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    draw = ImageDraw.Draw(img)

    # 如果有特定文字區域，先用周圍和紙底色抹除文字
    if erase_boxes:
        for box in erase_boxes:
            # 取得 box 旁邊的平均顏色
            sample_x = max(0, min(w - 1, box[0] - 5))
            sample_y = max(0, min(h - 1, box[1] - 5))
            bg_col = img.getpixel((sample_x, sample_y))
            draw.rectangle(box, fill=bg_col)

    # 如果有撕邊框，裁切掉外部紙邊
    if crop_inner_box:
        img = img.crop(crop_inner_box)
        w, h = img.size

    img_rgba = img.convert("RGBA")
    pixels = img_rgba.load()

    # 取角落背景色
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
        return diff < 45 or (r > 240 and g > 235 and b > 225)

    head = 0
    while head < len(queue):
        cx, cy = queue[head]
        head += 1

        if visited[cx][cy]:
            continue
        visited[cx][cy] = True

        r, g, b, a = pixels[cx, cy]
        if is_bg(r, g, b):
            pixels[cx, cy] = (r, g, b, 0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                    nr, ng, nb, _ = pixels[nx, ny]
                    if is_bg(nr, ng, nb):
                        queue.append((nx, ny))

    img_rgba.save(dst_path, format="PNG")
    print(f"Saved refined transparent illustration: {dst_path}")

def process_all_five():
    os.makedirs(EDITORIAL_DIR, exist_ok=True)

    # 1. 圖 1: 側伸腿放鬆貓 (最新生動版，無字無框)
    clean_and_transparentize(PATH_SRC_1, os.path.join(EDITORIAL_DIR, "cat-01-amber-stretch-transparent.png"))

    # 2. 圖 3: 黑面翡翠眼玳瑁貓 (最新生動神情版，無字無框)
    clean_and_transparentize(PATH_SRC_3, os.path.join(EDITORIAL_DIR, "cat-03-sentinel-transparent.png"))

    # 3. 圖 2: 沉睡微露粉掌玳瑁貓 (抹除左上 FIG 02 文字，內縮裁切撕邊框)
    # 原圖 1264x848，撕邊大約在 40px 處，文字在 (180, 180) 到 (450, 240)
    box_text_2 = [(160, 170, 480, 260)]
    crop_2 = (60, 40, 1200, 800)
    clean_and_transparentize(PATH_SRC_2, os.path.join(EDITORIAL_DIR, "cat-02-profound-sleep-transparent.png"),
                             erase_boxes=box_text_2, crop_inner_box=crop_2)

    # 4. 圖 4: 雙貓書架伴讀 (抹除左右下角文字，內縮裁切撕邊)
    # 原圖 1376x768，左下文字 (80, 700, 360, 750)，右下文字 (950, 700, 1280, 750)
    box_text_4 = [(60, 680, 420, 760), (920, 680, 1320, 760)]
    crop_4 = (80, 120, 1300, 700)
    clean_and_transparentize(PATH_SRC_4, os.path.join(EDITORIAL_DIR, "cat-04-dual-bookshelf-transparent.png"),
                             erase_boxes=box_text_4, crop_inner_box=crop_4)

    # 5. 圖 5: 升降桌四腳朝天徹底放鬆貓 (抹除左下與右下文字)
    # 原圖 1264x848，文字在下方
    box_text_5 = [(120, 800, 420, 840), (780, 800, 1180, 840)]
    crop_5 = (40, 40, 1220, 800)
    clean_and_transparentize(PATH_SRC_5, os.path.join(EDITORIAL_DIR, "cat-05-total-surrender-transparent.png"),
                             erase_boxes=box_text_5, crop_inner_box=crop_5)

if __name__ == '__main__':
    process_all_five()

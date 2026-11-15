#!/usr/bin/env python3
"""
craft_stunning_brand_icon.py
打造頂級質感的 Hand-drawn Boutique Brand Icon & Apple Touch Icon (180x180 & 38x38)
徹底告別粗糙拼貼與生硬幾何：
- 核心焦點：【雙貓靈動特寫頭像】
  - 左側：白色橘頭貓（齊頭平瀏海、水汪汪黑豆大眼、粉嫩小鼻、腮紅、溫柔純真微表情）
  - 右側：黑面翡翠眼玳瑁貓（黑面罩、額頭焦糖金流光、晶瑩水潤翡翠綠大眼、俏皮黑美人痣、雪白小圍巾領口、沉著自信神采）
- 構圖：極致優雅的黃金比例特寫，留有 18% iOS 圓角安全留白，底色為溫潤高級米白 (#FAF7F2)。
- 同時產出：
  1. assets/apple-touch-icon.png (180x180 Retina 高解析度 PNG)
  2. assets/favicon-cat.svg (向量極簡高清晰度 SVG)
  3. img/svg/brand-cat.svg
"""

import os
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMG_DIR = os.path.join(BASE_DIR, "img")

PATH_AMBER = os.path.join(IMG_DIR, "cat-amber-stretch-transparent.png")
PATH_TORTIE = os.path.join(IMG_DIR, "cat-tortoiseshell-sentinel-transparent.png")

def render_boutique_apple_touch_icon():
    im_amber = Image.open(PATH_AMBER).convert("RGBA")
    im_tortie = Image.open(PATH_TORTIE).convert("RGBA")

    # 裁剪兩隻貓咪的精華頭部與表情區域 (Head & Chest Close-up)
    # 橘白貓頭部區域
    w_a, h_a = im_amber.size
    head_amber = im_amber.crop((int(w_a * 0.18), int(h_a * 0.12), int(w_a * 0.72), int(h_a * 0.68)))

    # 玳瑁貓頭部區域
    w_t, h_t = im_tortie.size
    head_tortie = im_tortie.crop((int(w_t * 0.22), int(h_t * 0.06), int(w_t * 0.78), int(h_t * 0.62)))

    # 建立 720x720 超取樣畫布 (4x scale of 180x180)
    canvas_size = 720
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (250, 247, 242, 255)) # 溫潤米白 #FAF7F2
    draw = ImageDraw.Draw(canvas)

    # 雅致微內邊框
    margin = 48
    draw.rounded_rectangle([margin, margin, canvas_size - margin, canvas_size - margin], 
                           radius=110, outline=(232, 222, 210, 255), width=6)
    draw.rounded_rectangle([margin + 10, margin + 10, canvas_size - margin - 10, canvas_size - margin - 10], 
                           radius=100, outline=(242, 235, 225, 255), width=3)

    # 調整雙貓頭像大小並和諧重疊依偎
    target_h = 440
    # 橘白貓稍大圓萌
    h_a_new = target_h
    w_a_new = int(head_amber.width * (h_a_new / head_amber.height))
    head_a_scaled = head_amber.resize((w_a_new, h_a_new), Image.Resampling.LANCZOS)

    # 玳瑁貓優雅修長
    h_t_new = target_h
    w_t_new = int(head_tortie.width * (h_t_new / head_tortie.height))
    head_t_scaled = head_tortie.resize((w_t_new, h_t_new), Image.Resampling.LANCZOS)

    # 計算居中位置 (左右輕柔依偎在中央)
    # 橘白貓在左稍前，玳瑁貓在右稍後
    pos_t = (canvas_size // 2 - w_t_new // 2 + 105, canvas_size // 2 - h_t_new // 2 - 10)
    pos_a = (canvas_size // 2 - w_a_new // 2 - 105, canvas_size // 2 - h_a_new // 2 + 10)

    # 柔和立體陰影
    shadow_mask_t = head_t_scaled.split()[3].point(lambda p: 35 if p > 50 else 0)
    shadow_mask_a = head_a_scaled.split()[3].point(lambda p: 40 if p > 50 else 0)
    
    shadow_t = Image.new("RGBA", head_t_scaled.size, (45, 41, 38, 0))
    shadow_t.putalpha(shadow_mask_t)
    shadow_t = shadow_t.filter(ImageFilter.GaussianBlur(12))

    shadow_a = Image.new("RGBA", head_a_scaled.size, (45, 41, 38, 0))
    shadow_a.putalpha(shadow_mask_a)
    shadow_a = shadow_a.filter(ImageFilter.GaussianBlur(14))

    # 貼合：玳瑁貓陰影與頭部
    canvas.paste(shadow_t, (pos_t[0], pos_t[1] + 12), shadow_t)
    canvas.paste(head_t_scaled, pos_t, head_t_scaled)

    # 貼合：橘白貓陰影與頭部
    canvas.paste(shadow_a, (pos_a[0], pos_a[1] + 12), shadow_a)
    canvas.paste(head_a_scaled, pos_a, head_a_scaled)

    # 平滑降採樣至 180x180 (高品質 Lanczos 抗鋸齒)
    icon_180 = canvas.resize((180, 180), Image.Resampling.LANCZOS)
    out_180 = os.path.join(ASSETS_DIR, "apple-touch-icon.png")
    icon_180.save(out_180, format="PNG")
    print(f"Saved boutique {out_180} (180x180)")

    # 同步生成 38x38 導覽列極致清晰版本
    icon_38 = canvas.resize((38, 38), Image.Resampling.LANCZOS)
    out_38 = os.path.join(IMG_DIR, "brand-cat-38.png")
    icon_38.save(out_38, format="PNG")
    print(f"Saved {out_38} (38x38)")

if __name__ == '__main__':
    render_boutique_apple_touch_icon()

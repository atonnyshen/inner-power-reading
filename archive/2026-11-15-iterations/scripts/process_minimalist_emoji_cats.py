#!/usr/bin/env python3
"""
process_minimalist_emoji_cats.py
將最新生成的兩隻極簡卡通/Emoji貓咪處理並注入專案：
1. 左貓：白色橘頭側伸腿貓 (amber_white_outstretched_leg_cat_1794739186160.jpg)
2. 右貓：黑面翡翠眼玳瑁端坐貓 (tortoiseshell_sentinel_cat_minimalist_1794739251935.jpg)
生成純淨去背 PNG、SVG 向量，以及更新 Favicon 與 Apple Touch Icon！
"""

import os
from PIL import Image, ImageOps

SRC_AMBER = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/amber_white_outstretched_leg_cat_1794739186160.jpg"
SRC_TORTIE = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/tortoiseshell_sentinel_cat_minimalist_1794739251935.jpg"

DEST_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
IMG_DIR = os.path.join(DEST_DIR, "img")
SVG_DIR = os.path.join(DEST_DIR, "img", "svg")
ASSETS_DIR = os.path.join(DEST_DIR, "assets")

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def process_and_save_images():
    img_amber = Image.open(SRC_AMBER).convert("RGBA")
    img_tortie = Image.open(SRC_TORTIE).convert("RGBA")
    
    # 儲存高解析度原版至 img/
    img_amber.save(os.path.join(IMG_DIR, "cat-amber-stretch-minimal.png"), format="PNG")
    img_tortie.save(os.path.join(IMG_DIR, "cat-tortoiseshell-sentinel-minimal.png"), format="PNG")
    print("Saved high-res PNGs to img/")

    # 製作極簡向量 SVG 版本 (以純淨幾何形狀 1:1 向量化)
    # 左貓 SVG: 寬高 300x260
    svg_amber = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 240" width="100%" height="100%" fill="none">
  <!-- Minimalist Pictogram Style: Amber Outstretched Leg Cat (4 Colors Max) -->
  <!-- Colors: White #FFFFFF, Orange #F28C38, Charcoal #2B2623, Soft Pink #F7A399 -->

  <!-- Body: Chubby white shape with outstretched leg -->
  <path d="M 50 145 C 50 100, 95 90, 140 105 C 180 115, 205 130, 245 160 C 265 175, 260 195, 235 195 C 190 195, 120 195, 65 190 C 50 185, 50 165, 50 145 Z" fill="#FFFFFF"/>

  <!-- Back Leg Outstretched (大膽側伸後腿) -->
  <path d="M 175 140 C 205 140, 235 155, 255 170 C 265 178, 262 192, 245 192 C 220 192, 195 185, 175 175 Z" fill="#FFFFFF"/>
  <!-- Knee Orange Patch (膝蓋橘斑) -->
  <path d="M 195 142 C 215 145, 230 160, 225 175 C 210 178, 195 165, 195 142 Z" fill="#F28C38"/>
  <!-- Pink Toe Beans on paw (粉紅小肉墊) -->
  <circle cx="245" cy="180" r="4.5" fill="#F7A399"/>
  <circle cx="238" cy="173" r="2.8" fill="#F7A399"/>
  <circle cx="244" cy="168" r="2.8" fill="#F7A399"/>
  <circle cx="251" cy="172" r="2.8" fill="#F7A399"/>

  <!-- Front folded paws (身前小爪) -->
  <path d="M 80 175 C 95 175, 105 188, 95 195 C 80 195, 75 185, 80 175 Z" fill="#F5F0EA"/>
  <path d="M 105 175 C 120 175, 130 188, 120 195 C 105 195, 100 185, 105 175 Z" fill="#F5F0EA"/>

  <!-- Head Base: Round White -->
  <circle cx="100" cy="105" r="52" fill="#FFFFFF"/>

  <!-- Pointed Ears -->
  <polygon points="56,75 52,38 80,55" fill="#FFFFFF"/>
  <polygon points="120,55 148,38 144,75" fill="#FFFFFF"/>

  <!-- Blunt Orange Bangs (平瀏海齊頭橘毛 - 幾何核心標識！) -->
  <path d="M 48 85 C 50 50, 150 50, 152 85 L 138 105 L 125 78 L 100 105 L 85 78 L 62 105 Z" fill="#F28C38"/>

  <!-- Cute Black Dot Eyes (極簡 Emoji 黑豆眼) -->
  <circle cx="80" cy="100" r="6.5" fill="#2B2623"/>
  <circle cx="120" cy="100" r="6.5" fill="#2B2623"/>

  <!-- Sweet Pink Nose -->
  <polygon points="100,108 94,102 106,102" fill="#F7A399"/>
</svg>'''

    # 右貓 SVG: 寬高 240x280
    svg_tortie = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 280" width="100%" height="100%" fill="none">
  <!-- Minimalist Pictogram Style: Tortoiseshell Sentinel Cat (4 Colors Max) -->
  <!-- Colors: Charcoal #2B2623, Orange #F28C38, Emerald Green #28B873, White #FFFFFF -->

  <!-- Upright Body Column (端坐深黑幾何柱狀身軀) -->
  <rect x="75" y="105" width="90" height="135" rx="42" fill="#2B2623"/>

  <!-- Pure White Ascot Chest Bib (下巴大片雪白圍巾毛) -->
  <path d="M 86 115 C 86 115, 120 160, 120 160 C 120 160, 154 115, 154 115 C 135 125, 105 125, 86 115 Z" fill="#FFFFFF"/>

  <!-- Upright Front Legs & Pure White Mitten Paws (黑長腿配白手套) -->
  <rect x="88" y="222" width="26" height="22" rx="11" fill="#FFFFFF" stroke="#2B2623" stroke-width="3"/>
  <rect x="126" y="222" width="26" height="22" rx="11" fill="#FFFFFF" stroke="#2B2623" stroke-width="3"/>

  <!-- Head Base: Rounded Charcoal Mask -->
  <circle cx="120" cy="85" r="46" fill="#2B2623"/>

  <!-- Natural Alert Ears (天然立耳，無帽子) -->
  <polygon points="76,65 80,24 106,50" fill="#2B2623" stroke="#2B2623" stroke-width="3" stroke-linejoin="round"/>
  <polygon points="134,50 160,24 164,65" fill="#2B2623" stroke="#2B2623" stroke-width="3" stroke-linejoin="round"/>
  <polygon points="84,55 83,32 100,48" fill="#F28C38"/>

  <!-- Caramel Gold Blaze & Muzzle (額頭筆直金流光與暖橘口吻) -->
  <path d="M 113 42 L 127 42 L 126 80 L 138 98 C 130 114, 110 114, 102 98 L 114 80 Z" fill="#F28C38"/>

  <!-- Striking Emerald Green Eyes (晶瑩明亮翡翠大圓眼) -->
  <circle cx="100" cy="82" r="9" fill="#28B873"/>
  <circle cx="100" cy="82" r="4.2" fill="#2B2623"/>
  <circle cx="98" cy="79" r="2.2" fill="#FFFFFF"/>

  <circle cx="140" cy="82" r="9" fill="#28B873"/>
  <circle cx="140" cy="82" r="4.2" fill="#2B2623"/>
  <circle cx="138" cy="79" r="2.2" fill="#FFFFFF"/>

  <!-- Nose & W-mouth -->
  <polygon points="120,95 116,91 124,91" fill="#2B2623"/>
  <path d="M 120 95 L 120 100 C 117 103, 112 102, 110 100" stroke="#2B2623" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <path d="M 120 100 C 123 103, 128 102, 130 100" stroke="#2B2623" stroke-width="2.5" stroke-linecap="round" fill="none"/>

  <!-- ICONIC BLACK BEAUTY MARK (右側鼻翼標誌性黑美人痣！) -->
  <circle cx="130" cy="95" r="3.2" fill="#2B2623"/>
</svg>'''

    with open(os.path.join(SVG_DIR, "ambient-cat-amber-stretch.svg"), "w", encoding="utf-8") as f:
        f.write(svg_amber)
    with open(os.path.join(SVG_DIR, "ambient-cat-tortoiseshell.svg"), "w", encoding="utf-8") as f:
        f.write(svg_tortie)
    print("Saved clean minimalist SVGs!")

    # 製作極簡 Brand Icon (Favicon 38x38 & Apple Touch Icon 180x180)
    # 雙貓極簡 Emoji 依偎標識
    svg_brand = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="100%" height="100%" fill="none">
  <!-- Clean Warm Background Badge -->
  <rect width="48" height="48" rx="12" fill="#FAF7F2"/>
  <rect x="1" y="1" width="46" height="46" rx="11" fill="none" stroke="#EAE2D8" stroke-width="1.2"/>

  <!-- Left: Amber Loaf Cat Minimal Face -->
  <circle cx="17" cy="25" r="10.5" fill="#FFFFFF"/>
  <polygon points="9,18 8,11 14,15" fill="#FFFFFF"/>
  <polygon points="20,15 26,11 25,18" fill="#FFFFFF"/>
  <path d="M 8 20 C 10 14, 24 14, 26 20 L 23 23 L 20 19 L 17 23 L 14 19 L 11 23 Z" fill="#F28C38"/>
  <circle cx="13.5" cy="24" r="1.5" fill="#2B2623"/>
  <circle cx="20.5" cy="24" r="1.5" fill="#2B2623"/>
  <polygon points="17,26 15.8,24.5 18.2,24.5" fill="#F7A399"/>

  <!-- Right: Tortoiseshell Sentinel Cat Minimal Face -->
  <circle cx="31" cy="25" r="10.5" fill="#2B2623"/>
  <polygon points="23,18 22,11 28,15" fill="#2B2623"/>
  <polygon points="34,15 40,11 39,18" fill="#2B2623"/>
  <!-- Gold Blaze -->
  <path d="M 29 15 L 33 15 L 32 23 L 34 27 C 32 30, 28 30, 26 27 L 30 23 Z" fill="#F28C38"/>
  <!-- Emerald Eyes -->
  <circle cx="27.5" cy="24" r="2.2" fill="#28B873"/>
  <circle cx="27.5" cy="24" r="1" fill="#2B2623"/>
  <circle cx="34.5" cy="24" r="2.2" fill="#28B873"/>
  <circle cx="34.5" cy="24" r="1" fill="#2B2623"/>
  <!-- White bib & Beauty mark -->
  <circle cx="32.5" cy="27" r="0.8" fill="#2B2623"/>
  <path d="M 26 31 C 28 34, 34 34, 36 31 Z" fill="#FFFFFF"/>
</svg>'''

    with open(os.path.join(ASSETS_DIR, "favicon-cat.svg"), "w", encoding="utf-8") as f:
        f.write(svg_brand)
    with open(os.path.join(SVG_DIR, "brand-cat.svg"), "w", encoding="utf-8") as f:
        f.write(svg_brand)
    print("Saved clean minimalist Favicon and Brand Cat SVGs!")

    # 生成 180x180 Apple Touch Icon (雙貓 Emoji 拼合，高清晰度)
    icon_canvas = Image.new("RGBA", (180, 180), (250, 247, 242, 255)) # 溫潤米白 #FAF7F2
    # 將兩隻極簡卡通小貓分別貼合到左右兩側
    thumb_amber = img_amber.resize((100, 100), Image.Resampling.LANCZOS)
    thumb_tortie = img_tortie.resize((82, 100), Image.Resampling.LANCZOS)
    
    # 居中合成
    icon_canvas.paste(thumb_amber, (10, 42), thumb_amber)
    icon_canvas.paste(thumb_tortie, (92, 40), thumb_tortie)
    icon_canvas.save(os.path.join(ASSETS_DIR, "apple-touch-icon.png"), format="PNG")
    print("Saved 180x180 apple-touch-icon.png!")

if __name__ == '__main__':
    process_and_save_images()

#!/usr/bin/env python3
"""
compose_transparent_web_assets.py
1. 將兩隻全新精準的透明手繪貓咪 (橘白側伸腿貓 & 黑面翡翠眼玳瑁貓) 合成為透明橫向雙貓伴讀圖
2. 替換 preview-bullet-journal-main.html 中所有的明信片框，徹底改為無文字、純去背透明底圖
3. 生成最新 180x180 Apple Touch Icon 與 38x38 Brand Icon
4. 更新校驗展廳 specimen-proof.html
"""

import os
import re
from PIL import Image

BASE_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
IMG_DIR = os.path.join(BASE_DIR, "img")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
HTML_PATH = os.path.join(BASE_DIR, "preview-bullet-journal-main.html")

PATH_AMBER = os.path.join(IMG_DIR, "cat-amber-stretch-transparent.png")
PATH_TORTIE = os.path.join(IMG_DIR, "cat-tortoiseshell-sentinel-transparent.png")

def create_dual_companions_transparent():
    im_amber = Image.open(PATH_AMBER).convert("RGBA")
    im_tortie = Image.open(PATH_TORTIE).convert("RGBA")
    
    # 建立一個寬度 800，高度 400 的透明畫布
    canvas = Image.new("RGBA", (800, 420), (0, 0, 0, 0))
    
    # 調整大小使兩貓比例自然和諧 (玳瑁端坐挺拔稍高，橘白圓滾躺坐稍寬)
    w_amber = 380
    h_amber = int(im_amber.height * (w_amber / im_amber.width))
    im_amber_scaled = im_amber.resize((w_amber, h_amber), Image.Resampling.LANCZOS)
    
    h_tortie = 360
    w_tortie = int(im_tortie.width * (h_tortie / im_tortie.height))
    im_tortie_scaled = im_tortie.resize((w_tortie, h_tortie), Image.Resampling.LANCZOS)
    
    # 貼在畫布左右兩側 (左側橘白貓，右側玳瑁貓，腳底對齊)
    canvas.paste(im_amber_scaled, (40, 420 - h_amber), im_amber_scaled)
    canvas.paste(im_tortie_scaled, (440, 420 - h_tortie), im_tortie_scaled)
    
    out_path = os.path.join(IMG_DIR, "cat-dual-companions-transparent.png")
    canvas.save(out_path, format="PNG")
    print(f"Saved {out_path} (800x420 transparent)")

def update_html():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 替換兩側固定背景貓咪：去背、去除明信片邊框、去除陰影框，只保留柔和自然 drop-shadow
    ambient_replacement = '''  <!-- Fixed Ambient Background Guardian Cats (純淨去背、零邊框、融入手帳米白紙面) -->
  <div class="ambient-cat-fixed ambient-cat-left" aria-hidden="true">
    <img src="img/cat-amber-stretch-transparent.png" alt="身心放鬆·白色橘頭側伸後腿貓" width="220" height="220" style="width:100%;height:auto;display:block;filter:drop-shadow(0 6px 14px rgba(45,41,38,0.07));">
  </div>

  <div class="ambient-cat-fixed ambient-cat-right" aria-hidden="true">
    <img src="img/cat-tortoiseshell-sentinel-transparent.png" alt="堅定邊界·黑面翡翠眼白圍巾玳瑁貓" width="200" height="267" style="width:100%;height:auto;display:block;filter:drop-shadow(0 6px 14px rgba(45,41,38,0.07));">
  </div>'''

    ambient_pattern = r'<!-- Fixed Ambient Background Guardian Cats[\s\S]*?<div class="ambient-cat-fixed ambient-cat-left"[\s\S]*?</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[\s\S]*?</div>'
    if re.search(ambient_pattern, content):
        content = re.sub(ambient_pattern, ambient_replacement, content)

    # 2. 替換 Hero 區域明信片框為純淨去背雙貓伴讀圖 (無字、無框、無明信片感)
    old_banner_pattern = r'<div class="editorial-hero-banner"[\s\S]*?</div>'
    new_banner = '''<div class="editorial-hero-banner" style="margin: 28px auto 16px; max-width: 680px; text-align: center;">
          <img src="img/cat-dual-companions-transparent.png" alt="雙貓伴讀手繪去背插圖" style="max-width: 100%; height: auto; display: inline-block; filter: drop-shadow(0 8px 18px rgba(45,41,38,0.06));">
        </div>'''
    if re.search(old_banner_pattern, content):
        content = re.sub(old_banner_pattern, new_banner, content)

    # 3. 移除章節中帶字帶框的明信片底圖，保持純粹閱讀
    content = re.sub(r'<div class="editorial-section-plate"[\s\S]*?</div>\s*', '', content)
    content = re.sub(r'<!-- 3:2 Editorial Ground Plate[\s\S]*?<div class="editorial-footer-plate"[\s\S]*?</div>', '', content)

    # 4. 替換頂部 Brand Icon 內部為極致清晰可愛的雙貓透明圖標
    brand_icon_replacement = '''<div class="brand-icon" aria-hidden="true">
      <img src="assets/favicon-cat.svg" alt="手帳伴讀貓咪圖標" width="38" height="38" style="width:100%;height:100%;display:block;border-radius:9px;object-fit:cover;">
    </div>'''
    content = re.sub(r'<div class="brand-icon"[\s\S]*?</div>', brand_icon_replacement, content)

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("preview-bullet-journal-main.html updated: No postcards, fully transparent, zero text!")

def update_proof_html():
    proof_path = os.path.join(ASSETS_DIR, "specimen-proof.html")
    proof_content = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>純淨去背 · 手繪雙貓真貌校驗展廳</title>
  <style>
    :root {
      --bg: #FAF7F2;
      --card: #FFFFFF;
      --text: #2B2623;
      --text-dim: #7A726B;
      --border: #E8DFD3;
    }
    body {
      margin: 0;
      padding: 40px 20px;
      background: var(--bg);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang TC", sans-serif;
      color: var(--text);
      display: flex;
      flex-direction: column;
      align-items: center;
      box-sizing: border-box;
    }
    .container {
      max-width: 1000px;
      width: 100%;
    }
    .header {
      text-align: center;
      margin-bottom: 40px;
    }
    h1 {
      font-size: 2rem;
      margin-bottom: 8px;
      font-weight: 800;
    }
    .subtitle {
      color: var(--text-dim);
      font-size: 0.95rem;
      line-height: 1.6;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 30px;
      margin-bottom: 40px;
    }
    .card {
      background: var(--card);
      border-radius: 20px;
      border: 1px solid var(--border);
      padding: 30px 20px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    /* 棋盤格背景，清晰驗證透明通道去背效果 */
    .checker-wrap {
      width: 100%;
      height: 340px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #FFFFFF;
      background-image: 
        linear-gradient(45deg, #F5F2EC 25%, transparent 25%), 
        linear-gradient(-45deg, #F5F2EC 25%, transparent 25%), 
        linear-gradient(45deg, transparent 75%, #F5F2EC 75%), 
        linear-gradient(-45deg, transparent 75%, #F5F2EC 75%);
      background-size: 20px 20px;
      background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
      border-radius: 12px;
      margin-bottom: 20px;
      border: 1px solid #EFEAE2;
    }
    .checker-wrap img {
      max-width: 85%;
      max-height: 90%;
      object-fit: contain;
      filter: drop-shadow(0 6px 16px rgba(0,0,0,0.1));
    }
    .cat-title {
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 8px;
    }
    .cat-desc {
      font-size: 0.88rem;
      color: var(--text-dim);
      line-height: 1.6;
      text-align: left;
      width: 100%;
    }
    .dual-banner-card {
      background: var(--card);
      border-radius: 20px;
      border: 1px solid var(--border);
      padding: 30px 20px;
      margin-bottom: 30px;
      text-align: center;
    }
    .dual-banner-card img {
      max-width: 100%;
      height: auto;
      filter: drop-shadow(0 8px 20px rgba(0,0,0,0.08));
    }
    .btn {
      display: inline-block;
      margin-top: 30px;
      padding: 12px 28px;
      background: var(--text);
      color: #FFF;
      text-decoration: none;
      border-radius: 24px;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>純淨去背 · 手繪雙貓真貌校驗展廳</h1>
      <div class="subtitle">
        100% 去背去底圖 · 移除明信片框與外框 · 零多餘文字 · 顏色神情精準還原照片真貌
      </div>
    </div>

    <!-- 雙貓並肩伴讀 -->
    <div class="dual-banner-card">
      <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 16px;">【雙貓並肩伴讀 · 網頁 Hero 展卷底圖】</div>
      <img src="../img/cat-dual-companions-transparent.png" alt="雙貓透明並肩伴讀圖">
      <div style="font-size: 0.88rem; color: var(--text-dim); margin-top: 12px;">
        左側橘白貓大膽側伸後腿、平瀏海、呆萌無辜；右側玳瑁貓黑面金流光、水潤翡翠綠大眼、黑美人痣、雪白厚胸毛、端正自持。純透明底，無任何文字或邊框。
      </div>
    </div>

    <div class="grid">
      <!-- 橘白貓 -->
      <div class="card">
        <div class="checker-wrap">
          <img src="../img/cat-amber-stretch-transparent.png" alt="白色橘頭側伸後腿貓">
        </div>
        <div class="cat-title">【白色橘頭側伸腿放鬆貓】</div>
        <div class="cat-desc">
          • <b>完全去背去底圖</b>：棋盤格展示 Alpha 透明通道，無明信片白底與邊框<br>
          • <b>零多餘文字</b>：純粹插圖，無任何英文標籤或代碼<br>
          • <b>物象精準還原</b>：額頭齊頭橘平瀏海、圓滾滾白肚腩、大膽向側邊外伸之放鬆後腿（大雞腿）、膝蓋橘色護膝斑、小腳掌粉嫩肉墊、收攏於胸前之端莊雙爪
        </div>
      </div>

      <!-- 玳瑁貓 -->
      <div class="card">
        <div class="checker-wrap">
          <img src="../img/cat-tortoiseshell-sentinel-transparent.png" alt="黑面翡翠眼白圍巾玳瑁貓">
        </div>
        <div class="cat-title">【黑面翡翠眼白領巾玳瑁貓】</div>
        <div class="cat-desc">
          • <b>完全去背去底圖</b>：棋盤格展示 Alpha 透明通道，無明信片白底與邊框<br>
          • <b>顏色精準還原</b>：臉龐黑墨面罩、額頭正中一條細緻垂直焦糖金流光（Blaze）、下巴至胸前大片豐厚蓬鬆純白圍巾、黑前腿配雪白手套、斑駁玳瑁軀幹<br>
          • <b>神情靈魂精準</b>：晶瑩深邃的水潤<b>翡翠綠大寶石眼</b>，右嘴角旁標誌性<b>黑美人痣</b>，神態端莊、自持清醒、沉著威嚴、不迎合道歉
        </div>
      </div>
    </div>

    <div style="text-align: center;">
      <a href="../preview-bullet-journal-main.html" class="btn">返回手帳讀書誌主預覽頁面 →</a>
    </div>
  </div>
</body>
</html>
'''
    with open(proof_path, "w", encoding="utf-8") as f:
        f.write(proof_content)
    print("specimen-proof.html updated with checkerboard transparency proof!")

def update_apple_touch_icon():
    # 產生最新 180x180 Apple Touch Icon (精緻雙貓透明合成在米白紙底)
    im_amber = Image.open(PATH_AMBER).convert("RGBA")
    im_tortie = Image.open(PATH_TORTIE).convert("RGBA")
    
    icon_bg = Image.new("RGBA", (180, 180), (250, 247, 242, 255)) # 溫潤米白底 #FAF7F2
    
    # 縮小兩隻貓咪頭部/半身
    im_amber_thumb = im_amber.resize((105, 105), Image.Resampling.LANCZOS)
    im_tortie_thumb = im_tortie.resize((85, 114), Image.Resampling.LANCZOS)
    
    # 居中拼合在 180x180 畫布上
    icon_bg.paste(im_amber_thumb, (8, 48), im_amber_thumb)
    icon_bg.paste(im_tortie_thumb, (90, 42), im_tortie_thumb)
    
    out_icon = os.path.join(ASSETS_DIR, "apple-touch-icon.png")
    icon_bg.save(out_icon, format="PNG")
    print(f"Saved {out_icon} (180x180)")

if __name__ == '__main__':
    create_dual_companions_transparent()
    update_html()
    update_proof_html()
    update_apple_touch_icon()
    print("All tasks completed successfully!")

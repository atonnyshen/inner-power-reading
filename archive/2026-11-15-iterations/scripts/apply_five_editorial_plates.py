#!/usr/bin/env python3
"""
apply_five_editorial_plates.py
依照使用者最新指令：
1. 絕不使用前幾輪畫的圖片，全面改用最新五張手繪紙本藝術插圖（Minimal Hand-drawn Paper Illustration）
2. 依照圖片的有效位置與長寬比例（3:2 與 16:9），精確運用於網頁的底圖中：
   - 圖 4 (16:9): 頂部 Hero 首頁展卷區伴讀全景底圖 (DUAL COMPANIONS ATOP BOOKSHELF)
   - 圖 1 (3:2): 左側固定浮動守護底圖 (AMBER STRETCH)
   - 圖 3 (3:2): 右側固定浮動守護底圖 (SENTINEL WITH BASKET)
   - 圖 2 (3:2): 閱讀心理學與心智鬆綁章節底圖 (PROFOUND SLEEP)
   - 圖 5 (3:2): 頁尾睡前定錨與身心重啟收尾底圖 (TOTAL SURRENDER)
3. 更新 specimen-proof.html 為五幅畫作的專屬藝術展廳校驗頁面。
"""

import os
import re
from PIL import Image

PROJECT_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
HTML_PATH = os.path.join(PROJECT_DIR, "preview-bullet-journal-main.html")
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")

def update_main_html():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 更新固定兩側守護底圖 (依照 3:2 比例)
    # 左側: 圖 1 (3:2), 右側: 圖 3 (3:2)
    new_ambient_cats = '''  <!-- Fixed Ambient Background Guardian Cats (以精確 3:2 比例運用最新手繪紙本插圖) -->
  <div class="ambient-cat-fixed ambient-cat-left" aria-hidden="true">
    <img src="img/editorial/cat-01-amber-stretch-3x2.jpg" alt="身心放鬆·白色橘頭側伸後腿貓" width="240" height="161" style="width:100%;height:auto;display:block;border-radius:12px;border:1px solid #EAE2D8;box-shadow:0 4px 16px rgba(0,0,0,0.06);">
  </div>

  <div class="ambient-cat-fixed ambient-cat-right" aria-hidden="true">
    <img src="img/editorial/cat-03-sentinel-basket-3x2.jpg" alt="堅定邊界·黑面翡翠眼白圍巾玳瑁貓" width="240" height="161" style="width:100%;height:auto;display:block;border-radius:12px;border:1px solid #EAE2D8;box-shadow:0 4px 16px rgba(0,0,0,0.06);">
  </div>'''

    ambient_pattern = r'<!-- Fixed Ambient Background Guardian Cats[\s\S]*?<div class="ambient-cat-fixed ambient-cat-left"[\s\S]*?</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[\s\S]*?</div>'
    if re.search(ambient_pattern, content):
        content = re.sub(ambient_pattern, new_ambient_cats, content)
    else:
        # 如果沒匹配到完整註釋，匹配 div
        div_pattern = r'<div class="ambient-cat-fixed ambient-cat-left"[\s\S]*?</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[\s\S]*?</div>'
        content = re.sub(div_pattern, new_ambient_cats, content)

    # 2. 在 Hero 區域注入「圖 4 · 雙貓高處書架伴讀 (16:9 全景比例)」
    hero_plate_html = '''        <!-- 16:9 Editorial Header Plate: 圖 4 雙貓高處書架俯瞰伴讀 -->
        <div class="editorial-hero-banner" style="margin: 32px auto 20px; max-width: 920px; aspect-ratio: 16/9; border-radius: 16px; overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-sm); background: #FAF7F2;">
          <img src="img/editorial/cat-04-dual-bookshelf-16x9.jpg" alt="雙貓高處俯瞰伴讀手繪紙本插圖" style="width: 100%; height: 100%; object-fit: cover; display: block;">
        </div>'''
    
    # 放置在 hero-subtitle 之後
    if '<div class="editorial-hero-banner"' not in content:
        content = content.replace('</p>\n        \n        <!-- CRISIS-TO-BOOK', f'</p>\n\n{hero_plate_html}\n        \n        <!-- CRISIS-TO-BOOK')

    # 3. 在「為什麼妳應該翻開原書？五大心智鬆綁」章節頂部注入「圖 2 · 沉睡微露粉掌的玳瑁貓 (3:2 比例)」
    reading_plate_html = '''      <div class="editorial-section-plate" style="margin: 28px auto 36px; max-width: 680px; aspect-ratio: 3/2; border-radius: 14px; overflow: hidden; border: 1px solid var(--border-card); box-shadow: var(--shadow-sm); background: #FAF7F2;">
        <img src="img/editorial/cat-02-profound-sleep-3x2.jpg" alt="深度睡眠卸下防衛手繪紙本插圖" style="width: 100%; height: 100%; object-fit: cover; display: block;">
      </div>'''
      
    if '<div class="editorial-section-plate"' not in content:
        content = content.replace('<!-- Section 2: Reading Psychology -->\n  <section id="reading-strategy">\n    <div class="container">\n      <div class="section-header">',
                                  f'<!-- Section 2: Reading Psychology -->\n  <section id="reading-strategy">\n    <div class="container">\n      <div class="section-header">\n{reading_plate_html}')

    # 4. 在頁尾閉卷定錨處注入「圖 5 · 升降桌四腳朝天徹底放鬆貓 (3:2 比例)」
    footer_plate_html = '''    <!-- 3:2 Editorial Ground Plate: 圖 5 升降桌四腳朝天徹底放鬆貓 -->
    <div class="editorial-footer-plate" style="margin: 40px auto 24px; max-width: 640px; aspect-ratio: 3/2; border-radius: 14px; overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-sm); background: #FAF7F2;">
      <img src="img/editorial/cat-05-total-surrender-3x2.jpg" alt="全然臣服身心重啟手繪紙本插圖" style="width: 100%; height: 100%; object-fit: cover; display: block;">
    </div>'''
    
    if '<div class="editorial-footer-plate"' not in content:
        content = content.replace('<footer>\n    <div class="container">',
                                  f'<footer>\n    <div class="container">\n{footer_plate_html}')

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("preview-bullet-journal-main.html successfully updated with 5 editorial plates!")

def update_specimen_proof_html():
    proof_path = os.path.join(ASSETS_DIR, "specimen-proof.html")
    
    proof_html = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>獨立出版級手繪紙本藝術插圖 · 五大有效長寬比例校驗展廳</title>
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
      max-width: 1100px;
      width: 100%;
    }
    .header {
      text-align: center;
      margin-bottom: 48px;
    }
    h1 {
      font-size: 2rem;
      margin-bottom: 12px;
      font-weight: 800;
      letter-spacing: -0.01em;
    }
    .subtitle {
      color: var(--text-dim);
      font-size: 0.98rem;
      line-height: 1.7;
      max-width: 780px;
      margin: 0 auto;
    }
    .gallery {
      display: flex;
      flex-direction: column;
      gap: 50px;
    }
    .plate-card {
      background: var(--card);
      border-radius: 20px;
      border: 1px solid var(--border);
      padding: 36px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .plate-img-wrap {
      width: 100%;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid #ECE3D7;
      background: #FAF7F2;
    }
    .plate-img-wrap img {
      width: 100%;
      height: auto;
      display: block;
    }
    .meta-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-top: 1px solid #F0E8DD;
      padding-top: 18px;
      gap: 20px;
      flex-wrap: wrap;
    }
    .meta-title {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 6px;
    }
    .meta-desc {
      font-size: 0.92rem;
      color: var(--text-dim);
      line-height: 1.6;
      max-width: 600px;
    }
    .badge-wrap {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .badge {
      font-size: 0.78rem;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 20px;
      background: #F3ECE2;
      color: #63574A;
    }
    .back-btn {
      display: inline-block;
      margin-top: 40px;
      padding: 12px 28px;
      background: var(--text);
      color: #FFF;
      text-decoration: none;
      border-radius: 24px;
      font-weight: 600;
      font-size: 0.95rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>獨立出版級手繪紙本藝術插圖 · 五大比例展廳</h1>
      <div class="subtitle">
        Strict Minimal Hand-Drawn Paper Illustration · Negative Space 80%+ · Strict 4-Color Compressed Palette<br>
        捨棄生硬幾何線條，精準提取 5 張真實照片物象基因，以 3:2 與 16:9 長寬比例無縫融入手帳閱讀頁面。
      </div>
    </div>

    <div class="gallery">
      <!-- Plate 4: 雙貓高處書架俯瞰伴讀 (16:9) -->
      <div class="plate-card">
        <div class="plate-img-wrap" style="aspect-ratio: 16/9;">
          <img src="../img/editorial/cat-04-dual-bookshelf-16x9.jpg" alt="FIG. 04 · DUAL COMPANIONS ATOP BOOKSHELF">
        </div>
        <div class="meta-row">
          <div>
            <div class="meta-title">【圖 4 · 雙貓高處書架俯瞰伴讀】(FIG. 04 · DUAL COMPANIONS)</div>
            <div class="meta-desc">
              對照照片 4：雙貓並排端坐在高高書架頂部。提取平瀏海橘白貓與黑面金流光玳瑁貓並肩俯瞰姿態，下方為極簡抽象書脊。<br>
              <b>網頁定位</b>：頂部 Hero 首頁展卷區伴讀全景底圖，開卷即見雙貓靜守。
            </div>
          </div>
          <div class="badge-wrap">
            <span class="badge" style="background:#EBF2ED;color:#286845;">有效比例: 16:9</span>
            <span class="badge">全景伴讀</span>
            <span class="badge">認知高處俯瞰</span>
          </div>
        </div>
      </div>

      <!-- Plate 1: 側伸後腿放鬆貓 (3:2) -->
      <div class="plate-card">
        <div class="plate-img-wrap" style="aspect-ratio: 3/2;">
          <img src="../img/editorial/cat-01-amber-stretch-3x2.jpg" alt="FIG. 01 · AMBER STRETCH">
        </div>
        <div class="meta-row">
          <div>
            <div class="meta-title">【圖 1 · 側伸後腿放鬆貓】(FIG. 01 · AMBER STRETCH)</div>
            <div class="meta-desc">
              對照照片 1：橘白貓坐在地板木梯凳旁，右後腿大膽橫向伸展。提取西瓜皮平瀏海、膝蓋橘護膝斑與粉紅肉墊。<br>
              <b>網頁定位</b>：左側固定背景底圖與「軌道一 · 身心放鬆」陪伴插畫。
            </div>
          </div>
          <div class="badge-wrap">
            <span class="badge" style="background:#FFF0E2;color:#C85E12;">有效比例: 3:2</span>
            <span class="badge">身心解凍</span>
            <span class="badge">大膽側伸大雞腿</span>
          </div>
        </div>
      </div>

      <!-- Plate 3: 端坐編織提籃旁玳瑁貓 (3:2) -->
      <div class="plate-card">
        <div class="plate-img-wrap" style="aspect-ratio: 3/2;">
          <img src="../img/editorial/cat-03-sentinel-basket-3x2.jpg" alt="FIG. 03 · SENTINEL WITH BASKET">
        </div>
        <div class="meta-row">
          <div>
            <div class="meta-title">【圖 3 · 端坐編織籃旁玳瑁貓】(FIG. 03 · SENTINEL WITH BASKET)</div>
            <div class="meta-desc">
              對照照片 3：端坐在木櫃上的玳瑁貓，身旁為編織提籃與垂掛毛球。提取黑面罩、額頭金流光、碧綠翡翠眼與黑美人痣。<br>
              <b>網頁定位</b>：右側固定背景底圖與「軌道二 · 堅定邊界」陪伴插畫。
            </div>
          </div>
          <div class="badge-wrap">
            <span class="badge" style="background:#E2F4EB;color:#187A4A;">有效比例: 3:2</span>
            <span class="badge">堅定邊界</span>
            <span class="badge">端坐自持不道歉</span>
          </div>
        </div>
      </div>

      <!-- Plate 2: 沉睡微露粉掌玳瑁貓 (3:2) -->
      <div class="plate-card">
        <div class="plate-img-wrap" style="aspect-ratio: 3/2;">
          <img src="../img/editorial/cat-02-profound-sleep-3x2.jpg" alt="FIG. 02 · PROFOUND SLEEP">
        </div>
        <div class="meta-row">
          <div>
            <div class="meta-title">【圖 2 · 沉睡微露粉掌玳瑁貓】(FIG. 02 · PROFOUND SLEEP)</div>
            <div class="meta-desc">
              對照照片 2：在白色邊櫃與暖氣片夾角熟睡的玳瑁貓，一隻毛茸茸前爪向前伸展露出粉紅肉墊。<br>
              <b>網頁定位</b>：「為什麼妳應該翻開原書？五大心智鬆綁」章節導讀紙本底圖。
            </div>
          </div>
          <div class="badge-wrap">
            <span class="badge" style="background:#FDE8E8;color:#A83232;">有效比例: 3:2</span>
            <span class="badge">卸下防衛</span>
            <span class="badge">安全感閱讀</span>
          </div>
        </div>
      </div>

      <!-- Plate 5: 升降桌四腳朝天徹底放鬆貓 (3:2) -->
      <div class="plate-card">
        <div class="plate-img-wrap" style="aspect-ratio: 3/2;">
          <img src="../img/editorial/cat-05-total-surrender-3x2.jpg" alt="FIG. 05 · TOTAL SURRENDER">
        </div>
        <div class="meta-row">
          <div>
            <div class="meta-title">【圖 5 · 升降桌四腳朝天放鬆貓】(FIG. 05 · TOTAL SURRENDER)</div>
            <div class="meta-desc">
              對照照片 5：在升降桌前四腳朝天仰面大躺平的橘白貓，四爪向空中伸展露出滿滿粉嫩肉墊。<br>
              <b>網頁定位</b>：頁尾睡前定錨與行動處方章節收尾底圖，通讀後全然釋懷。
            </div>
          </div>
          <div class="badge-wrap">
            <span class="badge" style="background:#FFF0E2;color:#C85E12;">有效比例: 3:2</span>
            <span class="badge">全然臣服</span>
            <span class="badge">睡前定錨重啟</span>
          </div>
        </div>
      </div>
    </div>

    <div style="text-align:center; margin-top: 40px;">
      <a href="../preview-bullet-journal-main.html" class="back-btn">返回手帳讀書誌主預覽頁面 →</a>
    </div>
  </div>
</body>
</html>
'''
    with open(proof_path, "w", encoding="utf-8") as f:
        f.write(proof_html)
        
    print("specimen-proof.html successfully updated!")

if __name__ == '__main__':
    update_main_html()
    update_specimen_proof_html()

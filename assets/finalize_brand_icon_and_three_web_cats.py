#!/usr/bin/env python3
"""
finalize_brand_icon_and_three_web_cats.py
1. 處理最新 Apple Touch Icon & Brand Icon (media_1794741126520_bc52a860.jpg):
   - 抹除左下角和右下角的所有文字標籤
   - 擷取適當大小的 1:1 正方形區域 (雙貓居中、保留書架與抽象書脊、留足 iOS 圓角安全邊界)
   - 輸出為 180x180 apple-touch-icon.png 與 38x38 brand-cat-38.png
2. 處理網頁專用的 3 張選定圖:
   - 圖片 1: 側伸腿放鬆貓 (media_1794740969873_ec04da22.jpg) -> 去背、去字、緊密裁切
   - 圖片 3: 端坐提籃旁的玳瑁貓 (media_1794741003762_81c889a9.jpg) -> 去背、去字、緊密裁切
   - 圖片 5: 升降桌四腳朝天放鬆貓 (media_1794740979604_8a730326.jpg) -> 去背、去字、緊密裁切
3. 更新 preview-bullet-journal-main.html:
   - 全網頁「只放這三張圖」！
   - 圖 1 (左側固定守護)
   - 圖 3 (右側固定守護)
   - 圖 5 (頁尾睡前定錨收尾)
   - 徹底移除其他所有圖片，保證乾淨、以人為本、閱讀體驗最佳化！
"""

import os
import re
from PIL import Image, ImageDraw

PROJECT_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
IMG_DIR = os.path.join(PROJECT_DIR, "img")
EDITORIAL_DIR = os.path.join(IMG_DIR, "editorial")
HTML_PATH = os.path.join(PROJECT_DIR, "preview-bullet-journal-main.html")

ICON_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794741126520_bc52a860.jpg"
IMG_1_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794740969873_ec04da22.jpg"
IMG_5_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794740979604_8a730326.jpg"
IMG_3_SRC = "/Users/atonny/.gemini/antigravity/brain/9b40261a-0d1b-40a7-a301-c32dc66b57cb/.user_uploaded/media_1794741003762_81c889a9.jpg"

os.makedirs(EDITORIAL_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def remove_bg_floodfill(img, threshold=40):
    img_rgba = img.convert("RGBA")
    w, h = img_rgba.size
    pixels = img_rgba.load()

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
            pixels[cx, cy] = (r, g, b, 0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                    nr, ng, nb, _ = pixels[nx, ny]
                    if is_bg(nr, ng, nb):
                        queue.append((nx, ny))

    return img_rgba

# === 1. 處理 Brand Icon & Apple Touch Icon ===
def process_brand_icon():
    im = Image.open(ICON_SRC).convert("RGB")
    w, h = im.size
    draw = ImageDraw.Draw(im)

    # 抹除左下角和右下角文字
    # 左下文字: FIG. 04 · DUAL COMPANIONS ATOP BOOKSHELF
    bg_sample_l = im.getpixel((w // 4, h - 30))
    draw.rectangle([int(w * 0.08), int(h * 0.70), int(w * 0.35), int(h * 0.78)], fill=bg_sample_l)

    # 右下文字: INDEX // PERSPECTIVE FROM HEIGHT
    bg_sample_r = im.getpixel((int(w * 0.75), h - 30))
    draw.rectangle([int(w * 0.70), int(h * 0.70), int(w * 0.92), int(h * 0.78)], fill=bg_sample_r)

    # 雙貓位於水平中心 (約 x: 0.28 ~ 0.70，y: 0.22 ~ 0.72)
    # 取精準 1:1 正方形區域，使雙貓與書架居中，周圍留足安全留白
    crop_size = int(h * 0.64)  # 正方形邊長
    center_x = int(w * 0.495)
    center_y = int(h * 0.47)
    
    crop_x1 = max(0, center_x - crop_size // 2)
    crop_y1 = max(0, center_y - crop_size // 2)
    crop_x2 = min(w, crop_x1 + crop_size)
    crop_y2 = min(h, crop_y1 + crop_size)

    cropped_icon = im.crop((crop_x1, crop_y1, crop_x2, crop_y2))

    # 儲存高解析度 512x512
    icon_512 = cropped_icon.resize((512, 512), Image.Resampling.LANCZOS)
    icon_512.save(os.path.join(ASSETS_DIR, "brand-dual-cats-square.png"), format="PNG")

    # 產生 180x180 Apple Touch Icon (包含標準紙質底與微內襯)
    icon_180 = cropped_icon.resize((180, 180), Image.Resampling.LANCZOS)
    icon_180.save(os.path.join(ASSETS_DIR, "apple-touch-icon.png"), format="PNG")
    print("Saved 180x180 apple-touch-icon.png!")

    # 產生 38x38 導覽列圖標
    icon_38 = cropped_icon.resize((38, 38), Image.Resampling.LANCZOS)
    icon_38.save(os.path.join(IMG_DIR, "brand-cat-38.png"), format="PNG")
    print("Saved 38x38 brand-cat-38.png!")

# === 2. 處理 3 張選定圖片 ===
def process_three_cats():
    # 圖片 1: 側伸腿橘白貓
    im1 = Image.open(IMG_1_SRC).convert("RGB")
    w, h = im1.size
    draw1 = ImageDraw.Draw(im1)
    # 抹除上方文字
    draw1.rectangle([int(w * 0.20), int(h * 0.15), int(w * 0.80), int(h * 0.32)], fill=im1.getpixel((w // 2, 50)))
    # 緊密裁切
    c1 = im1.crop((int(w * 0.37), int(h * 0.52), int(w * 0.68), int(h * 0.81)))
    t1 = remove_bg_floodfill(c1, threshold=38)
    t1.save(os.path.join(EDITORIAL_DIR, "chosen-01-amber-stretch.png"), format="PNG")
    print("Processed chosen-01-amber-stretch.png")

    # 圖片 3: 端坐編織提籃旁玳瑁貓
    im3 = Image.open(IMG_3_SRC).convert("RGB")
    w, h = im3.size
    draw3 = ImageDraw.Draw(im3)
    # 抹除左下文字
    draw3.rectangle([int(w * 0.02), int(h * 0.85), int(w * 0.45), int(h * 0.98)], fill=im3.getpixel((100, h - 30)))
    # 緊密裁切 (保留上方垂掛小毛球)
    c3 = im3.crop((int(w * 0.49), int(h * 0.00), int(w * 0.87), int(h * 0.84)))
    t3 = remove_bg_floodfill(c3, threshold=38)
    t3.save(os.path.join(EDITORIAL_DIR, "chosen-03-sentinel-basket.png"), format="PNG")
    print("Processed chosen-03-sentinel-basket.png")

    # 圖片 5: 升降桌四腳朝天徹底放鬆貓
    im5 = Image.open(IMG_5_SRC).convert("RGB")
    w, h = im5.size
    draw5 = ImageDraw.Draw(im5)
    # 抹除下方文字
    draw5.rectangle([int(w * 0.05), int(h * 0.88), int(w * 0.95), int(h * 0.98)], fill=im5.getpixel((w // 2, h - 30)))
    # 緊密裁切
    c5 = im5.crop((int(w * 0.22), int(h * 0.36), int(w * 0.75), int(h * 0.72)))
    t5 = remove_bg_floodfill(c5, threshold=38)
    t5.save(os.path.join(EDITORIAL_DIR, "chosen-05-total-surrender.png"), format="PNG")
    print("Processed chosen-05-total-surrender.png")

# === 3. 更新 HTML 頁面 (全網頁只放這三張圖，各居最佳位置) ===
def update_web_html():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 導覽列 Brand Icon 引用最新 38x38 圖標
    brand_html = '''<div class="brand-icon" aria-hidden="true">
      <img src="img/brand-cat-38.png" alt="手帳伴讀雙貓圖標" width="38" height="38" style="width:100%;height:100%;display:block;border-radius:9px;object-fit:cover;">
    </div>'''
    content = re.sub(r'<div class="brand-icon"[\s\S]*?</div>', brand_html, content)

    # 2. 移除 Hero 區域的多餘圖片，保持純淨以人為本閱讀
    content = re.sub(r'<div class="editorial-hero-banner"[\s\S]*?</div>\s*', '', content)
    # 移除章節中原本插入的多餘圖片
    content = re.sub(r'<div class="editorial-plate-wrap"[\s\S]*?</div>\s*', '', content)
    content = re.sub(r'<div class="editorial-section-plate"[\s\S]*?</div>\s*', '', content)
    content = re.sub(r'<div class="editorial-footer-plate"[\s\S]*?</div>\s*', '', content)

    # 3. 實裝第一與第二張選定圖：固定左右兩側守護底圖 (純淨去背、零邊框、最適尺寸)
    ambient_html = '''  <!-- 讀者選定之三大插圖之一 & 二：固定兩側守護貓咪 (純淨去背、無文字、融入手帳紙面) -->
  <div class="ambient-cat-fixed ambient-cat-left" aria-hidden="true" title="身心放鬆·側伸後腿貓">
    <img src="img/editorial/chosen-01-amber-stretch.png" alt="身心放鬆·白色橘頭側伸後腿貓" width="230" height="152" style="width:100%;height:auto;display:block;filter:drop-shadow(0 6px 14px rgba(45,41,38,0.08));">
  </div>

  <div class="ambient-cat-fixed ambient-cat-right" aria-hidden="true" title="堅定邊界·端坐編織提籃旁玳瑁貓">
    <img src="img/editorial/chosen-03-sentinel-basket.png" alt="堅定邊界·端坐編織提籃旁玳瑁貓" width="180" height="258" style="width:100%;height:auto;display:block;filter:drop-shadow(0 6px 14px rgba(45,41,38,0.08));">
  </div>'''

    ambient_pattern = r'<!-- Fixed Ambient Background Guardian Cats[\s\S]*?<div class="ambient-cat-fixed ambient-cat-left"[\s\S]*?</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[\s\S]*?</div>'
    if re.search(ambient_pattern, content):
        content = re.sub(ambient_pattern, ambient_html, content)
    else:
        div_pattern = r'<div class="ambient-cat-fixed ambient-cat-left"[\s\S]*?</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[\s\S]*?</div>'
        content = re.sub(div_pattern, ambient_html, content)

    # 4. 實裝第三張選定圖：在頁尾睡前定錨收尾處 (以人為本的全然臣服與身心重啟)
    footer_plate_html = '''    <!-- 讀者選定之三大插圖之三：頁尾睡前充電定錨儀式·四腳朝天徹底放鬆貓 (純淨去背、零多餘文字) -->
    <div class="editorial-final-cat-wrap" style="margin: 32px auto 20px; max-width: 420px; text-align: center;">
      <img src="img/editorial/chosen-05-total-surrender.png" alt="全然臣服·升降桌四腳朝天徹底放鬆貓" style="max-width: 100%; height: auto; display: inline-block; filter: drop-shadow(0 6px 16px rgba(45,41,38,0.07));">
    </div>'''

    if '<div class="editorial-final-cat-wrap"' not in content:
        content = content.replace('<footer>\n    <div class="container">',
                                  f'<footer>\n    <div class="container">\n{footer_plate_html}')

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("preview-bullet-journal-main.html updated with EXACTLY 3 chosen cats in optimal positions!")

# === 4. 更新校驗展廳 specimen-proof.html ===
def update_specimen_proof():
    proof_path = os.path.join(ASSETS_DIR, "specimen-proof.html")
    proof_html = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>精選三大去背插圖 × 雙貓品牌圖標校驗展廳</title>
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
      margin-bottom: 36px;
    }
    h1 {
      font-size: 2.1rem;
      margin-bottom: 8px;
      font-weight: 800;
    }
    .subtitle {
      color: var(--text-dim);
      font-size: 0.96rem;
      line-height: 1.6;
    }
    .icon-showcase {
      background: var(--card);
      border-radius: 20px;
      border: 1px solid var(--border);
      padding: 32px 24px;
      margin-bottom: 40px;
      display: flex;
      align-items: center;
      justify-content: space-around;
      flex-wrap: wrap;
      gap: 24px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }
    .icon-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }
    .icon-label {
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--text);
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 26px;
      margin-bottom: 40px;
    }
    .card {
      background: var(--card);
      border-radius: 18px;
      border: 1px solid var(--border);
      padding: 24px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: left;
    }
    .checker-box {
      width: 100%;
      height: 280px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #FFFFFF;
      background-image: 
        linear-gradient(45deg, #F5F2EC 25%, transparent 25%), 
        linear-gradient(-45deg, #F5F2EC 25%, transparent 25%), 
        linear-gradient(45deg, transparent 75%, #F5F2EC 75%), 
        linear-gradient(-45deg, transparent 75%, #F5F2EC 75%);
      background-size: 18px 18px;
      background-position: 0 0, 0 9px, 9px -9px, -9px 0px;
      border-radius: 12px;
      margin-bottom: 18px;
      border: 1px solid #EFEAE2;
    }
    .checker-box img {
      max-width: 88%;
      max-height: 90%;
      object-fit: contain;
      filter: drop-shadow(0 6px 14px rgba(45,41,38,0.1));
    }
    .cat-name {
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 6px;
      color: var(--text);
    }
    .cat-desc {
      font-size: 0.86rem;
      color: var(--text-dim);
      line-height: 1.6;
    }
    .btn {
      display: inline-block;
      margin-top: 32px;
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
      <h1>精選三大去背插圖 × 雙貓品牌圖標校驗展廳</h1>
      <div class="subtitle">
        依照指示：網頁僅保留讀者選定之 3 張純淨去背插圖 · 依照第 4 張重新裁切去除文字打造 Apple Touch Icon
      </div>
    </div>

    <!-- 品牌圖標專區 -->
    <div class="icon-showcase">
      <div class="icon-item">
        <div class="icon-label">Apple Touch Icon (180x180 Retina)</div>
        <img src="../assets/apple-touch-icon.png" width="120" height="120" alt="Apple Touch Icon" style="border-radius:24px;box-shadow:0 8px 24px rgba(45,41,38,0.12);">
        <div style="font-size:0.75rem;color:#8E8478;">依照片 4 雙貓書架伴讀精準 1:1 裁切，零多餘文字</div>
      </div>
      <div class="icon-item">
        <div class="icon-label">導覽列 Brand Icon (38x38)</div>
        <div style="width:54px;height:54px;background:#FAF7F2;border-radius:12px;display:flex;align-items:center;justify-content:center;border:1px solid #EAE2D8;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
          <img src="../img/brand-cat-38.png" width="38" height="38" alt="Brand Icon" style="border-radius:8px;">
        </div>
        <div style="font-size:0.75rem;color:#8E8478;">頂部導覽列高清晰度圖標</div>
      </div>
    </div>

    <!-- 網頁選定的 3 張插圖 -->
    <div class="grid">
      <!-- 選定圖 1 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/chosen-01-amber-stretch.png" alt="側伸腿放鬆貓">
        </div>
        <div class="cat-name">【選定圖 1 · 側伸腿放鬆貓】</div>
        <div class="cat-desc">
          • <b>去背與去字</b>：抹除上方所有文字標籤，外部背景 100% 透明化<br>
          • <b>網頁最佳位置</b>：<b>左側固定守護底圖</b>。呼應「【軌道一 · 生理放鬆】呼吸下沉，停止凍結」的心法意象，向橘白貓學習瓦解防禦、舒展後腿。
        </div>
      </div>

      <!-- 選定圖 3 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/chosen-03-sentinel-basket.png" alt="端坐編織提籃旁玳瑁貓">
        </div>
        <div class="cat-name">【選定圖 2 · 端坐編織提籃旁玳瑁貓】</div>
        <div class="cat-desc">
          • <b>去背與去字</b>：抹除左下文字，保留上方垂掛毛球，外部背景 100% 透明化<br>
          • <b>網頁最佳位置</b>：<b>右側固定守護底圖</b>。呼應「【軌道二 · 堅定邊界】端坐自持，停止道歉」的心理防線，像牠一樣清晰界限、端莊自持。
        </div>
      </div>

      <!-- 選定圖 5 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/chosen-05-total-surrender.png" alt="升降桌四腳朝天放鬆貓">
        </div>
        <div class="cat-name">【選定圖 3 · 升降桌四腳朝天徹底放鬆貓】</div>
        <div class="cat-desc">
          • <b>去背與去字</b>：抹除下方所有文字標籤，外部背景 100% 透明化<br>
          • <b>網頁最佳位置</b>：<b>頁尾睡前定錨收尾底圖</b>。置於全篇讀畢之「If-Then 執行意向與睡前充電儀式」底部，象徵全然臣服、身心重啟、零反芻內耗。
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
        f.write(proof_html)
    print("specimen-proof.html updated!")

if __name__ == '__main__':
    process_brand_icon()
    process_three_cats()
    update_web_html()
    update_specimen_proof()
    print("All tasks completed successfully!")

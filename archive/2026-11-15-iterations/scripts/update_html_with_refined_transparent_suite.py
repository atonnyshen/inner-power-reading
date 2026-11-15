#!/usr/bin/env python3
"""
update_html_with_refined_transparent_suite.py
將全套純淨透明、無明信片外框、無多餘文字、神情活靈活現的 5 幅手繪插畫與精品級圖標注入：
1. preview-bullet-journal-main.html
2. specimen-proof.html
"""

import os
import re

PROJECT_DIR = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading"
HTML_PATH = os.path.join(PROJECT_DIR, "preview-bullet-journal-main.html")
PROOF_PATH = os.path.join(PROJECT_DIR, "assets", "specimen-proof.html")

def update_main():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 更新導航列 Brand Icon
    brand_icon_html = '''<div class="brand-icon" aria-hidden="true">
      <img src="img/brand-cat-38.png" alt="手帳伴讀雙貓圖標" width="38" height="38" style="width:100%;height:100%;display:block;border-radius:9px;object-fit:cover;">
    </div>'''
    content = re.sub(r'<div class="brand-icon"[\s\S]*?</div>', brand_icon_html, content)

    # 2. 更新固定兩側守護貓咪 (純淨透明、無框、無文字、微投影)
    ambient_html = '''  <!-- Fixed Ambient Background Guardian Cats (純淨去背、零邊框、神情生動、融入手帳米白紙面) -->
  <div class="ambient-cat-fixed ambient-cat-left" aria-hidden="true">
    <img src="img/editorial/cat-01-amber-stretch-transparent.png" alt="身心放鬆·白色橘頭側伸後腿貓" width="220" height="220" style="width:100%;height:auto;display:block;filter:drop-shadow(0 6px 14px rgba(45,41,38,0.08));">
  </div>

  <div class="ambient-cat-fixed ambient-cat-right" aria-hidden="true">
    <img src="img/editorial/cat-03-sentinel-transparent.png" alt="堅定邊界·黑面翡翠眼白圍巾玳瑁貓" width="180" height="240" style="width:100%;height:auto;display:block;filter:drop-shadow(0 6px 14px rgba(45,41,38,0.08));">
  </div>'''
    ambient_pattern = r'<!-- Fixed Ambient Background Guardian Cats[\s\S]*?<div class="ambient-cat-fixed ambient-cat-left"[\s\S]*?</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[\s\S]*?</div>'
    if re.search(ambient_pattern, content):
        content = re.sub(ambient_pattern, ambient_html, content)

    # 3. 更新 Hero 橫幅底圖 (圖 4 雙貓書架伴讀，純淨透明、無字無框)
    hero_banner_html = '''<div class="editorial-hero-banner" style="margin: 24px auto 16px; max-width: 680px; text-align: center;">
          <img src="img/editorial/cat-04-dual-bookshelf-transparent.png" alt="雙貓書架俯瞰伴讀手繪去背插圖" style="max-width: 100%; height: auto; display: inline-block; filter: drop-shadow(0 8px 18px rgba(45,41,38,0.06));">
        </div>'''
    old_banner_pattern = r'<div class="editorial-hero-banner"[\s\S]*?</div>'
    if re.search(old_banner_pattern, content):
        content = re.sub(old_banner_pattern, hero_banner_html, content)

    # 4. 在「為什麼妳應該翻開原書？五大心智鬆綁」頂部加入「圖 2 沉睡微露粉掌玳瑁貓」(純淨透明、無字無框)
    plate_2_html = '''      <div class="editorial-plate-wrap" style="margin: 20px auto 28px; max-width: 480px; text-align: center;">
        <img src="img/editorial/cat-02-profound-sleep-transparent.png" alt="深度睡眠卸下防衛手繪去背插圖" style="max-width: 100%; height: auto; display: inline-block; filter: drop-shadow(0 6px 14px rgba(45,41,38,0.06));">
      </div>'''
    if '<div class="editorial-plate-wrap"' not in content:
        content = content.replace('<!-- Section 2: Reading Psychology -->\n  <section id="reading-strategy">\n    <div class="container">\n      <div class="section-header">',
                                  f'<!-- Section 2: Reading Psychology -->\n  <section id="reading-strategy">\n    <div class="container">\n      <div class="section-header">\n{plate_2_html}')

    # 5. 在頁尾收尾處加入「圖 5 升降桌四腳朝天徹底放鬆貓」(純淨透明、無字無框)
    plate_5_html = '''    <!-- 圖 5 升降桌四腳朝天徹底放鬆貓 (純淨去背、零文字、釋放所有壓力) -->
    <div class="editorial-footer-plate" style="margin: 24px auto 20px; max-width: 460px; text-align: center;">
      <img src="img/editorial/cat-05-total-surrender-transparent.png" alt="全然臣服身心重啟手繪去背插圖" style="max-width: 100%; height: auto; display: inline-block; filter: drop-shadow(0 6px 14px rgba(45,41,38,0.06));">
    </div>'''
    if '<div class="editorial-footer-plate"' not in content:
        content = content.replace('<footer>\n    <div class="container">',
                                  f'<footer>\n    <div class="container">\n{plate_5_html}')

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("preview-bullet-journal-main.html updated with clean transparent suite!")

def update_proof():
    proof_content = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>精品級雙貓圖標 × 五大純手繪透明插圖校驗展廳</title>
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
      max-width: 1040px;
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
    /* Brand Icon Showcase Box */
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
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-dim);
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
    /* 棋盤格背景展示真實透明通道 */
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
      <h1>精品級雙貓圖標 × 五大純手繪透明插圖校驗展廳</h1>
      <div class="subtitle">
        100% 去背去底圖 · 移除明信片框 · 零多餘文字 · 顏色神情傳神再現真實照片
      </div>
    </div>

    <!-- 頂級 Brand Icon & Apple Touch Icon 專區 -->
    <div class="icon-showcase">
      <div class="icon-item">
        <div class="icon-label">Apple Touch Icon (180x180 Retina)</div>
        <img src="../assets/apple-touch-icon.png" width="120" height="120" alt="Apple Touch Icon" style="border-radius:24px;box-shadow:0 8px 24px rgba(45,41,38,0.12);">
        <div style="font-size:0.75rem;color:#8E8478;">iPhone 桌面特寫雙貓依偎</div>
      </div>
      <div class="icon-item">
        <div class="icon-label">導覽列 Brand Icon (38x38)</div>
        <div style="width:54px;height:54px;background:#FAF7F2;border-radius:12px;display:flex;align-items:center;justify-content:center;border:1px solid #EAE2D8;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
          <img src="../img/brand-cat-38.png" width="38" height="38" alt="Brand Icon" style="border-radius:8px;">
        </div>
        <div style="font-size:0.75rem;color:#8E8478;">頂部導覽列高清晰度</div>
      </div>
    </div>

    <!-- 五大插圖卡片展廳 -->
    <div class="grid">
      <!-- 圖 4 -->
      <div class="card" style="grid-column: 1 / -1;">
        <div class="checker-box" style="height: 320px;">
          <img src="../img/editorial/cat-04-dual-bookshelf-transparent.png" alt="圖 4 雙貓書架俯瞰伴讀">
        </div>
        <div class="cat-name">【圖 4 · 雙貓高處書架俯瞰伴讀】(16:9 全景伴讀底圖)</div>
        <div class="cat-desc">
          <b>神色表情</b>：雙貓並排於書架頂層，橘白貓眼神溫和平靜、知性放鬆；玳瑁貓黑面墨色深沉、額頭焦糖金流光，雙眸專注俯瞰。下方勾勒簡約書脊。純去背透明底，零多餘文字。
        </div>
      </div>

      <!-- 圖 1 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/cat-01-amber-stretch-transparent.png" alt="圖 1 側伸腿放鬆貓">
        </div>
        <div class="cat-name">【圖 1 · 側伸後腿放鬆貓】(左側固定守護底圖)</div>
        <div class="cat-desc">
          <b>神色表情</b>：整齊平瀏海齊頭橘毛，黑豆大眼帶純真信任，粉鼻腮紅；身軀圓滾白拋，後腿瀟灑側伸露出橘色護膝斑與粉紅肉墊，前爪乖巧收於胸前。
        </div>
      </div>

      <!-- 圖 3 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/cat-03-sentinel-transparent.png" alt="圖 3 端坐玳瑁貓">
        </div>
        <div class="cat-name">【圖 3 · 黑面翡翠眼白領巾玳瑁貓】(右側固定守護底圖)</div>
        <div class="cat-desc">
          <b>神色表情</b>：水潤晶瑩的<b>碧綠翡翠大眼睛</b>，眼神清醒、端莊自持、不卑不亢；黑面罩臉龐帶正中金流光，右嘴角精巧點綴標誌性<b>黑美人痣</b>，胸前大片雪白厚毛圍巾，黑前腿配白手套。
        </div>
      </div>

      <!-- 圖 2 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/cat-02-profound-sleep-transparent.png" alt="圖 2 沉睡微露粉掌玳瑁貓">
        </div>
        <div class="cat-name">【圖 2 · 沉睡微露粉掌玳瑁貓】(心智鬆綁章節底圖)</div>
        <div class="cat-desc">
          <b>神色表情</b>：仰頭在櫃角熟睡，雙眼安詳微閉成線，神態極致安寧；一隻毛茸茸前爪向前舒展，露出粉嫩肉墊，象徵全然卸下防線的安全感。
        </div>
      </div>

      <!-- 圖 5 -->
      <div class="card">
        <div class="checker-box">
          <img src="../img/editorial/cat-05-total-surrender-transparent.png" alt="圖 5 升降桌四腳朝天放鬆貓">
        </div>
        <div class="cat-name">【圖 5 · 升降桌四腳朝天放鬆貓】(頁尾睡前定錨底圖)</div>
        <div class="cat-desc">
          <b>神色表情</b>：在升降桌上四腳朝天仰面大躺平，四隻腳爪向空中伸展露出滿滿粉嫩肉墊，嘴角沉醉安詳，象徵閱讀完畢後徹底釋懷與身心重啟。
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
    with open(PROOF_PATH, "w", encoding="utf-8") as f:
        f.write(proof_content)
    print("specimen-proof.html updated with refined suite!")

if __name__ == '__main__':
    update_main()
    update_proof()

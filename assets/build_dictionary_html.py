#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from generate_symbols import ALL_SYMBOLS, ASSETS_DIR

def build():
    dict_path = os.path.join(ASSETS_DIR, "svg-dictionary.html")
    
    catalog_cards = []
    embedded_symbols = []
    
    for item in ALL_SYMBOLS:
        embedded_symbols.append(f'  <symbol id="{item["id"]}" viewBox="{item["viewBox"]}">\n{item["content"]}\n  </symbol>')
        
        card_class = "catalog-card catalog-card-wide" if item["is_plate"] else "catalog-card"
        icon_display = f'''<div class="card-preview">
  <svg class="preview-svg" viewBox="{item['viewBox']}" role="img" aria-label="{item['title']}">
    <use href="#{item['id']}"/>
  </svg>
</div>'''
        code_raw = f'<svg class="{ "bujo-specimen-svg" if item["is_plate"] else "riso-icon" }" role="img" aria-label="{item["title"]}"><use href="assets/riso-symbols.svg#{item["id"]}"/></svg>'
        code_escaped = code_raw.replace('<', '&lt;').replace('>', '&gt;')
        
        catalog_cards.append(f'''
      <article class="{card_class}" id="card-{item['id']}">
        {icon_display}
        <div class="card-meta">
          <span class="card-tag">ID: #{item['id']}</span>
          <h3 class="card-title">{item['title']}</h3>
          <span class="card-dim">VIEWBOX: {item['viewBox']} · FILE: {item['filename']}</span>
          <div class="code-box">
            <code>{code_escaped}</code>
          </div>
          <button type="button" class="btn-copy" onclick="copySnippet(this, '{item['id']}')" aria-label="複製 {item['title']} 引用碼">複製引用碼</button>
        </div>
      </article>''')

    cards_html = '\n'.join(catalog_cards)
    symbols_embedded_html = '\n'.join(embedded_symbols)

    template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>瑞士解構 Risograph 雙色向量符號庫字典 | 溫柔生長・手帳讀書誌</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --font-serif: "Noto Serif TC", "Noto Serif SC", "Songti TC", "Songti SC", "Source Han Serif TC", serif;
      --font-sans: "Noto Sans TC", "Noto Sans SC", "PingFang TC", "Source Han Sans TC", system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
      
      --riso-ink: #2D2926;
      --riso-rose: #C06C52;
      --riso-sage: #3E6B56;
      --riso-amber: #9E6234;
      --riso-paper: #FAF8F5;
      --riso-paper-alt: #F4EFEA;
      --riso-grid-line: rgba(45, 41, 38, 0.12);
      
      --bg-page: #FAF8F5;
      --bg-card: #FFFFFF;
      --text-main: #2D2926;
      --text-muted: #59534D;
      --text-dim: #888077;
      --border-subtle: #E8E1D7;
      --border-card: #EFE8DE;
      --nav-height: 64px;
      scroll-padding-top: var(--nav-height);
    }

    [data-theme="night"],
    @media (prefers-color-scheme: dark) {
      :root {
        --riso-ink: #E8E5DE;
        --riso-paper: #181B1E;
        --riso-paper-alt: #22262B;
        --riso-rose: #E2856E;
        --riso-sage: #6EA98F;
        --riso-amber: #C98A55;
        --riso-grid-line: rgba(232, 229, 222, 0.12);
        
        --bg-page: #14171A;
        --bg-card: #1C2024;
        --text-main: #E8E5DE;
        --text-muted: #A3A099;
        --text-dim: #7C7A75;
        --border-subtle: #2C3036;
        --border-card: #2E3339;
      }
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      min-width: 0;
    }

    html, body {
      overflow-x: hidden;
      width: 100%;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg-page);
      background-image: radial-gradient(rgba(200, 190, 178, 0.35) 1px, transparent 1px);
      background-size: 24px 24px;
      color: var(--text-main);
      line-height: 1.8;
      padding-top: var(--nav-height);
    }

    /* Focus visible accessibility */
    :focus-visible {
      outline: 2px solid var(--riso-rose);
      outline-offset: 2px;
    }

    /* Navigation Bar */
    header.top-nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: var(--nav-height);
      background: rgba(250, 248, 245, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      z-index: 100;
      display: flex;
      align-items: center;
      padding: 0 24px;
      transition: transform 0.25s ease;
    }

    [data-theme="night"] header.top-nav {
      background: rgba(20, 23, 26, 0.88);
    }

    .nav-container {
      max-width: 1080px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .nav-brand {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      color: var(--text-main);
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: 1.05rem;
    }

    .nav-brand svg {
      width: 24px;
      height: 24px;
      flex-shrink: 0;
    }

    .nav-chip-list {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: nowrap;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      -webkit-overflow-scrolling: touch;
      padding-bottom: 2px;
    }

    .nav-chip {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 4px 10px;
      border-radius: 4px;
      background: rgba(45, 41, 38, 0.04);
      color: var(--text-muted);
      text-decoration: none;
      white-space: nowrap;
      transition: background 0.15s ease, color 0.15s ease;
      flex-shrink: 0;
    }

    .nav-chip:hover {
      background: var(--riso-rose);
      color: #FFFFFF;
    }

    main.content-area {
      max-width: 1080px;
      margin: 0 auto;
      padding: 36px 20px 64px 20px;
    }

    .hero-banner {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 12px;
      padding: 36px 32px;
      margin-bottom: 36px;
      box-shadow: 0 4px 24px rgba(45, 41, 38, 0.04);
    }

    .eyebrow-tag {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--riso-rose);
      letter-spacing: 0.1em;
      margin-bottom: 8px;
    }

    h1.hero-title {
      font-family: var(--font-serif);
      font-size: 1.85rem;
      font-weight: 700;
      line-height: 1.4;
      margin-bottom: 12px;
    }

    p.hero-desc {
      max-width: 680px;
      font-size: 0.96rem;
      color: var(--text-muted);
      line-height: 1.8;
      margin-bottom: 20px;
    }

    .palette-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      padding-top: 18px;
      border-top: 1px dashed var(--border-subtle);
    }

    .palette-chip {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
      background: var(--bg-card);
    }

    .chip-swatch {
      width: 14px;
      height: 14px;
      border-radius: 2px;
      flex-shrink: 0;
    }

    /* Section Structure */
    .catalog-section {
      margin-bottom: 48px;
    }

    .section-header {
      margin-bottom: 24px;
    }

    h2.section-heading {
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 600;
      margin-bottom: 6px;
    }

    p.section-sub {
      font-size: 0.88rem;
      color: var(--text-dim);
    }

    /* Catalog Cards Grid */
    .catalog-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
    }

    .catalog-card {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 10px;
      padding: 22px;
      box-shadow: 0 2px 10px rgba(45, 41, 38, 0.03);
      display: flex;
      flex-direction: column;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .catalog-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(45, 41, 38, 0.07);
    }

    .catalog-card-wide {
      grid-column: 1 / -1;
    }

    .card-preview {
      background: var(--riso-paper);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 140px;
      margin-bottom: 16px;
    }

    .catalog-card-wide .card-preview {
      min-height: 240px;
      max-height: 380px;
    }

    .preview-svg {
      width: 100%;
      height: 100%;
      max-height: 280px;
      shape-rendering: geometricPrecision;
    }

    .card-meta {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .card-tag {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--riso-rose);
      font-weight: 700;
    }

    h3.card-title {
      font-family: var(--font-serif);
      font-size: 1.05rem;
      font-weight: 600;
    }

    .card-dim {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--text-dim);
    }

    .code-box {
      background: var(--riso-paper-alt);
      border: 1px solid var(--border-subtle);
      border-radius: 4px;
      padding: 8px 10px;
      margin: 8px 0;
      overflow-x: auto;
    }

    code {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--text-main);
      white-space: pre-wrap;
      word-break: break-all;
    }

    .btn-copy {
      background: rgba(45, 41, 38, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 500;
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      align-self: flex-start;
      transition: all 0.15s ease;
    }

    .btn-copy:hover {
      background: var(--riso-rose);
      color: #FFFFFF;
      border-color: var(--riso-rose);
    }

    /* Toast Notification for Accessibility */
    #status-toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--text-main);
      color: var(--bg-page);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      padding: 10px 18px;
      border-radius: 6px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
      opacity: 0;
      pointer-events: none;
      transform: translateY(8px);
      transition: opacity 0.2s ease, transform 0.2s ease;
      z-index: 999;
    }

    #status-toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* Footer */
    footer.colophon-footer {
      border-top: 1px solid var(--border-subtle);
      padding: 40px 20px;
      font-size: 0.82rem;
      color: var(--text-dim);
      background: var(--bg-card);
      margin-top: 48px;
    }

    .footer-container {
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .footer-links {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
    }

    .footer-links a {
      color: var(--riso-sage);
      text-decoration: none;
    }

    .footer-links a:hover {
      text-decoration: underline;
    }

    /* Media Queries */
    @media (max-width: 768px) {
      header.top-nav {
        padding: 0 16px;
      }
      main.content-area {
        padding: 24px 16px 48px 16px;
      }
      .hero-banner {
        padding: 24px 18px;
      }
      h1.hero-title {
        font-size: 1.45rem;
      }
      .catalog-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>
  <!-- Master SVG Sprite Embedded -->
  <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
__SYMBOLS_EMBEDDED__
  </svg>

  <!-- Top Navigation Header -->
  <header class="top-nav">
    <div class="nav-container">
      <a href="#" class="nav-brand">
        <svg viewBox="0 0 32 32" role="img" aria-label="手帳讀書誌標識"><use href="#symbol-brand-cat"/></svg>
        <span>溫柔生長・手帳讀書誌</span>
      </a>
      <nav class="nav-chip-list" aria-label="符號分類導覽">
        <a href="#specimens" class="nav-chip">雙貓心理學標本</a>
        <a href="#card-symbol-glasses" class="nav-chip">生活花草物件</a>
        <a href="#card-symbol-lightning" class="nav-chip">系統機能圖示</a>
        <a href="../preview-bullet-journal-main.html" class="nav-chip">回手帳首頁</a>
      </nav>
    </div>
  </header>

  <main class="content-area" id="main-content">
    <!-- Hero Banner -->
    <section class="hero-banner" id="hero">
      <span class="eyebrow-tag">SWISS DECONSTRUCTED · RISOGRAPH DUAL-DRUM · VECTOR ASSETS</span>
      <h1 class="hero-title">抽象幾何標識字典與 SVG 樣式手冊</h1>
      <p class="hero-desc">
        依據瑞士幾何構造線與 Risograph 雙色印刷錯位體系，將雙貓心理學姿態與五大生活花草物件提煉為純量向量符號庫。全面杜絕寫實照片與多餘出血，在物理尺度一致性下支援微型坐標註記與手帳點陣紙紋。
      </p>
      <div class="palette-strip">
        <div class="palette-chip"><div class="chip-swatch" style="background:#C06C52;"></div> <span>RISO ROSE #C06C52</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#3E6B56;"></div> <span>RISO SAGE #3E6B56</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#9E6234;"></div> <span>RISO AMBER #9E6234</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#2D2926;"></div> <span>RISO INK #2D2926</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#FAF8F5; border:1px solid #ddd;"></div> <span>RISO PAPER #FAF8F5</span></div>
      </div>
    </section>

    <!-- Symbols Catalog Grid -->
    <section class="catalog-section" id="specimens">
      <div class="section-header">
        <h2 class="section-heading">全量向量標識目錄 (17 組符號規格)</h2>
        <p class="section-sub">點擊下方「複製引用碼」即可直接複製對應的 SVG 標籤結構。</p>
      </div>

      <div class="catalog-grid">
__CARDS_HTML__
      </div>
    </section>
  </main>

  <!-- Live Status Toast for Screen Readers & Keyboard Users -->
  <div id="status-toast" role="status" aria-live="polite">已複製 SVG 引用標籤</div>

  <!-- Footer Colophon -->
  <footer class="colophon-footer">
    <div class="footer-container">
      <p>版權聲明：本手帳讀書誌所有向量標識與幾何構造圖形，均依據文化教育推廣與非營利導讀之合理使用原則建構。</p>
      <p>資料來源與引證：解構瑞士國際主義平面設計風格、史丹佛權力學、密西根神經反芻腦科學與 Risograph 物理錯位印刷。</p>
      <div class="footer-links">
        <span>著作權與權利人聯絡聯繫與優先下架管道：contact@inner-power-reading.org</span>
        <a href="#hero">返回頂部</a>
      </div>
    </div>
  </footer>

  <script>
    function copySnippet(btn, id) {
      const isPlate = id.includes('plate');
      const cls = isPlate ? 'bujo-specimen-svg' : 'riso-icon';
      const code = '<svg class="' + cls + '" role="img" aria-label="' + id + '"><use href="assets/riso-symbols.svg#' + id + '"/></svg>';
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(code).then(() => {
          showToast('已成功複製 #' + id + ' 引用碼');
        });
      } else {
        showToast('已複製 #' + id);
      }
    }

    function showToast(msg) {
      const toast = document.getElementById('status-toast');
      if (!toast) return;
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2200);
    }

    // Keyboard support for Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const toast = document.getElementById('status-toast');
        if (toast) toast.classList.remove('show');
      }
    });
  </script>
</body>
</html>"""

    final_html = template.replace("__SYMBOLS_EMBEDDED__", symbols_embedded_html).replace("__CARDS_HTML__", cards_html)

    with open(dict_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Generated visual dictionary HTML: {dict_path}")

if __name__ == "__main__":
    build()

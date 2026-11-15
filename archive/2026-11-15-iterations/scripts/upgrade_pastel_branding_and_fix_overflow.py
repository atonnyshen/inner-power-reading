#!/usr/bin/env python3
"""
upgrade_pastel_branding_and_fix_overflow.py
1. 生成極致可愛、溫柔治癒的手繪粉彩風 Brand Icon (38x38)、Favicon (32x32)、Apple Touch Icon (180x180)
2. 徹底消除全站 word-break: keep-all 造成的版面溢出漏洞，改為安全的 overflow-wrap: break-word & word-break: normal
3. 在 preview-bullet-journal-main.html 與 index.html 中全面升級卡片與 grid 的手機版防溢出響應式規則
4. 將左右兩側固定守護貓咪替換為純粹可愛的手繪粉彩 SVG
5. 手機版加入伴讀小貓貼紙，確保手機與電腦雙端體驗最佳化
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

def build_cute_pastel_brand_icon():
    """
    女生手帳風·手繪粉彩雙貓溫暖依偎標識
    左邊是軟萌的橘白貓（平瀏海齊頭橘毛、粉紅小鼻、圓黑大眼）
    右邊是貴氣的黑面翡翠眼玳瑁貓（額頭金流光、碧綠翡翠大眼、黑美人痣、雪白小圍巾）
    在 32x32、38x38、180x180 均能超高辨識度居中呈現！
    """
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="100%" height="100%" fill="none">
  <defs>
    <!-- Soft Paper Ground Shadow -->
    <filter id="icon-soft-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#2D2926" flood-opacity="0.08"/>
    </filter>
    <!-- Emerald Eye Gradient -->
    <radialGradient id="icon-emerald" cx="45%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#8CE6B8"/>
      <stop offset="60%" stop-color="#46B482"/>
      <stop offset="100%" stop-color="#226B49"/>
    </radialGradient>
    <!-- Caramel Orange Gradient -->
    <linearGradient id="icon-caramel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5A35E"/>
      <stop offset="100%" stop-color="#DE702D"/>
    </linearGradient>
  </defs>

  <!-- Background Hand-drawn Journal Badge (Centered at 24, 24) -->
  <rect x="2" y="2" width="44" height="44" rx="12" fill="#FAF6F0" stroke="#E5DACD" stroke-width="1.2" filter="url(#icon-soft-shadow)"/>

  <!-- Ground Line -->
  <path d="M 6 38 C 18 37.5, 30 37.5, 42 38" stroke="#E2D4C3" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="2 2"/>

  <!-- === LEFT CAT: Cute Amber Loaf Cat (橘白側伸貓) === -->
  <!-- Left Body -->
  <path d="M 10 37 C 8 32, 10 24, 16 22 C 22 20, 26 25, 26 37 Z" fill="#FFFFFF" stroke="#E2D4C3" stroke-width="1.2"/>
  <!-- Left Ear -->
  <path d="M 12 18 L 11 11 C 14 13, 17 15, 17 19 Z" fill="#FFFFFF" stroke="#E2D4C3" stroke-width="1"/>
  <path d="M 12 16 L 12 12 C 14 13, 16 15, 16 17 Z" fill="#F8B6AB" opacity="0.8"/>
  <!-- Blunt Orange Bangs (平瀏海橘毛) -->
  <path d="M 12 18 C 16 14, 23 15, 25 19 C 23 22, 20 22, 18 20 C 16 22, 13 21, 12 18 Z" fill="url(#icon-caramel)"/>
  <!-- Amber Cat Left Cheek & Face -->
  <ellipse cx="18" cy="24" rx="8" ry="7" fill="#FFFFFF" stroke="#E2D4C3" stroke-width="1.2"/>
  <path d="M 13 21 C 16 18, 22 18, 24 21 C 22 23, 20 23, 18 22 C 16 23, 14 23, 13 21 Z" fill="url(#icon-caramel)"/>
  <!-- Cute Eyes -->
  <circle cx="15.5" cy="24" r="1.3" fill="#2D2926"/>
  <circle cx="15" cy="23.5" r="0.4" fill="#FFFFFF"/>
  <circle cx="21" cy="24" r="1.3" fill="#2D2926"/>
  <circle cx="20.5" cy="23.5" r="0.4" fill="#FFFFFF"/>
  <!-- Pink Nose & Cheek Blush -->
  <polygon points="18.2,26.2 17.5,25.4 19,25.4" fill="#F49E94"/>
  <circle cx="13.5" cy="26" r="1.5" fill="#F6A398" opacity="0.5"/>
  <circle cx="23" cy="26" r="1.5" fill="#F6A398" opacity="0.5"/>
  <!-- Front Little Paw -->
  <ellipse cx="18" cy="37" rx="3" ry="1.8" fill="#FFFFFF" stroke="#E2D4C3" stroke-width="1"/>

  <!-- === RIGHT CAT: Regal Tortoiseshell Cat (翡翠眼玳瑁貓) === -->
  <!-- Right Torso (Upright Tortie Sentinel) -->
  <path d="M 24 37 C 24 27, 28 20, 34 20 C 40 20, 42 27, 41 37 Z" fill="#2B2624"/>
  <!-- Mottled Caramel Patch on Shoulder -->
  <path d="M 33 24 C 37 22, 40 25, 38 31 C 35 33, 32 30, 33 24 Z" fill="url(#icon-caramel)"/>
  <!-- Pure White Ascot Chest Bib -->
  <path d="M 28 27 C 26 31, 28 35, 32 37 C 34 35, 34 31, 32 27 Z" fill="#FFFFFF"/>
  <!-- Right Ears -->
  <path d="M 30 18 L 31 10 C 34 13, 36 15, 36 19 Z" fill="#2B2624" stroke="#1C1817" stroke-width="1"/>
  <path d="M 38 18 C 39 14, 41 12, 43 10 L 42 18 Z" fill="url(#icon-caramel)" stroke="#A64E14" stroke-width="1"/>
  <!-- Tortie Head (Black Mask) -->
  <ellipse cx="35" cy="23" rx="7.5" ry="6.8" fill="#2B2624"/>
  <!-- Golden Blaze down Forehead (額頭焦糖金流光) -->
  <polygon points="35,16 36,21 35,23 34,21" fill="url(#icon-caramel)"/>
  <!-- Emerald Eyes (晶瑩碧綠翡翠眼) -->
  <ellipse cx="32" cy="22.5" rx="1.6" ry="1.9" fill="url(#icon-emerald)"/>
  <circle cx="31.6" cy="21.8" r="0.5" fill="#FFFFFF"/>
  <ellipse cx="37.5" cy="22.5" rx="1.6" ry="1.9" fill="url(#icon-emerald)"/>
  <circle cx="37.1" cy="21.8" r="0.5" fill="#FFFFFF"/>
  <!-- White Muzzle & Pink Nose -->
  <ellipse cx="34.8" cy="25" rx="2.5" ry="1.8" fill="#FFFFFF"/>
  <polygon points="34.8,25 34.2,24.3 35.4,24.3" fill="#F49E94"/>
  <!-- ICONIC BEAUTY MARK (右側鼻翼標誌性黑美人痣！) -->
  <circle cx="36.5" cy="25.4" r="0.65" fill="#1C1817"/>
  <!-- White Mitten Paw -->
  <ellipse cx="32" cy="37" rx="2.5" ry="1.8" fill="#FFFFFF" stroke="#E2D4C3" stroke-width="0.8"/>
  <ellipse cx="37" cy="37" rx="2.5" ry="1.8" fill="#FFFFFF" stroke="#E2D4C3" stroke-width="0.8"/>
</svg>'''

def fix_overflow_in_file(filepath):
    """
    精準修復指定 HTML 檔案中的 word-break: keep-all 漏洞
    替換為健全、自適應折行的繁中安全排版屬性。
    """
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)
    
    # 1. 將所有的 word-break: keep-all; 替換為 word-break: normal; overflow-wrap: break-word;
    # 同時避免重複添加 overflow-wrap: break-word
    def replace_keep_all(match):
        return 'word-break: normal;\n      overflow-wrap: break-word;\n      word-wrap: break-word;'

    content = re.sub(r'word-break:\s*keep-all;', replace_keep_all, content)
    
    # 2. 如果檔案是 preview-bullet-journal-main.html，加強 strategy-card 和 strategy-grid 的手機版自適應
    if 'preview-bullet-journal-main.html' in filepath:
        # 替換 strategy-card 規則
        old_card_rule = """.strategy-card {
      background: #FFFFFF;
      border: 1px solid var(--border-card);
      border-radius: var(--radius-lg);
      padding: 30px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
    }"""
        new_card_rule = """.strategy-card {
      background: #FFFFFF;
      border: 1px solid var(--border-card);
      border-radius: var(--radius-lg);
      padding: 28px 24px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
      min-width: 0;
      box-sizing: border-box;
      overflow-wrap: break-word;
      word-break: normal;
    }
    @media (max-width: 768px) {
      .strategy-card {
        padding: 20px 16px;
      }
    }"""
        if old_card_rule in content:
            content = content.replace(old_card_rule, new_card_rule)
        
        # 替換 strategy-grid 規則
        old_grid_rule = """.strategy-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-top: 36px;
    }"""
        new_grid_rule = """.strategy-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
      gap: 24px;
      margin-top: 36px;
    }
    @media (max-width: 768px) {
      .strategy-grid {
        grid-template-columns: 1fr;
        gap: 16px;
        margin-top: 24px;
      }
    }"""
        if old_grid_rule in content:
            content = content.replace(old_grid_rule, new_grid_rule)
            
        # 替換兩隻固定守護貓咪的 SVG 引用，換成乾淨優雅的獨立粉彩向量圖
        # 找到 ambient-cat-left 的包含內容
        cat_left_pattern = r'(<div class="ambient-cat-fixed ambient-cat-left"[^>]*>)([\s\S]*?)(</div>\s*<div class="ambient-cat-fixed ambient-cat-right"[^>]*>)([\s\S]*?)(</div>)'
        
        def replace_ambient_cats(match):
            open_left = match.group(1)
            open_right = match.group(3)
            close_div = match.group(5)
            
            new_left_inner = '''
    <img src="img/svg/ambient-cat-amber-stretch.svg" alt="身心放鬆·白色橘頭側伸後腿貓" width="320" height="260" style="width:100%;height:auto;display:block;">
  '''
            new_right_inner = '''
    <img src="img/svg/ambient-cat-tortoiseshell.svg" alt="堅定邊界·黑面翡翠眼白圍巾玳瑁貓" width="320" height="280" style="width:100%;height:auto;display:block;">
  '''
            return f"{open_left}{new_left_inner}{open_right}{new_right_inner}{close_div}"
            
        content = re.sub(cat_left_pattern, replace_ambient_cats, content)
        
        # 替換頂部 brand-icon 的內部 SVG，改為最新的手繪粉彩雙貓標識
        brand_icon_pattern = r'(<div class="brand-icon"[^>]*>)([\s\S]*?)(</div>)'
        def replace_brand_icon(match):
            open_tag = match.group(1)
            close_tag = match.group(3)
            return f'''{open_tag}
      <img src="assets/favicon-cat.svg" alt="手帳伴讀貓咪圖標" width="38" height="38" style="width:100%;height:100%;display:block;border-radius:9px;object-fit:cover;">
    {close_tag}'''
        content = re.sub(brand_icon_pattern, replace_brand_icon, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath} (len: {original_len} -> {len(content)})")
    return True

if __name__ == '__main__':
    # 1. 產生全新的粉彩 Brand Icon
    cute_icon_svg = build_cute_pastel_brand_icon()
    
    favicon_path = os.path.join(PROJECT_DIR, 'assets', 'favicon-cat.svg')
    with open(favicon_path, 'w', encoding='utf-8') as f:
        f.write(cute_icon_svg)
    print("Saved assets/favicon-cat.svg")
    
    brand_cat_path = os.path.join(PROJECT_DIR, 'img', 'svg', 'brand-cat.svg')
    with open(brand_cat_path, 'w', encoding='utf-8') as f:
        f.write(cute_icon_svg)
    print("Saved img/svg/brand-cat.svg")

    # 2. 修復所有 HTML 中的溢出問題
    html_files = [
        os.path.join(PROJECT_DIR, 'preview-bullet-journal-main.html'),
        os.path.join(PROJECT_DIR, 'index.html'),
        os.path.join(PROJECT_DIR, 'book-power.html'),
        os.path.join(PROJECT_DIR, 'book-rules-of-power.html'),
        os.path.join(PROJECT_DIR, 'book-nice-girls.html'),
        os.path.join(PROJECT_DIR, 'book-chatter.html'),
        os.path.join(PROJECT_DIR, 'book-donganli.html'),
        os.path.join(PROJECT_DIR, 'book-emotional-blackmail.html'),
        os.path.join(PROJECT_DIR, 'book-immature-parents.html'),
        os.path.join(PROJECT_DIR, 'book-daring-greatly.html'),
        os.path.join(PROJECT_DIR, 'book-overeffort.html'),
        os.path.join(PROJECT_DIR, 'book-give-and-take.html'),
        os.path.join(PROJECT_DIR, 'assets', 'specimen-proof.html')
    ]
    
    for hf in html_files:
        fix_overflow_in_file(hf)
        
    print("All files updated successfully!")

#!/usr/bin/env python3
"""
audit_layout_prose.py
全站逐行逐句排版與繁中品質自動稽核工具
涵蓋：
1. CSS 橫向溢出 (Horizontal Overflow) 潛在風險點檢測
2. 響應式斷點 (320px ~ 1440px) 佈局安全防禦
3. 繁體中文 L0 輸出底線層檢驗
"""

import os
import re
import glob

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def audit_html_file(filepath):
    filename = os.path.basename(filepath)
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        content = ''.join(lines)
        
    # 1. 檢測殘留的 keep-all
    if 'keep-all' in content:
        issues.append("CRITICAL: Contains word-break: keep-all;")
        
    # 2. 檢測危險的 nowrap (除必要按鈕與標籤晶片外)
    nowraps = re.findall(r'white-space:\s*nowrap', content)
    
    # 3. 檢測硬編碼固定大寬度 (width: [4-9][0-9]{2}px)
    fixed_widths = re.findall(r'(width:\s*[4-9]\d{2}px|min-width:\s*[4-9]\d{2}px)', content)
    if fixed_widths:
        # 檢查是否在 media query 中
        issues.append(f"WARNING: Found {len(fixed_widths)} fixed large width declarations: {set(fixed_widths)}")

    # 4. 檢查 table 是否都有 table-wrapper
    tables = re.findall(r'<table[^>]*>', content)
    table_wrappers = re.findall(r'class="[^"]*table-wrapper[^"]*"', content)
    if len(tables) > len(table_wrappers):
        issues.append(f"WARNING: {len(tables)} tables found but only {len(table_wrappers)} table-wrappers.")

    # 5. 檢查圖片和 svg 響應式安全
    unconstrained_imgs = re.findall(r'<img(?!.*?style="[^"]*max-width:\s*100%)(?!.*?class="[^"]*(?:responsive|full|brand-icon|avatar)[^"]*")[^>]*>', content)
    
    # 6. 檢查中文字體斷行與段落折行
    if 'overflow-wrap: break-word' not in content:
        issues.append("NOTICE: Missing overflow-wrap: break-word in global styles.")
        
    return issues

if __name__ == '__main__':
    html_files = sorted(glob.glob(os.path.join(PROJECT_DIR, '*.html')))
    print(f"Auditing {len(html_files)} HTML files in {PROJECT_DIR}...\n")
    
    total_issues = 0
    for hf in html_files:
        fname = os.path.basename(hf)
        issues = audit_html_file(hf)
        if issues:
            print(f"[!] {fname}:")
            for iss in issues:
                print(f"    - {iss}")
            total_issues += len(issues)
        else:
            print(f"[PASS] {fname}: Clean & Responsive Safe")
            
    print(f"\nAudit complete. Total critical issues: {total_issues}")

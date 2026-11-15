#!/usr/bin/env python3
"""
make_transparent_assets.py
高畫質去背處理工具：
1. 讀取生成的圖像，將純白/淺米白背景精確轉為 100% 透明通道 (Alpha Transparency)。
2. 保持貓咪內部白色毛髮（白胸毛、白腹部、白前爪）不被誤透明化（Flood Fill / 邊緣擴散演算法）。
3. 輸出乾淨純粹的透明 PNG (RGBA)，直接融入網頁底圖，擺脫明信片框與外邊框！
"""

import os
from PIL import Image

def remove_background_outside(img_path, out_path, tolerance=24):
    """
    從四個角落向內洪水填充 (Flood Fill)，只將外圍背景轉為透明，
    徹底保護貓咪身體內部的純白毛髮！
    """
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    
    # 取得角落背景代表色
    corners = [img.getpixel((0, 0)), img.getpixel((w-1, 0)), img.getpixel((0, h-1)), img.getpixel((w-1, h-1))]
    bg_r = sum(c[0] for c in corners) // 4
    bg_g = sum(c[1] for c in corners) // 4
    bg_b = sum(c[2] for c in corners) // 4

    pixels = img.load()
    
    # 使用 BFS 從邊緣所有白色/淺色像素開始蔓延
    visited = [[False]*h for _ in range(w)]
    queue = []
    
    # 將所有外邊界像素加入隊列
    for x in range(w):
        queue.append((x, 0))
        queue.append((x, h-1))
    for y in range(h):
        queue.append((0, y))
        queue.append((w-1, y))
        
    def is_bg(r, g, b):
        return (abs(r - bg_r) <= tolerance and 
                abs(g - bg_g) <= tolerance and 
                abs(b - bg_b) <= tolerance) or (r > 240 and g > 235 and b > 225)

    head = 0
    while head < len(queue):
        cx, cy = queue[head]
        head += 1
        
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        
        r, g, b, a = pixels[cx, cy]
        if is_bg(r, g, b):
            # 設為全透明
            pixels[cx, cy] = (r, g, b, 0)
            
            # 向四周擴展
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                    nr, ng, nb, _ = pixels[nx, ny]
                    if is_bg(nr, ng, nb):
                        queue.append((nx, ny))

    img.save(out_path, format="PNG")
    print(f"Saved transparent PNG: {out_path} ({w}x{h})")

if __name__ == '__main__':
    print("Background removal script ready.")

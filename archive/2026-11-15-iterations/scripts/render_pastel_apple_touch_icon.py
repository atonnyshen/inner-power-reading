#!/usr/bin/env python3
"""
render_pastel_apple_touch_icon.py
使用 Pillow 繪製 180x180 官方 iOS Apple Touch Icon (Retina 3x 規格)
呈現手繪粉彩雙貓溫暖依偎圖標：
- 左側：白色橘頭貓（齊瀏海橘毛、呆萌圓眼、粉嫩腮紅與小鼻）
- 右側：黑面翡翠眼玳瑁貓（額頭金流光、寶石翡翠眼、黑美人痣、雪白胸毛）
- 完美居中、留足 18% iOS 圓角裁切安全邊界。
"""

import math
from PIL import Image, ImageDraw, ImageFilter

def create_apple_touch_icon():
    size = 180
    scale = 4  # 4x 超取樣抗鋸齒繪製 (720x720)
    w = size * scale
    h = size * scale

    img = Image.new("RGBA", (w, h), (250, 246, 240, 255)) # 溫暖米白紙底 #FAF6F0
    draw = ImageDraw.Draw(img)

    # 繪製溫和的手帳雙層精緻邊框
    border_col = (222, 212, 198, 255)
    inner_border_col = (235, 227, 215, 255)
    draw.rounded_rectangle([12 * scale, 12 * scale, (size - 12) * scale, (size - 12) * scale], radius=28 * scale, outline=border_col, width=3 * scale)
    draw.rounded_rectangle([15 * scale, 15 * scale, (size - 15) * scale, (size - 15) * scale], radius=25 * scale, outline=inner_border_col, width=1 * scale)

    # 地平線/手帳坐標虛線 (Y = 138)
    ground_y = 138 * scale
    draw.line([(24 * scale, ground_y), ((size - 24) * scale, ground_y)], fill=(225, 215, 202, 255), width=2 * scale)

    # === 左貓：白色橘頭側伸貓 (Amber Loaf Cat) ===
    # 貓身白拋拋身軀 (坐標中心 ~ 68, 108)
    body_bbox = [(38 * scale, 82 * scale), (98 * scale, 138 * scale)]
    draw.ellipse(body_bbox, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255), width=2 * scale)

    # 左耳
    ear_l = [(46 * scale, 75 * scale), (44 * scale, 50 * scale), (62 * scale, 64 * scale)]
    draw.polygon(ear_l, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255))
    ear_l_in = [(47 * scale, 70 * scale), (46 * scale, 55 * scale), (58 * scale, 64 * scale)]
    draw.polygon(ear_l_in, fill=(248, 182, 171, 200)) # 內耳柔粉

    # 橘毛頭頂與瀏海 (齊頭橘平瀏海！)
    cap_poly = [(48 * scale, 72 * scale), (68 * scale, 60 * scale), (88 * scale, 72 * scale), 
                (84 * scale, 86 * scale), (76 * scale, 88 * scale), (68 * scale, 84 * scale), 
                (60 * scale, 88 * scale), (52 * scale, 86 * scale)]
    draw.polygon(cap_poly, fill=(243, 156, 85, 255)) # 溫暖焦糖橘

    # 左貓面部白底圓蛋
    face_bbox = [(48 * scale, 70 * scale), (88 * scale, 110 * scale)]
    draw.ellipse(face_bbox, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255), width=2 * scale)
    # 補回額頭瀏海
    bangs = [(52 * scale, 74 * scale), (68 * scale, 68 * scale), (84 * scale, 74 * scale),
             (80 * scale, 84 * scale), (74 * scale, 86 * scale), (68 * scale, 83 * scale),
             (62 * scale, 86 * scale), (56 * scale, 84 * scale)]
    draw.polygon(bangs, fill=(243, 156, 85, 255))

    # 左貓眼睛 (黑曜石圓眼 + 高光白點)
    draw.ellipse([(57 * scale, 88 * scale), (65 * scale, 97 * scale)], fill=(45, 40, 38, 255))
    draw.ellipse([(59 * scale, 89 * scale), (62 * scale, 92 * scale)], fill=(255, 255, 255, 255))

    draw.ellipse([(71 * scale, 88 * scale), (79 * scale, 97 * scale)], fill=(45, 40, 38, 255))
    draw.ellipse([(73 * scale, 89 * scale), (76 * scale, 92 * scale)], fill=(255, 255, 255, 255))

    # 粉嫩鼻子與三瓣嘴
    draw.polygon([(68 * scale, 100 * scale), (65 * scale, 97 * scale), (71 * scale, 97 * scale)], fill=(244, 158, 148, 255))
    draw.line([(68 * scale, 100 * scale), (68 * scale, 103 * scale)], fill=(65, 55, 50, 255), width=2 * scale)
    draw.arc([(64 * scale, 100 * scale), (68 * scale, 105 * scale)], start=0, end=180, fill=(65, 55, 50, 255), width=2 * scale)
    draw.arc([(68 * scale, 100 * scale), (72 * scale, 105 * scale)], start=0, end=180, fill=(65, 55, 50, 255), width=2 * scale)

    # 萌萌粉腮紅
    draw.ellipse([(52 * scale, 98 * scale), (58 * scale, 104 * scale)], fill=(246, 163, 152, 140))
    draw.ellipse([(78 * scale, 98 * scale), (84 * scale, 104 * scale)], fill=(246, 163, 152, 140))

    # 前爪支撐
    draw.rounded_rectangle([(62 * scale, 118 * scale), (74 * scale, 138 * scale)], radius=5 * scale, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255), width=2 * scale)

    # 大膽側伸後腿的小腳丫 (向左伸出，粉紅肉墊露出！)
    leg_poly = [(48 * scale, 124 * scale), (30 * scale, 132 * scale), (26 * scale, 138 * scale), (45 * scale, 138 * scale)]
    draw.polygon(leg_poly, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255))
    # 伸展腿護膝橘斑！
    draw.ellipse([(36 * scale, 126 * scale), (48 * scale, 136 * scale)], fill=(243, 156, 85, 255))
    # 小腳肉墊
    draw.ellipse([(28 * scale, 133 * scale), (33 * scale, 137 * scale)], fill=(244, 158, 148, 255))

    # === 右貓：黑面翡翠眼白圍巾玳瑁貓 (Regal Tortoiseshell Sentinel) ===
    # 挺拔端坐黑色身軀 (坐標中心 ~ 118, 106)
    tortie_body = [(94 * scale, 85 * scale), (142 * scale, 138 * scale)]
    draw.ellipse(tortie_body, fill=(43, 38, 36, 255)) # 墨黑底毛

    # 玳瑁焦糖金斑塊 (肩膀與腰側)
    draw.ellipse([(118 * scale, 92 * scale), (138 * scale, 118 * scale)], fill=(217, 122, 38, 255))
    draw.ellipse([(96 * scale, 114 * scale), (114 * scale, 136 * scale)], fill=(242, 165, 74, 255))

    # 胸前雪白厚毛圍巾 (White Ascot Bib)
    bib_poly = [(106 * scale, 102 * scale), (102 * scale, 124 * scale), (115 * scale, 135 * scale), (128 * scale, 124 * scale), (124 * scale, 102 * scale)]
    draw.polygon(bib_poly, fill=(255, 255, 255, 255))

    # 右耳 (焦糖金斑)
    ear_r = [(125 * scale, 72 * scale), (135 * scale, 50 * scale), (142 * scale, 75 * scale)]
    draw.polygon(ear_r, fill=(217, 122, 38, 255), outline=(166, 78, 20, 255))
    # 左耳 (深墨黑)
    ear_m = [(100 * scale, 72 * scale), (104 * scale, 50 * scale), (116 * scale, 72 * scale)]
    draw.polygon(ear_m, fill=(43, 38, 36, 255), outline=(28, 24, 23, 255))

    # 玳瑁貓面部 (黑面罩)
    face_tortie = [(98 * scale, 68 * scale), (138 * scale, 108 * scale)]
    draw.ellipse(face_tortie, fill=(43, 38, 36, 255))

    # 額頭金流光 (Golden Blaze!)
    blaze = [(118 * scale, 62 * scale), (122 * scale, 78 * scale), (118 * scale, 86 * scale), (114 * scale, 78 * scale)]
    draw.polygon(blaze, fill=(242, 165, 74, 255))

    # 水潤晶瑩翡翠綠大眼睛 (Emerald Gem Eyes!)
    # 左翡翠眼
    draw.ellipse([(105 * scale, 84 * scale), (115 * scale, 96 * scale)], fill=(70, 180, 130, 255))
    draw.ellipse([(108 * scale, 85 * scale), (112 * scale, 95 * scale)], fill=(20, 20, 20, 255)) # 瞳孔
    draw.ellipse([(107 * scale, 86 * scale), (109 * scale, 89 * scale)], fill=(255, 255, 255, 255)) # 高光

    # 右翡翠眼
    draw.ellipse([(121 * scale, 84 * scale), (131 * scale, 96 * scale)], fill=(70, 180, 130, 255))
    draw.ellipse([(124 * scale, 85 * scale), (128 * scale, 95 * scale)], fill=(20, 20, 20, 255))
    draw.ellipse([(123 * scale, 86 * scale), (125 * scale, 89 * scale)], fill=(255, 255, 255, 255))

    # 口鼻雪白淨區
    draw.ellipse([(112 * scale, 94 * scale), (124 * scale, 104 * scale)], fill=(255, 255, 255, 255))
    # 粉紅小鼻
    draw.polygon([(118 * scale, 97 * scale), (115 * scale, 94 * scale), (121 * scale, 94 * scale)], fill=(244, 158, 148, 255))

    # 標誌性黑美人痣 (Iconic Beauty Mark on right cheek!)
    draw.ellipse([(122 * scale, 97 * scale), (124.5 * scale, 100 * scale)], fill=(28, 24, 23, 255))

    # 雪白前手套 (抓在桌沿)
    draw.rounded_rectangle([(108 * scale, 126 * scale), (118 * scale, 138 * scale)], radius=4 * scale, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255), width=2 * scale)
    draw.rounded_rectangle([(122 * scale, 126 * scale), (132 * scale, 138 * scale)], radius=4 * scale, fill=(255, 255, 255, 255), outline=(225, 215, 202, 255), width=2 * scale)

    # 底部手帳雅緻銘牌："READING JOURNAL"
    # 小小裝飾愛心/星光
    draw.ellipse([(89 * scale, 148 * scale), (93 * scale, 152 * scale)], fill=(217, 93, 80, 255))

    # 4x 超取樣平滑降採樣至 180x180 (高品質 Lanczos 抗鋸齒)
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    out_path = "/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading/assets/apple-touch-icon.png"
    final_img.save(out_path, format="PNG")
    print(f"Saved {out_path} ({size}x{size})")

if __name__ == '__main__':
    create_apple_touch_icon()

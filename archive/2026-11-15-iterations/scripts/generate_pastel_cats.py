#!/usr/bin/env python3
"""
generate_pastel_cats.py
溫柔手帳讀書誌 · 核心物象基因手繪粉彩風貓咪生成器
精準提取使用者照片中雙貓的核心物象基因：
1. 左側【白色橘頭側伸後腿放鬆貓】：
   - 齊瀏海橘色平頭 (Blunt Orange Bangs)
   - 呆萌大圓眼、粉嫩小鼻子、三瓣嘴、萌萌腮紅
   - 圓滾滾白拋拋身軀
   - 靈魂特徵：大膽向側邊外伸展的放鬆後腿 (Outstretched Leg)、膝蓋橘色護膝斑、粉紅肉墊
   - 背脊焦糖橘大鞍斑、蓬鬆橘色虎斑條紋尾巴
2. 右側【黑面金流光翡翠眼白圍巾玳瑁貓】：
   - 天然靈動直立雙耳（絕無帽子！）
   - 墨黑面罩臉龐 (Black Mask)
   - 額頭正中央筆直劃下的焦糖金黃流光 (Caramel Gold Blaze)
   - 水潤晶瑩的翡翠綠大寶石眼睛 (Emerald Green Gaze)
   - 右側鼻翼/嘴角旁標誌性「黑美人痣」 (Iconic Beauty Mark)
   - 下巴延伸至前胸的蓬鬆大片雪白襯衫毛 (White Ascot Bib)
   - 前腿深黑長襪配雪白小手套 (White Paws)
   - 斑斕柔和的焦糖金橘、深黑與栗褐粉彩筆觸交融玳瑁身軀
   - 端端正正坐在桌沿邊緣的沉著自持神態
"""

import os

def build_amber_stretch_svg():
    return '''<svg viewBox="0 0 320 260" width="100%" height="100%" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Soft Pastel Crayon Grain Filter -->
    <filter id="amber-pastel-paper" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" result="grain"/>
      <feDisplacementMap in="SourceGraphic" in2="grain" scale="1.6" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <!-- Soft Rosy Glow for Cheeks & Pads -->
    <radialGradient id="amber-blush" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F6A398" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#F6A398" stop-opacity="0"/>
    </radialGradient>
    <!-- Caramel Orange Pastel Gradient -->
    <linearGradient id="amber-caramel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F39C55"/>
      <stop offset="50%" stop-color="#E77937"/>
      <stop offset="100%" stop-color="#D26325"/>
    </linearGradient>
    <!-- White Fur Pastel Shadow Gradient -->
    <linearGradient id="white-fur-shading" x1="30%" y1="0%" x2="70%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="70%" stop-color="#FAF5EE"/>
      <stop offset="100%" stop-color="#EFE6DA"/>
    </linearGradient>
  </defs>

  <g filter="url(#amber-pastel-paper)">
    <!-- Ground Shadow (Soft Warm Paper Hue) -->
    <ellipse cx="165" cy="225" rx="115" ry="14" fill="#EDE4D8" opacity="0.6"/>

    <!-- Tail (Curled fluffily around the right flank) -->
    <path d="M 230 185 C 265 175, 290 195, 280 220 C 272 232, 245 230, 235 210" 
          stroke="url(#amber-caramel)" stroke-width="22" stroke-linecap="round" fill="none"/>
    <!-- Tail Rings / Fluff texture -->
    <path d="M 255 186 C 265 188, 275 198, 275 210" stroke="#FAF5EE" stroke-width="4.5" stroke-linecap="round" fill="none" opacity="0.8"/>
    <path d="M 275 212 C 270 224, 255 226, 245 218" stroke="#D26325" stroke-width="4.5" stroke-linecap="round" fill="none"/>

    <!-- THE OUTSTRETCHED BACK LEG (照片靈魂：大膽側伸出去的放鬆大雞腿！) -->
    <!-- Leg White Meat Base -->
    <path d="M 140 185 C 115 180, 85 195, 45 208 C 32 212, 25 222, 35 228 C 45 233, 65 230, 95 220 C 125 212, 145 210, 155 200 Z" 
          fill="url(#white-fur-shading)" stroke="#E5D9CC" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    
    <!-- Knee Orange Patch (照片中伸展腿膝蓋處的可愛橘色護膝斑塊！) -->
    <path d="M 68 202 C 82 195, 102 198, 112 212 C 98 218, 80 220, 68 212 Z" 
          fill="url(#amber-caramel)"/>

    <!-- Pink Paw Toe Beans (伸展小腳掌上的粉紅小肉墊！) -->
    <ellipse cx="34" cy="220" rx="4.5" ry="3.5" fill="#F49E94"/>
    <circle cx="28" cy="216" r="2.2" fill="#F49E94"/>
    <circle cx="31" cy="212" r="2.2" fill="#F49E94"/>
    <circle cx="38" cy="213" r="2.2" fill="#F49E94"/>

    <!-- Main Torso: Chubby, Relaxed, Loafing White Body -->
    <path d="M 125 110 C 105 130, 100 170, 115 210 C 130 222, 205 224, 235 205 C 255 175, 250 135, 225 115 C 200 95, 150 95, 125 110 Z" 
          fill="url(#white-fur-shading)" stroke="#E5D9CC" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Back & Saddle Caramel Patch (背部大片溫暖焦糖橘鞍斑) -->
    <path d="M 180 115 C 205 105, 235 115, 242 145 C 248 170, 235 195, 215 198 C 195 185, 185 160, 175 140 C 170 128, 172 120, 180 115 Z" 
          fill="url(#amber-caramel)"/>
    <path d="M 195 125 C 215 120, 228 135, 230 155" stroke="#FCE8D3" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.6"/>

    <!-- Left Seated Paw (曲在腹下露出的小雪白後爪) -->
    <ellipse cx="145" cy="216" rx="14" ry="9" fill="#FFFFFF" stroke="#E5D9CC" stroke-width="2"/>
    <line x1="141" y1="214" x2="141" y2="223" stroke="#D8C8B8" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="147" y1="214" x2="147" y2="223" stroke="#D8C8B8" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Two Front Paws (乖巧端端正正撐在身前的兩隻雪白小柱爪) -->
    <rect x="156" y="155" width="18" height="55" rx="9" fill="#FFFFFF" stroke="#E5D9CC" stroke-width="2"/>
    <line x1="162" y1="198" x2="162" y2="207" stroke="#D8C8B8" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="168" y1="198" x2="168" y2="207" stroke="#D8C8B8" stroke-width="1.8" stroke-linecap="round"/>

    <rect x="178" y="155" width="18" height="55" rx="9" fill="#FFFFFF" stroke="#E5D9CC" stroke-width="2"/>
    <line x1="184" y1="198" x2="184" y2="207" stroke="#D8C8B8" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="190" y1="198" x2="190" y2="207" stroke="#D8C8B8" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Head: Round, Sweet, Chubby Cheeks (圓潤飽滿軟萌大頭) -->
    <ellipse cx="168" cy="95" rx="42" ry="36" fill="url(#white-fur-shading)" stroke="#E5D9CC" stroke-width="2.5"/>

    <!-- Ears -->
    <!-- Left Ear (White & soft pink inside) -->
    <path d="M 132 75 L 126 42 C 138 46, 148 55, 152 70 Z" fill="#FFFFFF" stroke="#E5D9CC" stroke-width="2" stroke-linejoin="round"/>
    <path d="M 134 70 L 130 50 C 137 53, 143 59, 146 68 Z" fill="#F8B6AB" opacity="0.75"/>

    <!-- Right Ear (Orange tipped!) -->
    <path d="M 184 70 C 188 55, 198 46, 210 42 L 204 75 Z" fill="url(#amber-caramel)" stroke="#D26325" stroke-width="2" stroke-linejoin="round"/>
    <path d="M 190 68 C 193 59, 199 53, 206 50 L 202 70 Z" fill="#F8B6AB" opacity="0.6"/>

    <!-- Blunt Cap Bangs (照片靈魂：額頭頂整齊可愛的平瀏海齊頭橘毛！) -->
    <path d="M 130 74 C 145 60, 190 60, 206 74 C 200 85, 185 86, 172 82 C 160 86, 140 85, 130 74 Z" 
          fill="url(#amber-caramel)"/>
    <!-- Cute little hair locks -->
    <path d="M 160 84 C 165 88, 172 88, 175 83" stroke="#D26325" stroke-width="2" stroke-linecap="round" fill="none"/>

    <!-- Rosy Pastel Cheeks (軟乎乎的粉彩腮紅) -->
    <circle cx="140" cy="106" r="10" fill="url(#amber-blush)"/>
    <circle cx="196" cy="106" r="10" fill="url(#amber-blush)"/>

    <!-- Eyes (Big, Round, Innocent, Serene & Trusting) -->
    <!-- Left Eye -->
    <ellipse cx="150" cy="95" rx="6.5" ry="7.5" fill="#2E2825"/>
    <circle cx="148" cy="92.5" r="2.5" fill="#FFFFFF"/>
    <circle cx="153" cy="97" r="1.2" fill="#FFFFFF"/>
    
    <!-- Right Eye -->
    <ellipse cx="186" cy="95" rx="6.5" ry="7.5" fill="#2E2825"/>
    <circle cx="184" cy="92.5" r="2.5" fill="#FFFFFF"/>
    <circle cx="189" cy="97" r="1.2" fill="#FFFFFF"/>

    <!-- Cute Pink Nose & W-Mouth (粉嫩小鼻子與三瓣嘴) -->
    <path d="M 168 102 L 164 98 C 166 97, 170 97, 172 98 Z" fill="#F49E94"/>
    <path d="M 168 102 L 168 106 C 165 109, 159 108, 158 105" stroke="#3D3531" stroke-width="1.8" stroke-linecap="round" fill="none"/>
    <path d="M 168 106 C 171 109, 177 108, 178 105" stroke="#3D3531" stroke-width="1.8" stroke-linecap="round" fill="none"/>

    <!-- Sweet Hand-drawn Whiskers -->
    <path d="M 142 102 C 126 100, 115 102, 105 106" stroke="#4A403A" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.6"/>
    <path d="M 140 106 C 125 107, 115 111, 108 116" stroke="#4A403A" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.6"/>
    <path d="M 194 102 C 210 100, 221 102, 231 106" stroke="#4A403A" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.6"/>
    <path d="M 196 106 C 211 107, 221 111, 228 116" stroke="#4A403A" stroke-width="1.2" stroke-linecap="round" fill="none" opacity="0.6"/>

    <!-- Companion Gentle Label (手帳小貼心手寫標籤) -->
    <g transform="translate(100, 240)">
      <rect x="0" y="0" width="120" height="18" rx="9" fill="#FFF8F0" stroke="#E4D2C0" stroke-width="1"/>
      <circle cx="10" cy="9" r="4" fill="#F39C55"/>
      <text x="20" y="12.5" font-family="'Zen Maru Gothic', 'PingFang TC', sans-serif" font-size="9" font-weight="700" fill="#6B5C50">身心放鬆 · 舒展後腿</text>
    </g>
  </g>
</svg>'''

def build_tortoiseshell_svg():
    return '''<svg viewBox="0 0 320 280" width="100%" height="100%" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Soft Pastel Crayon Grain Filter -->
    <filter id="tortie-pastel-paper" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" result="grain"/>
      <feDisplacementMap in="SourceGraphic" in2="grain" scale="1.6" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <!-- Emerald Gem Eye Radial Gradient -->
    <radialGradient id="emerald-eye-left" cx="45%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#80E0B0"/>
      <stop offset="45%" stop-color="#46B482"/>
      <stop offset="85%" stop-color="#287854"/>
      <stop offset="100%" stop-color="#194D36"/>
    </radialGradient>
    <radialGradient id="emerald-eye-right" cx="45%" cy="40%" r="55%">
      <stop offset="0%" stop-color="#80E0B0"/>
      <stop offset="45%" cy="45%" stop-color="#46B482"/>
      <stop offset="85%" stop-color="#287854"/>
      <stop offset="100%" stop-color="#194D36"/>
    </radialGradient>
    <!-- Tortoiseshell Mottled Caramel Gradient -->
    <linearGradient id="tortie-caramel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F2A54A"/>
      <stop offset="60%" stop-color="#D97A26"/>
      <stop offset="100%" stop-color="#A64E14"/>
    </linearGradient>
    <!-- Tortoiseshell Charcoal Black -->
    <linearGradient id="tortie-charcoal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#453E3B"/>
      <stop offset="60%" stop-color="#2B2624"/>
      <stop offset="100%" stop-color="#1C1817"/>
    </linearGradient>
  </defs>

  <g filter="url(#tortie-pastel-paper)">
    <!-- Wooden Table Ledge (照片中端端正正端坐的溫暖木桌沿) -->
    <rect x="25" y="238" width="270" height="12" rx="4" fill="#D7BEA8" stroke="#BFA38C" stroke-width="1.5"/>
    <line x1="25" y1="242" x2="295" y2="242" stroke="#FAF0E6" stroke-width="1.5" opacity="0.6"/>

    <!-- Fluffy Dark Tail resting over table ledge -->
    <path d="M 225 195 C 248 190, 268 210, 255 240 C 248 252, 230 256, 218 248 C 210 240, 218 225, 222 210" 
          stroke="url(#tortie-charcoal)" stroke-width="20" stroke-linecap="round" fill="none"/>
    <path d="M 235 220 C 245 228, 248 238, 238 246" stroke="url(#tortie-caramel)" stroke-width="5" stroke-linecap="round" fill="none"/>

    <!-- Upright Sentinel Body Base (端坐挺拔的沉穩身軀) -->
    <path d="M 115 115 C 95 145, 90 190, 105 238 L 215 238 C 230 190, 225 145, 205 115 Z" 
          fill="url(#tortie-charcoal)"/>

    <!-- Tortoiseshell Mottled Amber & Russet Patches on Torso (身體斑斕焦糖金與栗褐粉彩筆觸) -->
    <path d="M 102 145 C 115 135, 135 140, 128 165 C 118 190, 96 185, 102 145 Z" fill="url(#tortie-caramel)"/>
    <path d="M 195 138 C 212 128, 226 142, 218 172 C 206 186, 188 170, 195 138 Z" fill="url(#tortie-caramel)"/>
    <path d="M 185 185 C 200 178, 216 188, 212 215 C 198 226, 182 212, 185 185 Z" fill="url(#tortie-caramel)"/>
    <path d="M 106 198 C 118 188, 132 196, 126 222 C 112 230, 100 218, 106 198 Z" fill="url(#tortie-caramel)"/>

    <!-- THE PURE WHITE ASCOT BIB (照片靈魂：下巴延伸至前胸大片蓬鬆雲朵雪白厚圍巾！) -->
    <path d="M 132 108 C 120 130, 122 175, 142 195 C 152 205, 168 205, 178 195 C 198 175, 200 130, 188 108 C 178 116, 142 116, 132 108 Z" 
          fill="#FFFFFF" stroke="#E6DDD2" stroke-width="2"/>
    <!-- Fluffy Chest Fur Tufts -->
    <path d="M 148 135 C 145 150, 155 165, 160 172 C 165 165, 175 150, 172 135" stroke="#EADFD4" stroke-width="2" stroke-linecap="round" fill="none"/>
    <path d="M 140 152 C 148 168, 158 185, 160 192 C 162 185, 172 168, 180 152" stroke="#EADFD4" stroke-width="2" stroke-linecap="round" fill="none"/>

    <!-- TWO UPRIGHT FRONT LEGS: Black Socks with PURE WHITE MITTENS (黑長靴配雪白小手套) -->
    <!-- Left Foreleg -->
    <path d="M 134 175 L 134 225 C 134 235, 148 235, 148 225 L 148 175 Z" fill="url(#tortie-charcoal)"/>
    <!-- Left White Glove / Mitten (雪白小手套抓在桌沿) -->
    <rect x="128" y="218" width="18" height="24" rx="9" fill="#FFFFFF" stroke="#E0D5C7" stroke-width="2"/>
    <line x1="134" y1="234" x2="134" y2="242" stroke="#D0C2B2" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="140" y1="234" x2="140" y2="242" stroke="#D0C2B2" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Right Foreleg -->
    <path d="M 172 175 L 172 225 C 172 235, 186 235, 186 225 L 186 175 Z" fill="url(#tortie-charcoal)"/>
    <!-- Right White Glove / Mitten with touch of caramel toe -->
    <rect x="174" y="218" width="18" height="24" rx="9" fill="#FFFFFF" stroke="#E0D5C7" stroke-width="2"/>
    <path d="M 183 228 C 188 226, 192 232, 190 238 L 183 238 Z" fill="url(#tortie-caramel)"/>
    <line x1="180" y1="234" x2="180" y2="242" stroke="#D0C2B2" stroke-width="1.8" stroke-linecap="round"/>
    <line x1="186" y1="234" x2="186" y2="242" stroke="#D0C2B2" stroke-width="1.8" stroke-linecap="round"/>

    <!-- Head: Noble, Alert, Beautiful Rounded Tortie Face -->
    <ellipse cx="160" cy="85" rx="38" ry="34" fill="url(#tortie-charcoal)"/>

    <!-- NATURAL ALERT EARS (天然清秀雙耳，絕無帽子！) -->
    <!-- Left Ear (Dark Charcoal with Caramel Tip) -->
    <path d="M 126 68 L 118 30 C 132 34, 144 45, 148 62 Z" fill="url(#tortie-charcoal)" stroke="#1C1817" stroke-width="2" stroke-linejoin="round"/>
    <path d="M 124 55 L 120 38 C 128 40, 134 46, 137 54 Z" fill="url(#tortie-caramel)"/>
    <path d="M 128 62 L 124 45 C 130 47, 134 52, 136 60 Z" fill="#F8B6AB" opacity="0.5"/>

    <!-- Right Ear (Caramel Amber Splattered) -->
    <path d="M 172 62 C 176 45, 188 34, 202 30 L 194 68 Z" fill="url(#tortie-caramel)" stroke="#A64E14" stroke-width="2" stroke-linejoin="round"/>
    <path d="M 178 60 C 182 48, 188 42, 194 38 L 190 62 Z" fill="#F8B6AB" opacity="0.6"/>

    <!-- GOLDEN BLAZE DOWN FOREHEAD (照片靈魂：額頭正中央筆直劃下的焦糖金流光！) -->
    <path d="M 160 48 L 165 72 L 160 84 L 155 72 Z" fill="url(#tortie-caramel)"/>
    <!-- Muzzle / Chin White Patch (口鼻雪白淨區) -->
    <path d="M 152 82 C 145 80, 140 85, 142 96 C 144 104, 154 106, 160 106 C 166 106, 176 104, 178 96 C 180 85, 175 80, 168 82 C 165 84, 155 84, 152 82 Z" 
          fill="#FFFFFF" stroke="#E6DDD2" stroke-width="1.5"/>

    <!-- THE EMERALD GREEN EYES (照片靈魂：明亮深邃、晶瑩剔透的碧綠翡翠大眼睛！) -->
    <!-- Left Emerald Eye -->
    <ellipse cx="144" cy="80" rx="7.5" ry="8.5" fill="url(#emerald-eye-left)"/>
    <ellipse cx="144" cy="80" rx="3.2" ry="7.2" fill="#151210"/> <!-- Slit/Oval Pupil -->
    <circle cx="142" cy="77" r="2.6" fill="#FFFFFF"/> <!-- Main Highlight -->
    <circle cx="146" cy="83" r="1.2" fill="#FFFFFF" opacity="0.8"/> <!-- Sub Highlight -->
    <circle cx="141" cy="81" r="1.0" fill="#A8F5D0" opacity="0.9"/> <!-- Rim Light -->

    <!-- Right Emerald Eye -->
    <ellipse cx="176" cy="80" rx="7.5" ry="8.5" fill="url(#emerald-eye-right)"/>
    <ellipse cx="176" cy="80" rx="3.2" ry="7.2" fill="#151210"/>
    <circle cx="174" cy="77" r="2.6" fill="#FFFFFF"/>
    <circle cx="178" cy="83" r="1.2" fill="#FFFFFF" opacity="0.8"/>
    <circle cx="173" cy="81" r="1.0" fill="#A8F5D0" opacity="0.9"/>

    <!-- Cute Pink Nose -->
    <polygon points="160,91 156,87 164,87" fill="#F49E94"/>

    <!-- ICONIC BLACK BEAUTY MARK (照片靈魂：右側鼻翼/嘴角旁標誌性「黑美人痣」！) -->
    <circle cx="167" cy="94" r="3.2" fill="#1C1817"/>

    <!-- Delicate Curved Mouth -->
    <path d="M 160 91 L 160 96 C 157 98, 153 98, 151 96" stroke="#2B2624" stroke-width="1.8" stroke-linecap="round" fill="none"/>
    <path d="M 160 96 C 163 98, 167 98, 169 96" stroke="#2B2624" stroke-width="1.8" stroke-linecap="round" fill="none"/>

    <!-- Radiant White Whiskers (向兩側優雅舒展的長長雪白鬍鬚) -->
    <path d="M 142 92 C 124 90, 110 92, 95 96" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" fill="none"/>
    <path d="M 140 96 C 122 97, 108 102, 98 108" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" fill="none"/>
    <path d="M 141 100 C 125 104, 112 110, 104 118" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" fill="none"/>

    <path d="M 178 92 C 196 90, 210 92, 225 96" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" fill="none"/>
    <path d="M 180 96 C 198 97, 212 102, 222 108" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" fill="none"/>
    <path d="M 179 100 C 195 104, 208 110, 216 118" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" fill="none"/>

    <!-- Companion Gentle Label (手帳小貼心手寫標籤) -->
    <g transform="translate(100, 258)">
      <rect x="0" y="0" width="120" height="18" rx="9" fill="#FFF8F0" stroke="#E4D2C0" stroke-width="1"/>
      <circle cx="10" cy="9" r="4" fill="#3E8E6A"/>
      <text x="20" y="12.5" font-family="'Zen Maru Gothic', 'PingFang TC', sans-serif" font-size="9" font-weight="700" fill="#4A3F35">堅定邊界 · 翡翠端坐</text>
    </g>
  </g>
</svg>'''

if __name__ == '__main__':
    amber_svg = build_amber_stretch_svg()
    tortie_svg = build_tortoiseshell_svg()
    
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'img', 'svg')
    os.makedirs(out_dir, exist_ok=True)
    
    with open(os.path.join(out_dir, 'ambient-cat-amber-stretch.svg'), 'w', encoding='utf-8') as f:
        f.write(amber_svg)
    print("Saved img/svg/ambient-cat-amber-stretch.svg")
    
    with open(os.path.join(out_dir, 'ambient-cat-tortoiseshell.svg'), 'w', encoding='utf-8') as f:
        f.write(tortie_svg)
    print("Saved img/svg/ambient-cat-tortoiseshell.svg")

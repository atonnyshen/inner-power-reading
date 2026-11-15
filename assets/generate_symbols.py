#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Swiss Deconstructed Risograph Vector Symbol Library Generator
Generates:
1. Individual standalone SVG files in img/svg/
2. Master SVG symbol sprite in assets/riso-symbols.svg
3. Master CSS system in assets/riso-symbols.css
4. Visual test dictionary catalog in assets/svg-dictionary.html
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
IMG_SVG_DIR = os.path.join(PROJECT_DIR, "img", "svg")
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")

os.makedirs(IMG_SVG_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# ══════════════════════════════════════════════════════════════════════
# SVG SYMBOL DEFINITIONS (Precision Swiss Geometry & Risograph Offset)
# ══════════════════════════════════════════════════════════════════════

# 1. Specimen 01: Amber Cat Loaf & Leg Stretch (橘白放鬆伸腿姿態)
# Dimensions: 280 x 200
AMBER_CAT_SPECIMEN_CONTENT = '''<g id="amber-cat-specimen-root">
  <!-- Swiss Precision Construction Grid (Background Layer) -->
  <rect x="0" y="0" width="280" height="200" fill="var(--riso-paper, #FAF8F5)" rx="6"/>
  <rect x="12" y="12" width="256" height="176" fill="none" stroke="var(--riso-grid-line, rgba(45,41,38,0.12))" stroke-width="0.8" stroke-dasharray="3 3"/>
  <rect x="20" y="20" width="240" height="160" fill="none" stroke="var(--riso-grid-line, rgba(45,41,38,0.08))" stroke-width="0.6"/>

  <!-- Technical Registration Crosshairs & Datum Lines -->
  <!-- Top Left Registration Mark -->
  <g transform="translate(24, 24)" stroke="var(--riso-rose, #C06C52)" stroke-width="0.8">
    <circle cx="0" cy="0" r="4.5" fill="none"/>
    <line x1="-7" y1="0" x2="7" y2="0"/>
    <line x1="0" y1="-7" x2="0" y2="7"/>
    <text x="9" y="3.5" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6.5" fill="var(--text-dim, #888077)" letter-spacing="0.08em" stroke="none">REG.MK 01-A // CH-01</text>
  </g>

  <!-- Top Right Micro Coordinates -->
  <g transform="translate(256, 26)" text-anchor="end">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="7" font-weight="700" fill="var(--riso-rose, #C06C52)" letter-spacing="0.1em">SPECIMEN 01 // E-01</text>
    <text x="0" y="9" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--text-dim, #888077)" letter-spacing="0.06em">AXIS 0.0 · φ=1.618 · DE-FREEZING</text>
  </g>

  <!-- Bottom Left Baseline Annotation -->
  <g transform="translate(24, 182)">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--riso-sage, #3E6B56)" font-weight="600" letter-spacing="0.06em">PARASYMPATHETIC ACTIVATION · VAGUS NERVE TONE</text>
  </g>

  <!-- Bottom Right Scale & Grid Spec -->
  <g transform="translate(256, 182)" text-anchor="end">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--text-dim, #888077)" letter-spacing="0.05em">280×200MM // 24×24 SWISS DOT</text>
  </g>

  <!-- Ground Plane Datum Axis -->
  <line x1="28" y1="148" x2="252" y2="148" stroke="var(--text-dim, #888077)" stroke-width="0.8" stroke-dasharray="2 3"/>
  <circle cx="28" cy="148" r="1.5" fill="var(--text-dim, #888077)"/>
  <circle cx="252" cy="148" r="1.5" fill="var(--text-dim, #888077)"/>

  <!-- Construction Geometric Arcs & Tangents (Deconstructed Swiss Anatomy) -->
  <!-- Concentric Torso Mass Guides -->
  <circle cx="118" cy="122" r="38" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.7" stroke-dasharray="2 3" opacity="0.45"/>
  <circle cx="118" cy="122" r="54" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <!-- Head Circle Guide -->
  <circle cx="86" cy="102" r="22" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="0.7" stroke-dasharray="2 2" opacity="0.4"/>
  <!-- Tangent Angle Vector for Hindlimb Extension -->
  <line x1="140" y1="126" x2="228" y2="144" stroke="var(--riso-rose, #C06C52)" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.6"/>
  <text x="232" y="142" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--riso-rose, #C06C52)">∡ 12.8°</text>

  <!-- RISOGRAPH LAYER 1 (Cool Sage Misregistration Shadow Layer - Offset dx=1.8, dy=-1.2) -->
  <g transform="translate(1.8, -1.2)" opacity="0.32" style="mix-blend-mode: multiply;">
    <!-- Cat Torso Silhouette Shift -->
    <path d="M 68 128 C 66 98, 92 84, 126 90 C 152 94, 168 106, 172 124 C 174 136, 154 146, 124 147 C 94 147, 72 143, 68 128 Z" fill="var(--riso-sage, #3E6B56)"/>
    <!-- Hind Leg Stretch Silhouette Shift -->
    <path d="M 148 124 C 168 126, 196 135, 222 140 C 228 141, 230 145, 224 147 C 206 149, 176 148, 154 138 Z" fill="var(--riso-sage, #3E6B56)"/>
    <!-- Head Shift -->
    <circle cx="86" cy="102" r="20" fill="var(--riso-sage, #3E6B56)"/>
    <!-- Tail Arc Shift -->
    <path d="M 68 132 C 48 134, 38 144, 44 156 C 50 164, 64 162, 72 154" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="4.5" stroke-linecap="round"/>
  </g>

  <!-- RISOGRAPH LAYER 2 (Warm Terracotta / Amber Primary Layer) -->
  <g>
    <!-- Cat Underbelly & Chest (Paper White Base Geometry) -->
    <path d="M 70 128 C 68 100, 92 86, 126 92 C 150 96, 166 108, 170 124 C 172 136, 152 146, 122 146 C 94 146, 72 142, 70 128 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>

    <!-- Amber Back & Dorsal Riso Inking Patch (The Classic Orange Cat Patch) -->
    <path d="M 88 94 C 108 90, 134 94, 154 104 C 166 112, 170 120, 168 128 C 162 134, 148 130, 138 124 C 120 114, 102 110, 88 114 Z" fill="var(--riso-rose, #C06C52)" opacity="0.88"/>

    <!-- Relaxed Extended Hind Leg (舒展後腿：放鬆、生理凍結瓦解之核心識別) -->
    <path d="M 148 124 C 168 126, 196 135, 222 140 C 228 141, 230 145, 224 147 C 206 149, 176 148, 154 138 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
    <!-- Amber Patch on Stretched Leg Thigh -->
    <path d="M 154 126 C 172 128, 190 134, 202 138 C 196 143, 178 143, 164 137 Z" fill="var(--riso-rose, #C06C52)" opacity="0.88"/>
    <!-- Leg Toe Pads (Delicate Geometric Circles) -->
    <circle cx="225" cy="142" r="1.8" fill="var(--riso-rose, #C06C52)"/>
    <circle cx="228" cy="144" r="1.8" fill="var(--riso-rose, #C06C52)"/>
    <circle cx="225" cy="146.5" r="1.8" fill="var(--riso-rose, #C06C52)"/>

    <!-- Head & Ears (Serene, Dropped Shoulders) -->
    <circle cx="86" cy="102" r="20" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4"/>
    <!-- Amber Forehead & Ear Mask Patch -->
    <path d="M 74 96 C 76 86, 84 84, 94 86 C 98 90, 96 98, 92 102 C 84 102, 76 100, 74 96 Z" fill="var(--riso-rose, #C06C52)" opacity="0.88"/>
    <!-- Left Triangular Ear -->
    <polygon points="72,90 78,70 88,86" fill="var(--riso-rose, #C06C52)" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linejoin="round"/>
    <polygon points="74,88 78,74 85,86" fill="#FFFFFF" opacity="0.4"/>
    <!-- Right Triangular Ear -->
    <polygon points="90,84 100,72 106,88" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linejoin="round"/>
    <polygon points="93,84 99,75 103,87" fill="var(--riso-rose, #C06C52)" opacity="0.75"/>

    <!-- Serene Closed Sleeping/Relaxed Eye Arc (放鬆閉眼、安定沉著) -->
    <path d="M 80 104 Q 85 108 90 104" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="1.6" stroke-linecap="round"/>
    <!-- Nose & Whisker Node -->
    <polygon points="86,108 84.5,106.5 87.5,106.5" fill="var(--riso-rose, #C06C52)"/>
    <line x1="88" y1="107" x2="98" y2="105" stroke="var(--text-main, #2D2926)" stroke-width="0.8" stroke-linecap="round"/>
    <line x1="88" y1="109" x2="97" y2="110" stroke="var(--text-main, #2D2926)" stroke-width="0.8" stroke-linecap="round"/>

    <!-- Lazy Curled Tail -->
    <path d="M 70 132 C 48 134, 38 144, 44 156 C 50 164, 64 162, 72 154" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="4.5" stroke-linecap="round"/>
    <path d="M 44 156 C 48 162, 58 161, 66 156" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="4.5" stroke-linecap="round"/>

    <!-- Front Paws (Folded Neatly Under Chest) -->
    <ellipse cx="94" cy="144" rx="8" ry="4.5" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
    <line x1="94" y1="142" x2="94" y2="146.5" stroke="var(--text-main, #2D2926)" stroke-width="0.9"/>
  </g>

  <!-- Micro Typographic Overlay & Coordinates -->
  <g transform="translate(148, 114)">
    <rect x="0" y="0" width="46" height="13" fill="var(--riso-paper, #FAF8F5)" stroke="var(--riso-rose, #C06C52)" stroke-width="0.7"/>
    <text x="4" y="9" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" font-weight="700" fill="var(--riso-rose, #C06C52)" letter-spacing="0.06em">CALM // 0.0</text>
  </g>
</g>'''

# 2. Specimen 02: Tortoiseshell Cat Upright Sentinel (玳瑁貓挺拔端坐姿態 · 無帽子天然警醒)
# Dimensions: 280 x 200
CALICO_CAT_SPECIMEN_CONTENT = '''<g id="calico-cat-specimen-root">
  <!-- Swiss Precision Construction Grid (Background Layer) -->
  <rect x="0" y="0" width="280" height="200" fill="var(--riso-paper, #FAF8F5)" rx="6"/>
  <rect x="12" y="12" width="256" height="176" fill="none" stroke="var(--riso-grid-line, rgba(45,41,38,0.12))" stroke-width="0.8" stroke-dasharray="3 3"/>
  <rect x="20" y="20" width="240" height="160" fill="none" stroke="var(--riso-grid-line, rgba(45,41,38,0.08))" stroke-width="0.6"/>

  <!-- Technical Registration Crosshairs & Datum Lines -->
  <!-- Top Left Registration Mark -->
  <g transform="translate(24, 24)" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.8">
    <circle cx="0" cy="0" r="4.5" fill="none"/>
    <line x1="-7" y1="0" x2="7" y2="0"/>
    <line x1="0" y1="-7" x2="0" y2="7"/>
    <text x="9" y="3.5" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6.5" fill="var(--text-dim, #888077)" letter-spacing="0.08em" stroke="none">REG.MK 02-B // CH-02</text>
  </g>

  <!-- Top Right Micro Coordinates -->
  <g transform="translate(256, 26)" text-anchor="end">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="7" font-weight="700" fill="var(--riso-sage, #3E6B56)" letter-spacing="0.1em">SPECIMEN 02 // TORTIE</text>
    <text x="0" y="9" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--text-dim, #888077)" letter-spacing="0.06em">AXIS 90.0° · ISOSCELES · SOLID BOUNDARIES</text>
  </g>

  <!-- Bottom Left Baseline Annotation -->
  <g transform="translate(24, 182)">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--riso-rose, #C06C52)" font-weight="600" letter-spacing="0.06em">ASSERTIVE POSTURE · ZERO REFLEXIVE APOLOGY</text>
  </g>

  <!-- Bottom Right Scale & Grid Spec -->
  <g transform="translate(256, 182)" text-anchor="end">
    <text x="0" y="0" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--text-dim, #888077)" letter-spacing="0.05em">280×200MM // 24×24 SWISS DOT</text>
  </g>

  <!-- Vertical Central Datum Axis (AXIS 90.0°) -->
  <line x1="140" y1="16" x2="140" y2="184" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.8" stroke-dasharray="3 3"/>
  <circle cx="140" cy="16" r="1.5" fill="var(--riso-sage, #3E6B56)"/>
  <circle cx="140" cy="184" r="1.5" fill="var(--riso-sage, #3E6B56)"/>

  <!-- Master Isosceles Triangle Construction Line (堅定邊界構造骨架) -->
  <polygon points="140,28 88,168 192,168" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="0.7" stroke-dasharray="2 3" opacity="0.45"/>
  <text x="143" y="34" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="6" fill="var(--riso-rose, #C06C52)">APEX 72°</text>

  <!-- Concentric Boundary Radial Waves (警醒雷達場) -->
  <circle cx="140" cy="68" r="30" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.4"/>
  <circle cx="140" cy="68" r="48" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.5" stroke-dasharray="4 4" opacity="0.3"/>
  <circle cx="140" cy="68" r="66" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.4" stroke-dasharray="5 5" opacity="0.2"/>

  <!-- Horizontal Ground Plane -->
  <line x1="36" y1="168" x2="244" y2="168" stroke="var(--text-dim, #888077)" stroke-width="0.8" stroke-dasharray="2 3"/>

  <!-- RISOGRAPH LAYER 1 (Terracotta Misregistration Shift Layer - dx=-1.5, dy=1.2) -->
  <g transform="translate(-1.5, 1.2)" opacity="0.35" style="mix-blend-mode: multiply;">
    <path d="M 124 74 L 112 110 L 98 168 H 182 L 168 110 L 156 74 Z" fill="var(--riso-amber, #D48834)"/>
    <circle cx="140" cy="68" r="19" fill="var(--riso-rose, #C06C52)"/>
  </g>

  <!-- RISOGRAPH LAYER 2 (Primary Tortoiseshell Charcoal & Mottled Amber Architecture) -->
  <g>
    <!-- Base Body Silhouette (深墨底色主體) -->
    <path d="M 126 76 C 122 96, 110 125, 100 168 H 180 C 170 125, 158 96, 154 76 Z" fill="#2A2624" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>

    <!-- Overlaid Tortoiseshell Mottled Fur Patches (玳瑁斑斕毛色) -->
    <path d="M 100 168 L 108 132 C 114 136, 122 144, 126 168 Z" fill="var(--riso-amber, #D48834)" opacity="0.9"/>
    <path d="M 154 76 C 158 96, 168 120, 180 168 L 166 168 C 158 140, 146 112, 142 94 Z" fill="var(--riso-rose, #D95D50)" opacity="0.88"/>
    <path d="M 134 110 C 142 106, 150 118, 146 132 C 138 140, 128 130, 134 110 Z" fill="var(--riso-amber, #D48834)"/>

    <!-- Two Parallel Pillar Front Legs (挺拔如柱：雙前腿筆直並攏，基底穩如泰山) -->
    <rect x="127" y="108" width="10" height="60" rx="4" fill="#2A2624" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
    <rect x="143" y="108" width="10" height="60" rx="4" fill="#2A2624" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
    <line x1="132" y1="160" x2="132" y2="167" stroke="#FFFFFF" stroke-width="0.8"/>
    <line x1="148" y1="160" x2="148" y2="167" stroke="#FFFFFF" stroke-width="0.8"/>

    <!-- Neatly Wrapped Tail Around Paws (收束防禦邊界，泰然自若) -->
    <path d="M 180 166 C 196 166, 198 152, 186 144 C 174 138, 170 148, 160 156 C 148 165, 120 167, 102 167" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="4" stroke-linecap="round"/>
    <path d="M 186 144 C 192 148, 194 158, 182 165" fill="none" stroke="var(--riso-amber, #D48834)" stroke-width="4" stroke-linecap="round"/>

    <!-- Head Contour (純粹貓頭，天然圓弧無帽子) -->
    <circle cx="140" cy="68" r="19" fill="#2A2624" stroke="var(--text-main, #2D2926)" stroke-width="1.4"/>
    
    <!-- Head Mottled Patch: Right Temple (Amber Blaze) -->
    <path d="M 140 50 C 148 50, 158 56, 158 68 C 158 74, 152 78, 144 76 Z" fill="var(--riso-amber, #D48834)"/>
    <!-- Head Mottled Patch: Left Brow (Terracotta Rose) -->
    <path d="M 122 64 C 122 54, 130 50, 140 50 L 138 62 C 132 64, 126 66, 122 64 Z" fill="var(--riso-rose, #D95D50)"/>

    <!-- Upright Pointed Triangular Ears (雙耳天然直立警醒 · 無帽子) -->
    <polygon points="121,62 115,36 133,48" fill="#2A2624" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linejoin="round"/>
    <polygon points="122,58 118,41 130,49" fill="var(--riso-rose, #D95D50)" opacity="0.85"/>
    <polygon points="147,48 165,36 159,62" fill="#2A2624" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linejoin="round"/>
    <polygon points="150,49 162,41 158,58" fill="var(--riso-amber, #D48834)"/>

    <!-- Alert Eyes (平視堅定眼神，不畏縮不道歉) -->
    <path d="M 126 68 Q 131 63 136 68 Q 131 73 126 68 Z" fill="#FAF6F0" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
    <circle cx="131" cy="68" r="2.2" fill="var(--text-main, #2D2926)"/>
    <circle cx="132" cy="67" r="0.7" fill="#FFFFFF"/>
    
    <path d="M 144 68 Q 149 63 154 68 Q 149 73 144 68 Z" fill="#FAF6F0" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
    <circle cx="149" cy="68" r="2.2" fill="var(--text-main, #2D2926)"/>
    <circle cx="150" cy="67" r="0.7" fill="#FFFFFF"/>

    <!-- Geometric Muzzle & Whiskers -->
    <polygon points="140,73 138,71 142,71" fill="var(--riso-rose, #D95D50)"/>
    <!-- Left Whiskers -->
    <line x1="135" y1="73" x2="116" y2="70" stroke="#FAF6F0" stroke-width="0.8" stroke-linecap="round"/>
    <line x1="135" y1="75" x2="118" y2="76" stroke="#FAF6F0" stroke-width="0.8" stroke-linecap="round"/>
    <!-- Right Whiskers -->
    <line x1="145" y1="73" x2="164" y2="70" stroke="#FAF6F0" stroke-width="0.8" stroke-linecap="round"/>
    <line x1="145" y1="75" x2="162" y2="76" stroke="#FAF6F0" stroke-width="0.8" stroke-linecap="round"/>
  </g>

  <!-- Technical Stamp Badge -->
  <g transform="translate(86, 126)">
    <rect x="0" y="0" width="34" height="12" fill="var(--riso-paper, #FAF8F5)" stroke="var(--text-main, #2D2926)" stroke-width="0.7"/>
    <text x="3" y="8.5" font-family="'JetBrains Mono', ui-monospace, monospace" font-size="5.5" font-weight="700" fill="var(--text-main, #2D2926)" letter-spacing="0.06em">BOUNDS</text>
  </g>
</g>'''

# 3. Micro Brand Icon: brand-cat (雙色解構貓咪微型標識)
# Dimensions: 32 x 32
BRAND_CAT_CONTENT = '''<g id="brand-cat-root">
  <!-- Deconstructed Dual-Feline Geometric Brand Crest (Perfect Visual Center at 16, 16) -->
  <!-- Left Triangular Ear Patch (Amber / Terracotta - Loaf Cat) -->
  <polygon points="7,13 10.5,5.5 14,14" fill="var(--riso-rose, #C06C52)" stroke="var(--text-main, #2D2926)" stroke-width="1.1" stroke-linejoin="round"/>
  
  <!-- Right Triangular Ear Patch (Sage / Calico Sentinel) -->
  <polygon points="18,14 21.5,5.5 25,13" fill="var(--riso-sage, #3E6B56)" stroke="var(--text-main, #2D2926)" stroke-width="1.1" stroke-linejoin="round"/>
  
  <!-- Feline Facial Arch Contour (Dropped Shoulders & Calm Posture) -->
  <path d="M 5.5 23 L 7.5 13 L 13.5 17.5 C 15 16.8 17 16.8 18.5 17.5 L 24.5 13 L 26.5 23" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
  
  <!-- Serene Eyes (Dual Balance) -->
  <circle cx="12.5" cy="17.2" r="1.3" fill="var(--text-main, #2D2926)"/>
  <circle cx="19.5" cy="17.2" r="1.3" fill="var(--text-main, #2D2926)"/>
  
  <!-- Minimal Nose Wedge -->
  <polygon points="16,20 14.8,18.5 17.2,18.5" fill="var(--riso-rose, #C06C52)"/>
  
  <!-- Geometric Datum Base (Center Balanced) -->
  <line x1="4.5" y1="25.5" x2="27.5" y2="25.5" stroke="var(--text-dim, #888077)" stroke-width="0.9" stroke-dasharray="1.8 1.8"/>
  <circle cx="16" cy="25.5" r="1.3" fill="var(--riso-rose, #C06C52)"/>
</g>'''

# 4. Icon: 細框眼鏡 (Wire-frame Spectacles)
# Dimensions: 32 x 32
ICON_GLASSES_CONTENT = '''<g id="icon-glasses-root">
  <!-- Construction Optical Crosshairs -->
  <line x1="10" y1="10" x2="10" y2="22" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.6" stroke-dasharray="1.5 1.5" opacity="0.5"/>
  <line x1="22" y1="10" x2="22" y2="22" stroke="var(--riso-rose, #C06C52)" stroke-width="0.6" stroke-dasharray="1.5 1.5" opacity="0.5"/>
  <!-- Left Lens (With Sage Tint) -->
  <circle cx="10" cy="16" r="6.5" fill="var(--riso-sage, #3E6B56)" fill-opacity="0.14" stroke="var(--text-main, #2D2926)" stroke-width="1.4"/>
  <!-- Right Lens (With Rose Tint) -->
  <circle cx="22" cy="16" r="6.5" fill="var(--riso-rose, #C06C52)" fill-opacity="0.14" stroke="var(--text-main, #2D2926)" stroke-width="1.4"/>
  <!-- Saddle Bridge Curve -->
  <path d="M 16.5 16 C 16 13.5, 16 13.5, 15.5 16" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linecap="round"/>
  <path d="M 14.2 15 C 15 13.5 17 13.5 17.8 15" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Left & Right Temples and Hinges -->
  <line x1="3.5" y1="16" x2="1" y2="13.5" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="28.5" y1="16" x2="31" y2="13.5" stroke="var(--text-main, #2D2926)" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Micro Rivet Dots -->
  <circle cx="3.8" cy="16" r="0.9" fill="var(--riso-rose, #C06C52)"/>
  <circle cx="28.2" cy="16" r="0.9" fill="var(--riso-sage, #3E6B56)"/>
</g>'''

# 5. Icon: 熱咖啡杯 (Steaming Coffee Cup)
# Dimensions: 32 x 32
ICON_COFFEE_CONTENT = '''<g id="icon-coffee-root">
  <!-- Rising Steam Harmonic Curves (Risograph Warm Rose) -->
  <path d="M 10 9 C 9 6.5, 11.5 5, 10.5 2.5" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="1.4" stroke-linecap="round"/>
  <path d="M 15 8 C 14 5, 16.5 4, 15.5 1.5" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="1.4" stroke-linecap="round"/>
  <path d="M 20 9 C 19 6.5, 21.5 5, 20.5 2.5" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Cup Body Silhouette (Swiss Ceramic Cylindrical) -->
  <path d="M 6 12 H 24 L 22.5 25 C 22 28, 19 29, 15 29 C 11 29, 8 28, 7.5 25 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Riso Offset Shadow (Terracotta Bottom Wedge) -->
  <path d="M 8.5 23 C 11 27, 19 27, 21.5 23 L 22 25 C 21 28, 18 29, 15 29 C 11 29, 9 28, 8 25 Z" fill="var(--riso-rose, #C06C52)" opacity="0.85"/>
  <!-- Internal Liquid Surface Level Line -->
  <line x1="8" y1="16" x2="22" y2="16" stroke="var(--riso-amber, #9E6234)" stroke-width="1" stroke-dasharray="2 2"/>
  <!-- Handle (Geometric Tangent D-Arc) -->
  <path d="M 23.5 14.5 C 28 14.5, 28 22.5, 22.5 23.5" fill="none" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linecap="round"/>
</g>'''

# 6. Icon: 鼠尾草枝條 (Sage Botanical Sprig)
# Dimensions: 32 x 32
ICON_SAGE_CONTENT = '''<g id="icon-sage-root">
  <!-- Central Botanical Stem Axis -->
  <line x1="16" y1="30" x2="16" y2="3" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.6" stroke-linecap="round"/>
  <!-- Leaf 1 (Bottom Left) -->
  <path d="M 16 23 C 7 21, 6 14, 13 12 C 16 17, 16 23, 16 23 Z" fill="var(--riso-sage, #3E6B56)" fill-opacity="0.38" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.2" stroke-linejoin="round"/>
  <!-- Leaf 2 (Bottom Right) -->
  <path d="M 16 19 C 25 17, 26 10, 19 8 C 16 13, 16 19, 16 19 Z" fill="var(--riso-sage, #3E6B56)" fill-opacity="0.38" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.2" stroke-linejoin="round"/>
  <!-- Leaf 3 (Mid Left) -->
  <path d="M 16 13 C 9 11, 8 6, 14 4.5 C 16 8.5, 16 13, 16 13 Z" fill="var(--riso-sage, #3E6B56)" fill-opacity="0.5" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.2" stroke-linejoin="round"/>
  <!-- Terminal Tip Bud -->
  <path d="M 16 7 C 12 4, 14 1.5, 16 2.5 C 18 1.5, 20 4, 16 7 Z" fill="var(--riso-sage, #3E6B56)" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.1"/>
  <!-- Riso Rose Pollen Accents -->
  <circle cx="16" cy="13" r="1.2" fill="var(--riso-rose, #C06C52)"/>
  <circle cx="16" cy="19" r="1.2" fill="var(--riso-rose, #C06C52)"/>
</g>'''

# 7. Icon: 洋甘菊花朵 (Chamomile Blossom)
# Dimensions: 32 x 32
ICON_CHAMOMILE_CONTENT = '''<g id="icon-chamomile-root">
  <!-- Concentric Petal Construction Circles -->
  <circle cx="16" cy="15" r="12" fill="none" stroke="var(--riso-grid-line, rgba(45,41,38,0.12))" stroke-width="0.6" stroke-dasharray="1.5 2"/>
  <!-- Geometric Radial Petals (12 Harmonious Arcs) -->
  <g fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.1" stroke-linejoin="round">
    <ellipse cx="16" cy="6" rx="2.2" ry="4.5"/>
    <ellipse cx="16" cy="24" rx="2.2" ry="4.5"/>
    <ellipse cx="7" cy="15" rx="4.5" ry="2.2"/>
    <ellipse cx="25" cy="15" rx="4.5" ry="2.2"/>
    <ellipse cx="9.6" cy="8.6" rx="2.2" ry="4.5" transform="rotate(-45 9.6 8.6)"/>
    <ellipse cx="22.4" cy="21.4" rx="2.2" ry="4.5" transform="rotate(-45 22.4 21.4)"/>
    <ellipse cx="22.4" cy="8.6" rx="2.2" ry="4.5" transform="rotate(45 22.4 8.6)"/>
    <ellipse cx="9.6" cy="21.4" rx="2.2" ry="4.5" transform="rotate(45 9.6 21.4)"/>
  </g>
  <!-- Petal Shadow Shift (Riso Sage Offset) -->
  <circle cx="16.8" cy="15.8" r="5" fill="var(--riso-sage, #3E6B56)" opacity="0.22"/>
  <!-- Central Golden Amber Disc (Stippled Flower Core) -->
  <circle cx="16" cy="15" r="5.2" fill="var(--riso-amber, #9E6234)" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <circle cx="16" cy="15" r="3.2" fill="none" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="1.2 1.2"/>
  <!-- Delicate Stem Tangent -->
  <path d="M 16 27 V 31" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.4" stroke-linecap="round"/>
</g>'''

# 8. Icon: 鋼筆尖 (Fountain Pen Nib)
# Dimensions: 32 x 32
ICON_PEN_CONTENT = '''<g id="icon-pen-root">
  <!-- Nib Silhouette (Sharp Architectural Triangle) -->
  <path d="M 10 28 L 10 21 C 10 16, 13.5 13, 16 3 C 18.5 13, 22 16, 22 21 L 22 28 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Tine Golden / Terracotta Inking Zone -->
  <path d="M 12.8 17 C 14.5 12, 16 5, 16 5 C 16 5, 17.5 12, 19.2 17 Z" fill="var(--riso-rose, #C06C52)" opacity="0.85"/>
  <!-- Circular Breather Hole -->
  <circle cx="16" cy="16" r="2" fill="var(--riso-paper, #FAF8F5)" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <!-- Central Ink Slit Hairline -->
  <line x1="16" y1="3" x2="16" y2="14" stroke="var(--text-main, #2D2926)" stroke-width="1.1"/>
  <line x1="16" y1="18" x2="16" y2="24" stroke="var(--text-main, #2D2926)" stroke-width="0.9"/>
  <!-- Collar Ring Line -->
  <line x1="10" y1="25" x2="22" y2="25" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <!-- Left/Right Nib Shoulder Accent Arcs -->
  <path d="M 12 21 C 13 18, 14 18, 14 21" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.9"/>
  <path d="M 20 21 C 19 18, 18 18, 18 21" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="0.9"/>
</g>'''

# 9. Extended System Icon: 心智自測 閃電 (Lightning Energy Bolt)
# Dimensions: 32 x 32
ICON_LIGHTNING_CONTENT = '''<g id="icon-lightning-root">
  <!-- Construction Guide Box -->
  <rect x="6" y="4" width="20" height="24" fill="none" stroke="var(--riso-grid-line, rgba(45,41,38,0.12))" stroke-width="0.6" stroke-dasharray="2 2"/>
  <!-- Riso Offset Shadow (Terracotta) -->
  <polygon points="17,3 9,17 15,17 12,29 23,13 17,13" transform="translate(1.2, 0.8)" fill="var(--riso-rose, #C06C52)" opacity="0.3"/>
  <!-- Main Crisp Lightning Bolt -->
  <polygon points="17,3 9,17 15,17 12,29 23,13 17,13" fill="var(--riso-amber, #9E6234)" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
</g>'''

# 10. Extended System Icon: 行動處方 膠囊 (Pill Capsule)
# Dimensions: 32 x 32
ICON_PILL_CONTENT = '''<g id="icon-pill-root">
  <g transform="rotate(45 16 16)">
    <!-- Capsule Body -->
    <rect x="10" y="6" width="12" height="20" rx="6" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4"/>
    <!-- Top Half (Terracotta Rose) -->
    <path d="M 10 16 H 22 V 12 C 22 8.7, 19.3 6, 16 6 C 12.7 6, 10 8.7, 10 12 Z" fill="var(--riso-rose, #C06C52)"/>
    <!-- Divider Line -->
    <line x1="10" y1="16" x2="22" y2="16" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
    <!-- Reflective Gloss Highlight -->
    <line x1="13" y1="9" x2="13" y2="13" stroke="#FFFFFF" stroke-width="1.2" stroke-linecap="round" opacity="0.8"/>
  </g>
</g>'''

# 11. Extended System Icon: 電子書庫 書本 (Open Book)
# Dimensions: 32 x 32
ICON_BOOK_CONTENT = '''<g id="icon-book-root">
  <!-- Left Page -->
  <path d="M 16 8 C 12 7, 7 8, 4 9 V 25 C 7 24, 12 23, 16 24 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Right Page -->
  <path d="M 16 8 C 20 7, 25 8, 28 9 V 25 C 25 24, 20 23, 16 24 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Sage Book Ribbon Bookmark -->
  <path d="M 16 8 V 27 L 14.5 25.5 L 13 27 V 8" fill="var(--riso-sage, #3E6B56)" stroke="var(--text-main, #2D2926)" stroke-width="0.8"/>
  <!-- Page Text Hairlines -->
  <line x1="7" y1="13" x2="13" y2="12.5" stroke="var(--text-dim, #888077)" stroke-width="0.8"/>
  <line x1="7" y1="17" x2="13" y2="16.5" stroke="var(--text-dim, #888077)" stroke-width="0.8"/>
  <line x1="19" y1="12.5" x2="25" y2="13" stroke="var(--text-dim, #888077)" stroke-width="0.8"/>
  <line x1="19" y1="16.5" x2="25" y2="17" stroke="var(--text-dim, #888077)" stroke-width="0.8"/>
</g>'''

# 12. Extended System Icon: 權力實戰 神廟 (Temple / Institutional Power)
# Dimensions: 32 x 32
ICON_TEMPLE_CONTENT = '''<g id="icon-temple-root">
  <!-- Pediment Triangular Roof -->
  <polygon points="16,4 4,11 28,11" fill="var(--riso-rose, #C06C52)" fill-opacity="0.25" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Architrave Beam -->
  <rect x="5" y="11" width="22" height="3" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <!-- 4 Columns -->
  <rect x="7" y="14" width="2.8" height="11" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.1"/>
  <rect x="12" y="14" width="2.8" height="11" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.1"/>
  <rect x="17.2" y="14" width="2.8" height="11" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.1"/>
  <rect x="22.2" y="14" width="2.8" height="11" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.1"/>
  <!-- Podium Stepped Base -->
  <rect x="4" y="25" width="24" height="2.5" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <rect x="2" y="27.5" width="28" height="2.5" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
</g>'''

# 13. Extended System Icon: 神經腦科學 大腦 (Brain / Neural Reflection)
# Dimensions: 32 x 32
ICON_BRAIN_CONTENT = '''<g id="icon-brain-root">
  <!-- Concentric Neural Convolutions -->
  <!-- Left Hemisphere (Rose) -->
  <path d="M 15 6 C 11 5, 6 8, 6 13 C 6 15, 8 16, 7 19 C 6 22, 9 26, 15 26" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 15 11 C 11 11, 10 14, 12 16 C 10 18, 12 21, 15 21" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Right Hemisphere (Sage) -->
  <path d="M 17 6 C 21 5, 26 8, 26 13 C 26 15, 24 16, 25 19 C 26 22, 23 26, 17 26" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 17 11 C 21 11, 22 14, 20 16 C 22 18, 20 21, 17 21" fill="none" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Center Synaptic Axis -->
  <line x1="16" y1="5" x2="16" y2="27" stroke="var(--text-main, #2D2926)" stroke-width="1" stroke-dasharray="2 2"/>
</g>'''

# 14. Extended System Icon: 心智護城河 盾牌 (Shield / Firm Boundary)
# Dimensions: 32 x 32
ICON_SHIELD_CONTENT = '''<g id="icon-shield-root">
  <!-- Outer Shield Contour -->
  <path d="M 16 4 L 27 8 V 16 C 27 22, 22 26.5, 16 29 C 10 26.5, 5 22, 5 16 V 8 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Left Field (Terracotta Rose) -->
  <path d="M 16 5.5 L 7 8.8 V 16 C 7 21.2, 11 24.8, 16 27 Z" fill="var(--riso-rose, #C06C52)" opacity="0.85"/>
  <!-- Right Field (Forest Sage) -->
  <path d="M 16 5.5 L 25 8.8 V 16 C 25 21.2, 21 24.8, 16 27 Z" fill="var(--riso-sage, #3E6B56)" opacity="0.85"/>
  <!-- Center Vertical Razor Hairline -->
  <line x1="16" y1="5.5" x2="16" y2="27" stroke="#FFFFFF" stroke-width="1.2"/>
</g>'''

# 15. Extended System Icon: 和解之鳥 和平鴿 (Dove / Reconciliation)
# Dimensions: 32 x 32
ICON_DOVE_CONTENT = '''<g id="icon-dove-root">
  <!-- Geometric Origami Flight Dove -->
  <path d="M 5 21 C 9 20, 13 18, 17 15 L 27 7 C 27 10, 24 14, 20 17 L 26 21 L 21 21 L 17 25 L 14 25 L 15 21 Z" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4" stroke-linejoin="round"/>
  <!-- Wing Riso Sage Accent -->
  <polygon points="17,15 27,7 23,14 18,17" fill="var(--riso-sage, #3E6B56)" opacity="0.75"/>
  <!-- Olive Branch in Beak -->
  <path d="M 5 21 L 2 20" stroke="var(--riso-sage, #3E6B56)" stroke-width="1.2"/>
  <circle cx="2" cy="19.5" r="1.2" fill="var(--riso-rose, #C06C52)"/>
</g>'''

# 16. Extended System Icon: 困境導引 羅盤 (Compass / Crisis Navigation)
# Dimensions: 32 x 32
ICON_COMPASS_CONTENT = '''<g id="icon-compass-root">
  <circle cx="16" cy="16" r="12" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1.4"/>
  <!-- Cardinal Tick Marks -->
  <line x1="16" y1="4" x2="16" y2="7" stroke="var(--riso-rose, #C06C52)" stroke-width="1.2"/>
  <line x1="16" y1="25" x2="16" y2="28" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <line x1="4" y1="16" x2="7" y2="16" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <line x1="25" y1="16" x2="28" y2="16" stroke="var(--text-main, #2D2926)" stroke-width="1.2"/>
  <!-- North Arrow (Terracotta Rose) -->
  <polygon points="16,8 18.5,16 16,15 13.5,16" fill="var(--riso-rose, #C06C52)" stroke="var(--text-main, #2D2926)" stroke-width="1"/>
  <!-- South Arrow (Paper/Sumi) -->
  <polygon points="16,24 18.5,16 16,17 13.5,16" fill="var(--text-main, #2D2926)"/>
  <!-- Central Pivot -->
  <circle cx="16" cy="16" r="1.8" fill="#FFFFFF" stroke="var(--text-main, #2D2926)" stroke-width="1"/>
</g>'''

# 17. Extended System Icon: 手帳印章 標籤 (Rubber Stamp Check)
# Dimensions: 32 x 32
ICON_STAMP_CONTENT = '''<g id="icon-stamp-root">
  <rect x="4" y="5" width="24" height="22" rx="3" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="1.5" stroke-dasharray="3 1.5"/>
  <rect x="7" y="8" width="18" height="16" rx="2" fill="var(--riso-rose, #C06C52)" fill-opacity="0.12" stroke="var(--riso-rose, #C06C52)" stroke-width="0.8"/>
  <path d="M 11 16 L 14.5 19.5 L 21 12" fill="none" stroke="var(--riso-rose, #C06C52)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</g>'''

# ══════════════════════════════════════════════════════════════════════
# COMPOSITE DICTIONARY & CODE ARTIFACTS
# ══════════════════════════════════════════════════════════════════════

ALL_SYMBOLS = [
    {
        "id": "symbol-cat-amber-plate",
        "title": "琥珀橘白放鬆伸腿標本板",
        "viewBox": "0 0 280 200",
        "filename": "cat-amber-stretch-specimen.svg",
        "content": AMBER_CAT_SPECIMEN_CONTENT,
        "is_plate": True
    },
    {
        "id": "symbol-cat-calico-plate",
        "title": "翡翠玳瑁端坐守護標本板",
        "viewBox": "0 0 280 200",
        "filename": "cat-tortoiseshell-sentinel-specimen.svg",
        "content": CALICO_CAT_SPECIMEN_CONTENT,
        "is_plate": True
    },
    {
        "id": "symbol-brand-cat",
        "title": "雙色解構貓咪微型標識",
        "viewBox": "0 0 32 32",
        "filename": "brand-cat.svg",
        "content": BRAND_CAT_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-glasses",
        "title": "細框眼鏡 (專注聚焦)",
        "viewBox": "0 0 32 32",
        "filename": "icon-glasses.svg",
        "content": ICON_GLASSES_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-coffee",
        "title": "熱咖啡杯 (溫熱平復)",
        "viewBox": "0 0 32 32",
        "filename": "icon-coffee.svg",
        "content": ICON_COFFEE_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-sage",
        "title": "鼠尾草枝條 (淨化心緒)",
        "viewBox": "0 0 32 32",
        "filename": "icon-sage.svg",
        "content": ICON_SAGE_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-chamomile",
        "title": "洋甘菊花朵 (安撫神經)",
        "viewBox": "0 0 32 32",
        "filename": "icon-chamomile.svg",
        "content": ICON_CHAMOMILE_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-pen",
        "title": "鋼筆尖 (深刻書寫)",
        "viewBox": "0 0 32 32",
        "filename": "icon-pen.svg",
        "content": ICON_PEN_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-lightning",
        "title": "閃電能量 (心智自測)",
        "viewBox": "0 0 32 32",
        "filename": "icon-lightning.svg",
        "content": ICON_LIGHTNING_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-pill",
        "title": "雙色處方膠囊 (行動處方)",
        "viewBox": "0 0 32 32",
        "filename": "icon-pill.svg",
        "content": ICON_PILL_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-book",
        "title": "開卷書本 (專書導讀與書庫)",
        "viewBox": "0 0 32 32",
        "filename": "icon-book.svg",
        "content": ICON_BOOK_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-temple",
        "title": "經典神廟 (史丹佛組織權力學)",
        "viewBox": "0 0 32 32",
        "filename": "icon-temple.svg",
        "content": ICON_TEMPLE_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-brain",
        "title": "神經迴路 (密西根大腦反芻)",
        "viewBox": "0 0 32 32",
        "filename": "icon-brain.svg",
        "content": ICON_BRAIN_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-shield",
        "title": "守護盾牌 (拒絕掠奪邊界)",
        "viewBox": "0 0 32 32",
        "filename": "icon-shield.svg",
        "content": ICON_SHIELD_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-dove",
        "title": "幾何和解鴿 (假性孤兒療癒)",
        "viewBox": "0 0 32 32",
        "filename": "icon-dove.svg",
        "content": ICON_DOVE_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-compass",
        "title": "困境羅盤 (心靈困境導引)",
        "viewBox": "0 0 32 32",
        "filename": "icon-compass.svg",
        "content": ICON_COMPASS_CONTENT,
        "is_plate": False
    },
    {
        "id": "symbol-stamp",
        "title": "手帳印章 (核准標記)",
        "viewBox": "0 0 32 32",
        "filename": "icon-stamp-check.svg",
        "content": ICON_STAMP_CONTENT,
        "is_plate": False
    }
]

def generate_individual_svg_files():
    for item in ALL_SYMBOLS:
        filepath = os.path.join(IMG_SVG_DIR, item["filename"])
        svg_xml = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{item['viewBox']}" width="100%" height="100%" fill="none" role="img" aria-label="{item['title']}">
{item['content']}
</svg>'''
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_xml)
        print(f"Generated standalone SVG: {filepath}")

def generate_master_svg_sprite():
    sprite_path = os.path.join(ASSETS_DIR, "riso-symbols.svg")
    symbols_xml = []
    for item in ALL_SYMBOLS:
        symbol_block = f'''  <symbol id="{item['id']}" viewBox="{item['viewBox']}">
{item['content']}
  </symbol>'''
        symbols_xml.append(symbol_block)
    
    master_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
  <defs>
    <!-- Risograph Paper Texture Filter (Optional Micro Stipple) -->
    <filter id="riso-stipple" x="0%" y="0%" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" result="noise"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.07 0"/>
      <feComposite in2="SourceGraphic" in="glitch" operator="in"/>
    </filter>
  </defs>
{chr(10).join(symbols_xml)}
</svg>'''
    with open(sprite_path, "w", encoding="utf-8") as f:
        f.write(master_svg)
    print(f"Generated master SVG sprite: {sprite_path}")

def generate_master_css():
    css_path = os.path.join(ASSETS_DIR, "riso-symbols.css")
    css_content = '''/* ══════════════════════════════════════════════════════════════════════
   SWISS DECONSTRUCTED RISOGRAPH VECTOR SYMBOL SYSTEM
   Standard: Unified House Style & Bullet Journal Reading Suite
   Colors: Terracotta Rose (#C06C52) · Forest Sage (#3E6B56) · Amber (#9E6234)
   ══════════════════════════════════════════════════════════════════════ */

:root {
  /* Risograph Authentic Color Drums */
  --riso-ink: #2D2926;
  --riso-rose: #C06C52;
  --riso-rose-shift: #D96B43;
  --riso-rose-tint: rgba(192, 108, 82, 0.16);
  --riso-sage: #3E6B56;
  --riso-sage-shift: #2F5D50;
  --riso-sage-tint: rgba(62, 107, 86, 0.16);
  --riso-amber: #9E6234;
  --riso-amber-tint: rgba(158, 98, 52, 0.16);
  --riso-paper: #FAF8F5;
  --riso-paper-alt: #F4EFEA;
  --riso-grid-line: rgba(45, 41, 38, 0.12);
  --riso-construction: rgba(62, 107, 86, 0.28);
  --riso-datum: rgba(192, 108, 82, 0.35);

  /* Standard Icon Sizes (Physical Scale Consistency) */
  --icon-size-xs: 14px;
  --icon-size-sm: 18px;
  --icon-size-md: 22px;
  --icon-size-lg: 28px;
  --icon-size-xl: 34px;
}

/* Dark Mode Token Adaptation (WCAG AA Strict Contrast) */
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
    --riso-construction: rgba(110, 169, 143, 0.35);
    --riso-datum: rgba(226, 133, 110, 0.4);
  }
}

/* ══════════════════════════════════════════════════════════════════════
   SVG RENDERING & PHYSICAL SCALE CLASSES
   ══════════════════════════════════════════════════════════════════════ */

/* General Riso Vector Icon */
.riso-icon {
  width: var(--icon-size-md);
  height: var(--icon-size-md);
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  shape-rendering: geometricPrecision;
  text-rendering: geometricPrecision;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.riso-icon-xs { width: var(--icon-size-xs); height: var(--icon-size-xs); }
.riso-icon-sm { width: var(--icon-size-sm); height: var(--icon-size-sm); vertical-align: -3px; }
.riso-icon-md { width: var(--icon-size-md); height: var(--icon-size-md); }
.riso-icon-lg { width: var(--icon-size-lg); height: var(--icon-size-lg); }
.riso-icon-xl { width: var(--icon-size-xl); height: var(--icon-size-xl); }

/* Top Navigation Brand Mark */
.riso-brand-mark {
  width: 26px;
  height: 26px;
  display: inline-block;
  vertical-align: middle;
  margin-right: 8px;
  flex-shrink: 0;
}

/* ══════════════════════════════════════════════════════════════════════
   SPECIMEN PLATE CONTAINERS (Replaces Realistic Photo Polaroids)
   ══════════════════════════════════════════════════════════════════════ */

.bujo-specimen-plate {
  width: 100%;
  aspect-ratio: 280 / 200;
  background: var(--riso-paper, #FAF8F5);
  border: 1px solid var(--border-card, #EFE8DE);
  border-radius: 8px;
  overflow: hidden;
  position: relative;
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.5), 0 2px 8px rgba(45, 41, 38, 0.04);
}

.bujo-specimen-plate svg {
  width: 100%;
  height: 100%;
  display: block;
  shape-rendering: geometricPrecision;
}

/* Risograph Mechanical Misregistration Shift Effect on Hover */
.polaroid-card:hover .bujo-specimen-plate svg [style*="mix-blend-mode: multiply"],
.bujo-specimen-plate:hover svg [style*="mix-blend-mode: multiply"] {
  transform: translate(2.5px, -1.8px) !important;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Risograph Color Blending */
.riso-multiply {
  mix-blend-mode: multiply;
}

/* Micro Technical Label */
.tech-label-mono {
  font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
'''
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print(f"Generated master CSS: {css_path}")

def generate_visual_dictionary():
    dict_path = os.path.join(ASSETS_DIR, "svg-dictionary.html")
    catalog_cards = []
    for item in ALL_SYMBOLS:
        card_class = "catalog-card catalog-card-wide" if item["is_plate"] else "catalog-card"
        icon_display = f'''<div class="card-preview">
  <svg class="preview-svg" viewBox="{item['viewBox']}" role="img" aria-label="{item['title']}">
    <use href="riso-symbols.svg#{item['id']}"/>
  </svg>
</div>'''
        code_snippet = f'''&lt;svg class="{ 'bujo-specimen-svg' if item['is_plate'] else 'riso-icon' }" role="img" aria-label="{item['title']}"&gt;
  &lt;use href="assets/riso-symbols.svg#{item['id']}"/&gt;
&lt;/svg&gt;'''
        catalog_cards.append(f'''
    <div class="{card_class}">
      {icon_display}
      <div class="card-meta">
        <span class="card-tag">ID: #{item['id']}</span>
        <h4 class="card-title">{item['title']}</h4>
        <span class="card-dim">VIEWBOX: {item['viewBox']} · FILE: {item['filename']}</span>
        <div class="code-box">
          <code>{code_snippet}</code>
        </div>
      </div>
    </div>''')

    html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>瑞士解構 Risograph 雙色向量符號庫字典 | Inner Power Reading Suite</title>
  <link rel="stylesheet" href="riso-symbols.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --font-serif: "Noto Serif TC", "Noto Serif SC", "Songti TC", "Songti SC", serif;
      --font-sans: "Noto Sans TC", "Noto Sans SC", "PingFang TC", system-ui, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --bg-page: #FAF8F5;
      --text-main: #2D2926;
      --text-dim: #888077;
      --border-subtle: #E8E1D7;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-page);
      background-image: radial-gradient(rgba(200, 190, 178, 0.4) 1px, transparent 1px);
      background-size: 24px 24px;
      color: var(--text-main);
      padding: 48px 24px;
      line-height: 1.7;
    }}
    .container {{
      max-width: 1120px;
      margin: 0 auto;
    }}
    .header-box {{
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: 0 4px 20px rgba(45, 41, 38, 0.05);
    }}
    .eyebrow {{
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--riso-rose);
      font-weight: 700;
      letter-spacing: 0.1em;
    }}
    h1 {{
      font-family: var(--font-serif);
      font-size: 1.85rem;
      font-weight: 700;
      margin: 8px 0 12px 0;
    }}
    .desc {{
      color: var(--text-dim);
      font-size: 0.95rem;
      max-width: 760px;
    }}
    .palette-strip {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px dashed var(--border-subtle);
    }}
    .palette-chip {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
      background: #FFFFFF;
    }}
    .chip-swatch {{
      width: 14px;
      height: 14px;
      border-radius: 2px;
    }}
    .catalog-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
      margin-bottom: 48px;
    }}
    .catalog-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(45, 41, 38, 0.04);
      display: flex;
      flex-direction: column;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .catalog-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(45, 41, 38, 0.08);
    }}
    .catalog-card-wide {{
      grid-column: 1 / -1;
    }}
    .card-preview {{
      background: var(--riso-paper);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 140px;
      margin-bottom: 16px;
    }}
    .catalog-card-wide .card-preview {{
      min-height: 240px;
      max-height: 360px;
    }}
    .preview-svg {{
      width: 100%;
      height: 100%;
      max-height: 260px;
    }}
    .card-meta {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .card-tag {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--riso-rose);
      font-weight: 700;
    }}
    .card-title {{
      font-family: var(--font-serif);
      font-size: 1.05rem;
      font-weight: 600;
    }}
    .card-dim {{
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--text-dim);
    }}
    .code-box {{
      background: #F8F6F2;
      border: 1px solid var(--border-subtle);
      border-radius: 4px;
      padding: 8px 10px;
      margin-top: 8px;
      overflow-x: auto;
    }}
    code {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: #3E3B36;
      white-space: pre-wrap;
      word-break: break-all;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header-box">
      <span class="eyebrow">SWISS DESIGN · RISOGRAPH DUAL-DRUM SYSTEM · SPECIMEN CATALOG</span>
      <h1>溫柔生長・手帳讀書誌：抽象幾何符號庫字典</h1>
      <p class="desc">
        本字典收錄全套 17 組自洽、高端、去寫實照片的純 SVG 符號系統。包含兩款 280×200 雙貓心理學標本板（橘白放鬆伸腿、三花堅定邊界）、五大生活花草物件（細框眼鏡、熱咖啡杯、鼠尾草枝條、洋甘菊花朵、鋼筆尖）與全站去 Emoji 系統功能符號。全向量支援微型坐標註記與 Risograph 雙色印刷機械錯位層疊。
      </p>
      <div class="palette-strip">
        <div class="palette-chip"><div class="chip-swatch" style="background:#C06C52;"></div> <span>RISO ROSE #C06C52</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#3E6B56;"></div> <span>RISO SAGE #3E6B56</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#9E6234;"></div> <span>RISO AMBER #9E6234</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#2D2926;"></div> <span>RISO INK #2D2926</span></div>
        <div class="palette-chip"><div class="chip-swatch" style="background:#FAF8F5; border:1px solid #ddd;"></div> <span>RISO PAPER #FAF8F5</span></div>
      </div>
    </div>

    <!-- Master Sprite Hidden Embedding -->
    <div style="display:none;">
      <!-- Master SVG Sprite Embedded for Immediate Test -->
    </div>

    <div class="catalog-grid">
      {''.join(catalog_cards)}
    </div>
  </div>
</body>
</html>'''

    with open(dict_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated visual dictionary HTML: {dict_path}")

if __name__ == "__main__":
    generate_individual_svg_files()
    generate_master_svg_sprite()
    generate_master_css()
    generate_visual_dictionary()
    print("All vector assets successfully generated!")

# 《溫柔生長讀書誌》專案治理與經驗沉澱規範書 (PROJECT_GOVERNANCE.md)

> **版本**：v3.2 Final Release  
> **專案路徑**：`/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading`  
> **生產網址**：`https://inner-power-reading.pages.dev`  
> **Git 基準**：分支 `main`（GitHub: `atonnyshen/inner-power-reading`）  
> **制定日期**：2026-11-16  

---

## 📖 一、 專案背景與治理目標

《溫柔生長讀書誌》（Inner Power Reading）為面向成年讀者、針對職場壓力、關係困難、情緒勒索與過度努力所打造的深度數位閱讀誌。本專案歷經架構重組、書目真偽考證、全站去防衛化文字重塑、手機版微觀排版防呆與 Cloudflare Pages 邊緣發布。

為確保後續維護、內容擴充或多工具協作時具備唯一事實來源（SSOT），特制定本治理規範書，將歷次決策、工程坑位與核心經驗全面沉澱。

---

## 🏛️ 二、 五大治理支柱 (Five Pillars of Project Governance)

### 支柱一：書目考證與版本真偽（EPUB SSOT 鐵律）

1. **唯一依據**：
   全站十本主書的正式書名、作者、譯者、出版社、出版年份及章節定位，**必須以實際收錄 EPUB 的內部版權頁（Copyright Page）為最高依據**。
2. **禁止事項**：
   * 嚴禁以 EPUB 的 OPF 檔案建立日期推定為出版年份。
   * 嚴禁依網路書單或台灣另一譯本的資訊覆蓋實際收錄之簡體版本資訊。
   * 同一英文原著的不同中文譯本，嚴禁混雜譯者、出版社、章節標題或引文。
3. **繁簡轉寫邊界**：
   簡體中文版 EPUB 於繁體中文網頁呈現時，依字形轉寫為正體漢字，但保留原版權頁的出版社與譯者原名（例如《職場女性：別讓這些細節絆住你》繼續沿用簡體版出版資訊；《鈍感力》載明青島出版社版本）。
4. **第十本主書定名裁決**：
   * 正式主標題定名為**《脆弱的力量》**（對應英文原著 *The Gifts of Imperfection*，布琳·布朗 著；浙江人民出版社 2014 年 5 月紙版，湛廬文化電子版）。
   * 台灣譯本名稱《不完美的禮物》僅作為對照輔助標示，不得佔用主標題。
   * 既有網址 `book-daring-greatly.html` 永久保留，嚴禁更名，避免既有外鏈失效。

---

### 支柱二：文字衛生與讀者口吻重塑（去防禦化與去 AI 腔）

本專案文字風格堅持成熟、親近、具體、準確，尊重讀者的生活經驗，徹底告別技術性與防禦性寫作：

1. **徹底根除過度防禦性寫作（Anti-Defensive Writing）**：
   * **消除法律/免責條款腔**：嚴禁在讀者閱讀情境中出現「以下為本站編輯整理...並非原書逐字引文...請自行確認原意」、「實際做法可以隨環境條件調整」、「不代表心理測驗結果」等免責聲明。
   * **消除退縮與預防性消極詞**：嚴禁「不保證立即入睡或消除焦慮」、「這是一種策略，不保證薪資談判成功」、「不能僅憑一次互動推斷神經機制」等生硬說辭。
   * **改法**：將防禦性宣告轉化為成熟、溫暖、有同理心且具建設性的「陪伴與實踐指引」。
2. **特許保留條款（唯一例外）**：
   首頁唯一經特許保留之句子為：
   > 「每本書附有書封、情境導讀、閱讀心法與專書頁。摘記由本站編輯依原著觀點整理，並非作者逐字引文。」
   此句僅保留於首頁 Section 4 核心導讀區，專書分頁嚴禁複製此句作為免責擋箭牌。
3. **日常練習標題統一**：
   全站十本專頁之 Section 4 標題全面統一為**「三項日常實踐練習」**，移除贅餘防禦詞「可自行調整」。
4. **L0 中文底線層落實**：
   * 去翻案腔（「不是 A 而是 B」「並非」「不在於」等）。
   * 去輕動詞包裝（「進行自我對話」→「與自己對話」）。
   * 去內部工程與設計代碼（全面清除 `PEN. 05`、`CAF. 02`、GitHub 原始碼技術連結）。

---

### 支柱三：跨平台閱讀生態與 App 喚起機制（Readify AI & Universal Links）

1. **推薦載具定位**：
   * 首選推薦 **Readify AI**（官方繁中入口：`https://readifyai.com/zh`），提供自然語音朗讀、重點提煉與 AI 問答。
   * 同時完整保留支援 Apple Books、微信讀書、Kobo、Kindle 等本機閱讀器。
2. **Apple 生態系 Universal Links 最佳實踐**：
   * **為什麼使用官方 HTTPS 連結**：iOS 與 macOS 具備 Universal Links（通用連結）機制。使用 `https://readifyai.com/zh` 能確保：
     * **已安裝 App 者**：點擊後由系統底層直接喚起本地 Readify AI App。
     * **未安裝 App 者**：平滑載入官方網頁並提供 App Store 下載按鈕（Graceful Fallback）。
   * **嚴禁自訂私有協議（如 `readify://`）**：在使用者未安裝 App 時，自訂協議會導致 Safari 跳出「網址無效」的刺眼報錯，破壞絲滑感。
3. **最自然的「下載 ➔ 閱讀」動線**：
   * 讀者點擊「下載 EPUB 電子書」取得檔案。
   * 於 iPhone / Mac 點擊下載後的檔案，呼叫系統原生 Share Sheet，直接選取「Readify」即可完成匯入。

---

### 支柱四：前端工程與防禦性 CSS 架構

1. **雙首頁同位元對齊鐵律**：
   * `index.html` 與 `preview-bullet-journal-main.html` 在任何修改後，必須執行 SHA256 校驗，保證 100% 同位元完全一致。
2. **手機端窄螢幕（320px/375px）掉字防護**：
   在 `assets/book-margin-companions.css` 中注入：
   ```css
   .showcase-chip > span:first-child { flex: 0 0 auto; white-space: nowrap; }
   .bujo-companion-reminder .reminder-tag { flex: 0 0 auto; white-space: nowrap; }
   ```
   確保「作者：」、「出版：」、「伴讀心法」等前置標籤在小螢幕下不被 flex 擠壓成單字直向排列。
3. **頁尾版面約束**：
   頁尾版權宣告必須收斂於 `.container` 內部，嚴禁在外部散落獨立 notice 標籤，防止版面超出邊界靠左歪斜。
4. **章節導航抽屜完整性**：
   全站 11 個導航項目必須配齊專屬小圖示（例如 `💬 現場溝通練習`），維持視覺節奏的一致性。

---

### 支柱五：DevOps、安全標頭與雲端部署治理

1. **Cloudflare Pages 直傳部署**：
   * 部署腳本：使用 `.agent/skills/cloudflare-deploy-ops/scripts/deploy.py`。
   * 免除 GitHub CI 構建延遲與 CDN 快取殘留，直接上傳至邊緣節點。
2. **安全標頭規範（`_headers`）**：
   * `X-Robots-Tag: noindex, nofollow, noarchive`（保護未經授權爬取）
   * `X-Content-Type-Options: nosniff`
   * `Referrer-Policy: strict-origin-when-cross-origin`
   * `Permissions-Policy: document-domain=(), microphone=(), camera=(), geolocation=()`
   * 嚴格的 CSP 配置。
3. **線上驗證防護**：
   * 透過 Python 進行線上邊緣節點檢測時，**必須指定標準瀏覽器 User-Agent**，防範 Cloudflare WAF 將預設 `Python-urllib` 判定為機器人而阻擋（HTTP 403）。

---

## 📂 三、 專案檔案清冊 (Directory Manifest)

```
inner-power-reading/
├── index.html                           # 正式首頁 (與 preview-bullet-journal-main.html 同位元一致)
├── preview-bullet-journal-main.html     # 預覽首頁 (同位元 SHA256 鏡像)
├── book-power.html                      # 專書頁 01：《懂權力，在每個角色上發光》
├── book-rules-of-power.html             # 專書頁 02：《精進權力》
├── book-nice-girls.html                 # 專書頁 03：《職場女性：別讓這些細節絆住你》
├── book-give-and-take.html              # 專書頁 04：《給予》
├── book-emotional-blackmail.html        # 專書頁 05：《情緒勒索》
├── book-chatter.html                    # 專書頁 06：《強大內心的自我對話習慣》
├── book-donganli.html                   # 專書頁 07：《鈍感力》
├── book-immature-parents.html           # 專書頁 08：《如果父母情緒不成熟》
├── book-overeffort.html                 # 專書頁 09：《過度努力》
├── book-daring-greatly.html             # 專書頁 10：《脆弱的力量》（台版對照《不完美的禮物》）
├── _headers                             # Cloudflare Pages 邊緣安全標頭設定檔
├── robots.txt                           # 搜尋引擎爬蟲限制規則
├── README.md                            # 專案公開說明文件
├── PROJECT_GOVERNANCE.md                # 本治理規範與經驗沉澱書
├── books/                               # 10 本核心專書 EPUB 實體檔案目錄 (受保護，零覆寫)
├── covers/                              # 10 本核心專書真實封面圖檔
├── img/                                 # 品牌插畫、雙貓伴讀透明圖檔與編輯插圖
├── assets/                              # 樣式表、Riso 符號庫與字型資源
│   ├── riso-symbols.css
│   ├── riso-symbols.svg
│   ├── book-margin-companions.css       # 伴讀貓咪與手機版標籤排版防護 CSS
│   └── favicon-cat.svg
└── js/
    └── chinese-convert.js               # 繁簡切換引擎
```

---

## 📋 四、 發布前驗收核對清單 (Release Gate Checklist)

在任何後續版本發布前，必須依序通過以下檢驗：

* [x] **Gate 1: 書目一致性** — 十本主書名稱與版本資訊符合 EPUB 版權頁，第十本標題為《脆弱的力量》。
* [x] **Gate 2: 核心內容保護** — 90 則摘記與 30 組情境正文未被更動。
* [x] **Gate 3: 雙首頁同位元校驗** — `cmp index.html preview-bullet-journal-main.html` 輸出 0。
* [x] **Gate 4: 文字衛生檢驗** — 無生硬免責語、無「不保證」等防禦性字眼、無內部設計代碼。
* [x] **Gate 5: 閱讀器生態連結** — Readify AI 官方連結指向 `https://readifyai.com/zh`，支援閱讀器完整列出。
* [x] **Gate 6: HTML 結構平衡** — 所有 `main`、`section`、`footer`、`article` 標籤 100% 閉合。
* [x] **Gate 7: 邊緣部署與線上複驗** — Cloudflare Pages 直傳成功，HTTP 200 回應，User-Agent 檢驗通過。

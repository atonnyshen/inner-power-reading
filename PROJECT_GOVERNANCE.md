# 《溫柔生長讀書誌》專案治理與經驗沉澱規範書 (PROJECT_GOVERNANCE.md)

> **版本**：v3.2 Final Release  
> **專案路徑**：`/Users/atonny/工作區/07_開發專案_Dev/inner-power-reading`  
> **生產網址**：`https://inner-power-reading.pages.dev`  
> **Git 基準**：分支 `main`（GitHub: `atonnyshen/inner-power-reading`）  
> **制定日期**：2026-11-16  

> **結案案例索引**：[`PROJECT_CASEBOOK.md`](PROJECT_CASEBOOK.md) 按人工裁決、Git 版本、實際缺陷、驗收收據及尚未證實事項整理 ChatGPT 接手期間的實務經驗。它是本規範的證據索引，不能用歷史 PASS 取代最新版本驗收。

---

## 📖 一、 專案背景與治理目標

《溫柔生長讀書誌》（Inner Power Reading）為面向成年讀者、針對職場壓力、關係困難、情緒勒索與過度努力所打造的深度數位閱讀誌。本專案歷經架構重組、書目真偽考證、全站去防衛化文字重塑、手機版微觀排版防呆與 Cloudflare Pages 邊緣發布。

為確保後續維護、內容擴充或多工具協作時能追溯版本與決策，特制定本治理規範書。**原著、當前檔案、人類裁決與歷史收據分屬不同來源層級**；詳細案例與限制見 `PROJECT_CASEBOOK.md`。不得以本規範的摘要自稱已回讀所有歷史對話。

---

## 🏛️ 二、 五大治理支柱 (Five Pillars of Project Governance)

### 支柱一：書目考證與版本真偽（實收 EPUB 版本優先）

1. **主要來源與複核**：
   全站十本主書的正式書名、作者、譯者、出版社、出版年份及章節定位，**以實際收錄 EPUB 的內部版權頁為優先起點**，再和書封、OPF、ISBN、出版方可查書目及可定位章節核對。若資料互相衝突，標記待查；來源檔案或單一版權頁也可能有誤植，不能把「使用者上傳」等同「自動驗真」。
2. **禁止事項**：
   * 嚴禁以 EPUB 的 OPF 檔案建立日期推定為出版年份。
   * 嚴禁依網路書單或台灣另一譯本的資訊覆蓋實際收錄之簡體版本資訊。
   * 同一英文原著的不同中文譯本，嚴禁混雜譯者、出版社、章節標題或引文。
3. **繁簡轉寫邊界**：
   簡體中文版 EPUB 於繁體中文網頁呈現時，依字形轉寫為正體漢字，但保留原版權頁的出版社與譯者原名（例如《職場女性：別讓這些細節絆住你》繼續沿用簡體版出版資訊；《鈍感力》載明青島出版社版本）。
4. **第十本主書定名裁決**：
   * 正式主標題定名為**《脆弱的力量》**（對應英文原著 *The Gifts of Imperfection*，布琳·布朗 著；浙江人民出版社 2014 年 5 月紙版，湛廬文化電子版）。
   * 台灣譯本名稱《不完美的禮物》僅作為對照輔助標示，不得佔用主標題。
   * 已發布的網址 `book-daring-greatly.html` 保留，以免既有連結失效。將來若經使用者批准遷移，也須維持舊網址可用並驗證重新導向，不能直接刪除舊路徑。

---

### 支柱二：文字衛生與讀者口吻重塑（去防禦化與去 AI 腔）

本專案文字風格堅持成熟、親近、具體、準確，尊重讀者的生活經驗，徹底告別技術性與防禦性寫作：

1. **去除重複的防禦性寫作（Anti-Defensive Writing）**：
   * **先判資訊功能**：摘記引言、情境指引與頁尾不反覆交代「請自行確認原意」「環境條件可以調整」「不保證效果」，避免讓閱讀變成內部審稿報告。
   * **不可用禁詞表刪真相**：作者／引文歸屬、編輯示例性質、問卷非診斷的必要事實界線，以及權利或安全所需說明，若能避免誤導，須在適當位置保留。使用者核准的例外不得被自動掃除。
   * **改法**：把多餘的交代轉為精確且自然的導讀；保留有證據的風險限定與來源界線，不虛構效果、不對讀者預設病因。
2. **特許保留條款（唯一例外）**：
   首頁唯一經特許保留之句子為：
   > 「每本書附有書封、情境導讀、閱讀心法與專書頁。摘記由本站編輯依原著觀點整理，並非作者逐字引文。」
   此句僅保留於首頁 Section 4 核心導讀區，專書分頁嚴禁複製此句作為免責擋箭牌。
3. **日常練習標題統一**：
   全站十本專頁之 Section 4 標題全面統一為**「三項日常實踐練習」**，移除贅餘防禦詞「可自行調整」。
4. **L0 中文底線層落實**：
   * 減少公式化翻案句（「不是 A 而是 B」等），但不能機械禁止具有必要邏輯功能的「並非／不在於」。
   * 去輕動詞包裝（「進行自我對話」→「與自己對話」）。
   * 去內部工程與設計代碼（全面清除 `PEN. 05`、`CAF. 02`、GitHub 原始碼技術連結）。
   * 每本書的引言須對得上其書旨與三個實際情境；避免十本全部套用「汲取力量」「練習堅定界線」，並檢查「這三個情境練習」等主謂搭配不當。

---

### 支柱三：跨平台閱讀生態與 App 喚起機制（Readify AI & Universal Links）

1. **推薦載具定位**：
   * 首選推薦 **Readify AI**（官方繁中入口：`https://readifyai.com/zh`），提供自然語音朗讀、重點提煉與 AI 問答。
   * 同時完整保留支援 Apple Books、微信讀書、Kobo、Kindle 等本機閱讀器。
2. **官方 HTTPS 與 Universal Links 的適用界線**：
   * `https://readifyai.com/zh` 是可供一般讀者開啟的官方網站入口。**HTTPS 連結本身不能保證開啟 App**：Universal Links 需 App 宣告 associated domains、網站提供可驗證 AASA、裝置已安裝相容版本，且符合瀏覽器、使用者選擇與觸發場景。
   * 未安裝或不符合上述條件時，通常開啟網頁；網頁是否提供 App Store、Google Play 或其他下載入口，依當期實際頁面為準，不能寫成系統保證。
   * 不使用尚未驗證的自訂私有協議（如 `readify://`）。要宣稱「已安裝即自動開啟」，先在目標真機驗 AASA、關聯設定與連結互動；未驗時標 `NOT_VERIFIED`。
3. **最自然的「下載 ➔ 閱讀」動線**：
   * 讀者點擊「下載 EPUB 電子書」取得檔案。
   * 在支援的裝置／App 版本上，讀者**可嘗試**透過檔案的分享選單或 Readify 內建匯入功能開書。Share Sheet 是否列出該 App 必須實測，不得預設所有 iPhone、Mac 與閱讀器一致。

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
   * 若採直傳，從公開資源白名單準備部署目錄；不把 `.git`、歷史收據、備份、腳本、憑證或治理文件連同網站上傳。直傳完成後仍須比對正式網址檔案位元與部署來源；Git push 不代表 Cloudflare 已更新。
2. **安全標頭規範（`_headers`）**：
   * `X-Robots-Tag: noindex, nofollow, noarchive`（搜尋索引限制；**不構成存取控制或權利授權**。若日後希望被搜尋到，須另作 SEO／發布裁決）
   * `X-Content-Type-Options: nosniff`
   * `Referrer-Policy: strict-origin-when-cross-origin`
   * `Permissions-Policy: document-domain=(), microphone=(), camera=(), geolocation=()`
   * 嚴格的 CSP 配置。
3. **線上驗證防護**：
   * 若發生 HTTP 403，檢查 WAF／快取與工具 User-Agent 的差異；可用標準瀏覽器 User-Agent 進行對照，但不能以改變 UA 冒充已修復安全策略。正式驗收仍查 HTTP、內容、SHA 與實際瀏覽器功能。

---

## 📂 三、 專案檔案清冊 (Directory Manifest)

```
inner-power-reading/
├── index.html                           # 正式首頁 (與 preview-bullet-journal-main.html 同位元一致)
├── preview-bullet-journal-main.html     # 預覽首頁 (同位元 SHA256 鏡像)
├── PROJECT_CASEBOOK.md                  # ChatGPT 裁決、實證失誤、收據索引與 Hallmark 對照
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

> 下列已勾選項目是 **2026-11-16 當次結案版本的歷史驗收摘要**，不自動代表未來變更、所有平台或公開散布權利均已通過。具名收據、未測項目及來源範圍見 `PROJECT_CASEBOOK.md`。

* [x] **Gate 1: 書目一致性** — 十本主書名稱與版本資訊符合 EPUB 版權頁，第十本標題為《脆弱的力量》。
* [x] **Gate 2: 核心內容保護** — 90 則摘記與 30 組情境正文未被更動。
* [x] **Gate 3: 雙首頁同位元校驗** — `cmp index.html preview-bullet-journal-main.html` 輸出 0。
* [x] **Gate 4: 文字衛生檢驗** — 無生硬免責語、無「不保證」等防禦性字眼、無內部設計代碼。
* [x] **Gate 5: 閱讀器生態連結** — Readify AI 官方連結指向 `https://readifyai.com/zh`，支援閱讀器完整列出。
* [x] **Gate 6: HTML 結構平衡** — 所有 `main`、`section`、`footer`、`article` 標籤 100% 閉合。
* [x] **Gate 7: 邊緣部署與線上複驗** — Cloudflare Pages 直傳成功，HTTP 200 回應，User-Agent 檢驗通過。

**獨立狀態**：出版內容的來源覆蓋（有別於摘記 90／90）、五本補充書出典、實機可及性、公開 EPUB／封面再散布權利均不得由上述技術 PASS 推定已核准。使用者已決定保留下載，本檔只忠實記錄其產品裁決及尚缺的權利證據，不重啟本案。

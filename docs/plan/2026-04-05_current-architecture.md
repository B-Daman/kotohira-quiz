# kotohira-quiz 現行アーキテクチャ設計書

更新日: 2026-04-05
ステータス: Phase 1 稼働中

---

## 概要

琴平町の知識と英単語を毎日10問で学べるデイリークイズサービス。
Discord Bot（2問ティーザー）+ Web アプリ（10問フル回答）の構成。

- Web: https://b-daman.github.io/kotohira-quiz/
- GitHub: https://github.com/B-Daman/kotohira-quiz (public)
- 問題データの正典: `C:\Users\user\hisho-bot\data\quiz\`

---

## 1. プロジェクト構成（実装済み）

```
kotohira-quiz/
├── web/                              # Vite + React + TypeScript + Tailwind CSS v4
│   ├── src/
│   │   ├── types.ts                  # 型定義（Question, AnswerRecord, QuizPhase等）
│   │   ├── utils/
│   │   │   └── date.ts              # JST日付ヘルパー（sv-SEロケール方式）
│   │   ├── data/
│   │   │   ├── questions.ts         # JSON fetch + キャッシュ + enabled/reviewedフィルタ
│   │   │   └── history.ts           # localStorage回答履歴・スコア管理
│   │   ├── hooks/
│   │   │   └── useQuiz.ts           # 問題選出（カテゴリ分散・パターン混合）+ 進行管理
│   │   ├── components/
│   │   │   ├── QuizCard.tsx         # 問題文 + 4択ボタン
│   │   │   ├── ResultCard.tsx       # 正解/不正解 + 解説（英語は答え/発音/例文を分離表示）
│   │   │   ├── ScoreSummary.tsx     # 10問完了後のスコア画面（カテゴリ別成績）
│   │   │   ├── ProgressBar.tsx      # 進捗バー（1/10）
│   │   │   └── ErrorMessage.tsx     # JSONロード失敗時のエラー表示
│   │   ├── pages/
│   │   │   └── DailyQuiz.tsx        # メインページ（phase状態遷移管理）
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css                # Tailwind directives
│   ├── public/data/                  # ビルド時にJSONを同梱（hisho-botからコピー）
│   │   ├── kotohira_questions.json   # 琴平町クイズ 500問
│   │   └── english_questions.json    # 英単語クイズ 500問
│   ├── index.html
│   ├── vite.config.ts                # base: '/kotohira-quiz/'（GitHub Pages用）
│   └── package.json
│
├── bot/                              # Discord Bot（Python, スタンドアロン）
│   ├── main.py                       # エントリ + 毎朝7:00ループ + PersistentView
│   ├── config.py                     # 環境変数（TOKEN, CHANNEL_ID, WEB_URL, DATA_DIR）
│   ├── quiz_store.py                 # 問題読み込み・選出（読み取り専用）
│   ├── daily_teaser.py               # 2問個別投稿（ボタン回答付き）+ Webリンク
│   ├── start_bot.bat                 # 起動バッチ
│   ├── register_task.ps1             # タスクスケジューラ登録スクリプト
│   ├── .env                          # 機密情報（.gitignore対象）
│   └── .env.example
│
├── data/
│   └── sync_to_web.sh               # hisho-bot/data/quiz/ → web/public/data/ コピー
│
├── .github/workflows/
│   └── deploy.yml                    # GitHub Pages自動デプロイ（push to master）
│
├── .gitignore
└── docs/                             # 設計書・調査・レビュー
```

---

## 2. 技術スタック

| レイヤー | 技術 | 選定理由 |
|---------|------|---------|
| フロントエンド | Vite + React 19 + TypeScript + Tailwind CSS v4 | 軽量・高速ビルド |
| Discord Bot | Python 3.14 + discord.py 2.7 | hisho-botと同じスタック |
| ホスティング | GitHub Pages | 無料、GitHub Actionsで自動デプロイ |
| データ保存（Phase 1） | localStorage | 認証不要の個人利用 |
| 問題データ管理 | JSONファイル（hisho-bot内が正典） | シンプル、git管理可能 |

---

## 3. 設計方針（レビュー指摘を反映）

- **Repository Pattern / DI は不使用** — Phase 1では過剰設計（YAGNI）。シンプルなfetch関数で実装
- **Bot の2問と Web の10問は独立** — 共有状態なし。Phase 1の意図的な割り切り
- **JST日付処理** — `toLocaleDateString('sv-SE', {timeZone: 'Asia/Tokyo'})` でUTC/JSTズレを防止
- **JSONロード失敗時のエラー画面** — 白い画面にしない
- **重複フィルタは `Set<string>` でID比較** — オブジェクト参照比較のバグを回避
- **正解はフロントに含まれる** — Phase 1個人利用では許容。Phase 2でサーバーサイド採点に移行

---

## 4. データフロー（Phase 1）

```
[問題データの正典]
hisho-bot/data/quiz/*.json
    │
    │ data/sync_to_web.sh（手動実行）
    ▼
web/public/data/*.json
    │
    │ git push → GitHub Actions
    ▼
GitHub Pages CDN
    │
    │ fetch (import.meta.env.BASE_URL + 'data/...')
    ▼
ブラウザ → useQuiz.ts で選出 → localStorage に回答記録
```

```
[Discord Bot]
bot/main.py → 毎朝7:00チェック
    │
    │ quiz_store.py → hisho-bot/data/quiz/*.json を直接読み込み
    ▼
Discord チャンネルに投稿
    ├── 🏛️ 琴平町クイズ 1問（Embed + 4択ボタン）
    ├── 🔤 英単語クイズ 1問（Embed + 4択ボタン）
    └── 📝 残り8問はWebで！ → URL（テキストメッセージ）
```

---

## 5. Discord Bot 投稿フォーマット

### 琴平町クイズ（1メッセージ）
- Embed: タイトル「🏛️ 琴平町クイズ」、問題文
- View: A/B/C/D ボタン（`SingleAnswerView`）
- ボタン押下 → ephemeral で正解/不正解 + 解説

### 英単語クイズ（1メッセージ）
- Embed: タイトル「🔤 英単語クイズ ・ 英→日」、問題文
- View: A/B/C/D ボタン

### Webリンク（1メッセージ）
- テキスト: `📝 **残り8問はWebで！** → https://b-daman.github.io/kotohira-quiz/`

### Bot再起動対応
- `PersistentTeaserView` で custom_id ベースのインタラクション処理
- Bot再起動後も過去のボタンが動作する

---

## 6. 問題データ

| 種別 | 問題数 | カテゴリ | 1日消費 | 持ち日数 |
|------|--------|---------|---------|---------|
| 琴平町クイズ | 498問（2問無効化済み） | shrine, history, theater, event, geography, gourmet, tourism, architecture, life, modern | 5問 | 約100日 |
| 英単語クイズ | 500問 | 感情, 日常動作, コミュニケーション, 描写, 仕事, 旅行, 食/健康, 抽象, 家庭, 天気, 買物, 関係, 技術, 教育, 感情状態, 身体, 時間, 形容詞 | 5問 | 100日 |

### 問題品質に関する既知の課題
- konpie-bot ナレッジベース由来の問題はAI生成のため、事実確認が不十分な可能性がある
- 例: 「こんぴらビール」は存在しない（正しくは「こんぴら麦酒」2008年製造終了、「呑象ブリューイング」2023年開業）
- 無効化済み: kotohira_070, kotohira_477

### 問題データスキーマ
**琴平クイズ**: `{id, category, difficulty, question, choices[], answer, explanation, source, reviewed, enabled}`
**英単語**: `{id, level, pattern, question, choices[], answer, explanation, word, pronunciation, reviewed, enabled}`

---

## 7. 運用手順

### 問題データ更新時
1. `hisho-bot/data/quiz/*.json` を編集
2. `cd kotohira-quiz && bash data/sync_to_web.sh`
3. `git add web/public/data/ && git commit && git push`
4. GitHub Actionsが自動デプロイ

### Bot 管理
- タスクスケジューラ名: `kotohira-quiz-bot`
- 起動: `Start-ScheduledTask -TaskName 'kotohira-quiz-bot'`
- 停止: `Stop-ScheduledTask -TaskName 'kotohira-quiz-bot'`
- ログ: コンソール出力（タスクスケジューラのログから確認）

### 障害時
| シナリオ | 影響 | 対応 |
|---------|------|------|
| GitHub Pages ダウン | Webクイズ不可。Bot は独立して動作 | GitHub Status確認、待機 |
| Bot クラッシュ | 朝の投稿なし。Web は独立して動作 | タスクスケジューラから再起動 |
| 問題JSON破損 | Web: エラー画面表示。Bot: 投稿失敗 | hisho-botの正典データから再コピー |

---

## 8. hisho-bot との関係

- hisho-bot の `src/cogs/_daily_quiz.py.disabled` — 無効化済み（`_` プレフィクスで自動ロード対象外）
- hisho-bot の `src/utils/quiz_store.py` — 残存（他のCogからは使われていないが、問題データ管理ツールとして利用可能）
- 問題データの正典は引き続き `hisho-bot/data/quiz/` に置く
- kotohira-quiz-bot は環境変数 `QUIZ_DATA_DIR` で hisho-bot のデータを直接参照

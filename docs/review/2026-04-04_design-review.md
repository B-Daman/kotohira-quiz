# デザインレビュー: kotohira-quiz アーキテクチャ設計書

作成日: 2026-04-04
レビュワー: Reviewer Agent
対象: `docs/plan/2026-04-04_architecture.md` + `docs/research/2026-04-04_tech-research.md`

---

## 総評

全体として調査・設計の質は高い。フェーズ分割の考え方・ホスティング選定・OAuthセキュリティ設計は理にかなっている。
一方で、**Phase 1 に持ち込みすぎている抽象化**と、**設計書が「実装が1箇所変えるだけ」と断言している箇所への過信**が主な懸念点。

---

## 問題一覧

### [S] Phase 1 への Repository Pattern 導入は YAGNI 違反

**問題の詳細**

設計書の最大の判断事項「`di.ts` 1ファイル変えれば Phase2 移行完了」という主張を支えるために、Phase 1 から Repository Pattern + DI + Service Layer という本格的な抽象化層を導入している。しかし実際の Phase 1 の要件は「個人が毎日10問解いてスコアを見る」だけであり、この複雑さは正当化されない。

**実際の影響範囲（「1ファイルだけ」は本当か？）**

`di.ts` 1行変更で済む、という主張は不完全。Phase 2 では以下の追加変更が必要になる:

| 変更箇所 | 内容 |
|---------|------|
| `web/src/di.ts` | リポジトリ差し替え（1行変更、これは本当） |
| `web/src/repositories/api/ApiQuestionRepository.ts` | **新規ファイル追加**（既存コードの変更はないが追加は必要） |
| `web/src/repositories/api/ApiScoreRepository.ts` | **新規ファイル追加** |
| `web/src/pages/` | ログイン・コールバック画面の**新規追加** |
| `web/src/hooks/useAuth.ts` | 認証フックの**新規追加** |
| 環境変数 | `VITE_API_BASE_URL` 等の追加。ビルド設定の変更が必要 |
| Cloudflare Pages 設定 | Workers バインディング、D1 バインディングの設定追加 |
| デプロイ設定 | `wrangler.toml` の新規作成 |
| `bot/src/` | 回答記録を API に送信する処理の追加 |

「di.ts 1ファイルだけ変える」は**データ取得ロジックだけに限定した話**であり、認証・インフラ・Bot 連携が加わると実態は大幅に異なる。設計書・調査書とも「フロントのビルド設定、環境変数、デプロイ設定」への言及がない点が抜け漏れ。

**改善提案**

Phase 1 は Repository Pattern を使わず、シンプルな fetch 関数で実装する。

```typescript
// Phase 1 の実装（これで十分）
// web/src/data/questions.ts
export async function getEnabledQuestions(): Promise<Question[]> {
  const [kotohira, english] = await Promise.all([
    fetch('/data/kotohira_questions.json').then(r => r.json()),
    fetch('/data/english_questions.json').then(r => r.json()),
  ]);
  return [...kotohira.questions, ...english.questions].filter(q => q.enabled && q.reviewed);
}
```

Phase 2 で API 移行するときに「リファクタリングして Repository Pattern を導入する」でよい。
Phase 2 では他にも大量の新規ファイルが必要になるのだから、このリファクタリングコストは誤差に過ぎない。

---

### [A] Bot が選出する「2問」と Web の「10問」の関係が未定義

**問題の詳細**

設計書には「Discord Bot: 毎朝2問投稿 + "詳しくはWebで" リンク付き」と書いてあるが、この 2問 と Web の 10問 の関係が明記されていない。

- Bot が選出した 2問 は Web の 10問 の部分集合なのか？
- それとも Bot と Web は独立して問題を選出するのか？
- Web で今日の回答を終えた後にBotの2問に回答することは想定されているか？

Phase 1 では Bot/Web の履歴が独立しているため、「Bot で正解した問題を Web でも出題される」「Web で10問全部やった後にBotで出題される」という状況が発生する。これがバグなのか仕様なのかを決めておく必要がある。

**改善提案**

設計書に明示的に定義を追記する。推奨は「Bot と Web は独立した出題」とする仕様（Phase 1 はシンプルに割り切る）。

---

### [A] `quiz_history.json` の管理主体が未定義

**問題の詳細**

現在の設計では:
- `bot/data/quiz/quiz_history.json` は Bot が管理する
- Web の回答履歴は `localStorage` に保存

しかし monorepo 構成では `bot/data/quiz/` がリポジトリ内に存在するため、Bot がファイルを更新するたびに git の作業ツリーが汚れる（untracked changes が常に発生する）。

`.gitignore` で `quiz_history.json` を除外するか、Bot が書き込む場所をリポジトリ外に変更しないと、`git status` が常に dirty になり Cloudflare Pages の自動デプロイが意図しないタイミングで走る可能性がある。

**改善提案**

`quiz_history.json` を `.gitignore` に追加する。または Bot の書き込み先を `kotohira-quiz` リポジトリ外のパス（例: ホームディレクトリ下）に変更する。

---

### [A] データスキーマの互換性保証がない

**問題の詳細**

`data/schemas/question.schema.json` が設計には含まれているが、これを実際に検証に使うフローが書かれていない。

Phase 1 から Phase 2 へ移行する際、Bot 側の `kotohira_questions.json` が Cloudflare D1 に移行するが:
- JSON スキーマと D1 のテーブル定義の整合性を誰が管理するか
- Bot 側で新しいフィールドを追加した場合、Web 側への影響を検知する手段がない

**改善提案**

Phase 1 では `sync_to_web.sh` 実行時に JSON スキーマバリデーションを走らせる（`ajv-cli` 等）。1行追加するだけでデータ不整合を早期検知できる。

---

### [B] 問題の正解がフロントエンドに丸見え

**問題の詳細**

Phase 1 では問題 JSON をそのまま `public/data/` に配置して CDN 配信する。`answer: "B"` がブラウザから直接取得可能。

個人利用・小規模なら許容範囲だが、Phase 2 でランキングを導入する際に「正解を先に取得してから回答する」チートが可能になる。

**改善提案**

Phase 1 では割り切って許容する（個人利用のため）。ただし Phase 2 設計書に「正解はサーバーサイドで検証する」という制約を明記しておく。Phase 2 では API が正解を返さず、回答を受け取った Workers 側で採点する設計にする。

---

### [B] 「1日分のクイズ」のリセットタイミングが未定義

**問題の詳細**

```typescript
const today = new Date().toISOString().split('T')[0];
```

このコードは UTC での日付を使用する。日本時間（JST = UTC+9）では夜9時以降に「翌日」と判定されてしまう。

例: 日本時間 2026-04-04 22:00 → UTC 2026-04-04 13:00 → `today = "2026-04-04"` は正しいが、
日本時間 2026-04-05 00:30 → UTC 2026-04-04 15:30 → `today = "2026-04-04"` となり、日本時間では翌日なのに前日扱いになる。

**改善提案**

```typescript
// JST で今日の日付を取得
const today = new Date().toLocaleDateString('sv-SE', { timeZone: 'Asia/Tokyo' });
// 'sv-SE' ロケールは YYYY-MM-DD 形式を返す
```

---

### [B] 障害時の影響範囲が未整理

**問題の詳細**

設計書に障害時の振る舞いが記述されていない。

| 障害シナリオ | 影響 |
|------------|------|
| Cloudflare Pages がダウン | Web クイズができない。Bot は独立して動作継続 |
| Discord Bot がクラッシュ | Bot の投稿なし。Web は独立して動作継続 |
| `public/data/*.json` のデータが壊れている | Web 側でクイズが開始できない（エラー画面が必要） |

特に「問題 JSON のロードに失敗した場合」の UI エラーハンドリングが実装ゼロの場合、白い画面（ホワイトスクリーン）が表示される可能性がある。

**改善提案**

JSON フェッチの失敗時に「問題データを読み込めませんでした。しばらく後に再試行してください。」というエラー表示を実装する。これは5行程度の追加で対処できる。

---

### [C] Discord → Web の遷移摩擦

**問題の詳細**

Bot の投稿から Web に誘導する UX について設計書に記述がない。「詳しくはWebで」と書いても、URL をタップしてブラウザが開き、ログイン（Phase 2 以降）して…という手順は意外と離脱ポイントになる。

**改善提案（Phase 1 時点で考慮する価値あり）**

- Web の URL を短く・覚えやすくする（例: `kotohira-quiz.pages.dev` ではなくカスタムドメイン）
- Bot のメッセージに毎日の直リンク（当日のクイズ画面への URL）を含める
- Phase 2 では Discord の埋め込みボタンを活用する

---

### [C] `QuizService.selectQuestions()` の重複問題フィルタが不完全

**問題の詳細**

研究レポートの実装コードにある `spreadByCategory` 内で:

```typescript
const candidates = byCategory[cat].filter(q => !selected.includes(q));
```

`selected.includes(q)` はオブジェクト参照比較のため、同じ内容のオブジェクトでも別参照なら重複扱いにならない。`getAll()` が毎回新しいオブジェクトを返す実装だと常に重複チェックが機能しない。

**改善提案**

```typescript
const selectedIds = new Set(selected.map(q => q.id));
const candidates = byCategory[cat].filter(q => !selectedIds.has(q.id));
```

---

## 良い点

- **フェーズ分割の考え方は正しい**: Phase 1 で認証・DB・ランキングを作らない判断は YAGNI に沿っている
- **Cloudflare Pages 選定は妥当**: 帯域無制限・Cold Start なし・Workers との統合という選定理由は合理的
- **OAuth2 + PKCE の設計は正しい**: `client_secret` をバックエンドのみに限定し、`httpOnly Cookie` でセッション管理する設計はセキュリティ要件を満たしている。`state` による CSRF 対策も明記されている
- **Bot との履歴分離を Phase 1 では割り切る判断**: 無理に統合しようとしない割り切りは正しい
- **問題データの正典（single source of truth）を `bot/data/quiz/` に定める**: 二重管理を避けている

---

## 優先改善アクション

| 優先度 | アクション |
|-------|----------|
| S | Phase 1 の Repository Pattern を除去してシンプルな関数に置き換える |
| S | 「di.ts 1ファイル変更で移行完了」という記述を実際の変更範囲（環境変数・デプロイ設定・新規ファイル等含む）に訂正する |
| A | Bot の2問と Web の10問の関係を設計書に明記する |
| A | `quiz_history.json` を `.gitignore` に追加する方針を明記する |
| A | `sync_to_web.sh` にスキーマバリデーションを追加する |
| B | `new Date()` の UTC/JST 問題を修正する（`sv-SE` ロケール使用） |
| B | JSON ロード失敗時のエラーハンドリングを実装に含める |

# 技術調査レポート: kotohira-quiz Webアプリ

作成日: 2026-04-04
調査者: Researcher Agent
対象プロジェクト: kotohira-quiz (Discord Bot → Web SPA 拡張)

---

## 1. クイズWebアプリのデータ取得層パターン

### 背景
現在の hisho-bot は `QuizStore` クラスで JSON ファイルを直接読み書きしている。
Web SPA では Phase1 で localStorage、Phase2 以降で API に移行することを想定する。

### 推奨: Repository Pattern + Service Layer

```typescript
// インターフェース定義（変更不要な部分）
interface Question {
  id: string;
  category: string;
  difficulty: 'easy' | 'medium' | 'hard';
  question: string;
  choices: string[];  // ["A. ...", "B. ...", "C. ...", "D. ..."]
  answer: string;     // "A" | "B" | "C" | "D"
  explanation: string;
  enabled: boolean;
  reviewed: boolean;
}

interface QuizHistory {
  date: string;       // "YYYY-MM-DD"
  questionId: string;
  selected: string;
  correct: boolean;
}

interface UserStats {
  total: number;
  correct: number;
  streak: number;
  accuracy: number;
}

// Repository インターフェース（データソースを抽象化）
interface IQuestionRepository {
  getAll(): Promise<Question[]>;
  getById(id: string): Promise<Question | null>;
  getEnabled(): Promise<Question[]>;
}

interface IHistoryRepository {
  getUserHistory(userId: string): Promise<QuizHistory[]>;
  saveAnswer(userId: string, entry: QuizHistory): Promise<void>;
  getTodayAnswered(userId: string): Promise<string[]>; // question IDs
}

// 実装A: localStorage（Phase1）
class LocalStorageQuestionRepository implements IQuestionRepository {
  private readonly KEY = 'kotohira_questions';

  async getAll(): Promise<Question[]> {
    const raw = localStorage.getItem(this.KEY);
    return raw ? JSON.parse(raw).questions : [];
  }

  async getById(id: string): Promise<Question | null> {
    const all = await this.getAll();
    return all.find(q => q.id === id) ?? null;
  }

  async getEnabled(): Promise<Question[]> {
    const all = await this.getAll();
    return all.filter(q => q.enabled && q.reviewed);
  }
}

// 実装B: API（Phase2 以降。インターフェースは同一）
class ApiQuestionRepository implements IQuestionRepository {
  constructor(private baseUrl: string) {}

  async getAll(): Promise<Question[]> {
    const res = await fetch(`${this.baseUrl}/api/questions`);
    return res.json();
  }

  async getById(id: string): Promise<Question | null> {
    const res = await fetch(`${this.baseUrl}/api/questions/${id}`);
    return res.ok ? res.json() : null;
  }

  async getEnabled(): Promise<Question[]> {
    const res = await fetch(`${this.baseUrl}/api/questions?enabled=true`);
    return res.json();
  }
}

// Service Layer（ビジネスロジック。リポジトリ実装に依存しない）
class QuizService {
  constructor(
    private questionRepo: IQuestionRepository,
    private historyRepo: IHistoryRepository,
  ) {}

  async selectQuestions(count: number, userId: string): Promise<Question[]> {
    const eligible = await this.questionRepo.getEnabled();
    const todayAnswered = await this.historyRepo.getTodayAnswered(userId);
    const fresh = eligible.filter(q => !todayAnswered.includes(q.id));
    return this.spreadByCategory(fresh.length >= count ? fresh : eligible, count);
  }

  private spreadByCategory(pool: Question[], count: number): Question[] {
    // カテゴリ分散ロジック（quiz_store.py の _select_with_category_spread と同等）
    const byCategory = pool.reduce((acc, q) => {
      (acc[q.category] ??= []).push(q);
      return acc;
    }, {} as Record<string, Question[]>);

    const selected: Question[] = [];
    const catCount: Record<string, number> = {};
    const categories = Object.keys(byCategory).sort(() => Math.random() - 0.5);

    while (selected.length < count) {
      let added = false;
      for (const cat of categories) {
        if (selected.length >= count) break;
        if ((catCount[cat] ?? 0) >= 2) continue;
        const candidates = byCategory[cat].filter(q => !selected.includes(q));
        if (candidates.length > 0) {
          selected.push(candidates[Math.floor(Math.random() * candidates.length)]);
          catCount[cat] = (catCount[cat] ?? 0) + 1;
          added = true;
        }
      }
      if (!added) break;
    }
    return selected;
  }
}
```

### 変更が必要な箇所 vs 不要な箇所

| 箇所 | Phase1→Phase2 での変更 |
|------|----------------------|
| `IQuestionRepository` インターフェース | **不要**（抽象化済み） |
| `IHistoryRepository` インターフェース | **不要** |
| `QuizService` のビジネスロジック | **不要** |
| `LocalStorageQuestionRepository` | 削除（使わなくなる） |
| `ApiQuestionRepository` | **新規追加**（実装を差し替え） |
| コンポーネント側の DI 設定 | 1箇所のみ変更 |

**結論**: Repository Pattern を使えば、SPA コンポーネントは一切修正不要。`QuizService` のコンストラクタに渡すリポジトリ実装を差し替えるだけで localStorage → API 移行が完結する。

---

## 2. Discord OAuth2 認証フロー

### Authorization Code Grant + PKCE の具体的ステップ

SPA は public client（クライアントシークレットを安全に保持できない）のため、**PKCE 必須**。

```
1. ユーザーが「Discordでログイン」をクリック

2. フロントエンド: code_verifier（ランダム文字列）を生成
   code_challenge = BASE64URL(SHA256(code_verifier))

3. フロントエンド: Discordの認可エンドポイントにリダイレクト
   https://discord.com/oauth2/authorize
     ?client_id=YOUR_CLIENT_ID
     &redirect_uri=https://your-app.com/callback
     &response_type=code
     &scope=identify guilds
     &state=RANDOM_STATE_VALUE  (CSRF対策)
     &code_challenge=xxx
     &code_challenge_method=S256

4. ユーザー: Discord でログイン・権限承認

5. Discord: redirect_uri に認可コードを付けてリダイレクト
   https://your-app.com/callback?code=AUTH_CODE&state=xxx

6. フロントエンド: state を検証（CSRF対策）

7. バックエンド（API Route / Function）: トークン交換
   POST https://discord.com/api/oauth2/token
   {
     grant_type: "authorization_code",
     code: AUTH_CODE,
     redirect_uri: "...",
     client_id: "...",
     client_secret: "...",  ← バックエンドでのみ使用
     code_verifier: "..."
   }
   → { access_token, refresh_token, token_type, expires_in }

8. バックエンド: access_token を httpOnly Cookie にセット
   Set-Cookie: session=...; HttpOnly; Secure; SameSite=Lax

9. フロントエンド: Cookieが自動付与されるため、JSからトークンへアクセス不可
```

### 必要なスコープ

| スコープ | 用途 |
|---------|------|
| `identify` | ユーザーID・ユーザー名・アバター取得（最小限） |
| `guilds` | ユーザーが参加しているサーバー一覧（メンバー確認用） |
| `guilds.members.read` | 特定サーバーのメンバー情報（ロール確認等。要申請の場合あり） |

**最小構成**: `identify` のみで十分（Phase1）。

### トークンの保存場所の選択

| 方式 | XSS耐性 | CSRF耐性 | 実装難易度 | 推奨 |
|------|---------|---------|----------|------|
| httpOnly Cookie | **強** | 中（SameSite=Laxで対応） | バックエンド必要 | **本番推奨** |
| localStorage | 弱（JSから読み取り可） | 強 | 簡単 | Phase1のみ許容 |
| メモリ（変数） | 強 | 強 | 中 | リロードで消える |

**結論**: Phase1（ユーザー認証なし）はトークン不要。Phase2でログイン実装する場合は **httpOnly Cookie + バックエンドでのトークン交換**が必須。localStorage への access_token 保存は本番では行わない。

### Discordアプリの設定に必要なもの

Discord Developer Portal での設定:
1. `OAuth2 > Redirects` に `https://your-app.com/callback` を追加
2. Client ID を控える（公開情報、フロントに埋め込み可）
3. Client Secret を控える（**バックエンドのみ**で使用、フロントに絶対露出しない）
4. Bot Token（既存の hisho-bot のもの）とは別管理

---

## 3. ホスティング比較

### 無料枠比較表

| 項目 | Vercel | Cloudflare Pages | Netlify |
|------|--------|-----------------|---------|
| **静的サイト** | 無制限 | 無制限 | 無制限 |
| **帯域幅** | 100 GB/月 | **無制限** | 100 GB/月 |
| **Serverless Functions** | 100K req/月、10秒タイムアウト | **無制限**（Workers、CPU時間制限あり） | 125K req/月、10秒タイムアウト |
| **ビルド時間** | 6,000分/月 | 500ビルド/月 | 300分/月 |
| **Cold Start** | 数百ms〜数秒 | **ほぼゼロ**（Edge Runtime） |  数百ms〜数秒 |
| **カスタムドメイン** | 無料 | 無料 | 無料 |
| **商用利用** | 可 | 可 | 可 |

### 静的サイト → API追加時の移行コスト

**Vercel**:
- `api/` ディレクトリにファイルを追加するだけ。移行コスト低。
- Next.js との親和性が高い。
- 無料枠の関数制限（100K/月）は小規模プロジェクトで問題なし。

**Cloudflare Pages**:
- `functions/` ディレクトリに追加。Workers 互換。
- 帯域無制限が最大の強み。
- Node.js 互換レイヤーあり（一部制限）。Discord OAuth2 のコールバックも実装可能。

**Netlify**:
- `netlify/functions/` に配置。AWS Lambda 互換。
- ビルド時間制限（300分/月）が3つの中で最も厳しい。
- 移行コストは低いが無料枠が最も限られる。

**推奨**: **Cloudflare Pages**。帯域無制限・Cold Start ほぼゼロ・Workers での Discord OAuth2 実装が可能。日本からのレイテンシも良好。小規模プロジェクトでは無料枠を超えない。

---

## 4. Bot ↔ Web データ共有方式

### 各方式の比較

#### A. ビルド時にJSONを同梱（静的）

```
hisho-bot/data/quiz/kotohira_questions.json
    ↓ ビルド時にコピー
kotohira-quiz/public/data/questions.json
    ↓ SPA からフェッチ
```

| 項目 | 内容 |
|------|------|
| **メリット** | 実装最小。インフラ不要。CDNで高速配信 |
| **デメリット** | Bot側で問題を追加しても即時反映されない。手動ビルドが必要 |
| **Phase1での変更点** | なし（静的ファイルのまま） |
| **Phase2での変更点** | 廃止してAPIに移行 |

**Phase1に最適**。問題データは頻繁に変わらないため許容範囲。

#### B. Git submodule / monorepo で共有

```
kotohira-quiz/ (monorepo)
├── packages/quiz-data/   ← hisho-botのquiz jsonを共有
├── apps/web/             ← SPA
└── apps/bot/             ← hisho-bot (or submodule)
```

| 項目 | 内容 |
|------|------|
| **メリット** | 単一リポジトリで管理。型定義を共有可能 |
| **デメリット** | 既存の hisho-bot リポジトリ構造を変更する必要がある。Git submodule は運用が煩雑 |
| **Phase1での変更点** | リポジトリ移行コストが高い |
| **Phase2での変更点** | monorepoにAPIサーバーを追加 |

既存 hisho-bot を触らずに済む方式が望ましいため、**現時点では非推奨**。

#### C. APIサーバー経由

```
hisho-bot → DB/JSON → API Server → SPA
                         ↑
                      (別サーバー or Cloudflare Workers)
```

| 項目 | 内容 |
|------|------|
| **メリット** | リアルタイム反映。認証・ランキング・統計も実装可能 |
| **デメリット** | Phase1では過剰設計。サーバー管理コスト発生 |
| **Phase1での変更点** | 不要 |
| **Phase2での変更点** | Cloudflare Workers / Vercel API Routes で実装 |

**Phase2以降で採用**。

#### D. CDN/S3にJSONを配置

```
hisho-bot が JSON更新時 → GitHub Actions → S3/R2 にアップロード
                                                ↓
                                    SPA がフェッチ（CDN経由）
```

| 項目 | 内容 |
|------|------|
| **メリット** | 準リアルタイム更新（数分ラグ）。APIサーバー不要 |
| **デメリット** | GitHub Actions または Bot側にアップロードロジックが必要 |
| **Phase1での変更点** | Bot側に R2/S3 アップロード処理を追加 |
| **Phase2での変更点** | APIに段階移行 |

**現実的な中間策**。Phase1.5として検討価値あり。

### 推奨フェーズ別戦略

```
Phase1: 方式A（ビルド時JSON同梱）
  → 実装コストゼロ。問題数が少ない間は問題なし

Phase1.5（問題更新頻度が上がったら）: 方式D（Cloudflare R2 + GitHub Actions）
  → hisho-bot がJSON更新 → Actions が R2 に自動プッシュ → SPA がフェッチ

Phase2（ユーザー認証・ランキング実装時）: 方式C（Cloudflare Workers API）
  → Cloudflare Pages + Workers で完結
```

---

## 5. 既存 kotohira-quiz プロジェクトの現状確認

### ディレクトリ構造

```
C:/Users/user/hisho-bot/
├── src/
│   ├── cogs/
│   │   └── daily_quiz.py          # Discord Bot Cog（クイズ出題・ボタン処理）
│   └── utils/
│       └── quiz_store.py          # データアクセス層（問題バンク・履歴管理）
└── data/quiz/
    ├── kotohira_questions.json    # 琴平町クイズ問題バンク
    ├── english_questions.json     # 英単語クイズ問題バンク
    └── quiz_history.json          # 出題履歴・ユーザー回答記録

C:/Users/user/kotohira-quiz/       # ← 現在は空（新規プロジェクト）
```

### 問題データ構造（kotohira_questions.json）

```json
{
  "version": 1,
  "questions": [
    {
      "id": "kotohira_001",
      "category": "shrine",
      "difficulty": "easy",
      "question": "金刀比羅宮の通称は何ですか？",
      "choices": ["A. おいなりさん", "B. こんぴらさん", "C. てんじんさん", "D. はちまんさん"],
      "answer": "B",
      "explanation": "...",
      "source": "konpie-bot/knowledge_base/shrine",
      "reviewed": true,
      "enabled": true
    }
  ]
}
```

確認されたカテゴリ: `shrine`（神社関連）。他にも `history`, `food`, `nature` 等が存在する可能性がある。

### QuizStore の選出アルゴリズム（quiz_store.py）

| 機能 | 詳細 |
|------|------|
| **フィルタリング** | `reviewed: true` かつ `enabled: true` のみ対象 |
| **クールダウン** | 直近30日間に出題された問題は除外（`quiz_history.json` 参照） |
| **カテゴリ分散** | 各カテゴリ最大2問、ラウンドロビンで選出 |
| **フォールバック** | 未出題問題が不足した場合、全eligible問題から選出 |
| **英単語パターン** | `en_to_ja` と `ja_to_en` を交互に混合 |

**Web SPAへの移植メモ**:
- `select_questions()` → `QuizService.selectQuestions()` として TypeScript で再実装（セクション1参照）
- クールダウン機能は Phase1 では簡略化可（localStorage に当日回答済みIDを保存するだけで十分）
- ランキングデータ（`get_ranking()`）は Phase2 以降でサーバーサイドに移行

### 課題

1. `kotohira-quiz/` は現在空。プロジェクト初期化が必要
2. 問題データは hisho-bot 側にのみ存在。Web SPA へのデータ共有方式を決める必要あり（セクション4参照）
3. Bot と Web で回答履歴が分離する問題（Phase2 で統合 API を設計する際に解決）

---

## まとめ・推奨構成（Phase1）

| 決定事項 | 推奨 | 理由 |
|---------|------|------|
| データ取得抽象化 | Repository Pattern | Phase1→2の移行コストを最小化 |
| Phase1データソース | ビルド時JSON同梱（方式A） | 実装ゼロ、インフラ不要 |
| Phase2データソース | Cloudflare Workers API（方式C） | 帯域無制限、Cold Startなし |
| ホスティング | Cloudflare Pages | 帯域無制限、Workers連携 |
| Discord OAuth2 | PKCE対応、トークンはhttpOnly Cookie | セキュリティ要件 |
| Phase1認証 | なし（匿名プレイ） | YAGNI原則 |

---

*参考URL*:
- [Discord OAuth2 Documentation](https://discord.com/developers/docs/topics/oauth2)
- [Vercel vs Cloudflare Pages vs Netlify 2025 Comparison](https://www.digitalapplied.com/blog/vercel-vs-netlify-vs-cloudflare-pages-comparison)
- [Cloudflare vs Vercel vs Netlify: Edge Performance 2026](https://dev.to/dataformathub/cloudflare-vs-vercel-vs-netlify-the-truth-about-edge-performance-2026-50h0)
- [Auth0: Token Storage Best Practices](https://auth0.com/docs/secure/security-guidance/data-security/token-storage)
- [PKCE in OAuth 2.0](https://www.authgear.com/post/pkce-in-oauth-2-0-how-to-protect-your-api-from-attacks)
- [Repository Pattern with TypeScript](https://blog.logrocket.com/exploring-repository-pattern-typescript-node/)

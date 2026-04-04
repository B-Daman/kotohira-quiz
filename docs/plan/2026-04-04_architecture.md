# アーキテクチャ設計書: kotohira-quiz

作成日: 2026-04-04
設計者: Planner Agent
対象プロジェクト: kotohira-quiz (Webクイズアプリ + Discord Bot)

---

## 1. プロジェクト構成（ディレクトリ構造）

### monorepo構成

```
kotohira-quiz/
├── web/                          # フロントエンド SPA
│   ├── src/
│   │   ├── components/           # UIコンポーネント（Quiz, Result, Stats等）
│   │   ├── repositories/         # データ取得層（Repository実装）
│   │   │   ├── interfaces.ts     # IQuestionRepository / IScoreRepository
│   │   │   ├── localStorage/     # Phase1実装
│   │   │   └── api/              # Phase2実装（差し替え用）
│   │   ├── services/             # ビジネスロジック（QuizService等）
│   │   ├── hooks/                # Reactカスタムフック
│   │   ├── pages/                # ページコンポーネント
│   │   └── di.ts                 # 依存性注入（リポジトリの切り替えはここだけ）
│   ├── public/
│   │   └── data/                 # Phase1: ビルド時JSON同梱
│   │       ├── kotohira_questions.json
│   │       └── english_questions.json
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   └── package.json
│
├── bot/                          # Discord Bot
│   ├── src/
│   │   ├── cogs/
│   │   │   └── daily_quiz.py     # クイズ出題・ボタン処理（hisho-botから移植）
│   │   └── utils/
│   │       └── quiz_store.py     # データアクセス層（hisho-botから移植）
│   ├── data/quiz/                # Phase1: JSONファイル（正典データ）
│   │   ├── kotohira_questions.json
│   │   ├── english_questions.json
│   │   └── quiz_history.json
│   └── requirements.txt
│
├── data/                         # 共有データ・型定義
│   ├── schemas/
│   │   └── question.schema.json  # JSONスキーマ（Bot・Webで共通検証）
│   └── scripts/
│       └── sync_to_web.sh        # bot/data → web/public/data のコピースクリプト
│
└── docs/
    ├── research/
    └── plan/
```

### 各ディレクトリの責務

| ディレクトリ | 責務 |
|------------|------|
| `web/` | ブラウザで動作するSPA。UI表示・クイズ進行・スコア保存 |
| `web/src/repositories/` | データソースを抽象化。Phase切り替えの唯一の変更箇所 |
| `web/src/services/` | ビジネスロジック（問題選出・採点）。データソースに依存しない |
| `web/src/di.ts` | リポジトリ実装の注入。Phase1→2の移行時にここだけ書き換える |
| `bot/` | Discord Bot。毎朝クイズ投稿・ボタン回答処理 |
| `bot/data/quiz/` | 問題JSONの正典（single source of truth） |
| `data/` | BotとWebで共有するスキーマ・同期スクリプト |

---

## 2. 技術スタック選定と理由

### フロントエンド

| 技術 | 選定理由 |
|------|---------|
| **Vite** | ビルドが高速。設定が少なく小規模プロジェクトに適切 |
| **React 19** | コンポーネントベースでUIの再利用性が高い。エコシステムが成熟 |
| **TypeScript** | Repository Patternのインターフェース定義に必須。Phase移行時の型安全性を保証 |
| **Tailwind CSS v4** | クラスベースで素早くスタイリング可能。カスタムデザイン不要な局面で最適 |

### Discord Bot

| 技術 | 選定理由 |
|------|---------|
| **Python 3.11+** | 既存のhisho-botがPython製。移植コスト最小化 |
| **discord.py 2.x** | 既存実装で実績あり。Cogシステムでモジュール分離が容易 |

### ホスティング

| 技術 | 選定理由 |
|------|---------|
| **Cloudflare Pages** | 帯域無制限・Cold Startほぼゼロ・Workers連携でPhase2のAPIも同一プラットフォームで完結 |
| **Cloudflare Workers（Phase2）** | Serverless Functionsが無制限リクエスト（CPU時間制限内）。Discord OAuth2コールバックも実装可能 |

---

## 3. フェーズ分割ロードマップ

### Phase 1: 個人利用（今すぐ作るもの）

**作るもの**

- Vite + React + TypeScript + Tailwind のSPAプロジェクト初期化
- 毎日10問クイズ画面（琴平5問 + 英単語5問）
- 問題データはビルド時に `web/public/data/` に同梱（静的JSON）
- 回答・スコアはlocalStorageに保存（ユーザー識別なし = 匿名）
- クイズ進行ロジック（問題選出・採点・解説表示）
- 当日の回答履歴（重複出題防止）
- シンプルな結果画面（今日の正答率）
- Discord Bot: 毎朝2問投稿 + "詳しくはWebで" リンク付き

**作らないもの**

- ユーザー認証（ログイン・サインアップ）
- バックエンドAPI・DBサーバー
- ランキング・他ユーザーとの比較
- 問題管理画面

**Phase 1の完成条件**

- `npm run build` → `web/dist/` が生成される
- Cloudflare Pages に `git push` でデプロイされる
- ブラウザで毎日10問を解いてスコアが表示される

---

### Phase 2: 複数ユーザー対応

**Phase 1からの変更箇所**

| 変更箇所 | 変更内容 |
|---------|---------|
| `web/src/di.ts` | `LocalStorageQuestionRepository` → `ApiQuestionRepository` に差し替え（1行変更） |
| `web/src/repositories/api/` | `ApiQuestionRepository` / `ApiHistoryRepository` を新規追加 |
| `web/src/pages/` | ログイン画面・コールバック画面を追加 |
| `web/src/hooks/useAuth.ts` | 認証状態管理フックを追加 |
| `bot/src/` | 回答記録をAPIに送信する処理を追加 |

**新規追加するもの**

- Discord OAuth2 + PKCE 認証フロー
- Cloudflare Workers APIサーバー（`/api/questions`, `/api/history`, `/api/auth/callback`）
- DB: Cloudflare D1（SQLite互換）またはKV（シンプルなKey-Value）
- ユーザー別スコア保存・表示

---

### Phase 3: コミュニティ機能

**追加で必要なもの**

- ランキング画面（日次・週次・累計）
- 実績バッジシステム（連続7日達成 等）
- Bot連携: 毎朝ランキング上位をDiscordに投稿
- Cloudflare D1へのデータ移行（KVではランキング集計が困難な場合）

---

## 4. データ取得層の抽象化設計

### インターフェース定義

```typescript
// web/src/repositories/interfaces.ts

export interface Question {
  id: string;
  category: string;
  difficulty: 'easy' | 'medium' | 'hard';
  question: string;
  choices: string[];   // ["A. ...", "B. ...", "C. ...", "D. ..."]
  answer: string;      // "A" | "B" | "C" | "D"
  explanation: string;
  enabled: boolean;
  reviewed: boolean;
}

export interface QuizHistory {
  date: string;        // "YYYY-MM-DD"
  questionId: string;
  selected: string;
  correct: boolean;
}

export interface UserStats {
  total: number;
  correct: number;
  streak: number;
  accuracy: number;
}

// 問題データ取得の抽象インターフェース
export interface IQuestionRepository {
  getAll(): Promise<Question[]>;
  getById(id: string): Promise<Question | null>;
  getEnabled(): Promise<Question[]>;
}

// 回答履歴・スコアの抽象インターフェース
export interface IScoreRepository {
  getUserHistory(userId: string): Promise<QuizHistory[]>;
  saveAnswer(userId: string, entry: QuizHistory): Promise<void>;
  getTodayAnswered(userId: string): Promise<string[]>;  // 回答済み問題ID
  getUserStats(userId: string): Promise<UserStats>;
}
```

### Phase 1: localStorage実装

```typescript
// web/src/repositories/localStorage/LocalStorageQuestionRepository.ts

import type { IQuestionRepository, Question } from '../interfaces';

export class LocalStorageQuestionRepository implements IQuestionRepository {
  // 問題データはビルド時にpublic/data/に同梱 → fetch()で取得
  private cache: Question[] | null = null;

  async getAll(): Promise<Question[]> {
    if (this.cache) return this.cache;
    const [kotohira, english] = await Promise.all([
      fetch('/data/kotohira_questions.json').then(r => r.json()),
      fetch('/data/english_questions.json').then(r => r.json()),
    ]);
    this.cache = [...kotohira.questions, ...english.questions];
    return this.cache;
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
```

```typescript
// web/src/repositories/localStorage/LocalStorageScoreRepository.ts

import type { IScoreRepository, QuizHistory, UserStats } from '../interfaces';

const HISTORY_KEY = 'kotohira_quiz_history';

export class LocalStorageScoreRepository implements IScoreRepository {
  async getUserHistory(_userId: string): Promise<QuizHistory[]> {
    const raw = localStorage.getItem(HISTORY_KEY);
    return raw ? JSON.parse(raw) : [];
  }

  async saveAnswer(_userId: string, entry: QuizHistory): Promise<void> {
    const history = await this.getUserHistory(_userId);
    history.push(entry);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
  }

  async getTodayAnswered(_userId: string): Promise<string[]> {
    const today = new Date().toISOString().split('T')[0];
    const history = await this.getUserHistory(_userId);
    return history.filter(h => h.date === today).map(h => h.questionId);
  }

  async getUserStats(_userId: string): Promise<UserStats> {
    const history = await this.getUserHistory(_userId);
    const total = history.length;
    const correct = history.filter(h => h.correct).length;
    // streakはlocalStorageで簡易計算
    return { total, correct, streak: 0, accuracy: total > 0 ? correct / total : 0 };
  }
}
```

### Phase 2: API実装（差し替え用）

```typescript
// web/src/repositories/api/ApiQuestionRepository.ts
// インターフェースは同一。コンポーネント側は一切変更不要。

import type { IQuestionRepository, Question } from '../interfaces';

export class ApiQuestionRepository implements IQuestionRepository {
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
```

### 依存性注入（DI）設定

```typescript
// web/src/di.ts
// Phase移行時に変更するのはこのファイルだけ

import { LocalStorageQuestionRepository } from './repositories/localStorage/LocalStorageQuestionRepository';
import { LocalStorageScoreRepository } from './repositories/localStorage/LocalStorageScoreRepository';
// Phase2に移行する場合は↑を↓に差し替えるだけ
// import { ApiQuestionRepository } from './repositories/api/ApiQuestionRepository';
// import { ApiScoreRepository } from './repositories/api/ApiScoreRepository';

import { QuizService } from './services/QuizService';

const questionRepo = new LocalStorageQuestionRepository();
const scoreRepo = new LocalStorageScoreRepository();

export const quizService = new QuizService(questionRepo, scoreRepo);
```

### コンポーネントからの呼び出し例

```typescript
// web/src/hooks/useQuiz.ts
// quizServiceを使う側。リポジトリ実装を知らない。

import { quizService } from '../di';

export function useQuiz(userId: string = 'anonymous') {
  const startQuiz = async () => {
    // Phase1でもPhase2でも同じ呼び出し
    const questions = await quizService.selectQuestions(10, userId);
    return questions;
  };

  const submitAnswer = async (questionId: string, selected: string, correct: boolean) => {
    await quizService.recordAnswer(userId, { questionId, selected, correct });
  };

  return { startQuiz, submitAnswer };
}
```

---

## 5. Discord Bot ↔ Web のデータフロー

### Phase 1: 静的JSON同梱方式

```
[正典データ]
bot/data/quiz/kotohira_questions.json
bot/data/quiz/english_questions.json
         |
         | data/scripts/sync_to_web.sh
         | (手動 or git push時にコピー)
         v
web/public/data/kotohira_questions.json
web/public/data/english_questions.json
         |
         | Vite ビルド時に dist/ に同梱
         v
Cloudflare Pages (CDNエッジ配信)
         |
         | fetch('/data/kotohira_questions.json')
         v
ブラウザ (LocalStorageQuestionRepository)

[回答履歴]
ブラウザ  ─── localStorage ──→ ブラウザ（次回アクセス時に参照）
Discord   ─── quiz_history.json ──→ Bot（次回出題時に参照）
※ Phase1ではBotとWebの履歴は独立。統合しない。
```

### Phase 2: API方式

```
[問題データ]
bot/data/quiz/*.json
         |
         | Bot起動時またはGitHub Actionsで
         v
Cloudflare D1 (DB) または KV
         |
         | GET /api/questions
         v
ApiQuestionRepository → QuizService → ブラウザ

[回答履歴]
ブラウザ ──→ POST /api/history ──→ Cloudflare D1
Discord Bot ──→ POST /api/history ──→ Cloudflare D1
                                           |
                                           | GET /api/stats/:userId
                                           v
                                       ブラウザ (統合スコア表示)
```

---

## 6. 認証追加時のアーキテクチャ（Phase 2）

### Discord OAuth2 + PKCE フロー

```
ユーザー       フロントエンド (SPA)       バックエンド (CF Workers)    Discord API
   |                  |                          |                        |
   |--[ログインクリック]-->|                          |                        |
   |                  |--[code_verifierを生成]      |                        |
   |                  |--[code_challenge作成]       |                        |
   |                  |  (SHA256(code_verifier))   |                        |
   |                  |                            |                        |
   |<--[Discordへリダイレクト (code_challenge付き)]---|                        |
   |------------------------------------------------------------------>     |
   |--[Discordでログイン・権限承認]--------------------------------------------->|
   |<------------------------------------------------------------[認可コード]--|
   |--[/callback?code=XXX&state=YYY]-->|                                    |
   |                  |--[state検証]   |                                    |
   |                  |--[code + code_verifier]--->|                        |
   |                  |                |--[POST /oauth2/token]------------->|
   |                  |                |           (code_verifier含む)      |
   |                  |                |<--[access_token, refresh_token]----|
   |                  |                |--[/users/@me]--------------------->|
   |                  |                |<--[userId, username, avatar]--------|
   |                  |<--[Set-Cookie: session=... (httpOnly)]--|
   |<--[ログイン完了画面]--|                                    |
   |                  |--[以降のAPIリクエストはCookieが自動付与]-->|
```

**ポイント**
- `code_verifier` と `code_challenge` はフロントエンドで生成・保持
- `client_secret` はバックエンド（CF Workers）にのみ存在。フロントには絶対に露出しない
- セッションは `httpOnly; Secure; SameSite=Lax` CookieでJSから読み取り不可
- `state` パラメータによりCSRF攻撃を防止

---

## 7. ホスティング戦略

### Phase 1: 静的サイト

```
リポジトリ (GitHub)
     |
     | git push → 自動ビルド & デプロイ
     v
Cloudflare Pages
     |
     | CDNエッジ (全世界)
     v
ブラウザ

構成:
- 静的HTML + JS + CSS + JSONファイル
- サーバーサイド処理: なし
- DB: なし（localStorage）
- 費用: 無料
```

### Phase 2: API追加

**変更箇所**

| 項目 | Phase 1 | Phase 2 | 変更内容 |
|------|---------|---------|---------|
| フロントエンド | Cloudflare Pages | Cloudflare Pages | **変更なし** |
| デプロイ方法 | git push で自動 | git push で自動 | **変更なし** |
| APIサーバー | なし | Cloudflare Workers | **新規追加** |
| DB | なし | Cloudflare D1 or KV | **新規追加** |
| 認証 | なし | Discord OAuth2 (CF Workers) | **新規追加** |
| 費用 | 無料 | 無料枠内 (Workers無制限req) | **変更なし** |

```
Phase 2 構成:

リポジトリ (GitHub)
     |
     | git push → 自動ビルド & デプロイ
     v
Cloudflare Pages (フロントエンド)
     |
     | fetch('/api/*') → 同一ドメインでルーティング
     v
Cloudflare Workers (APIサーバー)
     |
     +--→ Cloudflare D1 (問題・履歴・ユーザー)
     +--→ Discord API (OAuthトークン交換・ユーザー情報取得)

メリット:
- フロントとAPIが同一ドメイン → CORSの設定不要
- Cloudflare一社で完結 → 設定・管理の複雑さを最小化
- Phase1で使ったCloudflare PagesをそのままPhase2でも利用
```

---

## 設計判断サマリー

| 判断事項 | 決定 | 理由 |
|---------|------|------|
| データ抽象化 | Repository Pattern + DI | Phase1→2の移行をdi.ts 1ファイルの変更で完結させる |
| Phase1データ | 静的JSON（ビルド時同梱） | インフラゼロ。問題数500問規模なら許容サイズ |
| Phase2データ | Cloudflare Workers + D1 | Pages + Workersで同一ドメイン完結 |
| ホスティング | Cloudflare Pages | 帯域無制限・Cold Startなし・Workersとの統合が容易 |
| 認証方式 | Discord OAuth2 + PKCE | SPAはclient_secret保持不可のためPKCE必須 |
| Phase1認証 | なし | YAGNI。匿名でも個人利用には十分 |
| Bot↔Web履歴 | Phase1は分離 | 統合のためにPhase1でサーバーを立てない |

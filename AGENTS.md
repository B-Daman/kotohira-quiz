# kotohira-quiz

琴平町ご当地クイズのプロジェクト。Web アプリ本体は `web/` 配下。

## Structure
- `web/`: React + TypeScript + Vite アプリ。
- クイズデータやアプリ設定を変更する時は、表示側とデータ形式の両方を確認する。

## Commands
```bash
cd web
npm install
npm run dev
npm run build
npm run lint
npm run preview
```

## Content Rules
- 琴平町に関する問題・解説は、推測ではなく確認済み情報をもとに書く。
- 観光、歴史、地域団体、店舗、人物に関する記述は、古くなり得るため必要に応じて公式情報で確認する。
- クイズとして面白くしつつ、誤解を招く断定や地域への失礼な表現を避ける。

## Development Notes
- React 19 + TypeScript + Vite 構成。
- UI はクイズとしてテンポよく操作できることを優先する。
- 変更後は `npm run build` と、可能なら `npm run lint` を確認する。

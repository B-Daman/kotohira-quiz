"""URLのページ内容からクイズ問題を生成するスクリプト

使い方:
  python scripts/generate_from_url.py <URL> [--count 5] [--category shrine] [--preview]

例:
  python scripts/generate_from_url.py https://www.kotohirakankou.jp/spot/see/entry-107.html --count 5 --category tourism
  python scripts/generate_from_url.py https://www.kotohirakankou.jp/spot/see/entry-107.html --preview

オプション:
  --count N      生成する問題数（デフォルト: 5）
  --category CAT カテゴリ指定（shrine/history/theater/event/geography/gourmet/tourism/architecture/life/modern）
  --preview      JSONファイルに書き込まず、プレビュー表示のみ
  --append       既存の問題バンクに追加（デフォルト）
"""

import argparse
import json
import os
import sys
from pathlib import Path

import anthropic
import httpx
from bs4 import BeautifulSoup

# hisho-botの.envからANTHROPIC_API_KEYを読み込み
HISHO_ENV = Path.home() / "hisho-bot" / ".env"
QUIZ_DATA = Path.home() / "hisho-bot" / "data" / "quiz"
KOTOHIRA_FILE = QUIZ_DATA / "kotohira_questions.json"
WEB_DATA = Path.home() / "kotohira-quiz" / "web" / "public" / "data"

CATEGORIES = [
    "shrine", "history", "theater", "event", "geography",
    "gourmet", "tourism", "architecture", "life", "modern",
]


def load_api_key() -> str:
    """hisho-botの.envからANTHROPIC_API_KEYを取得"""
    if os.getenv("ANTHROPIC_API_KEY"):
        return os.getenv("ANTHROPIC_API_KEY")  # type: ignore
    if HISHO_ENV.exists():
        for line in HISHO_ENV.read_text(encoding="utf-8").splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip()
    raise ValueError("ANTHROPIC_API_KEY が見つかりません")


def fetch_page(url: str) -> str:
    """URLからページのテキストを取得"""
    resp = httpx.get(url, timeout=30, follow_redirects=True)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 不要な要素を除去
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    # 連続空行を圧縮
    lines = [line for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def get_next_id(data: dict) -> int:
    """次の問題IDの番号を取得"""
    ids = [q["id"] for q in data.get("questions", [])]
    if not ids:
        return 1
    return max(int(id_.split("_")[1]) for id_ in ids) + 1


def get_site_name(url: str) -> str:
    """URLからサイト名を推定"""
    from urllib.parse import urlparse
    host = urlparse(url).hostname or ""
    mapping = {
        "www.kotohirakankou.jp": "琴平町観光協会",
        "kotohirakankou.jp": "琴平町観光協会",
        "www.konpira.or.jp": "金刀比羅宮 公式サイト",
        "konpira.or.jp": "金刀比羅宮 公式サイト",
        "www.nishino-kinryo.co.jp": "西野金陵 公式サイト",
        "www.nakanoya.net": "中野うどん学校 公式サイト",
        "kamitsubaki.com": "CAFE&レストラン神椿 公式サイト",
        "www.ikesyouten.com": "五人百姓 池商店",
        "ikesyouten.com": "五人百姓 池商店",
        "kyuman.co.jp": "灸まん本舗石段や 公式サイト",
        "ja.wikipedia.org": "Wikipedia",
        "tabelog.com": "食べログ",
    }
    return mapping.get(host, host)


def generate_questions(
    page_text: str,
    url: str,
    count: int,
    category: str,
    start_id: int,
) -> list[dict]:
    """Claude APIで問題を生成"""
    api_key = load_api_key()
    client = anthropic.Anthropic(api_key=api_key)

    site_name = get_site_name(url)

    prompt = f"""以下のWebページの内容から、琴平町に関する4択クイズ問題を{count}問生成してください。

## 絶対ルール
1. ページに書かれている事実のみを使うこと。推測や一般知識で補完しない
2. 問題文が聞いていること・正解・解説が完全に一致すること
3. 解説は正解を直接述べてから補足情報を追加すること
4. 不正解の選択肢はもっともらしいが明確に間違いであること

## 出力フォーマット（JSON配列）
各問題は以下の形式:
{{
  "id": "kotohira_{start_id:03d}",
  "category": "{category}",
  "difficulty": "easy" or "medium" or "hard",
  "question": "問題文",
  "choices": ["A. 選択肢1", "B. 選択肢2", "C. 選択肢3", "D. 選択肢4"],
  "answer": "正解のラベル（A/B/C/D）",
  "explanation": "解説文。（出典: [{site_name}]({url})）",
  "source": "{url}",
  "reviewed": false,
  "enabled": true
}}

IDは kotohira_{start_id:03d} から連番で振ってください。
reviewed は false にしてください（人間レビュー前）。
解説の末尾に必ず（出典: [{site_name}]({url})）を含めてください。

## ページ内容
{page_text[:8000]}

## 出力
JSON配列のみを出力してください。説明や前置きは不要です。"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text  # type: ignore
    # JSON部分を抽出
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]

    return json.loads(text)


def preview_questions(questions: list[dict]) -> None:
    """問題をプレビュー表示"""
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
    for q in questions:
        print(f"\n{'='*60}")
        print(f"[{q['id']}] {q['category']} / {q['difficulty']}")
        print(f"Q: {q['question']}")
        for c in q["choices"]:
            marker = " *" if c.startswith(f"{q['answer']}.") else ""
            print(f"  {c}{marker}")
        print(f"解説: {q['explanation']}")
        print(f"reviewed: {q['reviewed']}")


def append_to_bank(questions: list[dict]) -> None:
    """問題バンクに追加"""
    with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["questions"].extend(questions)

    with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Webにも同期
    if WEB_DATA.exists():
        import shutil
        shutil.copy2(KOTOHIRA_FILE, WEB_DATA / "kotohira_questions.json")
        print(f"Web data synced: {WEB_DATA}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="URLからクイズ問題を生成"
    )
    parser.add_argument("url", help="問題のソースURL")
    parser.add_argument(
        "--count", type=int, default=5,
        help="生成する問題数（デフォルト: 5）",
    )
    parser.add_argument(
        "--category", default="tourism",
        choices=CATEGORIES,
        help="カテゴリ（デフォルト: tourism）",
    )
    parser.add_argument(
        "--preview", action="store_true",
        help="プレビューのみ（ファイルに書き込まない）",
    )
    args = parser.parse_args()

    print(f"Fetching: {args.url}")
    page_text = fetch_page(args.url)
    print(f"Page text: {len(page_text)} chars")

    # 現在の最大IDを取得
    with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    start_id = get_next_id(data)
    print(f"Next ID: kotohira_{start_id:03d}")

    print(f"Generating {args.count} questions ({args.category})...")
    questions = generate_questions(
        page_text, args.url, args.count, args.category, start_id,
    )
    print(f"Generated {len(questions)} questions")

    preview_questions(questions)

    if args.preview:
        print("\n[Preview mode] ファイルには書き込みません。")
        return

    print(f"\n{len(questions)}問を問題バンクに追加しますか？ (y/n): ", end="")
    if input().strip().lower() != "y":
        print("キャンセルしました。")
        return

    append_to_bank(questions)
    print(f"追加完了！ 問題バンク: {KOTOHIRA_FILE}")
    print("reviewed: false で追加されています。レビュー後に true に変更してください。")


if __name__ == "__main__":
    main()

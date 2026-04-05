"""一時スクリプト: 金刀比羅宮分社ページから問題追加"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/articles_2023/0925_subsidiary-shrine/article.html"
sl = f"（出典: [金刀比羅宮 分社情報]({url})）"

new_qs = [
    {
        "id": "kotohira_548", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の東京分社は現在どこにありますか？",
        "choices": ["A. 港区虎ノ門", "B. 文京区本郷", "C. 江東区深川", "D. 千代田区神田"],
        "answer": "B",
        "explanation": f"東京分社は現在、東京都文京区本郷1-5-11にあります。昭和39年（1964年）に深川から移転しました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_549", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の東京分社が最初に祀られたのは何年ですか？",
        "choices": ["A. 寛政元年（1789年）", "B. 文化9年（1812年）", "C. 文政2年（1819年）", "D. 明治13年（1880年）"],
        "answer": "C",
        "explanation": f"東京分社は文政2年（1819年）に板橋市左衛門の邸内祠として創設されました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_550", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の分社のうち、最も古い記録があるのはどこですか？",
        "choices": ["A. 東京分社（1819年）", "B. 尾張分社（1812年）", "C. 神戸分社（1882年）", "D. 松山分社（1878年）"],
        "answer": "B",
        "explanation": f"尾張分社は文化9年（1812年）の記録が最古で、平田家の邸内祠として始まりました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_551", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の鳥羽分社で行われる特徴的な行事は何ですか？",
        "choices": ["A. 蹴鞠", "B. 神輿の海上渡御と花火大会", "C. 歌舞伎公演", "D. 流鏑馬"],
        "answer": "B",
        "explanation": f"鳥羽分社では神輿の海上渡御と花火大会が行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_552", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の神戸分社の祭神に含まれ、他の分社にはいない神様は誰ですか？",
        "choices": ["A. 天照大御神", "B. 武甕槌神", "C. 素戔嗚尊", "D. 菅原道真"],
        "answer": "B",
        "explanation": f"神戸分社の祭神は大物主神・崇徳天皇に加え、武甕槌神も祀られています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_553", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の尾張分社はどこにありますか？",
        "choices": ["A. 名古屋市", "B. 一宮市", "C. 豊橋市", "D. 岡崎市"],
        "answer": "B",
        "explanation": f"尾張分社は愛知県一宮市にあります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_554", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の松山分社が分社に昇格したのは何年ですか？",
        "choices": ["A. 明治11年", "B. 大正5年", "C. 昭和30年", "D. 昭和41年"],
        "answer": "D",
        "explanation": f"松山分社は明治11年に支教会となり、昭和41年（1966年）に分社に昇格しました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_548-554)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")
    print(f"  解説: {q['explanation'][:80]}...")

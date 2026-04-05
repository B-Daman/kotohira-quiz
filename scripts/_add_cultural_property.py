"""一時スクリプト: 金刀比羅宮 重要文化財ページから問題追加"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/articles_2024/20240518_important-cultural-propertys/article.html"
sl = f"（出典: [金刀比羅宮 重要文化財指定]({url})）"

new_qs = [
    {
        "id": "kotohira_555", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮等が重要文化財に指定されたのはいつですか？",
        "choices": ["A. 平成30年8月15日", "B. 令和4年5月17日", "C. 令和6年8月15日", "D. 令和6年5月17日"],
        "answer": "C",
        "explanation": f"令和6年8月15日（2024年）に重要文化財に指定されました。答申は令和6年5月17日でした。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_556", "category": "shrine", "difficulty": "medium",
        "question": "令和6年に重要文化財に指定された金刀比羅宮の建造物は何棟ですか？",
        "choices": ["A. 5棟", "B. 8棟", "C. 12棟", "D. 15棟"],
        "answer": "C",
        "explanation": f"令和6年8月15日に12棟が重要文化財に指定されました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_557", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮拝殿が建設されたのは何年ですか？",
        "choices": ["A. 明治5年", "B. 明治8年", "C. 明治11年", "D. 明治15年"],
        "answer": "C",
        "explanation": f"御本宮拝殿は明治11年に建設されました。木造、入母屋造、檜皮葺の建物です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_558", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の御本宮の屋根はどのような葺き方ですか？",
        "choices": ["A. 瓦葺", "B. 銅板葺", "C. 茅葺", "D. 檜皮葺"],
        "answer": "D",
        "explanation": f"御本宮は檜皮葺（ひわだぶき）です。総檜素木造りで蒔絵装飾が施されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_559", "category": "history", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮が現在の姿になったのは、何に対応するためでしたか？",
        "choices": ["A. 戦災復興", "B. 神仏分離", "C. 廃藩置県", "D. 明治天皇の行幸"],
        "answer": "B",
        "explanation": f"明治7〜11年にかけて神仏分離に対応する形で現在の姿が創出されました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_560", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の建物に施されている神紋はどのような形ですか？",
        "choices": ["A. 菊の御紋", "B. 丸金の神紋", "C. 三つ巴紋", "D. 五七桐紋"],
        "answer": "B",
        "explanation": f"金刀比羅宮の建物には丸金の神紋が施されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_555-560)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

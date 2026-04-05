"""一時スクリプト: 奥社編から問題追加 + 既存問題にソースURL追記"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"
url = "https://www.konpira.or.jp/articles/20200616_guide_inner-shrine/article.htm"
sl = f"（出典: [金刀比羅宮 奥社参拝ガイド]({url})）"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- 既存問題にソースURL追記 ---
source_targets = [
    "kotohira_002", "kotohira_003", "kotohira_004",
    "kotohira_100", "kotohira_101", "kotohira_322",
    "kotohira_348", "kotohira_385", "kotohira_431",
    "kotohira_499",
]
updated = 0
for q in data["questions"]:
    if q["id"] in source_targets and "出典:" not in q.get("explanation", ""):
        q["explanation"] = q["explanation"].rstrip() + f" {sl}"
        q["source"] = url
        updated += 1
        print(f"Updated: {q['id']} - {q['question'][:40]}")

# --- 新規問題 ---
new_qs = [
    {
        "id": "kotohira_600", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の御本宮から奥社までの距離はおよそ何キロメートルですか？",
        "choices": ["A. 約0.5キロ", "B. 約0.8キロ", "C. 約1.2キロ", "D. 約2.0キロ"],
        "answer": "C",
        "explanation": f"御本宮から奥社までの距離は約1.2キロメートルです。石段583段を登ります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_601", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の厳魂神社（奥社）の海抜は何メートルですか？",
        "choices": ["A. 251メートル", "B. 321メートル", "C. 421メートル", "D. 538メートル"],
        "answer": "C",
        "explanation": f"厳魂神社（奥社）の海抜は421メートルです。御本宮は海抜251メートル。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_602", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の白峰神社に祀られている3柱の神様に含まれないのは誰ですか？",
        "choices": ["A. 崇徳天皇", "B. 待賢門院", "C. 大山祇神", "D. 菅原道真命"],
        "answer": "D",
        "explanation": f"白峰神社には崇徳天皇、待賢門院、大山祇神が祀られています。菅原道真命は菅原神社の祭神です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_603", "category": "history", "difficulty": "hard",
        "question": "金刀比羅宮の厳魂彦命は、戦国時代にどの家の家臣の子として生まれましたか？",
        "choices": ["A. 長宗我部家", "B. 生駒家", "C. 松平家", "D. 京極家"],
        "answer": "B",
        "explanation": f"厳魂彦命は戦国時代に生駒家家臣の子として出生しました。宥盛と称して修行し、金毘羅大権現を再興しました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_604", "category": "history", "difficulty": "hard",
        "question": "金刀比羅宮の厳魂彦命が天狗と化して姿を消したとされるのは何年ですか？",
        "choices": ["A. 天正18年（1590年）", "B. 慶長5年（1600年）", "C. 慶長18年（1613年）", "D. 元和元年（1615年）"],
        "answer": "C",
        "explanation": f"慶長18年（1613年）に厳魂彦命は天狗と化して姿を消したと伝えられています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_605", "category": "history", "difficulty": "hard",
        "question": "崇徳天皇が配流される原因となった戦いは何ですか？",
        "choices": ["A. 応仁の乱", "B. 保元の乱", "C. 壬申の乱", "D. 承久の乱"],
        "answer": "B",
        "explanation": f"保元元年（1156年）の保元の乱に敗れた崇徳天皇は讃岐に配流されました。金刀比羅宮の白峰神社に祀られています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_606", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の真井貯水池は何のために作られましたか？",
        "choices": ["A. 飲料水", "B. 農業用水", "C. 防火用水", "D. 庭園用水"],
        "answer": "C",
        "explanation": f"真井貯水池は明治37年（1904年）に防火用水源として作製されました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_607", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の境内にある菅原神社に祀られているのは誰ですか？",
        "choices": ["A. 崇徳天皇", "B. 厳魂彦命", "C. 菅原道真", "D. 大物主神"],
        "answer": "C",
        "explanation": f"菅原神社には菅原道真命が祀られています。学問の神様として知られています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nUpdated sources: {updated}")
print(f"Added {len(new_qs)} questions (kotohira_600-607)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

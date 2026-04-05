"""一時スクリプト: 参拝ガイドから追加問題（未使用の事実）"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/articles/20200616_guide/article.htm"
sl = f"（出典: [金刀比羅宮 参拝ガイド]({url})）"

new_qs = [
    {
        "id": "kotohira_595", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の真須賀神社に祀られている神様は誰ですか？",
        "choices": ["A. 大物主神と崇徳天皇", "B. 天照大御神と月読命", "C. 建速須佐之男尊と奇稲田姫尊", "D. 伊邪那岐神と伊邪那美神"],
        "answer": "C",
        "explanation": f"真須賀神社には建速須佐之男尊と奇稲田姫尊が祀られています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_596", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の灯明堂が建立されたのは何年ですか？",
        "choices": ["A. 天保6年（1835年）", "B. 弘化2年（1845年）", "C. 安政5年（1858年）", "D. 万延元年（1860年）"],
        "answer": "C",
        "explanation": f"灯明堂は安政5年（1858年）に備後国因之島浦々講中の寄進で建立されました。船の下梁を利用した建物で、重要有形民俗文化財です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_597", "category": "history", "difficulty": "hard",
        "question": "天正年間に金刀比羅宮を再営した戦国武将は誰ですか？",
        "choices": ["A. 織田信長", "B. 豊臣秀吉", "C. 長宗我部元親", "D. 毛利元就"],
        "answer": "C",
        "explanation": f"天正年間（1573-1592年）に長宗我部元親が金刀比羅宮を再営しました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_598", "category": "history", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮が最初に改築された記録は何年ですか？",
        "choices": ["A. 延暦13年（794年）", "B. 長保3年（1001年）", "C. 元亀4年（1573年）", "D. 万治2年（1659年）"],
        "answer": "B",
        "explanation": f"長保3年（1001年）に一條天皇によって改築された記録が最古です。その後、元亀4年（1573年）、天正年間の長宗我部元親、万治2年（1659年）の松平頼重など複数回の改築が行われました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_599", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の大門から先の境内は何に指定されていますか？",
        "choices": ["A. 世界遺産", "B. 国宝", "C. 国の名勝・天然記念物", "D. 国立公園のみ"],
        "answer": "C",
        "explanation": f"大門以降の境内は国の名勝・天然記念物に指定されており、瀬戸内海国立公園にも含まれています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_595-599)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

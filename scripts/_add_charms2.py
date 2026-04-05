"""一時スクリプト: 授与品ページから追加問題"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/charms/article.php"
sl = f"（出典: [金刀比羅宮 授与品]({url})）"

new_qs = [
    {
        "id": "kotohira_581", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の「こんぴら狗みくじ《置物型》」は何でできていますか？",
        "choices": ["A. 木彫り", "B. 陶器", "C. ガラス", "D. 紙"],
        "answer": "B",
        "explanation": f"こんぴら狗みくじ（置物型）は陶器製です。おみくじは下から取り出し、取り出した後は置物として飾れます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_582", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の令和八年限定御朱印紙に切り絵で描かれている2頭の神馬の名前は何ですか？",
        "choices": ["A. 月光号と日光号", "B. 光驥号と白平号", "C. 金毘羅号と象頭号", "D. 瑞穂号と千歳号"],
        "answer": "B",
        "explanation": f"令和八年丙午の限定御朱印紙には、金刀比羅宮の神馬「光驥号」と「白平号」が切り絵で描かれています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_583", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の厳魂神社 天狗御守は、どのような力が宿るとされていますか？",
        "choices": ["A. 学業成就の力", "B. 霊妙不可思議な能力", "C. 海上安全の力", "D. 商売繁盛の力"],
        "answer": "B",
        "explanation": f"厳魂彦命の人知では計り知れない霊妙不可思議な能力が宿るとされ、諸々の災厄から身を守る「身守り」として授与されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_581-583)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

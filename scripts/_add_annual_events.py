"""一時スクリプト: 金刀比羅宮 年間行事ページから問題追加"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/articles_2026/20260225_annual-events/article.html"
sl = f"（出典: [金刀比羅宮 年間行事]({url})）"

new_qs = [
    {
        "id": "kotohira_561", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の「初こんぴら」（初十日祭）は毎年何月何日ですか？",
        "choices": ["A. 1月1日", "B. 1月3日", "C. 1月10日", "D. 1月15日"],
        "answer": "C",
        "explanation": f"初十日祭（初こんぴら）は毎年1月10日に行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_562", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の例大祭は何月何日から何日まで行われますか？",
        "choices": ["A. 9月9日〜11日", "B. 10月9日〜11日", "C. 10月10日〜12日", "D. 11月9日〜11日"],
        "answer": "B",
        "explanation": f"例大祭は10月9日（宵宮祭）、10日（例祭・神幸祭）、11日（還幸祭）の3日間行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_563", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の大祓式は年に何回行われますか？",
        "choices": ["A. 年1回（12月）", "B. 年2回（6月と12月）", "C. 年4回（四季）", "D. 毎月"],
        "answer": "B",
        "explanation": f"大祓式は6月30日と12月31日の年2回行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_564", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の月次祭は毎月何回行われますか？",
        "choices": ["A. 毎月1回", "B. 毎月2回", "C. 毎月3回以上", "D. 年4回のみ"],
        "answer": "C",
        "explanation": f"月次祭は毎月1日・6日・10日・26日など複数回行われます。御本宮、三穂津姫社、旭社、厳魂神社など対象も異なります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_565", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の節分祭は何月何日に行われますか？",
        "choices": ["A. 1月31日", "B. 2月3日", "C. 2月11日", "D. 3月3日"],
        "answer": "B",
        "explanation": f"節分祭は2月3日に行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_566", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の御田植祭は何月何日に行われますか？",
        "choices": ["A. 3月15日", "B. 4月15日", "C. 5月15日", "D. 6月15日"],
        "answer": "B",
        "explanation": f"御田植祭は4月15日に行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_567", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮で海上安全を特別に祈願する祭りは何月に行われますか？",
        "choices": ["A. 5月", "B. 6月", "C. 7月", "D. 8月"],
        "answer": "C",
        "explanation": f"海上安全特別大祈願祭は7月20日に行われます。金刀比羅宮は海の守り神として知られています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_568", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の例大祭で、御神輿が出発する日は何日ですか？",
        "choices": ["A. 10月9日", "B. 10月10日", "C. 10月11日", "D. 10月12日"],
        "answer": "B",
        "explanation": f"10月10日に例祭・神幸祭が行われ、御神輿が発御します。翌11日に還幸祭で御神輿が還御します。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_569", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の年末の大掃除にあたる行事「煤払式」は何月何日ですか？",
        "choices": ["A. 12月10日", "B. 12月13日", "C. 12月25日", "D. 12月28日"],
        "answer": "B",
        "explanation": f"煤払式は12月13日に行われます。同日に御年木伐神事も執り行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_570", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の厳魂神社（奥社）の例祭は何月何日ですか？",
        "choices": ["A. 1月1日", "B. 1月6日", "C. 4月6日", "D. 10月6日"],
        "answer": "B",
        "explanation": f"厳魂神社の例祭は1月6日に行われます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_561-570)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

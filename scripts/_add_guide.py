"""一時スクリプト: 参拝ガイド御本宮編から問題追加"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/articles/20200616_guide/article.htm"
sl = f"（出典: [金刀比羅宮 参拝ガイド]({url})）"

new_qs = [
    {
        "id": "kotohira_584", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の大門を寄進した讃岐国高松藩主は誰ですか？",
        "choices": ["A. 京極高和", "B. 松平頼重", "C. 生駒親正", "D. 山内一豊"],
        "answer": "B",
        "explanation": f"大門は讃岐国高松藩主の松平頼重が寄進しました。松平頼重は水戸光圀の兄です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_585", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の松平頼重は、歴史上有名な人物の兄ですが、誰の兄ですか？",
        "choices": ["A. 徳川家光", "B. 徳川綱吉", "C. 水戸光圀", "D. 前田利常"],
        "answer": "C",
        "explanation": f"大門を寄進した松平頼重は、「水戸黄門」で知られる水戸光圀の兄です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_586", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の御本宮の海抜は何メートルですか？",
        "choices": ["A. 151メートル", "B. 201メートル", "C. 251メートル", "D. 301メートル"],
        "answer": "C",
        "explanation": f"御本宮は海抜251メートルの位置にあります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_587", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の灯明堂は何を利用して建てられましたか？",
        "choices": ["A. 城の廃材", "B. 船の下梁", "C. 寺院の柱", "D. 鳥居の木材"],
        "answer": "B",
        "explanation": f"灯明堂は備後国因之島浦々講中の寄進で、船の下梁を利用して安政5年（1853年）に建立されました。重要有形民俗文化財です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_588", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の賢木門の名前の由来は何ですか？",
        "choices": ["A. 賢い宮大工が建てた", "B. 一本の柱が逆さまに取り付けられた", "C. 神聖な木で作られた", "D. 賢者が命名した"],
        "answer": "B",
        "explanation": f"賢木門は建築時に一本の柱が逆さまに取り付けられたことが名前の由来です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_589", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の旭社が完成したのは何年ですか？",
        "choices": ["A. 文化2年（1805年）", "B. 文政8年（1825年）", "C. 弘化2年（1845年）", "D. 安政5年（1858年）"],
        "answer": "C",
        "explanation": f"旭社は弘化2年（1845年）に完成しました。四国最大級の文化財建造物です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_590", "category": "history", "difficulty": "hard",
        "question": "金刀比羅宮の第19代宮司・琴陵宥常が創立した組織は何ですか？",
        "choices": ["A. 日本赤十字社", "B. 帝国水難救済会", "C. 海上保安協会", "D. 日本海事財団"],
        "answer": "B",
        "explanation": f"琴陵宥常（1840-1892）は帝国水難救済会を創立しました。その30周年記念として昭和2年（1927年）に銅像が建立されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_591", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の木馬舎に納められている木馬が献納されたのは何年ですか？",
        "choices": ["A. 元和元年（1615年）", "B. 慶安3年（1650年）", "C. 寛文5年（1665年）", "D. 延宝7年（1679年）"],
        "answer": "B",
        "explanation": f"木馬舎の木馬は慶安3年（1650年）に献納されました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_592", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の旭社に祀られている神様の中に含まれるのは誰ですか？",
        "choices": ["A. 大物主神", "B. 厳魂彦命", "C. 天照大御神", "D. 崇徳天皇"],
        "answer": "C",
        "explanation": f"旭社には天御中主神、高皇産霊神、神皇産霊神、伊邪那岐神、伊邪那美神、天照大御神、天津神、国津神、八百万神が祀られています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_593", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の大門から桜馬場までの距離はおよそ何メートルですか？",
        "choices": ["A. 50メートル", "B. 100メートル", "C. 150メートル", "D. 300メートル"],
        "answer": "C",
        "explanation": f"大門から桜馬場までは150メートル程です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_594", "category": "shrine", "difficulty": "medium",
        "question": "高橋由一は日本の何の開拓者として知られていますか？",
        "choices": ["A. 日本画", "B. 洋画", "C. 版画", "D. 水墨画"],
        "answer": "B",
        "explanation": f"高橋由一は日本洋画の開拓者として知られ、金刀比羅宮の高橋由一館に27点の油絵が収蔵されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_584-594)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

"""一時スクリプト: 金刀比羅宮ガイドPDFから問題追加"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/articles_2024/20241029_booklets/kotohira-gu-booklets.pdf"
sl = f"（出典: [金刀比羅宮 オフィシャルガイド]({url})）"

new_qs = [
    {
        "id": "kotohira_538", "category": "shrine", "difficulty": "hard",
        "question": "カフェ＆レストラン神椿がある場所には、以前誰が寄贈した茶屋がありましたか？",
        "choices": ["A. 松平頼重", "B. 山本弥三郎", "C. 京極高和", "D. 琴陵光重"],
        "answer": "B",
        "explanation": f"神椿の場所には、以前は山本弥三郎（1797年）寄贈の茶屋がありました。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_539", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の旭社はどのような位置づけの文化財建造物ですか？",
        "choices": ["A. 日本最古の建造物", "B. 四国最大級の文化財建造物", "C. 国宝指定の建造物", "D. 世界遺産の建造物"],
        "answer": "B",
        "explanation": f"旭社は四国最大級の文化財建造物で、重要文化財に指定されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_540", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の旭社から御本宮に至るルートはどうなっていますか？",
        "choices": ["A. 自由に往復できる", "B. 一方通行", "C. 時間帯で変わる", "D. ガイド同伴が必要"],
        "answer": "B",
        "explanation": f"旭社から御本宮に至るルートは一方通行になっています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_541", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮直前にある「御前四段坂」は何段ですか？",
        "choices": ["A. 93段", "B. 113段", "C. 133段", "D. 153段"],
        "answer": "C",
        "explanation": f"御本宮までの最後の難関、御前四段坂は133段あります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_542", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮は何年に一度、檜皮の屋根の葺き替えを行いますか？",
        "choices": ["A. 20年に一度", "B. 25年に一度", "C. 33年に一度", "D. 50年に一度"],
        "answer": "C",
        "explanation": f"御本宮は33年に一度、檜皮のお屋根の葺き替えを行っています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_543", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の御本宮拝殿の格天井を装飾した漆職人はどこの出身ですか？",
        "choices": ["A. 京都", "B. 金沢", "C. 石川県・輪島", "D. 奈良"],
        "answer": "C",
        "explanation": f"拝殿の格天井は石川県・輪島の漆職たちによる桜の木地蒔絵で装飾されています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_544", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の御本宮北側展望台から見える、美しい形の山は何ですか？",
        "choices": ["A. 象頭山", "B. 讃岐富士（飯野山）", "C. 五色台", "D. 屋島"],
        "answer": "B",
        "explanation": f"御本宮北側展望台からは讃岐平野・瀬戸内海が見渡せ、正面に讃岐富士（飯野山）が見られます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_545", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の奥社にある天狗面のうち、鼻高天狗は何を表していますか？",
        "choices": ["A. 旅の安全", "B. 五穀豊穣", "C. 奥社の神様", "D. 海上守護"],
        "answer": "C",
        "explanation": f"奥社には天狗の面が2面掛けられており、鼻高天狗は奥社の神様を表し、烏天狗は旅の安全を守ります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_546", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の蹴鞠の鞠庭に植えられている4本の木は何ですか？",
        "choices": ["A. 松・竹・梅・桜", "B. 桜・柳・楓・松", "C. 杉・檜・桜・楓", "D. 梅・桃・桜・柳"],
        "answer": "B",
        "explanation": f"鞠庭には桜・柳・楓・松の4本の木が植えられています。二股に分かれたところに神様が座って蹴鞠をご覧になると言われています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_547", "category": "shrine", "difficulty": "medium",
        "question": "蹴鞠が現在も行われている場所は日本で何か所ですか？",
        "choices": ["A. 京都のみ", "B. 京都と金刀比羅宮の2か所", "C. 全国5か所", "D. 全国10か所以上"],
        "answer": "B",
        "explanation": f"蹴鞠は現在、京都と金刀比羅宮にしか遺っていません。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_538-547)")
print(f"Total: {len(data['questions'])} questions")

# プレビュー
for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

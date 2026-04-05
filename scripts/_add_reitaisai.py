"""一時スクリプト: 例大祭ページから問題追加 + 既存問題ソース追記"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"
url = "https://www.konpira.or.jp/ARCHIVES/ritual/00_annual-festival/page.html"
sl = f"\n（出典: [金刀比羅宮 例大祭]({url})）"
sl_inline = f"（出典: [金刀比羅宮 例大祭]({url})）"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# 既存問題にソース追記
targets = [
    "kotohira_010", "kotohira_011", "kotohira_075", "kotohira_104",
    "kotohira_120", "kotohira_188", "kotohira_191", "kotohira_205",
    "kotohira_327", "kotohira_346", "kotohira_441", "kotohira_469",
    "kotohira_517", "kotohira_562", "kotohira_568",
]
updated = 0
for q in data["questions"]:
    if q["id"] in targets and url not in q.get("explanation", ""):
        q["explanation"] = q["explanation"].rstrip() + sl
        updated += 1
        print(f"Updated: {q['id']}")

# 新規問題
new_qs = [
    {
        "id": "kotohira_657", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の例大祭は全体で何日間にわたりますか？",
        "choices": ["A. 3日間", "B. 10日間", "C. 30日間", "D. 46日間"],
        "answer": "D",
        "explanation": f"例大祭は8月31日の口明神事から10月15日の焼払神事まで46日間にわたります。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_658", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の例大祭で「お頭人さん」として行列を導くのは誰ですか？",
        "choices": ["A. 宮司", "B. 男女の児童", "C. 地元の長老", "D. 巫女"],
        "answer": "B",
        "explanation": f"お頭人さんは乗馬の男子児童2名と駕籠の女子児童2名です。邪心のない子どもたちは神を導くことができるとされています。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_659", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の例大祭の御神輿渡御の距離はおよそ何キロメートルですか？",
        "choices": ["A. 約500メートル", "B. 約1キロ", "C. 約2キロ", "D. 約5キロ"],
        "answer": "C",
        "explanation": f"御神輿渡御は御本宮から御神事場まで約2キロメートルの道のりを約2時間かけて進みます。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_660", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の例大祭で食される「七膳片箸」に含まれないものはどれですか？",
        "choices": ["A. うどん", "B. あんころもち", "C. 赤飯", "D. 甘酒"],
        "answer": "C",
        "explanation": f"七膳片箸はうどん・卵豆腐・あんころもち・雑炊・団子吸い物・魚吸い物・甘酒の七つの膳です。甘酒に箸が1本だけ添えられることからそう呼ばれます。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_661", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の例大祭の「潮川神事」は元々どこで行われていましたか？",
        "choices": ["A. 瀬戸内海の島", "B. 多度津の海岸", "C. 金倉川の上流", "D. 象頭山の山頂"],
        "answer": "B",
        "explanation": f"潮川神事は古くは多度津の海岸で行われていましたが、正平年間（1346-70年）の兵乱で中止。以降は多度津の海水と海藻を金倉川に混ぜて行われるようになりました。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_662", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の例大祭で祝舎が1か所に統合されたのは何年ですか？",
        "choices": ["A. 明治31年", "B. 大正12年", "C. 昭和31年", "D. 平成元年"],
        "answer": "C",
        "explanation": f"昭和31年（1956年）より祝舎は1か所に統合されました。以前は上祝舎と次祝舎の2か所に設けられていました。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_663", "category": "event", "difficulty": "hard",
        "question": "金刀比羅宮の例大祭で、昔お頭人さんを輪番で勤めていた4つの村はどれですか？",
        "choices": ["A. 琴平・善通寺・多度津・丸亀", "B. 四条・五条・榎井・苗田", "C. 象郷・琴平・満濃・仲南", "D. 琴平・榎井・善通寺・観音寺"],
        "answer": "B",
        "explanation": f"昔は琴平山麓の四条・五条・榎井・苗田の4つの村が毎年輪番で祝舎神事を勤めていました。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_664", "category": "event", "difficulty": "medium",
        "question": "金刀比羅宮の例大祭の最後の神事「焼払神事」では何を行いますか？",
        "choices": ["A. 松明を燃やす", "B. 祝舎の用材や御幣を焼払う", "C. 護摩木を焚く", "D. 花火を打ち上げる"],
        "answer": "B",
        "explanation": f"10月15日の焼払神事では、祝舎の建物を取り壊し、その用材や御幣などを焼払います。これで46日間の例大祭が終了します。{sl_inline}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nUpdated sources: {updated}")
print(f"Added {len(new_qs)} questions (kotohira_657-664)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

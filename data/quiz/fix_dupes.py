import json

with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["id"] == "kotohira_205":
        q["question"] = "金刀比羅宮の例大祭の初日は何月何日ですか？"
        q["choices"] = ["A. 10月1日", "B. 10月9日", "C. 10月10日", "D. 10月15日"]
        q["answer"] = "B"
        q["explanation"] = "金刀比羅宮の例大祭は10月9日から始まります。10月9日〜11日の3日間にわたって行われます。"
    elif q["id"] == "kotohira_477":
        q["question"] = "琴平町で地ビールを楽しめるのはどのブランドですか？"
        q["choices"] = ["A. 讃岐エール", "B. こんぴらビール", "C. 象頭山ブリュー", "D. 金毘羅ラガー"]
        q["answer"] = "B"
        q["explanation"] = "琴平町ではこんぴらビールという地ビールブランドが楽しめます。地元で醸造されたビールです。"

with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify no more duplicates
from collections import Counter
q_texts = [q["question"] for q in data["questions"]]
dupes = [q for q, c in Counter(q_texts).items() if c > 1]
print(f"Remaining duplicates: {len(dupes)}")
print(f"Total questions: {len(data['questions'])}")

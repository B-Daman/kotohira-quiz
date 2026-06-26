import json
from collections import Counter

with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_texts = [(q["id"], q["question"]) for q in data["questions"]]
text_count = Counter(t for _, t in q_texts)
dupes = {t for t, c in text_count.items() if c > 1}

for qid, qt in q_texts:
    if qt in dupes:
        print(f"{qid}: {qt}")

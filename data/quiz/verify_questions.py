import json
from collections import Counter

with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
print(f"Total: {len(questions)}")

# Category distribution
cats = Counter(q["category"] for q in questions)
print("\nCategory distribution:")
for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {count}")

# Difficulty distribution
diffs = Counter(q["difficulty"] for q in questions)
print("\nDifficulty distribution:")
for d, count in sorted(diffs.items()):
    pct = count / len(questions) * 100
    print(f"  {d}: {count} ({pct:.1f}%)")

# Check all have reviewed=True, enabled=True
all_reviewed = all(q.get("reviewed") == True for q in questions)
all_enabled = all(q.get("enabled") == True for q in questions)
print(f"\nAll reviewed: {all_reviewed}")
print(f"All enabled: {all_enabled}")

# Check for duplicate questions
q_texts = [q["question"] for q in questions]
dupes = [q for q, c in Counter(q_texts).items() if c > 1]
if dupes:
    print(f"\nDuplicate questions found: {len(dupes)}")
    for d in dupes[:5]:
        print(f"  - {d}")
else:
    print("\nNo duplicate questions found!")

# Verify answer matches choices
bad = []
for q in questions:
    ans_letter = q["answer"]
    matching = [c for c in q["choices"] if c.startswith(f"{ans_letter}.")]
    if not matching:
        bad.append(q["id"])
if bad:
    print(f"\nBad answer references: {bad}")
else:
    print("All answers reference valid choices!")

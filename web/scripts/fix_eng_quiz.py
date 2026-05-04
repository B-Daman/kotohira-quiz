import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "public" / "data" / "english_questions.json"

# Read current file
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
print(f"Total questions: {len(questions)}")

# Keep original 500 questions
original = questions[:500]

# Get new questions (500 onward)
new_qs = questions[500:]
print(f"New questions: {len(new_qs)}")

# Find unique new words and keep first 250
seen_words = set()
new_words_ordered = []
for q in new_qs:
    if q["word"] not in seen_words:
        seen_words.add(q["word"])
        new_words_ordered.append(q["word"])

print(f"New unique words: {len(new_words_ordered)}")

# Take exactly 250 words
target_words = set(new_words_ordered[:250])
print(f"Target words: {len(target_words)}")

# Filter new questions to only include target words
filtered_new = [q for q in new_qs if q["word"] in target_words]
print(f"Filtered new questions: {len(filtered_new)}")

# Now fix answer distribution
# Count current distribution
ans_count = {"A": 0, "B": 0, "C": 0, "D": 0}
for q in filtered_new:
    ans_count[q["answer"]] += 1
print(f"Current answer distribution: {ans_count}")

# Target: 500 questions, ~125 each for A/B/C/D
# We need to rotate answers for questions that have too many A's
# Strategy: for each question, rotate the choices so the answer changes
# but the correct answer text stays in the right position

def rotate_answer(q, new_ans):
    """Rotate choices so that the correct answer is at position new_ans"""
    current_ans = q["answer"]
    if current_ans == new_ans:
        return q

    # Find current correct choice index
    ans_map = {"A": 0, "B": 1, "C": 2, "D": 3}
    rev_map = {0: "A", 1: "B", 2: "C", 3: "D"}

    current_idx = ans_map[current_ans]
    new_idx = ans_map[new_ans]

    choices = list(q["choices"])
    # Swap the correct answer to the new position
    choices[current_idx], choices[new_idx] = choices[new_idx], choices[current_idx]

    # Update the letter prefixes
    new_choices = []
    for i, choice in enumerate(choices):
        # Replace the prefix letter
        prefix = f"{rev_map[i]}. "
        # Remove old prefix
        text = choice[3:]  # Remove "X. " prefix
        new_choices.append(prefix + text)

    q_copy = dict(q)
    q_copy["choices"] = new_choices
    q_copy["answer"] = new_ans
    return q_copy

# Balance distribution
target_per_answer = len(filtered_new) // 4  # 125 each
remainder = len(filtered_new) % 4

targets = {
    "A": target_per_answer + (1 if remainder > 0 else 0),
    "B": target_per_answer + (1 if remainder > 1 else 0),
    "C": target_per_answer + (1 if remainder > 2 else 0),
    "D": target_per_answer,
}
print(f"Target distribution: {targets}")

# Group questions by current answer
by_answer = {"A": [], "B": [], "C": [], "D": []}
for i, q in enumerate(filtered_new):
    by_answer[q["answer"]].append(i)

# Redistribute
current_counts = {k: len(v) for k, v in by_answer.items()}
print(f"Current per-answer counts: {current_counts}")

# Find which answers have excess and which have deficit
excess = {}
deficit = {}
for ans in "ABCD":
    diff = current_counts[ans] - targets[ans]
    if diff > 0:
        excess[ans] = diff
    elif diff < 0:
        deficit[ans] = -diff

print(f"Excess: {excess}")
print(f"Deficit: {deficit}")

# Move excess to deficit
balanced = list(filtered_new)
for excess_ans, excess_count in excess.items():
    indices_to_move = by_answer[excess_ans][-excess_count:]  # Take from end

    for idx in indices_to_move:
        # Find which deficit answer needs more
        for deficit_ans in sorted(deficit.keys()):
            if deficit[deficit_ans] > 0:
                balanced[idx] = rotate_answer(balanced[idx], deficit_ans)
                deficit[deficit_ans] -= 1
                if deficit[deficit_ans] == 0:
                    del deficit[deficit_ans]
                break

# Verify
final_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
for q in balanced:
    final_counts[q["answer"]] += 1
print(f"Final answer distribution: {final_counts}")

# Re-number IDs
for i, q in enumerate(balanced):
    q["id"] = f"eng_{501 + i:03d}"

# Verify correctness - make sure each answer letter matches the correct choice
errors = 0
for q in balanced:
    ans_idx = {"A": 0, "B": 1, "C": 2, "D": 3}[q["answer"]]
    choice = q["choices"][ans_idx]
    # For en_to_ja, the correct Japanese meaning should be in the explanation
    # For ja_to_en, the correct English word should be in the explanation
    word = q["word"]
    if q["pattern"] == "ja_to_en":
        if word.lower() not in choice.lower():
            errors += 1
            print(f"ERROR in {q['id']}: answer {q['answer']} = '{choice}' but word is '{word}'")

print(f"Verification errors: {errors}")

# Combine
all_questions = original + balanced
data["questions"] = all_questions
print(f"\nFinal total questions: {len(all_questions)}")

# Final unique word count
all_words = set(q["word"] for q in all_questions)
print(f"Total unique words: {len(all_words)}")
new_unique = set(q["word"] for q in balanced)
print(f"New unique words: {len(new_unique)}")

# Level distribution for new words
new_a2 = len(set(q["word"] for q in balanced if q["level"] == "A2"))
new_b1 = len(set(q["word"] for q in balanced if q["level"] == "B1"))
print(f"New A2 words: {new_a2}, New B1 words: {new_b1}")

# Write
with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nFile written successfully!")

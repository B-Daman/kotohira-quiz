"""一時スクリプト: 金刀比羅宮 授与品ページから問題追加"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/charms/article.php"
sl = f"（出典: [金刀比羅宮 授与品]({url})）"

new_qs = [
    {
        "id": "kotohira_571", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮で最も有名なお守りの色は何色ですか？",
        "choices": ["A. 赤色", "B. 白色", "C. 黄色", "D. 青色"],
        "answer": "C",
        "explanation": f"「幸福の黄色いお守り」は金刀比羅宮を代表する鬱金色（黄色）の肌守りです。黄色は稲や麦の稔りの色、豊穣の色とされています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_572", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の「親子守り」のデザインに関わったイラストレーター「犬ん子」が手掛けた作品は何ですか？",
        "choices": ["A. 映画「こんぴら物語」", "B. 単行本「こんぴら狗」の装画・挿絵", "C. 金刀比羅宮の公式ロゴ", "D. 琴平町の観光ポスター"],
        "answer": "B",
        "explanation": f"犬ん子（いぬんこ）は単行本「こんぴら狗」の装画・挿絵やNHK朝ドラ「おちょやん」も手掛けたイラストレーターです。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_573", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の「こんぴら狗守り《首輪リード型》」に使われている伝統素材は何ですか？",
        "choices": ["A. 西陣織", "B. 博多織", "C. 真田紐", "D. 組紐"],
        "answer": "C",
        "explanation": f"450年の伝統がある国産の真田紐が使われています。愛犬に着けて金刀比羅宮に参拝すれば、江戸時代のこんぴら狗の代参に思いをはせることができます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_574", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の海上安全守り（ステッカー型）にデザインされている「セーマンドーマン」はどこの文化に由来しますか？",
        "choices": ["A. 沖縄の漁師", "B. 三重県志摩地方の海女", "C. 紀州の船乗り", "D. 瀬戸内海の漁師"],
        "answer": "B",
        "explanation": f"セーマンドーマンは金刀比羅宮の鳥羽分社が鎮座する三重県志摩地方の海女さんが身につける魔除けです。五芒星がデザインされています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_575", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮オリジナル紋様「こんぴら七宝」の円の下側は何をイメージしていますか？",
        "choices": ["A. 山", "B. 石段", "C. 波", "D. 雲"],
        "answer": "C",
        "explanation": f"「こんぴら七宝」の円の下側は海の神様を表す「波」を、上側は象頭山の「木の葉」をイメージしたデザインです。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_576", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の「桜蒔絵御朱印帳」のモチーフになっているのは、御本宮のどの部分ですか？",
        "choices": ["A. 屋根の鬼瓦", "B. 格天井の桜樹木地蒔絵", "C. 鳥居の装飾", "D. 石段の模様"],
        "answer": "B",
        "explanation": f"重要文化財に指定答申された御本宮の格天井に施されている桜樹木地蒔絵をモチーフにデザインされています。濃藍と淡黄の2色展開です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_577", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の厳魂神社の御朱印紙に描かれている「烏天狗」はどのような存在とされていますか？",
        "choices": ["A. 悪霊を追い払う", "B. 旅人を導く", "C. 五穀豊穣をもたらす", "D. 海上を守る"],
        "answer": "B",
        "explanation": f"御朱印紙には威徳巖の天狗と烏天狗の彫り物が描かれており、烏天狗は旅人を導くといわれています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_578", "category": "shrine", "difficulty": "medium",
        "question": "単行本「こんぴら狗」の主人公の犬の名前は何ですか？",
        "choices": ["A. ゲン", "B. ポチ", "C. ムツキ", "D. タロウ"],
        "answer": "C",
        "explanation": f"主人公は雑種犬のムツキ。「こんぴら狗」として江戸から金毘羅参りに向かう物語です。著者は今井恭子、装画・挿絵は犬ん子（いぬんこ）。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_579", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の白峰神社の御朱印紙にデザインされている歌は、誰が詠んだ小倉百人一首の歌ですか？",
        "choices": ["A. 大物主神", "B. 崇徳天皇", "C. 厳魂彦命", "D. 菅原道真"],
        "answer": "B",
        "explanation": f"白峰神社の御祭神・崇徳天皇が詠んだ「瀬をはやみ 岩にせかるる 滝川の われても末に 逢はむとぞ思ふ」がデザインされています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_580", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮とコラボレーションした御朱印帳を制作した航空会社はどこですか？",
        "choices": ["A. JAL", "B. ANA", "C. スカイマーク", "D. ピーチ"],
        "answer": "B",
        "explanation": f"金刀比羅宮とANAのコラボレーション御朱印帳があり、海をイメージした波のレーザーカットに石段・鳥居・社殿・こんぴら狗が描かれています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_571-580)")
print(f"Total: {len(data['questions'])} questions")

for q in new_qs:
    ans_idx = ord(q["answer"]) - ord("A")
    print(f"\n[{q['id']}] {q['difficulty']}")
    print(f"  Q: {q['question']}")
    print(f"  正解: {q['choices'][ans_idx]}")

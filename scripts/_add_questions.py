"""一時スクリプト: トップページから追加問題を生成"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

url = "https://www.konpira.or.jp/"
sl = "（出典: [金刀比羅宮 公式サイト](https://www.konpira.or.jp/)）"

new_qs = [
    {
        "id": "kotohira_521", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の宝物館はどの曜日に休館ですか？",
        "choices": ["A. 月曜日", "B. 火曜日", "C. 水曜日", "D. 木曜日"],
        "answer": "B",
        "explanation": f"宝物館の開館日は土日祝日等で、期間中は火曜日が休館日です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_522", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の高橋由一館の通常の開館日はいつですか？",
        "choices": ["A. 毎日", "B. 平日のみ", "C. 土日祝日", "D. 月・水・金"],
        "answer": "C",
        "explanation": f"高橋由一館の通常開館日は土日祝日です。そのほか4/29〜5/6、6/16〜9/30、12/30〜1/3も開館します。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_523", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の御本宮での御祈祷の受付は何時までですか？",
        "choices": ["A. 15時", "B. 15時半", "C. 16時", "D. 16時半"],
        "answer": "D",
        "explanation": f"御祈祷の受付は午後4時半（16時半）までです。御祈祷自体は午前9時〜午後5時。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_524", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の授与所の営業時間は何時から何時までですか？",
        "choices": ["A. 7時〜17時", "B. 8時〜16時半", "C. 8時半〜17時", "D. 9時〜17時"],
        "answer": "C",
        "explanation": f"授与所の営業時間は午前8時半〜午後5時です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_525", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮でお神楽が奏進されるのは、いくら以上の献金をした場合ですか？",
        "choices": ["A. 3万円以上", "B. 5万円以上", "C. 10万円以上", "D. 20万円以上"],
        "answer": "C",
        "explanation": f"お神楽は10万円以上の献金をした場合に奏進されます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_526", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の海上安全御守（ミサンガ型）は令和8年4月1日からいくらですか？",
        "choices": ["A. 500円", "B. 800円", "C. 1,000円", "D. 1,500円"],
        "answer": "C",
        "explanation": f"海上安全御守（ミサンガ型・ステッカー型）は令和8年4月1日より1,000円に改定されます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_527", "category": "shrine", "difficulty": "hard",
        "question": "金刀比羅宮の分社はいくつありますか？",
        "choices": ["A. 3社", "B. 6社", "C. 10社", "D. 15社"],
        "answer": "B",
        "explanation": f"東京分社、尾張分社、鳥羽分社、神戸分社、出雲分社、松山分社の6分社があります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_528", "category": "event", "difficulty": "easy",
        "question": "金刀比羅宮の桜花祭は毎年何月何日に行われますか？",
        "choices": ["A. 3月21日", "B. 4月1日", "C. 4月10日", "D. 5月5日"],
        "answer": "C",
        "explanation": f"桜花祭は例年4月10日に斎行されます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_529", "category": "event", "difficulty": "easy",
        "question": "金刀比羅宮の紅葉祭は毎年何月何日に行われますか？",
        "choices": ["A. 10月10日", "B. 11月3日", "C. 11月10日", "D. 11月23日"],
        "answer": "C",
        "explanation": f"紅葉祭は例年11月10日に斎行されます。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_530", "category": "gourmet", "difficulty": "medium",
        "question": "カフェ＆レストラン神椿の料理・スイーツを担当しているのはどこですか？",
        "choices": ["A. 帝国ホテル", "B. 東京銀座の資生堂パーラー", "C. 京都の虎屋", "D. 高松の三越"],
        "answer": "B",
        "explanation": f"神椿の料理やスイーツは東京銀座の資生堂パーラーが担当しています。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_531", "category": "shrine", "difficulty": "medium",
        "question": "カフェ＆レストラン神椿の駐車場は石段の何段目にありますか？",
        "choices": ["A. 100段目", "B. 300段目", "C. 500段目", "D. 785段目"],
        "answer": "C",
        "explanation": f"神椿の駐車場は石段500段目にあります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_532", "category": "geography", "difficulty": "medium",
        "question": "金刀比羅宮に車で参拝する際、ナビの目的地として推奨されているのはどこですか？",
        "choices": ["A. 金刀比羅宮", "B. JR琴平駅", "C. 琴平町役場", "D. 参道入口"],
        "answer": "B",
        "explanation": f"車のナビゲーション目的地はJR琴平駅とすることが推奨されています。金刀比羅宮には駐車場がありません。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_533", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮に専用駐車場はありますか？",
        "choices": ["A. 100台分ある", "B. 神椿利用者のみある", "C. ない", "D. 500台分ある"],
        "answer": "C",
        "explanation": f"金刀比羅宮には駐車場がありません。JR琴平駅周辺の駐車場を利用します。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_534", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮の御本宮から奥社までの所要時間は片道どのくらいですか？",
        "choices": ["A. 約20分", "B. 約30分", "C. 約45分", "D. 約1時間"],
        "answer": "D",
        "explanation": f"御本宮から奥社までは片道約1時間かかります。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_535", "category": "shrine", "difficulty": "medium",
        "question": "金刀比羅宮のお問い合わせ電話番号は何番ですか？",
        "choices": ["A. 0877-75-1234", "B. 0877-75-2121", "C. 0877-75-3333", "D. 0877-75-5555"],
        "answer": "B",
        "explanation": f"お問い合わせ電話番号は0877-75-2121です。午後5時以降は翌日に順次対応。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_536", "category": "history", "difficulty": "medium",
        "question": "金刀比羅宮では例年何月に蹴鞠を公開していましたか？",
        "choices": ["A. 1月と8月", "B. 3月と9月", "C. 5月と7月", "D. 4月と10月"],
        "answer": "C",
        "explanation": f"金刀比羅宮では例年5月と7月に蹴鞠を公開していました。蹴鞠は県無形民俗文化財です。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
    {
        "id": "kotohira_537", "category": "history", "difficulty": "hard",
        "question": "日本で初めての神前結婚式が行われたのはいつですか？",
        "choices": ["A. 明治30年3月3日", "B. 明治34年3月3日", "C. 大正元年3月3日", "D. 明治34年5月10日"],
        "answer": "B",
        "explanation": f"初の神前結婚式は明治34年3月3日に日比谷大神宮で行われました。明治33年5月10日の嘉仁親王と九條節子妃の成婚を記念して制定されたものです。{sl}",
        "source": url, "reviewed": False, "enabled": True,
    },
]

KOTOHIRA_FILE = r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json"

with open(KOTOHIRA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
data["questions"].extend(new_qs)
with open(KOTOHIRA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_qs)} questions (kotohira_521-537)")
print(f"Total: {len(data['questions'])} questions")

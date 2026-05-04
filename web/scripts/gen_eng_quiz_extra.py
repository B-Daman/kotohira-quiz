import json
import urllib.parse
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "public" / "data" / "english_questions.json"

# Read existing file
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing = data["questions"]
print(f"Existing questions: {len(existing)}")

existing_words = set()
for q in existing:
    existing_words.add(q["word"])
print(f"Existing unique words: {len(existing_words)}")

# Find the last ID
last_id = max(int(q["id"].replace("eng_", "")) for q in existing)
print(f"Last ID: eng_{last_id}")

# 30 additional words to reach 250 new words total
extra_words = [
    ("dispute", "dispjúːt", "紛争", "B1",
     ["A. 紛争争い", "B. 表示画面", "C. 処分廃棄", "D. 配分分配"], "A",
     ["A. dispute", "B. display", "C. dispose", "D. disrupt"], "A",
     "The territorial dispute lasted for decades.（領土紛争は何十年も続いた。）",
     "They resolved the dispute through negotiation.（彼らは交渉で紛争を解決した。）"),
    ("conscious", "kɑ́nʃəs", "意識的な", "B1",
     ["A. 意識的な", "B. 良心的な", "C. 結果的な", "D. 一定不変の"], "A",
     ["A. conscious", "B. cautious", "C. conscience", "D. consensus"], "A",
     "She made a conscious effort to be polite.（彼女は意識的に礼儀正しくする努力をした。）",
     "Be conscious of your surroundings.（周囲に意識的であれ。）"),
    ("consent", "kənsént", "同意", "B1",
     ["A. 内容物質", "B. 文脈背景", "C. 同意承諾", "D. 概念思想"], "C",
     ["A. consent", "B. concept", "C. concern", "D. content"], "A",
     "You need parental consent to join.（参加するには親の同意が必要だ。）",
     "She gave her consent to the procedure.（彼女はその手続きに同意した。）"),
    ("contemplate", "kɑ́ntəmplèit", "熟考する", "B1",
     ["A. 見下す行為", "B. 汚染する", "C. 対抗する", "D. 熟考する"], "D",
     ["A. contemplate", "B. contaminate", "C. contradict", "D. contempt"], "A",
     "He sat quietly to contemplate his future.（彼は静かに座って将来を熟考した。）",
     "Take time to contemplate the decision.（その決定を熟考する時間を取りなさい。）"),
    ("correspond", "kɔ̀ːrəspɑ́nd", "対応する", "B1",
     ["A. 修正する", "B. 対応する", "C. 腐敗する", "D. 相談する"], "B",
     ["A. correspond", "B. corporate", "C. correlate", "D. corrupt"], "A",
     "The results correspond to our predictions.（結果は予測に対応している。）",
     "Each number corresponds to a letter.（各数字は文字に対応している。）"),
    ("congress", "kɑ́ŋgrəs", "議会", "B1",
     ["A. 議会組織", "B. 混雑状態", "C. 祝辞表現", "D. 一致同意"], "A",
     ["A. congress", "B. congest", "C. converse", "D. conquest"], "A",
     "Congress passed the new education bill.（議会は新しい教育法案を可決した。）",
     "The issue was debated in congress.（その問題は議会で議論された。）"),
    ("constitute", "kɑ́nstətjùːt", "構成する", "B1",
     ["A. 構成する", "B. 建設する", "C. 相談する", "D. 消費する"], "A",
     ["A. constitute", "B. construct", "C. constraint", "D. consume"], "A",
     "Women constitute 60% of the workforce.（女性が労働力の60%を構成する。）",
     "These actions constitute a violation of the law.（これらの行動は法律違反を構成する。）"),
    ("conform", "kənfɔ́ːrm", "従う", "B1",
     ["A. 確認する", "B. 対立する", "C. 従う適合", "D. 混乱させる"], "C",
     ["A. confirm", "B. confront", "C. conform", "D. confuse"], "C",
     "Students must conform to the dress code.（学生は服装規定に従わなければならない。）",
     "The product conforms to safety standards.（その製品は安全基準に従っている。）"),
    ("compel", "kəmpél", "強いる", "B1",
     ["A. 訴える", "B. 編集する", "C. 強いる迫る", "D. 競争する"], "C",
     ["A. compel", "B. compete", "C. compile", "D. compose"], "A",
     "The law compels employers to pay minimum wage.（法律は雇用者に最低賃金を支払うことを強いる。）",
     "Nothing can compel me to change my mind.（何も私の考えを変えることを強いることはできない。）"),
    ("deprive", "dipráiv", "奪う", "B1",
     ["A. 由来する", "B. 奪い取る", "C. 軽蔑する", "D. 望む欲する"], "B",
     ["A. derive", "B. deprive", "C. despise", "D. desire"], "B",
     "Sleep deprivation can deprive you of focus.（睡眠不足は集中力を奪うことがある。）",
     "No one should be deprived of education.（誰も教育を奪われるべきではない。）"),
    ("designate", "dézignèit", "指定する", "B1",
     ["A. 設計する", "B. 希望する", "C. 指定する", "D. 絶望する"], "C",
     ["A. designate", "B. devastate", "C. dominate", "D. duplicate"], "A",
     "This area is designated as a national park.（この地域は国立公園に指定されている。）",
     "She was designated as team leader.（彼女はチームリーダーに指定された。）"),
    ("estate", "istéit", "不動産", "B1",
     ["A. 推定値", "B. 不動産", "C. 見積額", "D. 確立度"], "B",
     ["A. estate", "B. estimate", "C. establish", "D. eternal"], "A",
     "The family owns a large estate in the countryside.（その家族は田舎に大きな不動産を所有している。）",
     "Real estate prices have risen dramatically.（不動産価格は劇的に上昇した。）"),
    ("excess", "iksés", "過剰", "B1",
     ["A. 過剰分量", "B. 接近行為", "C. 成功達成", "D. 運動活動"], "A",
     ["A. excess", "B. access", "C. express", "D. exercise"], "A",
     "Excess sugar is bad for your health.（過剰な砂糖は健康に悪い。）",
     "The excess baggage fee is expensive.（超過手荷物料金は高い。）"),
    ("extract", "ikstrǽkt", "抽出する", "B1",
     ["A. 抽出する", "B. 極端にする", "C. 追加する", "D. 消滅する"], "A",
     ["A. extract", "B. extreme", "C. extinct", "D. exclaim"], "A",
     "They extract oil from olives.（彼らはオリーブから油を抽出する。）",
     "The dentist had to extract the tooth.（歯科医はその歯を抽出しなければならなかった。）"),
    ("impulse", "ímpʌls", "衝動", "B1",
     ["A. 衝動的欲求", "B. 影響力効果", "C. 衝突の結果", "D. 輸入品目"], "A",
     ["A. impulse", "B. impact", "C. import", "D. impress"], "A",
     "She bought the dress on impulse.（彼女は衝動的にそのドレスを買った。）",
     "Try to resist the impulse to eat sweets.（甘いものを食べたい衝動に抵抗しなさい。）"),
    ("incline", "inkláin", "傾く", "B1",
     ["A. 含む組入", "B. 傾く傾斜", "C. 増加する", "D. 示す表す"], "B",
     ["A. include", "B. incline", "C. increase", "D. indicate"], "B",
     "I incline to agree with your opinion.（あなたの意見に同意する方に傾く。）",
     "The road inclines steeply uphill.（その道は急な上り坂に傾いている。）"),
    ("intensive", "inténsiv", "集中的な", "B1",
     ["A. 意図的な", "B. 集中的な", "C. 不可欠な", "D. 対話的な"], "B",
     ["A. intensive", "B. intentional", "C. interactive", "D. internal"], "A",
     "The course requires intensive study.（その課程は集中的な学習が必要だ。）",
     "Intensive care is provided in this ward.（この病棟では集中的なケアが提供される。）"),
    ("humiliate", "hjuːmílièit", "屈辱を与える", "B1",
     ["A. 加湿する", "B. 屈辱を与える", "C. 人間らしくする", "D. ユーモアある"], "B",
     ["A. humiliate", "B. humidify", "C. humanize", "D. harmonize"], "A",
     "Don't humiliate people in public.（人前で人に屈辱を与えてはいけない。）",
     "He was humiliated by the defeat.（彼は敗北によって屈辱を与えられた。）"),
    ("critic", "krítik", "批評家", "B1",
     ["A. 危機的状況", "B. 批評家評論", "C. 犯罪者", "D. 基準事項"], "B",
     ["A. crisis", "B. critic", "C. criminal", "D. critical"], "B",
     "The film received praise from critics.（その映画は批評家から賞賛を受けた。）",
     "She is a well-known art critic.（彼女は有名な美術批評家だ。）"),
    ("attribute", "ətríbjuːt", "帰する", "B1",
     ["A. 帰する原因", "B. 態度行動", "C. 引きつける", "D. 出席する"], "A",
     ["A. attitude", "B. attribute", "C. attract", "D. attorney"], "B",
     "She attributes her success to hard work.（彼女は成功を努力に帰する。）",
     "The painting is attributed to Monet.（その絵画はモネの作品に帰される。）"),
    ("abundant", None, None, None, None, None, None, None, None, None),  # already added
    # More A2 level words to balance distribution
    ("grocery", None, None, None, None, None, None, None, None, None),  # already exists
    ("pedestrian", "pədéstriən", "歩行者", "A2",
     ["A. 歩行者", "B. 小児科医", "C. 教育学者", "D. 悲観主義"], "A",
     ["A. pedestrian", "B. pediatric", "C. peninsula", "D. pessimist"], "A",
     "Always watch out for pedestrians.（常に歩行者に注意してください。）",
     "The pedestrian crossing is ahead.（歩行者用横断歩道はこの先にある。）"),
    ("specimen", None, None, None, None, None, None, None, None, None),  # already added
    ("suburb", "sʌ́bəːrb", "郊外", "A2",
     ["A. 郊外地域", "B. 地下鉄", "C. 代用品", "D. 主題内容"], "A",
     ["A. suburb", "B. subway", "C. substance", "D. subject"], "A",
     "They live in a quiet suburb.（彼らは静かな郊外に住んでいる。）",
     "Many families prefer the suburbs.（多くの家庭が郊外を好む。）"),
    ("tuition", "tjuːíʃən", "授業料", "A2",
     ["A. 授業料金", "B. 直感感覚", "C. 伝統行事", "D. 翻訳作業"], "A",
     ["A. tuition", "B. intuition", "C. tradition", "D. transition"], "A",
     "University tuition fees have increased.（大学の授業料が上がった。）",
     "She received a scholarship to cover tuition.（彼女は授業料をまかなう奨学金を受け取った。）"),
    ("colleague", None, None, None, None, None, None, None, None, None),  # already exists
    ("warehouse", "wéərhaus", "倉庫", "A2",
     ["A. 倉庫施設", "B. 戦争行為", "C. 警告通知", "D. 保証書類"], "A",
     ["A. warehouse", "B. warfare", "C. warranty", "D. wardrobe"], "A",
     "The goods are stored in a warehouse.（商品は倉庫に保管されている。）",
     "The company built a new warehouse.（会社は新しい倉庫を建てた。）"),
    ("aisle", "áil", "通路", "A2",
     ["A. 島の地形", "B. 通路座席", "C. 目的意図", "D. 不在状態"], "B",
     ["A. island", "B. aisle", "C. aside", "D. isolate"], "B",
     "Please keep the aisle clear.（通路を空けておいてください。）",
     "She walked down the aisle of the airplane.（彼女は飛行機の通路を歩いた。）"),
    ("beverage", "bévəridʒ", "飲み物", "A2",
     ["A. 飲み物飲料", "B. 利用可能", "C. 平均値段", "D. 行動態度"], "A",
     ["A. beverage", "B. behavior", "C. bargain", "D. benefit"], "A",
     "Hot and cold beverages are available.（温かい飲み物と冷たい飲み物がある。）",
     "What beverage would you like?（何の飲み物がいいですか？）"),
    ("pedestrian", None, None, None, None, None, None, None, None, None),  # already added
    ("corridor", "kɔ́ːridɔːr", "廊下", "A2",
     ["A. 廊下通路", "B. 回廊庭園", "C. 海岸地域", "D. 指揮者"], "A",
     ["A. corridor", "B. courtyard", "C. coastline", "D. conductor"], "A",
     "The corridor leads to the conference room.（廊下は会議室に通じている。）",
     "Please don't run in the corridor.（廊下を走らないでください。）"),
    ("heritage", None, None, None, None, None, None, None, None, None),  # already added
    ("intersection", "ìntərsékʃən", "交差点", "A2",
     ["A. 交差点", "B. 面接試験", "C. 中断状態", "D. 相互作用"], "A",
     ["A. intersection", "B. interview", "C. interruption", "D. interaction"], "A",
     "Turn left at the intersection.（交差点で左に曲がってください。）",
     "There was an accident at the intersection.（交差点で事故があった。）"),
    ("pedestrian", None, None, None, None, None, None, None, None, None),  # already added
    ("nuance", "njúːɑːns", "ニュアンス", "B1",
     ["A. ニュアンス", "B. 迷惑行為", "C. 看護業務", "D. 栄養成分"], "A",
     ["A. nuisance", "B. nuance", "C. nursing", "D. nutrient"], "B",
     "There is a subtle nuance in her words.（彼女の言葉には微妙なニュアンスがある。）",
     "Understanding cultural nuances is important.（文化的なニュアンスを理解することは重要だ。）"),
    ("prominent", "prɑ́mənənt", "著名な", "B1",
     ["A. 著名な目立つ", "B. 約束の内容", "C. 促進の行為", "D. 即座の反応"], "A",
     ["A. prominent", "B. promising", "C. promoting", "D. prompt"], "A",
     "She is a prominent scientist.（彼女は著名な科学者だ。）",
     "The building is in a prominent location.（その建物は目立つ場所にある。）"),
    ("rhetoric", "rétərik", "修辞法", "B1",
     ["A. 修辞法技術", "B. リズム感覚", "C. 押韻構造", "D. 暴動騒乱"], "A",
     ["A. rhetoric", "B. rhythm", "C. rhyme", "D. ritual"], "A",
     "The politician's rhetoric was persuasive.（その政治家の修辞法は説得力があった。）",
     "Empty rhetoric will not solve the problem.（空虚な修辞法では問題は解決しない。）"),
]

# Filter out None entries
extra_words = [w for w in extra_words if w[1] is not None]
print(f"Extra words to add: {len(extra_words)}")

# Check for duplicates
extra_word_names = [w[0] for w in extra_words]
dupes = [w for w in extra_word_names if w in existing_words]
if dupes:
    print(f"WARNING: Duplicates with existing: {dupes}")
    extra_words = [w for w in extra_words if w[0] not in existing_words]
    print(f"After removing dupes: {len(extra_words)}")

# Check internal duplicates
from collections import Counter
counts = Counter([w[0] for w in extra_words])
internal_dupes = {w: c for w, c in counts.items() if c > 1}
if internal_dupes:
    print(f"WARNING: Internal duplicates: {internal_dupes}")
    # Deduplicate
    seen = set()
    deduped = []
    for w in extra_words:
        if w[0] not in seen:
            seen.add(w[0])
            deduped.append(w)
    extra_words = deduped
    print(f"After dedup: {len(extra_words)}")

# Generate questions
new_questions = []
q_id = last_id + 1
answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

for word_data in extra_words:
    word, pron, ja_meaning, level, en_ja_choices, en_ja_ans, ja_en_choices, ja_en_ans, en_ja_ex, ja_en_ex = word_data

    search_url = f"https://www.google.com/search?q={word}+meaning"
    translate_url = f"https://translate.google.co.jp/details?sl=en&tl=ja&text={urllib.parse.quote(word)}&op=translate"

    en_to_ja = {
        "id": f"eng_{q_id:03d}",
        "level": level,
        "pattern": "en_to_ja",
        "question": f"\"{word}\" の意味は？",
        "choices": en_ja_choices,
        "answer": en_ja_ans,
        "explanation": f"{word} = {ja_meaning}。例: {en_ja_ex}",
        "word": word,
        "pronunciation": pron,
        "reviewed": True,
        "enabled": True,
        "search_url": search_url,
        "translate_url": translate_url
    }
    new_questions.append(en_to_ja)
    answer_counts[en_ja_ans] += 1
    q_id += 1

    ja_to_en = {
        "id": f"eng_{q_id:03d}",
        "level": level,
        "pattern": "ja_to_en",
        "question": f"「{ja_meaning}」を英語で言うと？",
        "choices": ja_en_choices,
        "answer": ja_en_ans,
        "explanation": f"{word} = {ja_meaning}。例: {ja_en_ex}",
        "word": word,
        "pronunciation": pron,
        "reviewed": True,
        "enabled": True,
        "search_url": search_url,
        "translate_url": translate_url
    }
    new_questions.append(ja_to_en)
    answer_counts[ja_en_ans] += 1
    q_id += 1

print(f"\nGenerated {len(new_questions)} extra questions")
print(f"Answer distribution: {answer_counts}")

# Append to existing
all_questions = existing + new_questions
data["questions"] = all_questions

# Final stats
all_words = set()
for q in all_questions:
    all_words.add(q["word"])
print(f"\nTotal questions: {len(all_questions)}")
print(f"Total unique words: {len(all_words)}")
print(f"Last ID: eng_{q_id - 1}")

# Level counts
a2_count = len(set(q["word"] for q in all_questions if q["level"] == "A2"))
b1_count = len(set(q["word"] for q in all_questions if q["level"] == "B1"))
print(f"A2 unique words (all): {a2_count}, B1 unique words (all): {b1_count}")

# New words only level counts
new_all_words = set(q["word"] for q in all_questions[500:])
new_a2 = len(set(q["word"] for q in all_questions[500:] if q["level"] == "A2"))
new_b1 = len(set(q["word"] for q in all_questions[500:] if q["level"] == "B1"))
print(f"New A2 words: {new_a2}, New B1 words: {new_b1}")
print(f"New unique words: {len(new_all_words)}")

# Overall answer distribution
total_ans = {"A": 0, "B": 0, "C": 0, "D": 0}
for q in all_questions[500:]:
    total_ans[q["answer"]] += 1
print(f"New questions answer distribution: {total_ans}")

# Write
with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nFile written successfully!")

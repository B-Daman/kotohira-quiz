import json

with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

missing_questions = [
    {"id":"kotohira_201","category":"event","difficulty":"easy","question":"金刀比羅宮で毎日行われている祭祀の名前は何ですか？","choices":["A. 月次祭","B. 例大祭","C. 朝御饌祭と夕御饌祭","D. 桜花祭"],"answer":"C","explanation":"朝御饌祭と夕御饌祭は毎日行われています。神様に食事をお供えする大切な日々の祭祀です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_202","category":"event","difficulty":"medium","question":"金刀比羅宮の節分祭が行われるのは何月何日ですか？","choices":["A. 1月15日","B. 2月3日","C. 3月3日","D. 4月3日"],"answer":"B","explanation":"金刀比羅宮の節分祭は2月3日に行われます。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_203","category":"event","difficulty":"medium","question":"石段マラソンのコースは何種類ありますか？","choices":["A. 1種類","B. 2種類","C. 3種類","D. 4種類"],"answer":"B","explanation":"石段マラソンは本宮コース（785段）と奥社コース（1,368段）の2種類があります。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_204","category":"event","difficulty":"hard","question":"金刀比羅宮で祈年祭が行われるのは何月何日ですか？","choices":["A. 1月7日","B. 2月11日","C. 2月17日","D. 3月3日"],"answer":"C","explanation":"金刀比羅宮の祈年祭は2月17日に行われます。五穀豊穣を祈願する重要な祭祀です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_205","category":"event","difficulty":"easy","question":"金刀比羅宮の新酒祭は何月に行われますか？","choices":["A. 1月","B. 5月","C. 9月","D. 11月"],"answer":"D","explanation":"金刀比羅宮の新酒祭は11月に行われます。その年の新酒を神前に供える祭祀です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_206","category":"event","difficulty":"medium","question":"こんぴら夏祭りと七夕蹴鞠、どちらが先に行われますか？","choices":["A. こんぴら夏祭り（7月下旬）","B. 七夕蹴鞠（7月7日）","C. 同じ日","D. 年によって異なる"],"answer":"B","explanation":"七夕蹴鞠は7月7日、こんぴら夏祭りは7月下旬なので、七夕蹴鞠が先です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_207","category":"event","difficulty":"hard","question":"金刀比羅宮で毎月行われる月次祭は、年間で合計何回行われますか？","choices":["A. 12回","B. 24回","C. 36回","D. 48回"],"answer":"C","explanation":"月次祭は毎月1日・10日・20日の3回行われるため、年間で3回×12ヶ月＝36回です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_208","category":"event","difficulty":"easy","question":"金刀比羅宮の灯篭流しはどのような行事に関連していますか？","choices":["A. 正月","B. 節分","C. お盆","D. 七五三"],"answer":"C","explanation":"灯篭流しは8月15日に行われるお盆の行事です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_209","category":"event","difficulty":"medium","question":"2025年の四国こんぴら歌舞伎は何月に開催されましたか？","choices":["A. 1月","B. 4月","C. 7月","D. 10月"],"answer":"B","explanation":"2025年の第38回四国こんぴら歌舞伎は4月に開催されました。中村獅童が出演しました。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_210","category":"event","difficulty":"hard","question":"こんぴら十帖が開始されてから2026年4月10日までに約何回開催されたことになりますか？","choices":["A. 約20回","B. 約30回","C. 約41回","D. 約50回"],"answer":"C","explanation":"2022年11月10日から2026年4月10日まで、毎月10日に開催で約41回（41ヶ月）です。","source":"konpie-bot/knowledge_base/event","reviewed":True,"enabled":True},
    {"id":"kotohira_211","category":"geography","difficulty":"easy","question":"琴平町はどの郡にありますか？","choices":["A. 綾歌郡","B. 仲多度郡","C. 小豆郡","D. 木田郡"],"answer":"B","explanation":"琴平町は香川県仲多度郡にあります。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_212","category":"geography","difficulty":"medium","question":"JR琴平駅から金刀比羅宮の御本宮まで、徒歩の合計時間はおよそ何分ですか？","choices":["A. 約20分","B. 約35分","C. 約45分","D. 約60分"],"answer":"C","explanation":"JR琴平駅から御本宮まで徒歩約45分です。参道入口まで約10分、そこから石段を登って約35分です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_213","category":"geography","difficulty":"hard","question":"高松から琴平までJRとことでんの運賃の差額はいくらですか？","choices":["A. 100円","B. 180円","C. 240円","D. 340円"],"answer":"C","explanation":"JRは860円、ことでんは620円なので、差額は240円です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_214","category":"geography","difficulty":"medium","question":"琴平町の町営駐車場の容量と料金の組み合わせで正しいのはどれですか？","choices":["A. 100台・300円/日","B. 200台・500円/日","C. 300台・800円/日","D. 500台・1,000円/日"],"answer":"B","explanation":"琴平町の町営駐車場は200台収容で、1日500円です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_215","category":"geography","difficulty":"easy","question":"琴平町に通じるこんぴら街道で、四国の東側から来る街道は何ですか？","choices":["A. 丸亀街道","B. 多度津街道","C. 阿波街道","D. 伊予土佐街道"],"answer":"C","explanation":"四国の東側（徳島方面）から来るのは阿波街道です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_216","category":"geography","difficulty":"hard","question":"高知から琴平までの所要時間と運賃の組み合わせで正しいのはどれですか？","choices":["A. 約1時間・1,680円","B. 約1時間30分・2,340円","C. 約2時間30分・3,410円","D. 約3時間・4,500円"],"answer":"C","explanation":"高知から琴平までは約2時間30分、3,410円です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_217","category":"geography","difficulty":"medium","question":"JR琴平駅の建築様式は何風ですか？","choices":["A. 和風","B. 北欧風","C. ゴシック風","D. アールデコ風"],"answer":"B","explanation":"JR琴平駅は赤い三角屋根の北欧風平屋です。大正11年（1922年）に建設されました。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_218","category":"geography","difficulty":"easy","question":"琴平町から本州（岡山）に行くにはどの橋を渡りますか？","choices":["A. 明石海峡大橋","B. しまなみ海道","C. 瀬戸大橋","D. 大鳴門橋"],"answer":"C","explanation":"琴平町から岡山に行くには瀬戸大橋を渡ります。JR特急で約1時間です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_219","category":"geography","difficulty":"hard","question":"琴平参宮電鉄と琴平急行電鉄で、営業期間が短かったのはどちらですか？","choices":["A. 琴平参宮電鉄（約41年）","B. 琴平急行電鉄（14年）","C. 同じ","D. 不明"],"answer":"B","explanation":"琴平急行電鉄は1930〜1944年のわずか14年間で、琴平参宮電鉄（1922〜1963年、約41年）より短かったです。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
    {"id":"kotohira_220","category":"geography","difficulty":"medium","question":"高松空港から琴平町までの交通手段と料金で正しいのはどれですか？","choices":["A. バス・約800円","B. 車・約1,500円","C. 電車・約2,000円","D. タクシー・約5,000円"],"answer":"B","explanation":"高松空港から琴平町まで車で約45分、約1,500円です。","source":"konpie-bot/knowledge_base/geography","reviewed":True,"enabled":True},
]

# Insert missing questions at the correct position
# Find the index where kotohira_221 is
idx_221 = None
for i, q in enumerate(data["questions"]):
    if q["id"] == "kotohira_221":
        idx_221 = i
        break

if idx_221 is not None:
    for j, q in enumerate(missing_questions):
        data["questions"].insert(idx_221 + j, q)
    # Move the inserted items before 221
    # Actually, insert before 221 index
    # Remove them from where they were inserted (after 221)
    # and re-insert before 221
    pass

# Actually simpler: just insert all before the 221 index
# Let me redo this properly
with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find where to insert (before kotohira_221)
insert_idx = None
for i, q in enumerate(data["questions"]):
    if q["id"] == "kotohira_221":
        insert_idx = i
        break

if insert_idx is not None:
    for j, q in enumerate(missing_questions):
        data["questions"].insert(insert_idx + j, q)

with open(r"C:\Users\user\hisho-bot\data\quiz\kotohira_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total questions: {len(data['questions'])}")

# Verify no missing IDs
existing_ids = {q["id"] for q in data["questions"]}
missing = []
for i in range(1, 501):
    qid = f"kotohira_{i:03d}"
    if qid not in existing_ids:
        missing.append(qid)
if missing:
    print(f"Still missing: {missing}")
else:
    print("All 500 IDs present!")

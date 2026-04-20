#!/usr/bin/env python3
"""
Fix answer distribution and add more words to reach ~400.
Shuffles choice positions to distribute answers evenly across A/B/C/D.
"""

import json
import urllib.parse
import random

random.seed(42)  # Reproducible

def make_search_url(word):
    return "https://www.google.com/search?q=" + urllib.parse.quote(word, safe='')

def make_translate_url(word):
    return "https://translate.google.co.jp/details?sl=ja&tl=en&text=" + urllib.parse.quote(word, safe='') + "&op=translate"

# Load the file
with open("C:/Users/user/kotohira-quiz/web/public/data/japanese_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
print(f"Current questions: {len(questions)}")

# Count existing words from jpn_199 onwards
existing_new_words = set()
for q in questions:
    if q["id"] >= "jpn_199":
        existing_new_words.add(q["word"])
print(f"Existing new words: {len(existing_new_words)}")

EXISTING_WORDS = {
    "石段", "参拝", "鳥居", "境内", "土産", "大人", "昨日", "上手", "祭り", "景色",
    "一人", "今朝", "奉納", "灯籠", "神楽", "御利益", "拝殿", "狛犬", "賽銭", "手水舎",
    "老舗", "風情", "雰囲気", "所謂", "流石", "素人", "玄人", "由緒", "金毘羅", "讃岐",
    "宮司", "禰宜", "神饌", "鎮座", "漸く", "歌舞伎", "琴平", "杞憂", "相殺", "忖度",
    "紅葉", "梅雨", "七夕", "小豆", "海老", "河童", "時雨", "眼鏡", "煙草", "田舎",
    "果物", "野菜", "挨拶", "案内", "階段", "従兄弟", "五月雨", "乙女", "若人", "可愛い",
    "御手洗", "注連縄", "神輿", "氏子", "御神籤", "社務所", "絵馬", "草鞋", "提灯", "行灯",
    "暖簾", "団扇", "扇子", "蝋燭", "障子", "襖", "畳", "急須", "丁寧", "挑戦",
    "憂鬱", "脆弱", "鈴生り", "茶碗", "勧請", "遷座", "祝詞", "幣帛", "玉串", "直会",
    "齟齬", "慇懃", "蒐集", "邂逅", "瑕疵", "僭越", "逡巡", "矜持", "糟糠"
}

all_words = EXISTING_WORDS | existing_new_words

# Additional ~90 words to add
# (word, reading, english, level, explanation, k2r_correct, k2r_wrong1, k2r_wrong2, k2r_wrong3,
#  r2k_correct, r2k_wrong1, r2k_wrong2, r2k_wrong3)
ADDITIONAL = [
    ("方角", "ほうがく", "direction, compass point", "medium",
     "方角（ほうがく）= 東西南北（とうざいなんぼく）の向（む）き。例: 神社（じんじゃ）の拝殿（はいでん）がどの方角を向（む）いているか確認（かくにん）する。",
     "ほうがく", "ほうかく", "かたすみ", "ほうかど",
     "方角", "放角", "芳角", "邦角"),
    ("天文", "てんもん", "astronomy", "medium",
     "天文（てんもん）= 星（ほし）や宇宙（うちゅう）を研究（けんきゅう）する学問（がくもん）。例: 古代（こだい）の人々（ひとびと）は天文の知識（ちしき）で暦（こよみ）を作（つく）った。",
     "てんもん", "てんぶん", "あまもん", "てんぶつ",
     "天文", "天聞", "天紋", "転文"),
    ("提灯", "ちょうちん", "paper lantern", "medium",
     "already_exists"),
    ("数寄屋", "すきや", "tea ceremony house", "hard",
     "数寄屋（すきや）= 茶室（ちゃしつ）風（ふう）の建築様式（けんちくようしき）。例: 数寄屋造（すきやづく）りは日本建築（にほんけんちく）の粋（すい）だ。",
     "すきや", "かずきや", "すうきや", "すきしゃ",
     "数寄屋", "好屋", "透屋", "数奇屋"),
    ("行李", "こうり", "wicker trunk", "hard",
     "行李（こうり）= 竹（たけ）や柳（やなぎ）で編（あ）んだ旅行用（りょこうよう）の荷物入（にもつい）れ。例: 昔（むかし）の旅人（たびびと）は行李に荷物（にもつ）を詰（つ）めた。",
     "こうり", "ぎょうり", "あんり", "こうすもも",
     "行李", "行理", "行利", "行裏"),
    ("鑿", "のみ", "chisel", "hard",
     "鑿（のみ）= 木（き）や石（いし）を彫（ほ）るための刃物（はもの）。例: 彫刻師（ちょうこくし）が鑿で仏像（ぶつぞう）を彫（ほ）る。",
     "のみ", "さく", "ほり", "つち",
     "鑿", "穿", "彫", "削"),
    ("鉋", "かんな", "plane (woodworking)", "hard",
     "鉋（かんな）= 木材（もくざい）の表面（ひょうめん）を削（けず）って滑（なめ）らかにする道具（どうぐ）。例: 大工（だいく）が鉋で板（いた）を削（けず）る。",
     "かんな", "ほうちょう", "かな", "かんば",
     "鉋", "鉗", "鉤", "鋸"),
    ("槌", "つち", "hammer, mallet", "medium",
     "槌（つち）= 物（もの）を打（う）ち付（つ）ける道具（どうぐ）。例: 大黒様（だいこくさま）は打出（うちで）の小槌（こづち）を持（も）っている。",
     "つち", "すい", "つき", "ちゅう",
     "槌", "椎", "墜", "追"),
    ("襷", "たすき", "sash, cord", "hard",
     "襷（たすき）= 袖（そで）をまとめるために肩（かた）から脇（わき）にかける紐（ひも）。例: 巫女（みこ）が襷をかけて神事（しんじ）に臨（のぞ）む。",
     "たすき", "えりかけ", "おびひも", "たもと",
     "襷", "裹", "纏", "繋"),
    ("紫陽花", "あじさい", "hydrangea", "hard",
     "紫陽花（あじさい）= 梅雨（つゆ）の時期（じき）に咲（さ）く色鮮（いろあざ）やかな花（はな）。例: 参道（さんどう）に紫陽花が美（うつく）しく咲（さ）いている。",
     "あじさい", "しようか", "むらさきはな", "あじか",
     "紫陽花", "紫陽化", "紫揚花", "子陽花"),
    ("向日葵", "ひまわり", "sunflower", "hard",
     "向日葵（ひまわり）= 太陽（たいよう）に向（む）かって咲（さ）く大（おお）きな花（はな）。例: 夏（なつ）になると向日葵畑（ひまわりばたけ）が広（ひろ）がる。",
     "ひまわり", "こうじつき", "むかいひまわり", "こうにちき",
     "向日葵", "向日花", "陽日葵", "朝日葵"),
    ("蒲公英", "たんぽぽ", "dandelion", "hard",
     "蒲公英（たんぽぽ）= 春（はる）に黄色（きいろ）い花（はな）を咲（さ）かせる野草（やそう）。例: 道端（みちばた）に蒲公英が咲（さ）いている。",
     "たんぽぽ", "ほこうえい", "がまこうえい", "かんぽう",
     "蒲公英", "蒲公栄", "蒲光英", "蒲工英"),
    ("百合", "ゆり", "lily", "medium",
     "百合（ゆり）= 大（おお）きく美（うつく）しい花（はな）を咲（さ）かせる植物（しょくぶつ）。例: 百合の花（はな）は清楚（せいそ）な美（うつく）しさがある。",
     "ゆり", "ひゃくごう", "ももあい", "ゆうり",
     "百合", "白合", "由利", "友合"),
    ("薔薇", "ばら", "rose", "hard",
     "薔薇（ばら）= 棘（とげ）のある美（うつく）しい花（はな）。例: 薔薇は世界中（せかいじゅう）で愛（あい）されている花（はな）だ。",
     "ばら", "しょうび", "そうび", "いばら",
     "薔薇", "荊薇", "蕃薇", "蔷薇"),
    ("桜", "さくら", "cherry blossom", "easy",
     "桜（さくら）= 春（はる）に咲（さ）く日本（にほん）を代表（だいひょう）する花（はな）。例: 金刀比羅宮（ことひらぐう）の境内（けいだい）には桜が美（うつく）しく咲（さ）く。",
     "さくら", "おう", "はな", "うめ",
     "桜", "櫻", "花", "梅"),
    ("藤", "ふじ", "wisteria", "easy",
     "藤（ふじ）= 紫色（むらさきいろ）の花（はな）が垂（た）れ下（さ）がる蔓植物（つるしょくぶつ）。例: 藤棚（ふじだな）の下（した）は涼（すず）しい。",
     "ふじ", "とう", "かずら", "つた",
     "藤", "冨", "不二", "富士"),
    ("椿", "つばき", "camellia", "medium",
     "椿（つばき）= 冬（ふゆ）から春（はる）にかけて咲（さ）く花（はな）。例: 椿は茶花（ちゃばな）としても重宝（ちょうほう）される。",
     "つばき", "ちん", "もくれん", "さざんか",
     "椿", "樁", "楝", "榎"),
    ("菖蒲", "しょうぶ", "iris, sweet flag", "hard",
     "菖蒲（しょうぶ）= 端午（たんご）の節句（せっく）に飾（かざ）る植物（しょくぶつ）。例: 菖蒲湯（しょうぶゆ）に入（はい）って無病息災（むびょうそくさい）を祈（いの）る。",
     "しょうぶ", "あやめ", "かきつばた", "はなしょう",
     "菖蒲", "尚武", "勝負", "消府"),
    ("朝顔", "あさがお", "morning glory", "easy",
     "朝顔（あさがお）= 夏（なつ）の朝（あさ）に咲（さ）く花（はな）。例: 朝顔の花（はな）は朝（あさ）だけ開（ひら）いて昼（ひる）には萎（しぼ）む。",
     "あさがお", "ちょうがん", "あさかお", "ちょうげん",
     "朝顔", "朝貌", "朝顏", "明顔"),
    ("団欒", "だんらん", "family gathering", "hard",
     "団欒（だんらん）= 家族（かぞく）が集（あつ）まって楽（たの）しく過（す）ごすこと。例: 囲炉裏（いろり）を囲（かこ）んで団欒する。",
     "だんらん", "だんかん", "だんえん", "とんらん",
     "団欒", "団覧", "壇蘭", "暖欒"),
    ("生垣", "いけがき", "hedge", "medium",
     "生垣（いけがき）= 生（い）きた木（き）を植（う）えて作（つく）った垣根（かきね）。例: 生垣で庭（にわ）を囲（かこ）む。",
     "いけがき", "なまがき", "せいがき", "しょうがき",
     "生垣", "生柿", "性垣", "成垣"),
    ("雪崩", "なだれ", "avalanche", "medium",
     "雪崩（なだれ）= 斜面（しゃめん）の雪（ゆき）が崩（くず）れ落（お）ちる現象（げんしょう）。例: 冬山（ふゆやま）では雪崩に注意（ちゅうい）が必要（ひつよう）だ。",
     "なだれ", "せっぽう", "ゆきくず", "せっかい",
     "雪崩", "雪堕", "雪壊", "雪流"),
    ("土砂", "どしゃ", "earth, sediment", "easy",
     "土砂（どしゃ）= 土（つち）と砂（すな）。例: 大雨（おおあめ）で土砂が流（なが）れる。",
     "どしゃ", "とすな", "どさ", "つちすな",
     "土砂", "土沙", "度砂", "渡砂"),
    ("街道", "かいどう", "highway, road", "easy",
     "街道（かいどう）= 都市間（としかん）を結（むす）ぶ主要（しゅよう）な道路（どうろ）。例: 金毘羅街道（こんぴらかいどう）は参詣者（さんけいしゃ）で賑（にぎ）わった。",
     "かいどう", "がいどう", "まちみち", "かいみち",
     "街道", "海道", "会道", "界道"),
    ("宿場", "しゅくば", "post town", "medium",
     "宿場（しゅくば）= 旅人（たびびと）が泊（と）まる宿（やど）のある町（まち）。例: 金毘羅街道（こんぴらかいどう）には宿場が点在（てんざい）していた。",
     "しゅくば", "やどば", "しゅくじょう", "やどじょう",
     "宿場", "宿馬", "縮場", "粛場"),
    ("木魚", "もくぎょ", "wooden fish drum", "medium",
     "木魚（もくぎょ）= 読経（どきょう）のときに叩（たた）く木製（もくせい）の打楽器（だがっき）。例: 僧侶（そうりょ）が木魚を叩（たた）きながら読経（どきょう）する。",
     "もくぎょ", "きぎょ", "ぼくうお", "もくうお",
     "木魚", "木漁", "木御", "牧魚"),
    ("戸棚", "とだな", "cupboard, closet", "easy",
     "戸棚（とだな）= 扉（とびら）のついた棚（たな）。例: 食器（しょっき）を戸棚に片付（かたづ）ける。",
     "とだな", "こだな", "とたな", "へだな",
     "戸棚", "戸壇", "渡棚", "都棚"),
    ("桶", "おけ", "bucket, tub", "easy",
     "桶（おけ）= 水（みず）を入（い）れるための木製（もくせい）の容器（ようき）。例: 手水舎（ちょうずや）に桶が置（お）かれている。",
     "おけ", "つう", "たらい", "かめ",
     "桶", "桝", "樽", "瓶"),
    ("杓子", "しゃくし", "ladle, scoop", "medium",
     "杓子（しゃくし）= 汁（しる）やご飯（はん）をすくう道具（どうぐ）。例: 杓子定規（しゃくしじょうぎ）という慣用句（かんようく）がある。",
     "しゃくし", "しゃもじ", "たまし", "さくし",
     "杓子", "酌子", "灼子", "爵子"),
    ("行水", "ぎょうずい", "bathing in a tub", "hard",
     "行水（ぎょうずい）= たらいに湯（ゆ）を張（は）って体（からだ）を洗（あら）うこと。例: 昔（むかし）は夏（なつ）に行水して涼（すず）んだ。",
     "ぎょうずい", "こうすい", "いきみず", "ぎょうすい",
     "行水", "行瑞", "業水", "仰水"),
    ("渋柿", "しぶがき", "astringent persimmon", "easy",
     "渋柿（しぶがき）= 渋（しぶ）くてそのままでは食（た）べられない柿（かき）。例: 渋柿は干（ほ）し柿（がき）にすると甘（あま）くなる。",
     "しぶがき", "じゅうし", "しゅうかき", "しぶかき",
     "渋柿", "澁柿", "汁柿", "十柿"),
    ("七輪", "しちりん", "charcoal brazier", "medium",
     "七輪（しちりん）= 炭（すみ）で火（ひ）を起（お）こす小型（こがた）の調理器具（ちょうりきぐ）。例: 七輪で魚（さかな）を焼（や）く。",
     "しちりん", "ななわ", "しちわ", "ななりん",
     "七輪", "七倫", "七林", "七厘"),
    ("火鉢", "ひばち", "hibachi, fire bowl", "medium",
     "火鉢（ひばち）= 炭火（すみび）を入（い）れて暖（あたた）を取（と）る器具（きぐ）。例: 昔（むかし）は火鉢で部屋（へや）を暖（あたた）めた。",
     "ひばち", "かはち", "ひぼん", "かばち",
     "火鉢", "火蜂", "火鉄", "火箱"),
    ("燭台", "しょくだい", "candlestick", "medium",
     "燭台（しょくだい）= 蝋燭（ろうそく）を立（た）てるための台（だい）。例: 燭台に蝋燭（ろうそく）を灯（とも）す。",
     "しょくだい", "そくだい", "しょうだい", "しくだい",
     "燭台", "触台", "嘱台", "殖台"),
    ("行脚", "あんぎゃ", "pilgrimage on foot", "hard",
     "行脚（あんぎゃ）= 修行（しゅぎょう）や巡礼（じゅんれい）のために各地（かくち）を歩（ある）き回（まわ）ること。例: 弘法大師（こうぼうだいし）は四国（しこく）を行脚した。",
     "あんぎゃ", "こうきゃく", "ぎょうきゃく", "ぎょうあし",
     "行脚", "行客", "行却", "行格"),
    ("遍路", "へんろ", "pilgrimage", "medium",
     "遍路（へんろ）= 四国八十八箇所（しこくはちじゅうはっかしょ）を巡（めぐ）る巡礼（じゅんれい）。例: 白装束（しろしょうぞく）の遍路が歩（ある）いている。",
     "へんろ", "へんじ", "べんろ", "あまねじ",
     "遍路", "偏路", "辺路", "変路"),
    ("巡礼", "じゅんれい", "pilgrimage", "medium",
     "巡礼（じゅんれい）= 聖地（せいち）を巡（めぐ）り歩（ある）くこと。例: 四国（しこく）の巡礼は有名（ゆうめい）だ。",
     "じゅんれい", "じゅんらい", "めぐりれい", "じゅんり",
     "巡礼", "順礼", "潤礼", "循礼"),
    ("先達", "せんだつ", "guide, predecessor", "hard",
     "先達（せんだつ）= 先（さき）に道（みち）を歩（あゆ）んだ経験者（けいけんしゃ）。例: 先達の教（おし）えに従（したが）って参拝（さんぱい）する。",
     "せんだつ", "せんたつ", "さきだち", "さきたつ",
     "先達", "先立", "先辰", "千達"),
    ("草庵", "そうあん", "thatched hut", "hard",
     "草庵（そうあん）= 草（くさ）や茅（かや）で作（つく）った粗末（そまつ）な小屋（こや）。例: 隠遁者（いんとんしゃ）が草庵で暮（く）らす。",
     "そうあん", "くさいおり", "そうい", "くさあん",
     "草庵", "草案", "草暗", "創庵"),
    ("襖絵", "ふすまえ", "painting on sliding doors", "medium",
     "襖絵（ふすまえ）= 襖（ふすま）に描（えが）かれた絵画（かいが）。例: 金刀比羅宮（ことひらぐう）の表書院（おもてしょいん）には見事（みごと）な襖絵がある。",
     "ふすまえ", "おうえ", "しょうえ", "とびらえ",
     "襖絵", "扉絵", "屏絵", "壁絵"),
    ("水墨画", "すいぼくが", "ink wash painting", "medium",
     "水墨画（すいぼくが）= 墨（すみ）の濃淡（のうたん）で描（えが）く絵画（かいが）。例: 水墨画は余白（よはく）の美（うつく）しさが特徴（とくちょう）だ。",
     "すいぼくが", "みずすみえ", "すいばくが", "すいもくが",
     "水墨画", "水黙画", "水牧画", "推墨画"),
    ("天井", "てんじょう", "ceiling", "easy",
     "天井（てんじょう）= 部屋（へや）の上面（じょうめん）。例: 寺院（じいん）の天井には龍（りゅう）の絵（え）が描（えが）かれていることがある。",
     "てんじょう", "てんい", "あまい", "てんせい",
     "天井", "天丼", "天上", "天成"),
    ("廊下", "ろうか", "corridor, hallway", "easy",
     "廊下（ろうか）= 建物（たてもの）の中（なか）の通路（つうろ）。例: 寺院（じいん）の長（なが）い廊下を歩（ある）く。",
     "ろうか", "かいか", "りょうか", "ろうげ",
     "廊下", "郎下", "朗下", "楼下"),
    ("縁側", "えんがわ", "veranda, porch", "medium",
     "縁側（えんがわ）= 日本家屋（にほんかおく）の外壁（がいへき）に沿（そ）った板張（いたば）りの通路（つうろ）。例: 縁側に座（すわ）って庭（にわ）を眺（なが）める。",
     "えんがわ", "ふちがわ", "えんそく", "へりがわ",
     "縁側", "縁川", "園側", "鳶側"),
    ("瓢箪", "ひょうたん", "gourd", "hard",
     "瓢箪（ひょうたん）= 乾燥（かんそう）させて容器（ようき）にするウリ科（か）の植物（しょくぶつ）。例: 瓢箪から駒（こま）ということわざがある。",
     "ひょうたん", "ひさごたん", "ひょうだん", "ひょうかん",
     "瓢箪", "瓢丹", "飄箪", "票箪"),
    ("杉", "すぎ", "cedar", "easy",
     "杉（すぎ）= まっすぐに伸（の）びる日本（にほん）の代表的（だいひょうてき）な針葉樹（しんようじゅ）。例: 参道（さんどう）に杉並木（すぎなみき）が続（つづ）く。",
     "すぎ", "まつ", "ひのき", "さん",
     "杉", "松", "檜", "柏"),
    ("松", "まつ", "pine", "easy",
     "松（まつ）= 常緑（じょうりょく）の針葉樹（しんようじゅ）で長寿（ちょうじゅ）の象徴（しょうちょう）。例: 松は正月（しょうがつ）の飾（かざ）りに欠（か）かせない。",
     "まつ", "しょう", "すぎ", "もり",
     "松", "枩", "杉", "柏"),
    ("竹", "たけ", "bamboo", "easy",
     "竹（たけ）= 節（ふし）のある細長（ほそなが）い植物（しょくぶつ）。例: 竹は日本（にほん）の文化（ぶんか）と深（ふか）い関（かか）わりがある。",
     "たけ", "ちく", "ささ", "しの",
     "竹", "笹", "篁", "簾"),
    ("梅", "うめ", "plum, ume", "easy",
     "梅（うめ）= 早春（そうしゅん）に咲（さ）く香（かお）りの良（よ）い花（はな）。例: 梅の花（はな）は春（はる）の訪（おとず）れを告（つ）げる。",
     "うめ", "ばい", "すもも", "もも",
     "梅", "楳", "苺", "桃"),
    ("柳", "やなぎ", "willow", "easy",
     "柳（やなぎ）= 枝（えだ）が垂（た）れ下（さ）がる落葉樹（らくようじゅ）。例: 川辺（かわべ）に柳が植（う）えられている。",
     "やなぎ", "りゅう", "かわ", "はぎ",
     "柳", "楊", "萩", "梁"),
    ("老松", "おいまつ", "old pine tree", "hard",
     "老松（おいまつ）= 樹齢（じゅれい）を重（かさ）ねた松（まつ）の木（き）。例: 境内（けいだい）の老松は御神木（ごしんぼく）として大切（たいせつ）にされている。",
     "おいまつ", "ろうしょう", "おいまち", "ろうまつ",
     "老松", "朗松", "労松", "郎松"),
    ("杜", "もり", "grove, forest", "medium",
     "杜（もり）= 神社（じんじゃ）の森（もり）、鎮守（ちんじゅ）の森（もり）。例: 鎮守（ちんじゅ）の杜に静（しず）けさが漂（ただよ）う。",
     "もり", "と", "はやし", "やしろ",
     "杜", "社", "森", "林"),
    ("宮", "みや", "shrine, palace", "easy",
     "宮（みや）= 神社（じんじゃ）の敬称（けいしょう）。例: 金刀比羅宮（ことひらぐう）は「宮」の称号（しょうごう）を持（も）つ。",
     "みや", "きゅう", "ぐう", "いえ",
     "宮", "宮", "宮", "宮"),  # Will fix below
    ("釣鐘", "つりがね", "hanging bell", "medium",
     "釣鐘（つりがね）= 寺（てら）に吊（つ）られた大（おお）きな鐘（かね）。例: 釣鐘の音（おと）が遠（とお）くまで響（ひび）く。",
     "つりがね", "ちょうしょう", "つりかね", "つるしがね",
     "釣鐘", "吊鐘", "釣金", "釣鉦"),
    ("築地", "ついじ", "earthen wall", "hard",
     "築地（ついじ）= 土（つち）を突（つ）き固（かた）めて作（つく）った塀（へい）。例: 寺院（じいん）の周囲（しゅうい）に築地が巡（めぐ）らされている。",
     "ついじ", "つきぢ", "ちくち", "きずち",
     "築地", "突地", "筑地", "蓄地"),
    ("参道", "さんどう", "approach to a shrine", "easy",
     "参道（さんどう）= 神社（じんじゃ）や寺（てら）へ通（つう）じる道（みち）。例: 金刀比羅宮（ことひらぐう）の参道には多（おお）くの店（みせ）が並（なら）ぶ。",
     "さんどう", "まいみち", "さんみち", "まいどう",
     "参道", "散道", "山道", "賛道"),
    ("石畳", "いしだたみ", "stone pavement", "easy",
     "石畳（いしだたみ）= 石（いし）を敷（し）き詰（つ）めた道（みち）。例: 石畳の参道（さんどう）を歩（ある）く。",
     "いしだたみ", "せきじょう", "いしだたき", "いしばたけ",
     "石畳", "石疊", "石文", "石嵩"),
    ("手摺り", "てすり", "handrail, railing", "easy",
     "手摺り（てすり）= 階段（かいだん）や廊下（ろうか）に取（と）り付（つ）けた掴（つか）まるための棒（ぼう）。例: 石段（いしだん）には手摺りが設置（せっち）されている。",
     "てすり", "しゅまり", "てずり", "てなでり",
     "手摺り", "手擦り", "手磨り", "手刷り"),
    ("柵", "さく", "fence, railing", "easy",
     "柵（さく）= 木（き）や金属（きんぞく）で作（つく）った仕切（しき）り。例: 危険（きけん）な場所（ばしょ）には柵が設（もう）けられている。",
     "さく", "しがらみ", "かき", "へい",
     "柵", "冊", "策", "削"),
    ("旗", "はた", "flag, banner", "easy",
     "旗（はた）= 布（ぬの）でできた目印（めじるし）や飾（かざ）り。例: 祭（まつ）りのときに旗が立（た）てられる。",
     "はた", "き", "のぼり", "まく",
     "旗", "機", "幟", "幕"),
    ("幕", "まく", "curtain, screen", "easy",
     "幕（まく）= 布（ぬの）を張（は）った仕切（しき）り。例: 祭（まつ）りの会場（かいじょう）に紅白（こうはく）の幕が張（は）られている。",
     "まく", "ばく", "とばり", "かたびら",
     "幕", "膜", "莫", "漠"),
    ("的", "まと", "target", "easy",
     "的（まと）= 矢（や）や弾（たま）を当（あ）てる目標物（もくひょうぶつ）。例: 弓道（きゅうどう）で的を射（い）る。",
     "まと", "てき", "めあて", "しるし",
     "的", "敵", "滴", "適"),
]

# Fix 宮 r2k choices
for i, w in enumerate(ADDITIONAL):
    if w[0] == "宮":
        ADDITIONAL[i] = ("宮", "みや", "shrine, palace", "easy",
            "宮（みや）= 神社（じんじゃ）の敬称（けいしょう）。例: 金刀比羅宮（ことひらぐう）は「宮」の称号（しょうごう）を持（も）つ。",
            "みや", "きゅう", "ぐう", "いえ",
            "宮", "宗", "官", "営")
        break

# Filter out already existing
additional_clean = []
for w in ADDITIONAL:
    if w[0] in all_words:
        continue
    if w[4] == "already_exists":
        continue
    additional_clean.append(w)
    all_words.add(w[0])

print(f"Additional words to add: {len(additional_clean)}")

# Get last ID
last_q = questions[-1]
next_id = int(last_q["id"].split("_")[1]) + 1
print(f"Next ID: {next_id}")

# Generate new questions for additional words with varied answer positions
answer_positions = ["A", "B", "C", "D"]
pos_idx = 0

for w in additional_clean:
    word, reading, english, level, explanation = w[0], w[1], w[2], w[3], w[4]
    k2r_correct, k2r_w1, k2r_w2, k2r_w3 = w[5], w[6], w[7], w[8]
    r2k_correct, r2k_w1, r2k_w2, r2k_w3 = w[9], w[10], w[11], w[12]

    search_url = make_search_url(word)
    translate_url = make_translate_url(word)

    # kanji_to_reading: place correct answer at position pos_idx
    k2r_all = [k2r_w1, k2r_w2, k2r_w3]
    random.shuffle(k2r_all)
    k2r_choices_raw = list(k2r_all)
    target_pos = pos_idx % 4
    k2r_choices_raw.insert(target_pos, k2r_correct)
    labels = ["A", "B", "C", "D"]
    k2r_choices = [f"{labels[j]}. {k2r_choices_raw[j]}" for j in range(4)]
    k2r_answer = labels[target_pos]

    q1 = {
        "id": f"jpn_{next_id:03d}",
        "level": level,
        "pattern": "kanji_to_reading",
        "question": f"「{word}」の読みは？",
        "choices": k2r_choices,
        "answer": k2r_answer,
        "explanation": explanation,
        "word": word,
        "reading": reading,
        "english": english,
        "search_url": search_url,
        "translate_url": translate_url,
        "reviewed": True,
        "enabled": True
    }
    questions.append(q1)
    next_id += 1
    pos_idx += 1

    # reading_to_kanji: place correct answer at position pos_idx
    r2k_all = [r2k_w1, r2k_w2, r2k_w3]
    random.shuffle(r2k_all)
    r2k_choices_raw = list(r2k_all)
    target_pos = pos_idx % 4
    r2k_choices_raw.insert(target_pos, r2k_correct)
    r2k_choices = [f"{labels[j]}. {r2k_choices_raw[j]}" for j in range(4)]
    r2k_answer = labels[target_pos]

    q2 = {
        "id": f"jpn_{next_id:03d}",
        "level": level,
        "pattern": "reading_to_kanji",
        "question": f"「{reading}」を漢字で書くと？",
        "choices": r2k_choices,
        "answer": r2k_answer,
        "explanation": explanation,
        "word": word,
        "reading": reading,
        "english": english,
        "search_url": search_url,
        "translate_url": translate_url,
        "reviewed": True,
        "enabled": True
    }
    questions.append(q2)
    next_id += 1
    pos_idx += 1

print(f"Total questions after adding: {len(questions)}")

# Now fix answer distribution for ALL new questions (jpn_199+)
# Shuffle correct answer positions for the existing batch too
new_qs = [q for q in questions if q["id"] >= "jpn_199"]
old_qs = [q for q in questions if q["id"] < "jpn_199"]

print(f"Old questions: {len(old_qs)}, New questions: {len(new_qs)}")

# For each new question, extract correct/wrong choices and redistribute
random.seed(12345)
target_dist = {"A": 0, "B": 0, "C": 0, "D": 0}

for i, q in enumerate(new_qs):
    # Parse current choices
    choices_text = []
    for c in q["choices"]:
        # Remove "A. ", "B. ", etc prefix
        choices_text.append(c[3:])

    # Find correct answer index
    correct_idx = ord(q["answer"]) - ord("A")
    correct_text = choices_text[correct_idx]

    # Get wrong answers
    wrong_texts = [choices_text[j] for j in range(4) if j != correct_idx]

    # Determine target position (cycle through A/B/C/D evenly)
    target_label = ["A", "B", "C", "D"][i % 4]
    target_idx = i % 4

    # Shuffle wrongs
    random.shuffle(wrong_texts)

    # Place correct at target position
    new_choices_text = list(wrong_texts)
    new_choices_text.insert(target_idx, correct_text)

    # Build new choices
    labels = ["A", "B", "C", "D"]
    q["choices"] = [f"{labels[j]}. {new_choices_text[j]}" for j in range(4)]
    q["answer"] = target_label
    target_dist[target_label] += 1

print(f"New answer distribution: {target_dist}")

# Combine and write
data["questions"] = old_qs + new_qs

with open("C:/Users/user/kotohira-quiz/web/public/data/japanese_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Final verification
total_words = set()
for q in data["questions"]:
    total_words.add(q["word"])
print(f"Total unique words: {len(total_words)}")
print(f"Total questions: {len(data['questions'])}")
print("Done!")

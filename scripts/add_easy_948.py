#!/usr/bin/env python3
"""Add easy questions 948-991 to kotohira_questions.json"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'web', 'public', 'data', 'kotohira_questions.json')

new_questions = [
    # === Team C: shrine (948-955) ===
    {
        "id": "kotohira_948", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の御本宮を参拝する際の拝観料はいくらですか？",
        "choices": ["A. 300円", "B. 500円", "C. 無料", "D. 800円"],
        "answer": "C",
        "explanation": "金刀比羅宮の御本宮への参拝は無料です。ただし、表書院や宝物館などの一部施設は有料となっています。（出典: [うどん県旅ネット](https://www.my-kagawa.jp/point/75/)）",
        "source": "https://www.my-kagawa.jp/point/75/",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_949", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の大門をくぐった先にある「桜馬場」の奥では、何を見ることができますか？",
        "choices": ["A. 御神木の大楠", "B. 神馬（しんめ）", "C. 青銅の大灯籠", "D. 石造りの手水鉢"],
        "answer": "B",
        "explanation": "大門から続く桜馬場の奥には神馬舎（御厩）があり、本物の神馬を見ることができます。神馬は例大祭にも随伴する神聖な馬です。（出典: [金刀比羅宮 公式サイト](https://www.konpira.or.jp/)）",
        "source": "https://www.konpira.or.jp/",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_950", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の御本宮から奥社（厳魂神社）まで歩くと、片道でおよそどのくらいかかりますか？",
        "choices": ["A. 約5分ほど", "B. 約15分ほど", "C. 約30分ほど", "D. 約60分ほど"],
        "answer": "C",
        "explanation": "御本宮から奥社までは石段583段・距離約1.2kmで、片道およそ20〜30分かかります。体力に合わせてゆっくり登りましょう。（出典: [金刀比羅宮 奥社参拝ガイド](https://www.konpira.or.jp/articles/20200616_guide_inner-shrine/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200616_guide_inner-shrine/article.htm",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_951", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の表書院の一般（大人）の入館料はいくらですか？",
        "choices": ["A. 400円", "B. 600円", "C. 800円", "D. 1,000円"],
        "answer": "C",
        "explanation": "表書院の入館料は一般800円、高校生・大学生400円、中学生以下は無料です。円山応挙の障壁画などを鑑賞できます。（出典: [金刀比羅宮 表書院](https://www.konpira.or.jp/articles/20200703_drawing-room/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200703_drawing-room/article.htm",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_952", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の境内で唯一商売を許されている「五人百姓」が売っている名物は何ですか？",
        "choices": ["A. きび団子", "B. 加美代飴", "C. 和三盆糖", "D. 讃岐おかき"],
        "answer": "B",
        "explanation": "五人百姓は大門の内側で約800年にわたり加美代飴（かみよあめ）を販売しています。境内で唯一商売を許された5軒の飴屋です。（出典: [五人百姓 池商店](https://www.ikesyouten.com/kamiyoame.html)）",
        "source": "https://www.ikesyouten.com/kamiyoame.html",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_953", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮で御朱印をいただける場所はどこですか？",
        "choices": ["A. 大門横の受付所", "B. 旭社の社務所", "C. 御本宮の授与所", "D. 表書院の窓口"],
        "answer": "C",
        "explanation": "金刀比羅宮の御朱印は、御本宮の社殿向かい側にある授与所でいただけます。奥社（厳魂神社）にも別の授与所があり、限定の御朱印を受けられます。（出典: [千年帳](https://sennencho.jp/konpirasan-goshuin)）",
        "source": "https://sennencho.jp/konpirasan-goshuin",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_954", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮の大門（境内入口）は朝何時に開門しますか？",
        "choices": ["A. 午前5時", "B. 午前6時", "C. 午前7時", "D. 午前8時"],
        "answer": "B",
        "explanation": "金刀比羅宮の大門は午前6時に開門し、午後6時に閉門します。御本宮の御扉は午前7時開扉・午後5時閉扉です。（出典: [金刀比羅宮 公式サイト](https://www.konpira.or.jp/)）",
        "source": "https://www.konpira.or.jp/",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_955", "category": "shrine", "difficulty": "easy",
        "question": "金刀比羅宮には年間およそ何万人の参拝者が訪れますか？",
        "choices": ["A. 約50万人", "B. 約100万人", "C. 約200万人", "D. 約400万人"],
        "answer": "D",
        "explanation": "金刀比羅宮には年間約400万人もの参拝者が国内外から訪れます。「一生に一度はこんぴら参り」と言われる人気の神社です。（出典: [GOOD LUCK TRIP](https://www.gltjp.com/ja/article/item/20810/)）",
        "source": "https://www.gltjp.com/ja/article/item/20810/",
        "reviewed": False, "enabled": True
    },
    # === Team C: geography (956-959) ===
    {
        "id": "kotohira_956", "category": "geography", "difficulty": "easy",
        "question": "琴平町の面積は約8.47km²ですが、これは香川県の市町で何番目に小さいですか？",
        "choices": ["A. 1番目に小さい", "B. 2番目に小さい", "C. 3番目に小さい", "D. 4番目に小さい"],
        "answer": "B",
        "explanation": "琴平町の面積は約8.47km²で、香川県の市町では宇多津町（約8.10km²）に次いで2番目に小さい町です。（出典: [琴平町公式ホームページ](https://www.town.kotohira.kagawa.jp/site/furusato/1649.html)）",
        "source": "https://www.town.kotohira.kagawa.jp/site/furusato/1649.html",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_957", "category": "geography", "difficulty": "easy",
        "question": "金刀比羅宮が鎮座する象頭山の標高はおよそ何メートルですか？",
        "choices": ["A. 約338メートル", "B. 約438メートル", "C. 約538メートル", "D. 約638メートル"],
        "answer": "C",
        "explanation": "象頭山の標高は538メートルです。山容が象の頭に似ていることからこの名がつきました。北西の大麻山（616m）と合わせた山塊全体を琴平山とも呼びます。（出典: [象頭山 - Wikipedia](https://ja.wikipedia.org/wiki/%E8%B1%A1%E9%A0%AD%E5%B1%B1_(%E9%A6%99%E5%B7%9D%E7%9C%8C))）",
        "source": "https://ja.wikipedia.org/wiki/%E8%B1%A1%E9%A0%AD%E5%B1%B1_(%E9%A6%99%E5%B7%9D%E7%9C%8C)",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_958", "category": "geography", "difficulty": "easy",
        "question": "琴平町を流れる金倉川は、全長約何kmの二級河川ですか？",
        "choices": ["A. 約10.5km", "B. 約15.5km", "C. 約20.5km", "D. 約25.5km"],
        "answer": "C",
        "explanation": "金倉川は全長約20.5kmの二級河川で、まんのう町の満濃池から流れ出し、琴平町の市街地を貫いて丸亀市で瀬戸内海に注ぎます。（出典: [金倉川 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%80%89%E5%B7%9D)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%80%89%E5%B7%9D",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_959", "category": "geography", "difficulty": "easy",
        "question": "琴平町に隣接していない自治体はどれですか？",
        "choices": ["A. 善通寺市", "B. 三豊市", "C. まんのう町", "D. 丸亀市"],
        "answer": "D",
        "explanation": "琴平町に隣接しているのは善通寺市（北〜北西）、三豊市（南西）、まんのう町（東・南）の3自治体です。丸亀市は隣接していません。（出典: [琴平町公式ホームページ](https://www.town.kotohira.kagawa.jp/site/furusato/1649.html)）",
        "source": "https://www.town.kotohira.kagawa.jp/site/furusato/1649.html",
        "reviewed": False, "enabled": True
    },
    # === Team A: history (960-974) ===
    {
        "id": "kotohira_960", "category": "history", "difficulty": "easy",
        "question": "明治元年（1868年）の神仏分離令により、金刀比羅宮はそれ以前に何と呼ばれていましたか？",
        "choices": ["A. 象頭山松尾寺", "B. 金毘羅大権現", "C. 琴平大明神", "D. 讃岐大権現"],
        "answer": "B",
        "explanation": "金刀比羅宮は明治元年の神仏分離令まで「象頭山金毘羅大権現」と呼ばれていました。神仏分離により仏教色を排し、「琴平山金刀比羅宮」へと改称されました。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_961", "category": "history", "difficulty": "easy",
        "question": "明治元年の神仏分離の際に、金毘羅大権現から金刀比羅宮への改称を主導した人物は誰ですか？",
        "choices": ["A. 大久保諶之丞", "B. 琴陵宥常", "C. 長谷川佐太郎", "D. 日柳燕石"],
        "answer": "B",
        "explanation": "琴陵宥常（ことおか ひろつね）は金刀比羅宮の第19代金光院別当で、神仏分離に際して「金毘羅大権現」を「金刀比羅宮」に改称し、神道の神社として再編しました。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_962", "category": "history", "difficulty": "easy",
        "question": "琴平町が町制を施行したのは明治何年ですか？",
        "choices": ["A. 明治18年（1885年）", "B. 明治20年（1887年）", "C. 明治23年（1890年）", "D. 明治25年（1892年）"],
        "answer": "C",
        "explanation": "琴平町は明治23年（1890年）2月15日に琴平村から町制を施行して琴平町となりました。（出典: [琴平町 - Wikipedia](https://ja.wikipedia.org/wiki/%E7%90%B4%E5%B9%B3%E7%94%BA)）",
        "source": "https://ja.wikipedia.org/wiki/%E7%90%B4%E5%B9%B3%E7%94%BA",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_963", "category": "history", "difficulty": "easy",
        "question": "高橋由一はどのような分野の先駆者として知られていますか？",
        "choices": ["A. 日本画の先駆者", "B. 洋画の先駆者", "C. 版画の先駆者", "D. 彫刻の先駆者"],
        "answer": "B",
        "explanation": "高橋由一（1828〜1894年）は近代日本における洋画の先駆者として知られています。明治12年に金刀比羅宮へ油絵を奉納し、現在は境内の「高橋由一館」で作品が公開されています。（出典: [高橋由一 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%AB%98%E6%A9%8B%E7%94%B1%E4%B8%80)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%AB%98%E6%A9%8B%E7%94%B1%E4%B8%80",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_964", "category": "history", "difficulty": "easy",
        "question": "高橋由一が金刀比羅宮に奉納した作品はどのようなものですか？",
        "choices": ["A. 日本画の掛軸", "B. 木彫りの仏像", "C. 油絵の洋画作品", "D. 陶磁器の花瓶"],
        "answer": "C",
        "explanation": "高橋由一は明治12年（1879年）に金刀比羅宮へ油絵を奉納しました。現在は境内の「高橋由一館」で『豆腐』『鯛』などの奉納作品が展示されています。（出典: [高橋由一 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%AB%98%E6%A9%8B%E7%94%B1%E4%B8%80)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%AB%98%E6%A9%8B%E7%94%B1%E4%B8%80",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_965", "category": "history", "difficulty": "easy",
        "question": "江戸時代に全国各地で組織された、金刀比羅宮への参拝を目的とした信仰集団を何と呼びますか？",
        "choices": ["A. 金毘羅講", "B. 金毘羅組", "C. 金毘羅座", "D. 金毘羅衆"],
        "answer": "A",
        "explanation": "金毘羅講とは、江戸時代中期に全国各地で組織された金刀比羅宮への参拝を目的とした信仰集団です。費用を積み立て、代表者が代わりに参拝する仕組みで、伊勢講に次ぐ規模を誇りました。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_966", "category": "history", "difficulty": "easy",
        "question": "讃岐鉄道が最初に開業した区間はどこからどこまでですか？",
        "choices": ["A. 高松から丸亀までの区間", "B. 丸亀から琴平までの区間", "C. 多度津から善通寺の区間", "D. 坂出から丸亀までの区間"],
        "answer": "B",
        "explanation": "讃岐鉄道は1889年（明治22年）5月23日に丸亀〜多度津〜琴平間で開業しました。これが四国で最初の鉄道開業であり、現在のJR予讃線・土讃線の一部にあたります。（出典: [讃岐鉄道 - Wikipedia](https://ja.wikipedia.org/wiki/%E8%AE%83%E5%B2%90%E9%89%84%E9%81%93)）",
        "source": "https://ja.wikipedia.org/wiki/%E8%AE%83%E5%B2%90%E9%89%84%E9%81%93",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_967", "category": "history", "difficulty": "easy",
        "question": "金毘羅参りで、費用を出して他の人や犬に代わりに参拝してもらう仕組みを何と呼びますか？",
        "choices": ["A. 祈祷参り", "B. 代参", "C. 奉納参り", "D. 遥拝"],
        "answer": "B",
        "explanation": "代参とは、自分の代わりに他の人や犬に参拝してもらう仕組みです。江戸時代には金毘羅講で費用を積み立て、代表者が代わりに参拝するほか、犬に初穂料を首にかけて参拝させる「こんぴら狗」の風習もありました。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_968", "category": "history", "difficulty": "easy",
        "question": "丸亀街道の起点である丸亀港に建つ、金毘羅参りの目印となった石造りの建造物は何ですか？",
        "choices": ["A. 太助灯籠", "B. 高燈籠", "C. 紫銅鳥居", "D. 町口鳥居"],
        "answer": "A",
        "explanation": "太助灯籠は丸亀港にある石造りの灯籠で、丸亀街道の起点に位置します。海路で金毘羅参りに訪れる参詣客の目印として機能しました。（出典: [金毘羅街道 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E6%AF%98%E7%BE%85%E8%A1%97%E9%81%93)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E6%AF%98%E7%BE%85%E8%A1%97%E9%81%93",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_969", "category": "history", "difficulty": "easy",
        "question": "1985年に金丸座でのこんぴら歌舞伎復活に尽力した、琴平グランドホテル社長は誰ですか？",
        "choices": ["A. 日柳燕石", "B. 長谷川佐太郎", "C. 近兼孝休", "D. 大久保諶之丞"],
        "answer": "C",
        "explanation": "近兼孝休は琴平グランドホテルの社長で、1984年に金丸座を訪れた歌舞伎役者たちの公演希望を受け、松竹やJTBの協力を取り付け、1985年の第1回「四国こんぴら歌舞伎大芝居」の開催を実現しました。（出典: [旧金毘羅大芝居 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_970", "category": "history", "difficulty": "easy",
        "question": "金丸座で「四国こんぴら歌舞伎大芝居」が復活公演されたのは何年ですか？",
        "choices": ["A. 1975年（昭和50年）", "B. 1980年（昭和55年）", "C. 1985年（昭和60年）", "D. 1990年（平成2年）"],
        "answer": "C",
        "explanation": "四国こんぴら歌舞伎大芝居は1985年（昭和60年）に第1回公演が開催されました。歌舞伎役者の澤村藤十郎らの要望がきっかけで実現しました。（出典: [旧金毘羅大芝居 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_971", "category": "history", "difficulty": "easy",
        "question": "明治維新以前の日本で、神道と仏教が一つの信仰体系として融合していた現象を何と呼びますか？",
        "choices": ["A. 廃仏毀釈", "B. 本地垂迹", "C. 神仏習合", "D. 神仏分離"],
        "answer": "C",
        "explanation": "神仏習合とは、日本土着の神道と仏教が融合し一つの信仰体系として再構成された宗教現象です。金刀比羅宮も明治以前は「金毘羅大権現」と称していました。（出典: [神仏習合 - Wikipedia](https://ja.wikipedia.org/wiki/%E7%A5%9E%E4%BB%8F%E7%BF%92%E5%90%88)）",
        "source": "https://ja.wikipedia.org/wiki/%E7%A5%9E%E4%BB%8F%E7%BF%92%E5%90%88",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_972", "category": "history", "difficulty": "easy",
        "question": "金毘羅五街道のうち、西国・九州からの参詣客で最も栄えた街道はどれですか？",
        "choices": ["A. 高松街道", "B. 阿波街道", "C. 多度津街道", "D. 伊予街道"],
        "answer": "C",
        "explanation": "多度津街道は西国・九州方面からの参詣客の玄関口として栄えました。天保年間に多度津藩が港を大改修した後は大いに賑わいました。（出典: [金毘羅街道 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E6%AF%98%E7%BE%85%E8%A1%97%E9%81%93)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E6%AF%98%E7%BE%85%E8%A1%97%E9%81%93",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_973", "category": "history", "difficulty": "easy",
        "question": "金刀比羅宮の大門より内側で、鎌倉時代から特別に営業を許されている商人たちを何と呼びますか？",
        "choices": ["A. 三人組合", "B. 五人百姓", "C. 七人衆", "D. 十人役"],
        "answer": "B",
        "explanation": "五人百姓とは、鎌倉時代から金刀比羅宮の大門内で特別に営業を許された5軒の商人です。現在も大門を入った場所で、大きな傘を広げて名物の加美代飴を販売しています。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_974", "category": "history", "difficulty": "easy",
        "question": "琴陵宥常が設立に尽力した、海難救助を目的とする団体は何ですか？",
        "choices": ["A. 日本赤十字社", "B. 帝国水難救済会", "C. 海上保安協会", "D. 日本救命協会"],
        "answer": "B",
        "explanation": "琴陵宥常は金刀比羅宮の宮司として、ノルマントン号事件を契機に大日本帝国水難救済会（帝国水難救済会）の設立に尽力しました。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    # === Team B: architecture (975-982) ===
    {
        "id": "kotohira_975", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の旭社はどのような建物ですか？",
        "choices": ["A. 御祭神を祀る本殿にあたる建物", "B. 天保時代の精緻な彫刻が施された社殿", "C. 明治時代に建てられた宝物の収蔵庫", "D. 大正時代に再建された拝殿にあたる建物"],
        "answer": "B",
        "explanation": "旭社は天保8年（1837年）に完成した銅瓦葺の二層入母屋造の社殿で、柱間や扉に人物・鳥獣・草花の精緻な彫刻が施されています。国の重要文化財に指定されています。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_976", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の表書院の障壁画を描いた画家は誰ですか？",
        "choices": ["A. 狩野永徳", "B. 円山応挙", "C. 伊藤若冲", "D. 長谷川等伯"],
        "answer": "B",
        "explanation": "表書院には円山応挙が天明7年（1787年）から寛政6年（1794年）にかけて描いた障壁画があり、「遊虎図」「瀑布及山水図」などが残されています。国の重要文化財に指定されています。（出典: [円山応挙 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%86%86%E5%B1%B1%E5%BF%9C%E6%8C%99)）",
        "source": "https://ja.wikipedia.org/wiki/%E5%86%86%E5%B1%B1%E5%BF%9C%E6%8C%99",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_977", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の宝物館に展示されている重要文化財の仏像はどれですか？",
        "choices": ["A. 阿弥陀如来坐像", "B. 薬師如来立像", "C. 十一面観音立像", "D. 地蔵菩薩立像"],
        "answer": "C",
        "explanation": "宝物館には、かつて観音堂の本尊であった重要文化財の十一面観音立像が展示されています。宝物館は明治38年（1905年）に建てられた石造2階建ての建物です。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_978", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の御本宮の建築様式は何ですか？",
        "choices": ["A. 大社関棟造", "B. 流造", "C. 春日造", "D. 入母屋造"],
        "answer": "A",
        "explanation": "御本宮は明治10年（1877年）に再建された「大社関棟造」の建物で、本殿・中殿・拝殿から構成されています。石段785段目、海抜251メートルに鎮座しています。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_979", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の表書院は、どの時代の建築様式で建てられていますか？",
        "choices": ["A. 寝殿造", "B. 書院造", "C. 数寄屋造", "D. 城郭建築"],
        "answer": "B",
        "explanation": "表書院は万治2年（1659年）に建立された書院造の建物です。書院造は室町時代から発達した武家住宅の様式で、床の間・襖・障子などを特徴とします。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_980", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の旭社が完成するまでにかかった寄進額はどれくらいですか？",
        "choices": ["A. 約5千両", "B. 約1万両", "C. 約2万両", "D. 約5万両"],
        "answer": "C",
        "explanation": "旭社は2万両の寄進によって建てられました。天保8年（1837年）に完成した銅瓦葺の二層入母屋造の建物で、高さ約18メートルを誇ります。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_981", "category": "architecture", "difficulty": "easy",
        "question": "高橋由一の油絵作品を展示するために金刀比羅宮に設置された施設は何ですか？",
        "choices": ["A. 表書院の特別展示室", "B. 高橋由一館", "C. 宝物館の2階展示室", "D. 奥書院の常設展示室"],
        "answer": "B",
        "explanation": "金刀比羅宮には「高橋由一館」が設置されています。高橋由一は明治12年（1879年）に『豆腐』『鯛』など35点の油絵を金刀比羅宮に奉納した、日本の洋画の先駆者です。（出典: [高橋由一 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%AB%98%E6%A9%8B%E7%94%B1%E4%B8%80)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%AB%98%E6%A9%8B%E7%94%B1%E4%B8%80",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_982", "category": "architecture", "difficulty": "easy",
        "question": "金刀比羅宮の旭社の屋根に使われている素材は何ですか？",
        "choices": ["A. 檜皮葺", "B. 銅瓦葺", "C. 茅葺き", "D. 瑠璃瓦"],
        "answer": "B",
        "explanation": "旭社の屋根は銅瓦葺です。天保8年（1837年）に完成した二層入母屋造の壮麗な建物で、国の重要文化財に指定されています。（出典: [金刀比羅宮 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE)）",
        "source": "https://ja.wikipedia.org/wiki/%E9%87%91%E5%88%80%E6%AF%94%E7%BE%85%E5%AE%AE",
        "reviewed": False, "enabled": True
    },
    # === Team B: theater (983-987) ===
    {
        "id": "kotohira_983", "category": "theater", "difficulty": "easy",
        "question": "歌舞伎の「回り舞台」とはどのような舞台機構ですか？",
        "choices": ["A. 舞台の床が円形に回転する仕組み", "B. 舞台の幕が自動で開閉する仕組み", "C. 舞台の床が上下に昇降する仕組み", "D. 舞台の照明が回転して動く仕組み"],
        "answer": "A",
        "explanation": "回り舞台は舞台の床面を円形に切り、中心の心棒で回転させる機構です。金丸座では舞台下の奈落で4人の人力により回します。（出典: [廻り舞台 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%BB%BB%E3%82%8A%E8%88%9E%E5%8F%B0)）",
        "source": "https://ja.wikipedia.org/wiki/%E5%BB%BB%E3%82%8A%E8%88%9E%E5%8F%B0",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_984", "category": "theater", "difficulty": "easy",
        "question": "歌舞伎の「花道」とはどのようなものですか？",
        "choices": ["A. 舞台から客席を縦断する通路", "B. 役者が化粧をする楽屋の通路", "C. 舞台の上に花を飾る装飾台", "D. 観客が役者に花を渡す場所"],
        "answer": "A",
        "explanation": "花道は舞台から客席を縦断するように張り出した通路で、役者の出入りや演技に使われます。揚幕から七三（花道の3割の位置）で見得を切るなどの演技が行われます。（出典: [花道 - Wikipedia](https://ja.wikipedia.org/wiki/%E8%8A%B1%E9%81%93)）",
        "source": "https://ja.wikipedia.org/wiki/%E8%8A%B1%E9%81%93",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_985", "category": "theater", "difficulty": "easy",
        "question": "こんぴら歌舞伎の「お練り」とはどのような行事ですか？",
        "choices": ["A. 歌舞伎役者が人力車で町内を巡る行列", "B. 歌舞伎役者が石段を駆け上がる競争行事", "C. 観客が歌舞伎衣装で参道を歩く仮装行列", "D. 歌舞伎役者が金倉川を船で下る水上行列"],
        "answer": "A",
        "explanation": "お練りは、こんぴら歌舞伎の公演期間中に歌舞伎役者が人力車に乗って琴平町内を巡る行列です。金刀比羅宮での成功祈願祭の一環として行われます。（出典: [旧金毘羅大芝居 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_986", "category": "theater", "difficulty": "easy",
        "question": "金丸座の花道にある「すっぽん」とはどのような仕組みですか？",
        "choices": ["A. 役者がせり上がって登場する小型の装置", "B. 舞台の照明を調節するための仕掛け装置", "C. 観客に菓子を配るための小窓の仕掛け", "D. 舞台裏へ通じる隠し扉として使う仕掛け"],
        "answer": "A",
        "explanation": "すっぽんは花道の七三付近に設置された小型のせり上がり装置で、役者が舞台下の奈落からせり上がって登場します。金丸座では4人ほどの人力で操作します。（出典: [旧金毘羅大芝居 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_987", "category": "theater", "difficulty": "easy",
        "question": "金丸座の二階中央部の観客席は何と呼ばれていますか？",
        "choices": ["A. 向桟敷", "B. 前舟・中舟・後舟", "C. 特等席", "D. 見晴席"],
        "answer": "B",
        "explanation": "金丸座の二階中央部の観客席は「前舟・中舟・後舟」と呼ばれています。一階中央の畳敷きの席は「桝席」、一階と二階の両脇の席は「桟敷」と呼ばれます。（出典: [旧金毘羅大芝居 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85",
        "reviewed": False, "enabled": True
    },
    # === Team B: culture (988-991) ===
    {
        "id": "kotohira_988", "category": "culture", "difficulty": "easy",
        "question": "加美代飴の「加美代」という名前の由来は何ですか？",
        "choices": ["A. 「神代」にちなんで名づけられた", "B. 「上代」にちなんで名づけられた", "C. 「加美」という地名に由来している", "D. 「紙代」の当て字に由来している"],
        "answer": "A",
        "explanation": "加美代飴の名前は「神代（かみよ）」にちなんでいます。戦後に類似商品が出回ったため、1950年頃に丸型から現在の扇形に改められました。（出典: [加美代飴 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%8A%A0%E7%BE%8E%E4%BB%A3%E9%A3%B4)）",
        "source": "https://ja.wikipedia.org/wiki/%E5%8A%A0%E7%BE%8E%E4%BB%A3%E9%A3%B4",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_989", "category": "culture", "difficulty": "easy",
        "question": "加美代飴はどのようにして食べる飴ですか？",
        "choices": ["A. 付属のハンマーで割って食べる", "B. お湯に溶かして飲むタイプ", "C. 手でちぎって少しずつ食べる", "D. 口の中でゆっくり溶かして味わう"],
        "answer": "A",
        "explanation": "加美代飴は扇形のべっこう飴で、付属の小さなハンマーで砕き割って食べます。金刀比羅宮の大門内で五人百姓が販売する名物です。（出典: [加美代飴 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%8A%A0%E7%BE%8E%E4%BB%A3%E9%A3%B4)）",
        "source": "https://ja.wikipedia.org/wiki/%E5%8A%A0%E7%BE%8E%E4%BB%A3%E9%A3%B4",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_990", "category": "culture", "difficulty": "easy",
        "question": "琴平町が一大産地として知られる農産物はどれですか？",
        "choices": ["A. ニンニク", "B. オリーブ", "C. みかん", "D. すだち"],
        "answer": "A",
        "explanation": "琴平町はニンニクの一大産地として知られており、「こんぴらにんにく」はブランド農産物として地域の特産品になっています。（出典: [琴平町 - Wikipedia](https://ja.wikipedia.org/wiki/%E7%90%B4%E5%B9%B3%E7%94%BA)）",
        "source": "https://ja.wikipedia.org/wiki/%E7%90%B4%E5%B9%B3%E7%94%BA",
        "reviewed": False, "enabled": True
    },
    {
        "id": "kotohira_991", "category": "culture", "difficulty": "easy",
        "question": "書院造とはどの時代に発達した建築様式ですか？",
        "choices": ["A. 奈良時代に発達した寺院建築の様式", "B. 平安時代に発達した貴族住宅の様式", "C. 室町時代に発達した武家住宅の様式", "D. 江戸時代に発達した町人住宅の様式"],
        "answer": "C",
        "explanation": "書院造は室町時代から近世初頭にかけて成立した武家住宅の様式で、床の間・襖・障子・畳敷きの部屋を特徴とします。金刀比羅宮の表書院はその代表的建築です。（出典: [書院造 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%9B%B8%E9%99%A2%E9%80%A0)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%9B%B8%E9%99%A2%E9%80%A0",
        "reviewed": False, "enabled": True
    },
]

# Load existing data
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check for ID conflicts
existing_ids = {q['id'] for q in data['questions']}
new_ids = {q['id'] for q in new_questions}
conflicts = existing_ids & new_ids
if conflicts:
    print(f"ERROR: ID conflicts: {conflicts}")
    exit(1)

# Append
data['questions'].extend(new_questions)

# Write FIRST
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Stats
enabled = [q for q in data['questions'] if q.get('enabled', True)]
easy = [q for q in enabled if q['difficulty'] == 'easy']
medium = [q for q in enabled if q['difficulty'] == 'medium']
hard = [q for q in enabled if q['difficulty'] == 'hard']

print(f"Added {len(new_questions)} questions (kotohira_948-991)")
print(f"Total: {len(data['questions'])} questions")
print(f"Enabled: {len(enabled)}")
print(f"Easy: {len(easy)} ({len(easy)/len(enabled)*100:.1f}%)")
print(f"Medium: {len(medium)} ({len(medium)/len(enabled)*100:.1f}%)")
print(f"Hard: {len(hard)} ({len(hard)/len(enabled)*100:.1f}%)")

# Choice length bias check
bias = 0
for q in new_questions:
    lengths = {c[0]: len(c) for c in q['choices']}
    ans_len = lengths[q['answer']]
    max_len = max(lengths.values())
    min_len = min(lengths.values())
    if ans_len == max_len and max_len / min_len > 1.3:
        bias += 1
        print(f"  BIAS: {q['id']} ans={q['answer']}({ans_len}) max={max_len} min={min_len}")
print(f"Choice length bias >1.3x: {bias}/{len(new_questions)}")

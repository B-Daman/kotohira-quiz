#!/usr/bin/env python3
"""Add questions 901-947 to kotohira_questions.json"""
import json
import os

JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'web', 'public', 'data', 'kotohira_questions.json')

new_questions = [
    # === Team A: 金刀比羅宮 (901-911) ===
    {
        "id": "kotohira_901",
        "category": "shrine",
        "difficulty": "medium",
        "question": "なぜ金刀比羅宮は象頭山の中腹に鎮座しているのか？",
        "choices": [
            "A. 修験道の修行の場として山奥が求められたから",
            "B. 古代に瀬戸内海の島であった象頭山に大物主神が行宮を造ったと伝わるから",
            "C. 平安時代に空海が霊場として選定したから",
            "D. 讃岐国司が防衛拠点として山城を築いたのが始まりだから"
        ],
        "answer": "B",
        "explanation": "金刀比羅宮の由緒によれば、古代の象頭山はかつて瀬戸内海に浮かぶ島であり、大物主神がその地勢を利用して行宮（あんぐう）を造営したとされています。その行宮の跡地に大物主神を奉斎したのが金刀比羅宮の起源と伝わっています。象の頭に似た特徴的な山容は、後に船乗りたちの航海の目印「山アテ」にもなりました。（出典: [金刀比羅宮 由緒](https://www.konpira.or.jp/articles/20200814_history/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200814_history/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_902",
        "category": "shrine",
        "difficulty": "medium",
        "question": "なぜ金刀比羅宮の大門から先にはお土産屋が並んでいないのか？",
        "choices": [
            "A. 大門より先は傾斜がきつく店を建てられないから",
            "B. 大門が神域の境界であり、境内での商売が原則禁止されているから",
            "C. 明治時代の条例で参道の景観保全が義務づけられたから",
            "D. 金刀比羅宮が店舗用地を買い上げたから"
        ],
        "answer": "B",
        "explanation": "金刀比羅宮の大門は神域（聖域）の入口にあたる総門で、慶安2年（1650年）に初代高松藩主・松平頼重が寄進しました。大門をくぐった先は神聖な境内とされ、商売は原則として許されていません。唯一の例外が、鎌倉時代から神事に奉仕してきた功績により特別に許された「五人百姓」の飴屋です。（出典: [うどん県旅ネット 金刀比羅宮](https://www.my-kagawa.jp/konpira/feature/kotohiragu/about)）",
        "source": "https://www.my-kagawa.jp/konpira/feature/kotohiragu/about",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_903",
        "category": "shrine",
        "difficulty": "medium",
        "question": "なぜ金刀比羅宮の境内では神馬（しんめ）が飼育されているのか？",
        "choices": [
            "A. 参拝客を石段の途中まで乗せて運ぶためだから",
            "B. 神様の乗り物として奉仕し、例大祭の神輿行列にも随伴するから",
            "C. 馬術の奉納演武を行うためだから",
            "D. 象頭山に自生する薬草の運搬に使うためだから"
        ],
        "answer": "B",
        "explanation": "神馬は「神の乗り物」として神社に奉献される馬で、人が乗ったことのない馬でなければ神馬にはなれないとされています。金刀比羅宮の神馬は、毎年10月10日の例大祭で御神輿の渡御行列に随伴する重要な役割を担います。かつては生きた馬を奉納していた風習が簡略化され、木や板に描いた「絵馬」が生まれました。つまり全国の神社にある絵馬の起源は、神馬の代替品だったのです。（出典: [四国新聞 金刀比羅宮 美の世界 第24話](https://www.shikoku-np.co.jp/feature/kotohira/story/24.html)）",
        "source": "https://www.shikoku-np.co.jp/feature/kotohira/story/24.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_904",
        "category": "shrine",
        "difficulty": "medium",
        "question": "なぜ金刀比羅宮の奥社（厳魂神社）には天狗とゆかりがあるのか？",
        "choices": [
            "A. 修験道の開祖・役小角が天狗として祀られたから",
            "B. 戦国時代の別当・宥盛が「死して永く当山を守護せん」と天狗に化して姿を消したと伝わるから",
            "C. 奥社の岩壁が天狗の鼻に似ていることにちなむから",
            "D. 江戸時代に天狗信仰の山伏が奥社を修行道場としたから"
        ],
        "answer": "B",
        "explanation": "奥社に祀られる厳魂彦命（いづたまひこのみこと）は、戦国時代に金光院の別当として荒廃した金毘羅大権現の再興に尽力した僧・宥盛のことです。慶長18年（1613年）、「死して永く当山を守護せん」と言い残し、天狗と化して忽然と姿を消したと伝えられています。以後「金剛坊」として金毘羅の守護神に。奥社の威徳巖には天狗と烏天狗の彫り物が掛けられ、ここでしか授かれない「天狗御守」も人気があります。（出典: [金刀比羅宮 参拝ガイド 奥社編](https://www.konpira.or.jp/articles/20200616_guide_inner-shrine/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200616_guide_inner-shrine/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_905",
        "category": "shrine",
        "difficulty": "medium",
        "question": "なぜ金刀比羅宮は「こんぴらさん」と呼ばれるのか？",
        "choices": [
            "A. 琴の音が平らに響く「琴平」の音読みが転じたから",
            "B. サンスクリット語でガンジス川のワニを神格化した「クンビーラ」が語源だから",
            "C. 讃岐方言で「金の比羅（ひら＝崖）」を意味する地名が由来だから",
            "D. 初代別当の法名「金比羅坊」が愛称として広まったから"
        ],
        "answer": "B",
        "explanation": "「こんぴら」の語源はサンスクリット語の「クンビーラ（Kumbhīra）」で、ガンジス川に棲むワニを神格化した水神です。大宝年間（701年頃）に修験道の役小角が象頭山に登った際、この護法善神に遭ったとの伝承があり、これが「金毘羅大権現」の縁起となりました。もとは「琴平神社」と称していましたが、中世に本地垂迹説の影響で「金毘羅」の名が定着し、「こんぴらさん」として親しまれるようになりました。（出典: [金刀比羅宮 由緒](https://www.konpira.or.jp/articles/20200814_history/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200814_history/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_906",
        "category": "shrine",
        "difficulty": "hard",
        "question": "なぜ円山応挙は金刀比羅宮の表書院に障壁画を描くことになったのか？",
        "choices": [
            "A. 高松藩主が藩の権威を示すために応挙を指名したから",
            "B. 京都の豪商・三井八郎兵衛の援助で、京随一と評された応挙に制作が依頼されたから",
            "C. 応挙が金毘羅参詣の際に自ら障壁画の奉納を申し出たから",
            "D. 金光院の別当が応挙の弟子だった縁で無償制作を依頼されたから"
        ],
        "answer": "B",
        "explanation": "表書院の障壁画は、金光院第10代別当・宥存の発意により、京都の豪商・三井八郎兵衛の資金援助で実現しました。当時「京随一」と評されていた円山応挙に制作が依頼され、天明7年（1787年）から寛政6年（1794年）まで7年の歳月をかけて4室・計90面の障壁画が完成しました。途中、天明8年の京都大火で応挙自身も焼け出されるという困難を乗り越えた大作です。（出典: [四国新聞 金刀比羅宮 美の世界 第12話](https://www.shikoku-np.co.jp/feature/kotohira/story/12.html)）",
        "source": "https://www.shikoku-np.co.jp/feature/kotohira/story/12.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_907",
        "category": "shrine",
        "difficulty": "medium",
        "question": "なぜ金刀比羅宮の「幸福の黄色いお守り」は黄色なのか？",
        "choices": [
            "A. 金刀比羅宮の社紋が金色であることにちなむから",
            "B. 鬱金（うこん）染めの絹糸が古来より厄除けに用いられ、黄色は豊穣と幸福の色とされるから",
            "C. 讃岐名産のオリーブの実の色に由来するから",
            "D. 五行思想で「土」を表す黄色が安定を象徴するから"
        ],
        "answer": "B",
        "explanation": "金刀比羅宮の「幸福の黄色いお守り」は、平安時代から用いられてきた鬱金（うこん）で絹糸を染めたものです。鬱金染めには虫除け・魔除けの効能があるとされてきました。また黄色は「稲や麦の稔りの色、豊穣の色」であり、「あふれんばかりの恵みと愛をもたらす色」とされています。御本宮でしか授与されないため、785段の石段を登り切った人だけが手にできる特別なお守りです。（出典: [金刀比羅宮 幸福の黄色いお守り](https://www.konpira.or.jp/articles/20221123_yellow-charm/index.html)）",
        "source": "https://www.konpira.or.jp/articles/20221123_yellow-charm/index.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_908",
        "category": "shrine",
        "difficulty": "easy",
        "question": "金刀比羅宮の参道にある「大門」とは、どのような役割を持つ建物ですか？",
        "choices": [
            "A. 宮司が参拝者を出迎える応接所",
            "B. 神域の入口を示す金刀比羅宮の総門",
            "C. お守りや御朱印を授与する窓口",
            "D. 参拝者が身を清める手水舎"
        ],
        "answer": "B",
        "explanation": "大門は慶安2年（1650年）に初代高松藩主・松平頼重が寄進した二層入母屋造瓦葺の門で、金刀比羅宮の「総門」にあたります。ここをくぐると神域に入り、参道の雰囲気が一変します。365段目に位置し、扁額の「琴平山」の文字は有栖川宮熾仁親王の筆によるものです。（出典: [うどん県旅ネット 金刀比羅宮](https://www.my-kagawa.jp/konpira/feature/kotohiragu/about)）",
        "source": "https://www.my-kagawa.jp/konpira/feature/kotohiragu/about",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_909",
        "category": "shrine",
        "difficulty": "easy",
        "question": "金刀比羅宮で古くから行われている「流し樽」とは、どのような風習ですか？",
        "choices": [
            "A. 年末に古いお札やお守りを樽に入れて焚き上げる行事",
            "B. 船が沖合から初穂料や神酒を入れた樽を海に流し、漁師が拾って代わりに奉納する風習",
            "C. 石段参道の途中で参拝者に樽酒を振る舞う接待の伝統",
            "D. 新年に境内の井戸から汲んだ水を樽で町中に配る神事"
        ],
        "answer": "B",
        "explanation": "金刀比羅宮に直接参詣できない船が沖合を通過する際、「奉納 金刀比羅宮」と書いた白幡を立てた樽に初穂料や神酒を入れて海に流します。それを拾った漁師が代わりに金刀比羅宮へ奉納する「代参」の一形態です。この風習は江戸時代から続き、現在でも海上自衛隊の艦艇が処女航海時に行うことがあります。（出典: [金刀比羅宮 こんぴら狗](https://www.konpira.or.jp/articles/20200907_konpira-dog/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200907_konpira-dog/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_910",
        "category": "shrine",
        "difficulty": "easy",
        "question": "金刀比羅宮の御本宮の展望台から讃岐平野が一望できるのはなぜですか？",
        "choices": [
            "A. 展望用に周囲の木を全て伐採しているから",
            "B. 御本宮が象頭山の中腹・海抜251メートルに位置し、周囲を見渡せる高さにあるから",
            "C. 讃岐平野が日本一狭い平野で見渡しやすいから",
            "D. 展望台が20世紀に鉄骨で増築されたから"
        ],
        "answer": "B",
        "explanation": "金刀比羅宮の御本宮は石段785段目、象頭山の中腹・海抜251メートルに鎮座しています。讃岐平野は標高の低い平坦な地形が広がっているため、この高さから遮るものなく一望できます。展望台からは讃岐富士（飯野山）や瀬戸大橋まで見渡せ、785段を登り切った参拝者へのご褒美ともいえる絶景です。（出典: [金刀比羅宮 参拝ガイド](https://www.konpira.or.jp/articles/20200616_guide/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200616_guide/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_911",
        "category": "shrine",
        "difficulty": "easy",
        "question": "金刀比羅宮の主祭神・大物主神はどのような神徳（ご利益）を持つ神様ですか？",
        "choices": [
            "A. 戦勝と武芸上達の神",
            "B. 農業・殖産・医薬・海上守護など幅広い神徳を持つ神",
            "C. 学問と芸能に特化した文化の神",
            "D. 火災や災害からの防災専門の神"
        ],
        "answer": "B",
        "explanation": "大物主神（おおものぬしのかみ）は大国主神の和魂（にぎみたま）とされ、農業・殖産・医薬・海上守護など幅広い神徳を持ちます。特に海上守護の面が江戸時代以降に強まり、全国の船乗りや漁師から厚い信仰を集めました。金刀比羅宮には崇徳天皇も配祀されており、永万元年（1165年）に合祀されました。（出典: [金刀比羅宮 由緒](https://www.konpira.or.jp/articles/20200814_history/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200814_history/article.htm",
        "reviewed": False,
        "enabled": True
    },
    # === Team B: 歌舞伎・歴史・五街道 (912-923) ===
    {
        "id": "kotohira_912",
        "category": "history",
        "difficulty": "medium",
        "question": "金丸座（旧金毘羅大芝居）が「現存する日本最古の芝居小屋」と呼ばれるのはなぜですか？",
        "choices": [
            "A. 奈良時代に建てられた能舞台を改築したものだから",
            "B. 天保6年（1835年）に建てられ、火災や戦災を免れて現存しているから",
            "C. 江戸幕府が公式に認定した最初の劇場だから",
            "D. 明治政府が「最古」の称号を授与したから"
        ],
        "answer": "B",
        "explanation": "金丸座は天保6年（1835年）に大坂道頓堀の大西芝居（後の浪花座）を模して建設された常設の芝居小屋です。全国にあった江戸時代の芝居小屋の多くが火災や老朽化で失われる中、金丸座は奇跡的に残り、昭和45年（1970年）に国の重要文化財に指定されました。（出典: [こんぴら歌舞伎 旧金毘羅大芝居について](https://www.konpirakabuki.jp/history/reform.html)）",
        "source": "https://www.konpirakabuki.jp/history/reform.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_913",
        "category": "history",
        "difficulty": "medium",
        "question": "金丸座が一度は衰退しながらも歌舞伎公演の場として復活できたのはなぜですか？",
        "choices": [
            "A. 文化庁が歌舞伎専用劇場として再建を命じたから",
            "B. 澤村藤十郎ら歌舞伎役者の公演希望を受け、近兼孝休らが実現に動いたから",
            "C. 松竹が自社の歌舞伎興行の地方拠点として買い取ったから",
            "D. 琴平町が町おこしのために新築の芝居小屋を建設したから"
        ],
        "answer": "B",
        "explanation": "1984年、テレビ番組の収録で金丸座を訪れた澤村藤十郎ら3名の歌舞伎役者が「この舞台で演じたい」と熱望しました。琴平グランドホテル社長の近兼孝休は、町の観光業に危機感を抱いていたこともあり、松竹やJTBの協力を取り付けて翌1985年に第1回「四国こんぴら歌舞伎大芝居」を実現させました。（出典: [旧金毘羅大芝居 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85)）",
        "source": "https://ja.wikipedia.org/wiki/%E6%97%A7%E9%87%91%E6%AF%98%E7%BE%85%E5%A4%A7%E8%8A%9D%E5%B1%85",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_914",
        "category": "history",
        "difficulty": "medium",
        "question": "日柳燕石が高松藩に投獄された理由は何ですか？",
        "choices": [
            "A. 藩の年貢を横領した罪に問われたため",
            "B. 長州藩士・高杉晋作を匿い逃亡させたため",
            "C. 禁止されていたキリスト教を布教したため",
            "D. 藩主を批判する漢詩を出版したため"
        ],
        "answer": "B",
        "explanation": "慶応元年（1865年）、幕吏に追われた長州藩の高杉晋作が榎井村の燕石を頼って亡命しました。燕石は高杉を匿い逃亡させましたが、この嫌疑で高松藩に捕らえられ、約4年間投獄されました。鳥羽・伏見の戦い後、高松藩が朝敵の汚名を恐れたことで慶応4年に出獄が許されました。（出典: [コトバンク 日柳燕石](https://kotobank.jp/word/%E6%97%A5%E6%9F%B3%E7%87%95%E7%9F%B3-16408)）",
        "source": "https://kotobank.jp/word/%E6%97%A5%E6%9F%B3%E7%87%95%E7%9F%B3-16408",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_915",
        "category": "history",
        "difficulty": "medium",
        "question": "琴陵宥常が大日本帝国水難救済会の設立に尽力した背景にある事件は何ですか？",
        "choices": [
            "A. 日清戦争での艦船沈没事故",
            "B. ノルマントン号事件で日本人乗客全員が水死した惨事",
            "C. 関門海峡での連絡船転覆事故",
            "D. 瀬戸内海での大規模な海賊被害"
        ],
        "answer": "B",
        "explanation": "1886年（明治19年）、英国船ノルマントン号が紀州沖で沈没し、英国人船員は全員救助されたものの日本人乗客25名は全員水死しました。海の守り神・金刀比羅宮の宮司であった琴陵宥常はこの惨事に強い問題意識を持ち、「大日本帝国水難救済会大旨」を作成。黒田清隆首相に直談判し、1889年に水難救済会の設立を実現させました。（出典: [琴陵宥常 飛鳥の扉](https://www.asuka-tobira.com/dozo/album/12meijijidai/kotookahirotsune/index.html)）",
        "source": "https://www.asuka-tobira.com/dozo/album/12meijijidai/kotookahirotsune/index.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_916",
        "category": "history",
        "difficulty": "medium",
        "question": "江戸時代に金毘羅参りが爆発的に流行した主な理由はどれですか？",
        "choices": [
            "A. 幕府が全国民に金毘羅参りを義務付けたため",
            "B. 交通網の整備や経済的余裕の出現で庶民の旅が可能になったため",
            "C. 金毘羅宮が無料の宿泊施設を全国に設置したため",
            "D. 外国人宣教師が金毘羅信仰を海外に広めたため"
        ],
        "answer": "B",
        "explanation": "江戸時代中期以降、五街道をはじめとする交通網の整備と治安の改善、さらに農業技術の進歩による庶民の現金収入の増加が旅の環境を整えました。「金毘羅講」という積立制度で旅費を工面する仕組みも広がり、伊勢参りと並んで「一生に一度はこんぴらさんへ」が庶民の夢となりました。（出典: [折橋商店 金毘羅信仰とは](https://orihasisyouten.jp/blog/konpira-shinkou/)）",
        "source": "https://orihasisyouten.jp/blog/konpira-shinkou/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_917",
        "category": "history",
        "difficulty": "medium",
        "question": "丸亀街道が金毘羅五街道の中で最も栄えた理由は何ですか？",
        "choices": [
            "A. 幕府が丸亀街道のみを公式参詣路と認定したため",
            "B. 丸亀港が海路で到着する参詣客の玄関口で、琴平までの陸路が短く平坦だったため",
            "C. 丸亀藩主が街道沿いに無料の茶屋を設けたため",
            "D. 丸亀街道沿いに温泉地が多く観光客を集めたため"
        ],
        "answer": "B",
        "explanation": "金毘羅参りの参詣客の大半は大坂や備前など各地から「金毘羅船」で海路丸亀港に到着しました。丸亀港の太助灯籠から琴平の高灯籠まで約150丁（約12km）と陸路が短く平坦であったことが、五街道の中でも最も利用された理由です。（出典: [丸亀市公式サイト 金毘羅街道](https://www.city.marugame.lg.jp/page/3064.html)）",
        "source": "https://www.city.marugame.lg.jp/page/3064.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_918",
        "category": "history",
        "difficulty": "medium",
        "question": "和田邦坊が灸まんの商品開発からパッケージデザインまでを手がけた経緯として正しいのはどれですか？",
        "choices": [
            "A. 東京の広告代理店から琴平の企業へ派遣されたため",
            "B. 故郷・琴平の菓子店から「本物の土産物を作りたい」と懇願されたため",
            "C. 自分で菓子店を創業し、自らデザインも担当したため",
            "D. 香川県庁の依頼で県内の土産物を統一デザインしたため"
        ],
        "answer": "B",
        "explanation": "和田邦坊は1899年に琴平町で生まれ、東京日日新聞で風刺漫画家として活躍した後、1938年に故郷へ帰りました。「こんぴら堂」（後の灸まん本舗石段や）の主人から何度も協力を求められ、当初は断っていたものの、「本物の琴平の土産物を作りたい」という真摯な思いを受けて、屋号・商品名・パッケージ・内装まで一貫してプロデュースしました。（出典: [灸まん美術館](https://kyuman.art/)）",
        "source": "https://kyuman.art/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_919",
        "category": "history",
        "difficulty": "easy",
        "question": "「金丸座」とはどのような建物ですか？",
        "choices": [
            "A. 琴平町にある江戸時代の商家を復元した資料館",
            "B. 天保6年（1835年）に建てられた、現存する日本最古の芝居小屋",
            "C. 金刀比羅宮の本殿に隣接する神楽殿",
            "D. 明治時代に建設された琴平町初の映画館"
        ],
        "answer": "B",
        "explanation": "金丸座（正式名称：旧金毘羅大芝居）は天保6年に建てられた芝居小屋で、国の重要文化財に指定されています。回り舞台やせり上がりなどの舞台機構がすべて人力で動く江戸時代のままの姿が残り、毎年春には「四国こんぴら歌舞伎大芝居」が上演されます。（出典: [琴平町 旧金毘羅大芝居（金丸座）](https://www.town.kotohira.kagawa.jp/soshiki/3/1270.html)）",
        "source": "https://www.town.kotohira.kagawa.jp/soshiki/3/1270.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_920",
        "category": "history",
        "difficulty": "easy",
        "question": "「金毘羅五街道」とは何ですか？",
        "choices": [
            "A. 金刀比羅宮の境内にある5つの参道の総称",
            "B. 各地から金刀比羅宮へ向かう参詣道のうち、特に利用者が多かった5つの街道の総称",
            "C. 江戸幕府が整備した東海道など五街道の別名",
            "D. 琴平町内の5つの商店街を結ぶ道路の愛称"
        ],
        "answer": "B",
        "explanation": "金毘羅五街道とは、丸亀街道・多度津街道・高松街道・阿波街道・伊予土佐街道の5つです。江戸時代、全国から金毘羅参りに訪れる参詣客がこれらの街道を利用しました。特に丸亀街道と多度津街道は、海路で港に着いた参詣客が多く利用し栄えました。（出典: [琴平町観光協会 こんぴら五街道](https://www.kotohirakankou.jp/spot/entry-54.html)）",
        "source": "https://www.kotohirakankou.jp/spot/entry-54.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_921",
        "category": "history",
        "difficulty": "easy",
        "question": "「こんぴら狗」とはどのような風習ですか？",
        "choices": [
            "A. 金刀比羅宮で飼われていた神の使いの犬を崇拝する祭り",
            "B. 飼い主の代わりに犬が金刀比羅宮を参拝する代参の風習",
            "C. 琴平の参道で犬を使って荷物を運ばせる運送の仕組み",
            "D. 石段の番犬として犬を配置して参拝者を守る制度"
        ],
        "answer": "B",
        "explanation": "江戸時代、参拝が難しい飼い主に代わって犬が金刀比羅宮を目指しました。犬の首には「こんぴら参り」と書いた袋が下げられ、中には飼い主の木札・初穂料・道中の食費が入っていました。街道筋の旅人や住民が次々と世話をしながらリレー式で犬を送り届けたのです。（出典: [金刀比羅宮 こんぴら狗](https://www.konpira.or.jp/articles/20200907_konpira-dog/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200907_konpira-dog/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_922",
        "category": "history",
        "difficulty": "easy",
        "question": "日柳燕石はどのような人物ですか？",
        "choices": [
            "A. 江戸時代に金刀比羅宮を建立した神職",
            "B. 琴平出身の幕末の勤王家で、詩文に長じた博徒の親分",
            "C. 琴平で讃岐うどんの製法を確立した料理人",
            "D. 明治時代に琴平の鉄道敷設を推進した実業家"
        ],
        "answer": "B",
        "explanation": "日柳燕石（1817-1868）は琴平出身の幕末の志士です。博徒の親分でありながら漢詩や書画に優れた文化人で、「呑象楼」と名づけた自邸に多くの勤王の志士を匿いました。長州藩の高杉晋作を匿った罪で投獄され、出獄後は戊辰戦争に従軍しましたが、越後柏崎の陣中で病没しました。（出典: [コトバンク 日柳燕石](https://kotobank.jp/word/%E6%97%A5%E6%9F%B3%E7%87%95%E7%9F%B3-16408)）",
        "source": "https://kotobank.jp/word/%E6%97%A5%E6%9F%B3%E7%87%95%E7%9F%B3-16408",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_923",
        "category": "history",
        "difficulty": "easy",
        "question": "「門前町」とはどのような町ですか？",
        "choices": [
            "A. 城の正門前に武家屋敷が並ぶ城下町の一種",
            "B. 神社や寺院の参道沿いに発展した町",
            "C. 港の入口に倉庫が建ち並ぶ貿易拠点の町",
            "D. 宿場町の中でも特に関所がある町"
        ],
        "answer": "B",
        "explanation": "門前町とは、神社や寺院の門前（参道沿い）に参拝者向けの宿屋・土産物店・飲食店などが集まって発展した町のことです。琴平町は金刀比羅宮の門前町として江戸時代から栄え、江戸時代のガイドブック『金毘羅参詣名所図会』にも宿屋や飲食店が軒を連ねる賑わいが描かれています。（出典: [LIFULL HOME'S 庶民の憧れだった参拝の旅](https://www.homes.co.jp/cont/press/reform/reform_01116/)）",
        "source": "https://www.homes.co.jp/cont/press/reform/reform_01116/",
        "reviewed": False,
        "enabled": True
    },
    # === Team C: 観光・文化・グルメ (924-935) ===
    {
        "id": "kotohira_924",
        "category": "culture",
        "difficulty": "medium",
        "question": "なぜ鞘橋には屋根がついているのですか？",
        "choices": [
            "A. 金毘羅祭礼図に描かれた市場の雨よけとして後から増設された",
            "B. 刀の鞘に見立てた唐破風造の屋根で、神橋としての格式を示すため",
            "C. 洪水で何度も流失したため、橋の強度を補強する目的で追加された",
            "D. 参拝者が雨宿りできるよう、明治時代に琴平町が設置した"
        ],
        "answer": "B",
        "explanation": "鞘橋は唐破風造・銅葺の屋根を備えるアーチ型木造橋で、刀の鞘を連想させる形状が名前の由来です。金刀比羅宮の神事専用橋として、祭典奉仕の神職や巫女のみが渡ることを許されており、屋根は神聖な空間を覆い格式を表す構造です。橋脚がなく川の上に浮いて見えることから別名「浮橋」とも呼ばれます。（出典: [琴平海洋博物館 鞘橋](https://kotohira.kaiyohakubutukan.or.jp/syuhen-spot/sayabashi/)）",
        "source": "https://kotohira.kaiyohakubutukan.or.jp/syuhen-spot/sayabashi/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_925",
        "category": "food",
        "difficulty": "medium",
        "question": "なぜ灸まんは「灸」の名を冠しているのですか？",
        "choices": [
            "A. 金刀比羅宮の境内で灸治療が行われていた歴史に由来する",
            "B. 参道の旅籠で名物だった「金毘羅灸」の逸話にちなみ、お灸の形をした饅頭として創作された",
            "C. 饅頭を焼く際にお灸と同じもぐさを燃料に使っていたため",
            "D. 創業者がお灸の製造販売から菓子業に転業したため"
        ],
        "answer": "B",
        "explanation": "灸まんの前身は1765年（明和2年）創業の旅籠「麻田屋久八」で、宿泊客に据える「金毘羅灸」が名物でした。天保年間に侠客・小金井小次郎が泊まった際、女中が柔らかい灸を据えたところ「こいつは甘めぇお灸だ」と言ったという逸話があり、六代目主人がこれに着想を得てお灸の形の饅頭を創始しました。（出典: [灸まん - Wikipedia](https://ja.wikipedia.org/wiki/%E7%81%B8%E3%81%BE%E3%82%93)）",
        "source": "https://ja.wikipedia.org/wiki/%E7%81%B8%E3%81%BE%E3%82%93",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_926",
        "category": "food",
        "difficulty": "medium",
        "question": "なぜ讃岐うどんは香川県の名物になったのですか？",
        "choices": [
            "A. 江戸幕府が讃岐藩にうどんの専売権を与えたため",
            "B. 温暖で雨が少ない瀬戸内海式気候のもと、小麦・塩・醤油・いりこが全て県内で揃ったため",
            "C. 弘法大師が唐から持ち帰ったうどんを高野山でのみ製造を許可したため",
            "D. 明治時代に讃岐出身の実業家が全国にチェーン展開したため"
        ],
        "answer": "B",
        "explanation": "香川県は温暖かつ降水量が少ない瀬戸内海式気候で、良質な小麦の栽培に適していました。さらに古くからの塩の産地であり、小豆島は江戸時代から醤油の名産地、瀬戸内海では上質ないりこが豊富に獲れたことから、うどん作りに必要な材料が全て地元で調達できました。米作りに不向きな土地柄も、うどん文化の発展を後押ししました。（出典: [般若林 讃岐うどんの歴史](https://hannyarin-sanukiudon.com/history/)）",
        "source": "https://hannyarin-sanukiudon.com/history/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_927",
        "category": "culture",
        "difficulty": "medium",
        "question": "なぜ讃岐一刀彫は琴平の土産物として定着したのですか？",
        "choices": [
            "A. 金刀比羅宮の旭社建立のため集まった宮大工が、余り材で木像を彫り参拝者に配ったのが始まりだから",
            "B. 江戸時代に琴平藩主が木彫りの技術を奨励し、藩の特産品として保護したから",
            "C. 明治時代に琴平出身の彫刻家が東京美術学校で学び、地元に持ち帰ったから",
            "D. 金刀比羅宮の神職が御札代わりに木彫りの守り神を参拝者に授与したから"
        ],
        "answer": "A",
        "explanation": "讃岐一刀彫は天保8年（1837年）頃、金刀比羅宮の重要文化財「旭社」建立のために全国から集まった宮大工たちが、余った木材やクスノキで腕試しに木像を彫り、参拝者に配ったことが起源です。参道という好立地もあり、参拝土産として自然に定着しました。（出典: [LOVEさぬきさん 第30回 讃岐一刀彫](https://www.kensanpin.org/report/no30/)）",
        "source": "https://www.kensanpin.org/report/no30/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_928",
        "category": "culture",
        "difficulty": "medium",
        "question": "なぜこんぴら温泉郷は1997年まで温泉がなかったのですか？",
        "choices": [
            "A. 琴平町の条例で温泉掘削が禁止されていたため",
            "B. 門前宿場町として参拝客で十分賑わっていたため温泉を掘る必要がなかった",
            "C. 地質調査で温泉脈が存在しないと判定されていたため",
            "D. 金刀比羅宮が神域の地下水利用を許可しなかったため"
        ],
        "answer": "B",
        "explanation": "琴平は江戸時代から金毘羅参りの門前町として栄え、温泉がなくても宿泊需要は十分でした。しかし1990年代にレジャーの多様化で宿泊客が減少。旅館経営者の近兼孝休が巻き返しを図り、1997年に自己保有地で温泉掘削に成功。周辺施設にも湯を供給して温泉郷が形成されました。（出典: [こんぴら温泉郷 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%81%93%E3%82%93%E3%81%B4%E3%82%89%E6%B8%A9%E6%B3%89%E9%83%B7)）",
        "source": "https://ja.wikipedia.org/wiki/%E3%81%93%E3%82%93%E3%81%B4%E3%82%89%E6%B8%A9%E6%B3%89%E9%83%B7",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_929",
        "category": "culture",
        "difficulty": "medium",
        "question": "なぜ琴平海洋博物館（海の科学館）は海のない内陸の琴平町にあるのですか？",
        "choices": [
            "A. 琴平町が瀬戸内海国立公園の管理拠点に指定されているため",
            "B. 金刀比羅宮が海上守護の神として信仰されており、海との深い縁があるため",
            "C. 建設当時、沿岸部より内陸のほうが土地代が安く、大規模施設を建設しやすかったため",
            "D. 讃岐の製塩業の歴史を紹介する目的で琴平が選ばれたため"
        ],
        "answer": "B",
        "explanation": "金刀比羅宮の御祭神・大物主神は海上守護の神徳を持ち、「海の神様の総本山」として全国の船乗りから信仰されてきました。伝説では琴平山はかつて瀬戸内海に浮かぶ島で、周辺は良港だったとされます。この海との深い結びつきから、金刀比羅宮のおひざ元に海洋博物館が建てられました。（出典: [金刀比羅宮 由緒](https://www.konpira.or.jp/articles/20200814_history/article.htm)）",
        "source": "https://www.konpira.or.jp/articles/20200814_history/article.htm",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_930",
        "category": "food",
        "difficulty": "medium",
        "question": "なぜ金陵は琴平の地酒として知られるようになったのですか？",
        "choices": [
            "A. 琴平の湧水が日本酒醸造に最適であることを科学的に証明した最初の蔵元だったから",
            "B. 八代目当主が水と米に恵まれた琴平で酒造株を取得し、金刀比羅宮の御神酒醸造元となったから",
            "C. 金刀比羅宮の神職が副業として酒造りを始め、参拝者に振る舞ったのが起源だから",
            "D. 明治政府の殖産興業政策により琴平に官営酒造工場が設立されたから"
        ],
        "answer": "B",
        "explanation": "西野金陵は万治元年（1658年）に阿波で藍の取り扱いから創業。安永8年（1779年）に酒造業を始め、寛政元年（1789年）に八代目当主が水と米に恵まれた琴平で酒造株を買い受けました。金刀比羅宮の御神酒醸造元となったことで「こんぴら酒」として全国の参拝客に親しまれるようになりました。「金陵」の名は儒学者・頼山陽が琴平を中国の古都・金陵（南京）になぞらえたことに由来します。（出典: [たのしいお酒.jp 金陵](https://tanoshiiosake.jp/7032)）",
        "source": "https://tanoshiiosake.jp/7032",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_931",
        "category": "food",
        "difficulty": "easy",
        "question": "讃岐うどんとはどのような特徴を持つうどんですか？",
        "choices": [
            "A. 極細麺で、温かいつゆにつけて食べるのが基本のうどん",
            "B. 香川県産の小麦を使い、強いコシと弾力が特徴の手打ちうどん",
            "C. そば粉を混ぜた灰色がかった太麺が特徴のうどん",
            "D. 卵を練り込んだ黄色い麺が特徴の平打ちうどん"
        ],
        "answer": "B",
        "explanation": "讃岐うどんは香川県の名物で、足踏みによって鍛えられた生地の強いコシと弾力が最大の特徴です。公正競争規約では、小麦粉に対し加水量40%以上、食塩3%以上、熟成2時間以上などの基準が定められています。香川県のうどん消費量・生産量は全国1位です。（出典: [坂出山下うどん 讃岐うどんの定義と特徴](https://yamashitaudon.shop/udon/)）",
        "source": "https://yamashitaudon.shop/udon/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_932",
        "category": "food",
        "difficulty": "easy",
        "question": "灸まんとはどんなお菓子ですか？",
        "choices": [
            "A. 金刀比羅宮の扇をかたどった飴菓子",
            "B. お灸（もぐさ）の形をした、黄身餡入りの饅頭",
            "C. こんにゃくを使った参道名物のヘルシー和菓子",
            "D. 抹茶餡を包んだ緑色のどら焼き"
        ],
        "answer": "B",
        "explanation": "灸まんは琴平名物の饅頭で、お灸のもぐさの形をしています。頂上部が丸く盛り上がったやや円錐形に近い形で、鶏卵の黄身を使った上品な甘さの餡が特徴です。灸まん本舗石段やは1765年（明和2年）に旅籠として創業し、参道の名物「金毘羅灸」にちなんでこの饅頭を考案しました。（出典: [灸まん - Wikipedia](https://ja.wikipedia.org/wiki/%E7%81%B8%E3%81%BE%E3%82%93)）",
        "source": "https://ja.wikipedia.org/wiki/%E7%81%B8%E3%81%BE%E3%82%93",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_933",
        "category": "culture",
        "difficulty": "easy",
        "question": "高灯籠とはどのような建造物ですか？",
        "choices": [
            "A. 金刀比羅宮の本殿前に置かれた石造りの小さな灯籠",
            "B. 高さ約27mの木造灯籠で、瀬戸内海を航行する船の目印だった",
            "C. 参道の入口に建つ青銅製の門灯",
            "D. 琴平山の山頂に設置された近代式の灯台"
        ],
        "answer": "B",
        "explanation": "高灯籠は慶応元年（1865年）に献納された高さ約27mの木造3階建ての灯籠で、木造灯籠としては日本一の高さを誇ります。丸亀沖の船にも光が届くよう設計され、瀬戸内海を航海する船の目標灯として機能しました。国の重要有形民俗文化財に指定されています。（出典: [琴平海洋博物館 高灯籠](https://kotohira.kaiyohakubutukan.or.jp/syuhen-spot/takatoro/)）",
        "source": "https://kotohira.kaiyohakubutukan.or.jp/syuhen-spot/takatoro/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_934",
        "category": "culture",
        "difficulty": "easy",
        "question": "鞘橋とはどんな橋ですか？",
        "choices": [
            "A. 金刀比羅宮の参道にある石造りのアーチ橋",
            "B. 刀の鞘に似た形の屋根付き木造橋で、神事の際にのみ渡れる",
            "C. 琴平町と隣町を結ぶ近代的な吊り橋",
            "D. 金倉川に架かる赤い欄干の太鼓橋"
        ],
        "answer": "B",
        "explanation": "鞘橋は金刀比羅宮の神事場にある唐破風造・銅葺の屋根を備えたアーチ型木造橋です。長さ23.6m、幅4.5mで、橋脚がないため川に浮いて見えることから別名「浮橋」とも呼ばれます。現在は大祭の御神輿渡御など神事の際にのみ使用され、一般の通行はできません。国の登録有形文化財です。（出典: [琴平海洋博物館 鞘橋](https://kotohira.kaiyohakubutukan.or.jp/syuhen-spot/sayabashi/)）",
        "source": "https://kotohira.kaiyohakubutukan.or.jp/syuhen-spot/sayabashi/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_935",
        "category": "culture",
        "difficulty": "easy",
        "question": "金陵の郷とはどのような施設ですか？",
        "choices": [
            "A. 金刀比羅宮が運営する宝物殿",
            "B. 寛政元年創業の酒蔵を復元した日本酒の資料館で、入場無料で見学・試飲ができる",
            "C. 琴平町の歴史民俗を展示する町立博物館",
            "D. 金刀比羅宮の神職養成のための研修施設"
        ],
        "answer": "B",
        "explanation": "金陵の郷は、寛政元年（1789年）創業の西野金陵の琴平本店酒蔵を創業当時の白壁の姿に復元した施設です。「歴史館」と「文化館」があり、江戸時代の酒造りの工程を人形や道具で再現しています。入場無料で清酒金陵の試飲もできます。（出典: [西野金陵 金陵の郷](https://www.nishino-kinryo.co.jp/museum/)）",
        "source": "https://www.nishino-kinryo.co.jp/museum/",
        "reviewed": False,
        "enabled": True
    },
    # === Team D: 地理・祭り・現代 (936-947) ===
    {
        "id": "kotohira_936",
        "category": "geography",
        "difficulty": "medium",
        "question": "琴平町が平成の大合併で周辺自治体と合併せず単独存続を選んだ主な背景はどれですか？",
        "choices": [
            "A. 県から合併対象外の特別指定を受けていたため",
            "B. 金刀比羅宮の門前町として独自の観光経済基盤を持ち、宿泊業などの労働生産性が高かったため",
            "C. 周辺自治体がすべて合併を拒否したため",
            "D. 町の面積が合併対象の基準を下回っていたため"
        ],
        "answer": "B",
        "explanation": "琴平町は面積約8.47km²と小さいものの、金刀比羅宮の門前町として「宿泊業・飲食サービス業」の労働生産性が香川県内で高い水準にあり、観光産業を軸とした独自の経済基盤が単独存続の判断を支えました。（出典: [全国町村会 琴平町](https://www.zck.or.jp/site/forum/7254.html)）",
        "source": "https://www.zck.or.jp/site/forum/7254.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_937",
        "category": "event",
        "difficulty": "medium",
        "question": "金刀比羅宮の例大祭で、御祭神が山上の御本宮から麓の門前町へ神輿で降りる「お下がり」が夜に行われるのはなぜですか？",
        "choices": [
            "A. 夜間の方が参道の混雑を避けられるため",
            "B. 神様の渡御は古来より神聖な夜の闇の中で厳かに行うものとされているため",
            "C. 電飾による演出効果を高めるため",
            "D. 門前町の店舗が閉店した後に行列を通すため"
        ],
        "answer": "B",
        "explanation": "御神幸（おみゆき）は江戸時代以前から続く神事で、神様の渡御は闇の中で厳粛に行われるのが古来の慣わしです。約500人が約700mの行列を作り、松明や提灯の灯りだけで2kmの道のりを進む様は、平安絵巻さながらと評されます。（出典: [物語を届けるしごと 金刀比羅宮例大祭](https://yousakana.jp/konpira-shrine-festival/)）",
        "source": "https://yousakana.jp/konpira-shrine-festival/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_938",
        "category": "event",
        "difficulty": "medium",
        "question": "こんぴら石段マラソンが琴平町で50年以上にわたり開催されている主な理由はどれですか？",
        "choices": [
            "A. 金刀比羅宮の785段の石段という全国有数の地形を活かし、例大祭の奉祝行事として健脚祈願を目的に始まったため",
            "B. 箱根駅伝の予選会場として選ばれたことがきっかけ",
            "C. 琴平町が国のスポーツ振興特区に指定されたため",
            "D. 地元の陸上競技連盟が合宿地として石段を利用していたため"
        ],
        "answer": "A",
        "explanation": "こんぴら石段マラソンは「金刀比羅宮例大祭奉祝奉賛行事」として開催され、全国有数の門前町・琴平の特徴である石段を登ることで観光地琴平の認識を深めるとともに、健脚を祈願することが目的です。2014年からは順位を競わない形式に変更され、誰でも気軽に参加できる大会となりました。（出典: [Moshicom こんぴら石段マラソン](https://moshicom.com/111190/)）",
        "source": "https://moshicom.com/111190/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_939",
        "category": "culture",
        "difficulty": "medium",
        "question": "民謡「金毘羅船々」が幕末から明治にかけて全国のお座敷に広まった主な理由はどれですか？",
        "choices": [
            "A. 明治政府が国民教育用の歌として全国の学校に配布したため",
            "B. 金毘羅参りの流行を背景に、短く軽妙な騒ぎ唄として座敷遊びに好まれたため",
            "C. レコード会社が流行歌として全国販売したため",
            "D. 金刀比羅宮が全国の分社に歌唱を義務付けたため"
        ],
        "answer": "B",
        "explanation": "江戸時代、金毘羅参りは伊勢詣と並ぶ庶民の憧れで、大坂から丸亀への参詣船「こんぴら船」が多くの旅人を運びました。その道中唄として生まれた「金毘羅船々」は、小気味よいテンポと情景豊かな歌詞から騒ぎ唄として座敷に取り入れられ、全国的に広まりました。（出典: [四国新聞 21世紀へ残したい香川](https://www.shikoku-np.co.jp/feature/nokoshitai/bu/9/)）",
        "source": "https://www.shikoku-np.co.jp/feature/nokoshitai/bu/9/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_940",
        "category": "geography",
        "difficulty": "medium",
        "question": "金刀比羅宮が鎮座する「象頭山（ぞうずさん）」の名前の由来として有力な説はどれですか？",
        "choices": [
            "A. 象の化石が山頂から発掘されたため",
            "B. 琴平街道から眺めた山容が象の頭に似ており、さらにインドの仏教聖地と山容・聖地としての性格が共通するため",
            "C. 江戸時代に象が参道を歩いたという記録があるため",
            "D. 山の岩肌が象の皮膚のような模様をしているため"
        ],
        "answer": "B",
        "explanation": "象頭山の名は、琴平街道から見た山の形が象の頭を思わせることに由来します。金刀比羅宮の位置が「目」にあたり、南側の愛宕山が「鼻」に見立てられます。また、インド中部ガヤーの聖地「ガヤーシールシャ」は漢訳経典で「象頭山」と訳され、金毘羅大権現が鎮座する聖地という共通性から同名で呼ばれたとする説もあります。（出典: [Wikipedia 象頭山 (香川県)](https://ja.wikipedia.org/wiki/%E8%B1%A1%E9%A0%AD%E5%B1%B1_(%E9%A6%99%E5%B7%9D%E7%9C%8C))）",
        "source": "https://ja.wikipedia.org/wiki/%E8%B1%A1%E9%A0%AD%E5%B1%B1_(%E9%A6%99%E5%B7%9D%E7%9C%8C)",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_941",
        "category": "modern",
        "difficulty": "medium",
        "question": "琴平町が2021年に電子地域通貨「KOTOCA（コトカ）」を導入した主な理由はどれですか？",
        "choices": [
            "A. 国の実証実験に選ばれたデジタル通貨モデル事業のため",
            "B. 新型コロナで打撃を受けた町内経済の活性化と、お金の地域内循環を促すため",
            "C. 外国人観光客の利便性向上のため",
            "D. 町役場の窓口業務をキャッシュレス化するため"
        ],
        "answer": "B",
        "explanation": "コロナ禍で観光客数が前年比4割超減少し、町内のスーパーも1店舗を残すのみとなるなど、地域経済が深刻な状況にありました。KOTOCAは全町民約8,600人に一律5,000コトカを給付して町内消費を喚起するとともに、非接触決済による感染症対策やDX推進を図る目的で導入されました。香川県内初の電子地域通貨給付事業でした。（出典: [フェリカポケットマーケティング KOTOCA](https://www.felicapocketmk.co.jp/news/20211215/812/)）",
        "source": "https://www.felicapocketmk.co.jp/news/20211215/812/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_942",
        "category": "modern",
        "difficulty": "medium",
        "question": "琴平町と旧大社町（現・出雲市）が2004年に友好都市協定を締結した主な理由はどれですか？",
        "choices": [
            "A. 両町の御祭神が同一の神であることが学術的に証明されたため",
            "B. 歌舞伎公演に伴うお練りへの相互参加など、長年の文化交流の実績があったため",
            "C. 四国と山陰を結ぶ高速道路の開通を記念したため",
            "D. 両町の人口規模と面積がほぼ同じだったため"
        ],
        "answer": "B",
        "explanation": "琴平町（金刀比羅宮）と旧大社町（出雲大社）はともに日本を代表する門前町であり、歌舞伎公演のお練りに相互参加するなど長年にわたる文化交流を重ねてきました。この友好関係を正式に認めるかたちで2004年9月25日に友好都市協定が締結されました。現在も「三麺交流会」（三輪そうめん・讃岐うどん・出雲そば）などの交流事業が行われています。（出典: [出雲市 国内友好交流都市事業の概要](https://www.city.izumo.shimane.jp/www/contents/1487306213767/index.html)）",
        "source": "https://www.city.izumo.shimane.jp/www/contents/1487306213767/index.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_943",
        "category": "event",
        "difficulty": "easy",
        "question": "金刀比羅宮の「例大祭」とは何ですか？",
        "choices": [
            "A. 毎年10月9日～11日に行われる、金刀比羅宮で最も重要な年中祭事",
            "B. 毎年1月に行われる初詣の特別行事",
            "C. 春に行われる桜の植樹祭",
            "D. 夏に行われる花火大会"
        ],
        "answer": "A",
        "explanation": "例大祭は金刀比羅宮の特殊神事であり、最も重要なお祭りです。全体の期間は8月31日の口明神事から10月15日の焼払神事まで46日間にわたりますが、中心となるのは10月9日～11日の3日間。10月10日夜の「お下がり」では御祭神が神輿で門前町に降り、約500人の行列が平安絵巻さながらに練り歩きます。（出典: [金刀比羅宮公式 例大祭のご案内](https://www.konpira.or.jp/articles_2025/20250910_1010/article.html)）",
        "source": "https://www.konpira.or.jp/articles_2025/20250910_1010/article.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_944",
        "category": "modern",
        "difficulty": "easy",
        "question": "琴平町のマスコットキャラクター「こんぴーくん」はどのような存在ですか？",
        "choices": [
            "A. 金刀比羅宮の石段に住むタヌキのキャラクター",
            "B. 天保6年（1835年）建造の旧金毘羅大芝居（金丸座）に生まれた小さな福の神様",
            "C. 讃岐うどんをモチーフにしたゆるキャラ",
            "D. 瀬戸内海のイルカをモデルにした海の妖精"
        ],
        "answer": "B",
        "explanation": "こんぴーくんは現存する日本最古の芝居小屋「旧金毘羅大芝居」に生まれた小さな福の神様という設定です。誕生日は天保6年10月9日で、歌舞伎をこよなく愛し、六方や見得を切ることが特技。好物は霞（かすみ）と讃岐うどん。毎年春の「四国こんぴら歌舞伎大芝居」を盛り上げるPRキャラクターとして活躍しています。（出典: [全国町村会 こんぴーくん](https://www.zck.or.jp/site/local-mascot/6391.html)）",
        "source": "https://www.zck.or.jp/site/local-mascot/6391.html",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_945",
        "category": "culture",
        "difficulty": "easy",
        "question": "「金毘羅船々（こんぴらふねふね）」とはどのような歌ですか？",
        "choices": [
            "A. 金刀比羅宮の神職が祭典で歌う祝詞の一種",
            "B. 金毘羅参りの道中で歌われた民謡で、お座敷遊びの歌としても全国的に知られる",
            "C. 明治時代に作られた軍歌",
            "D. 昭和時代のNHK朝ドラの主題歌"
        ],
        "answer": "B",
        "explanation": "「金毘羅船々」は香川県琴平町を中心に歌われてきた民謡で、江戸時代に大坂から丸亀への参詣船（こんぴら船）の道中で歌われた騒ぎ唄がルーツとされます。「追風（おいて）に帆かけてシュラシュシュシュ」の軽快なフレーズが特徴で、幕末から明治にかけてお座敷遊びの歌として全国に広まりました。（出典: [四国新聞 21世紀へ残したい香川](https://www.shikoku-np.co.jp/feature/nokoshitai/bu/9/)）",
        "source": "https://www.shikoku-np.co.jp/feature/nokoshitai/bu/9/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_946",
        "category": "event",
        "difficulty": "easy",
        "question": "「こんぴら石段マラソン」とはどのようなイベントですか？",
        "choices": [
            "A. 金刀比羅宮の785段の石段を駆け上がるマラソン大会で、例大祭の奉祝行事として毎年10月に開催される",
            "B. 琴平町内の平地を走るフルマラソン大会",
            "C. 石段を使った登山トレーニング合宿",
            "D. 金刀比羅宮の神職が走る奉納行事"
        ],
        "answer": "A",
        "explanation": "こんぴら石段マラソンは金刀比羅宮例大祭の奉祝奉賛行事として毎年10月に開催されます。表参道から御本宮までの785段を往復する約2.5kmのコースで、50年以上の歴史を持ちます。2014年以降は順位を競わず健脚祈願を目的とした内容に変更され、誰でも気軽に参加できるようになりました。（出典: [Moshicom こんぴら石段マラソン](https://moshicom.com/111190/)）",
        "source": "https://moshicom.com/111190/",
        "reviewed": False,
        "enabled": True
    },
    {
        "id": "kotohira_947",
        "category": "modern",
        "difficulty": "easy",
        "question": "琴平町の電子地域通貨「KOTOCA（コトカ）」とは何ですか？",
        "choices": [
            "A. 琴平町が導入した町内の加盟店で使える電子マネーで、チャージ時にプレミアムポイントが付く",
            "B. 金刀比羅宮の参拝に使える専用電子チケット",
            "C. 琴平町と丸亀市で共通利用できる交通系ICカード",
            "D. 琴平町の公共施設の予約に使うポイントカード"
        ],
        "answer": "A",
        "explanation": "KOTOCAは2021年12月に導入された琴平町の電子地域通貨です。町内の加盟店での買い物に使え、チャージ時にプレミアムポイントが付与されます。導入時には全町民約8,600人に一律5,000コトカが給付されました。お金を地域内で循環させることで町内経済を活性化させる狙いがあります。（出典: [琴平町公式 電子地域通貨KOTOCA](https://www.town.kotohira.kagawa.jp/site/denshitiikituuka-kotoca/)）",
        "source": "https://www.town.kotohira.kagawa.jp/site/denshitiikituuka-kotoca/",
        "reviewed": False,
        "enabled": True
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
    print(f"ERROR: ID conflicts found: {conflicts}")
    exit(1)

# Append new questions
data['questions'].extend(new_questions)

# Write back
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully added {len(new_questions)} questions (kotohira_901 - kotohira_947)")
print(f"Total questions now: {len(data['questions'])}")

# Stats
enabled = sum(1 for q in data['questions'] if q.get('enabled', True))
easy = sum(1 for q in data['questions'] if q.get('difficulty') == 'easy' and q.get('enabled', True))
medium = sum(1 for q in data['questions'] if q.get('difficulty') == 'medium' and q.get('enabled', True))
hard = sum(1 for q in data['questions'] if q.get('difficulty') == 'hard' and q.get('enabled', True))
reason = sum(1 for q in data['questions'] if q.get('enabled', True) and ('なぜ' in q.get('question', '') or 'のはなぜ' in q.get('question', '') or '理由' in q.get('question', '') or '背景' in q.get('question', '') or '経緯' in q.get('question', '')))

print(f"\n--- Updated Stats ---")
print(f"Enabled: {enabled}")
print(f"Easy: {easy} ({easy/enabled*100:.1f}%)")
print(f"Medium: {medium} ({medium/enabled*100:.1f}%)")
print(f"Hard: {hard} ({hard/enabled*100:.1f}%)")
print(f"Reason-type (estimated): {reason} ({reason/enabled*100:.1f}%)")

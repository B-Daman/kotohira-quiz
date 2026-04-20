import json, re, os
from collections import defaultdict, Counter

with open('C:/Users/user/kotohira-quiz/web/public/data/kotohira_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
qs = data['questions']

def classify(q):
    text = q['question'] + ' ' + q.get('explanation', '')
    cat = q['category']

    # === 金刀比羅宮 (shrine category + architecture/history with 金刀比羅宮) ===
    if cat == 'shrine' or ('金刀比羅宮' in text and cat in ('history','architecture')):
        if any(k in text for k in ['祭神', '大物主', '崇徳天皇', '由緒', '創建', '起源', '御祭神', '祀', '御神体']):
            return ('金刀比羅宮', '祭神・由緒')
        if any(k in text for k in ['石段', '段数', '参拝', '参道', '登', '所要時間', 'かご', '駕籠', '杖']):
            return ('金刀比羅宮', '石段・参拝')
        if any(k in text for k in ['奥社', '厳魂神社', '奥宮']):
            return ('金刀比羅宮', '奥社')
        if any(k in text for k in ['御守', 'お守り', 'おまもり', 'お札', '御朱印', 'おみくじ', '授与', '黄色いお守']):
            return ('金刀比羅宮', 'お守り・授与品')
        if any(k in text for k in ['書院', '襖絵', '円山応挙', '障壁画', '美術', '宝物', '表書院', '高橋由一']):
            return ('金刀比羅宮', '書院・美術')
        if any(k in text for k in ['例大祭', '紅葉祭', '桜花祭', '蹴鞠', '奉納', '頭人', 'お頭人', '神事']):
            return ('金刀比羅宮', '祭事・神事')
        if any(k in text for k in ['本宮', '旭社', '大門', '社殿', '鳥居', '灯明', '灯籠', '狛犬', '建物', '門', '回廊', '神馬', '絵馬堂', '絵馬', '五人百姓', '神楽殿', '賢木門', '南渡殿', '北渡殿', '御前四段坂', '緑黛殿', '図書館', '宝物館']):
            return ('金刀比羅宮', '建造物・境内')
        if any(k in text for k in ['海', '航海', '船', '水軍', '海上', '漁', '金毘羅', 'こんぴら船', '丸金印', '海難']):
            return ('金刀比羅宮', '海上信仰・金毘羅信仰')
        if any(k in text for k in ['こんぴら狗', '犬', '代参']):
            return ('金刀比羅宮', 'こんぴら狗・代参')
        if any(k in text for k in ['通称', 'こんぴらさん', '年間参', '参拝者', '参詣者']):
            return ('金刀比羅宮', '基本情報')
        if any(k in text for k in ['象頭山', '森', '植物', '木', '桜', '楠', '大楠', '自然']):
            return ('金刀比羅宮', '境内・自然')
        return ('金刀比羅宮', 'その他')

    # === 金丸座・歌舞伎 ===
    if cat == 'theater' or ('金丸座' in text or '旧金毘羅大芝居' in text):
        if any(k in text for k in ['歴史', '建設', '建てられ', '重要文化財', '指定', '復元', '移築', '天保']):
            return ('金丸座・歌舞伎', '歴史・文化財')
        if any(k in text for k in ['構造', '回り舞台', '花道', 'すっぽん', 'セリ', '升席', '桟敷', '座席', '幕', 'ぶどう棚', '天井', '楽屋', '奈落']):
            return ('金丸座・歌舞伎', '建築・舞台構造')
        if any(k in text for k in ['四国こんぴら歌舞伎', '公演', '上演', '役者', '俳優', '演目', '市川', '中村', '片岡', '松本', '尾上']):
            return ('金丸座・歌舞伎', '四国こんぴら歌舞伎大芝居')
        return ('金丸座・歌舞伎', 'その他')

    # === 歴史・文化 ===
    if cat == 'history':
        if any(k in text for k in ['高灯籠', '灯台', '高燈籠']):
            return ('歴史・文化', '高灯籠')
        if any(k in text for k in ['丸亀藩', '高松藩', '藩', '大名', '生駒', '京極', '松平']):
            return ('歴史・文化', '藩政・大名')
        if any(k in text for k in ['明治', '廃藩置県', '近代化', '鉄道', '琴平電鉄', '琴電', '開通', '讃岐鉄道', '町制']):
            return ('歴史・文化', '近代化・交通史')
        if any(k in text for k in ['戦', '合戦', '源平', '平家', '屋島']):
            return ('歴史・文化', '合戦・源平')
        if any(k in text for k in ['空海', '弘法大師', '善通寺', '曼荼羅寺', '遍路', '四国霊場', '札所', '松尾寺']):
            return ('歴史・文化', '弘法大師・遍路')
        if any(k in text for k in ['金毘羅参', '参詣', '街道', '丸亀街道', '参拝道', '門前町']):
            return ('歴史・文化', '金毘羅参り・街道')
        if any(k in text for k in ['城', '天霧城', '櫛梨城']):
            return ('歴史・文化', '城')
        if any(k in text for k in ['日柳燕石', '高杉晋作', '幕末', '志士']):
            return ('歴史・文化', '幕末・日柳燕石')
        if any(k in text for k in ['平賀源内', '久米通賢', '長谷川佐太郎', '大原東野', '呑象楼', '満濃池', '藤ノ棚']):
            return ('歴史・文化', '郷土の偉人')
        if any(k in text for k in ['合併', '榎井', '象郷']):
            return ('歴史・文化', '町の沿革')
        return ('歴史・文化', 'その他')

    # === 祭り・イベント ===
    if cat == 'event':
        if any(k in text for k in ['例大祭', '大祭', '金刀比羅']):
            return ('祭り・イベント', '金刀比羅宮の祭事')
        if any(k in text for k in ['まつり', '祭り', '祭', 'フェスティバル']):
            return ('祭り・イベント', '地域の祭り・イベント')
        if any(k in text for k in ['桜', '紅葉', '花見', '季節', '正月', '初詣', '年末年始']):
            return ('祭り・イベント', '季節行事')
        return ('祭り・イベント', 'その他')

    # === 琴平町・地理 ===
    if cat == 'geography':
        if any(k in text for k in ['琴平町', '町', '人口', '面積', '住所', '合併', '仲多度郡', '郵便', '町長']):
            return ('琴平町・地理', '町の基本情報')
        if any(k in text for k in ['川', '土器川', '金倉川', '財田川', '河川']):
            return ('琴平町・地理', '河川・水系')
        if any(k in text for k in ['山', '象頭山', '大麻山', '琴平山']):
            return ('琴平町・地理', '山・地形')
        if any(k in text for k in ['駅', '鉄道', '電車', '琴電', 'JR', '交通', 'バス', 'アクセス', 'ことでん']):
            return ('琴平町・地理', '交通・アクセス')
        if any(k in text for k in ['香川', '讃岐', '四国']):
            return ('琴平町・地理', '香川県・四国')
        if any(k in text for k in ['街道', 'こんぴら街道']):
            return ('琴平町・地理', '街道')
        return ('琴平町・地理', 'その他')

    # === 建築・建造物 ===
    if cat == 'architecture':
        if any(k in text for k in ['金丸座', '芝居', '升席']):
            return ('金丸座・歌舞伎', '建築・舞台構造')
        if any(k in text for k in ['金刀比羅宮', '緑黛殿', '旭社', '神楽殿', '宝物館', '図書館']):
            return ('金刀比羅宮', '建造物・境内')
        if any(k in text for k in ['高燈籠', '高灯籠']):
            return ('建築・建造物', '高灯籠')
        if any(k in text for k in ['鞘橋', '大宮橋', '橋']):
            return ('建築・建造物', '橋梁')
        if any(k in text for k in ['鳥居', '紫銅鳥居', '町口鳥居', '街道']):
            return ('建築・建造物', '鳥居・道標')
        if any(k in text for k in ['燈籠', '灯籠', '並び燈籠', '尾州燈籠']):
            return ('建築・建造物', '灯籠')
        if any(k in text for k in ['JR琴平駅', '駅']):
            return ('建築・建造物', 'JR琴平駅')
        if any(k in text for k in ['公会堂', '琴平町公会堂']):
            return ('建築・建造物', '公共建築')
        if any(k in text for k in ['金陵', '丸尾醸造', '醸造']):
            return ('建築・建造物', '歴史的商業建築')
        if any(k in text for k in ['海の科学館']):
            return ('建築・建造物', '博物館・施設')
        if any(k in text for k in ['文化財', '登録有形文化財', '国登録']):
            return ('建築・建造物', '文化財総合')
        if any(k in text for k in ['温泉', '琴平温泉']):
            return ('建築・建造物', '温泉施設')
        return ('建築・建造物', 'その他')

    # === 観光・宿泊 ===
    if cat == 'tourism':
        if any(k in text for k in ['温泉', '琴平花壇', '紅梅亭', '宿', 'ホテル', '旅館', '敷島館', '八千代']):
            return ('観光・宿泊', '温泉・宿泊')
        if any(k in text for k in ['お土産', '土産', 'おみやげ', '買', '扇子']):
            return ('観光・宿泊', 'お土産')
        if any(k in text for k in ['表参道', '商店街', '門前']):
            return ('観光・宿泊', '表参道・門前町')
        if any(k in text for k in ['池商店', '最古', '飴']):
            return ('観光・宿泊', '老舗・名物店')
        return ('観光・宿泊', 'その他')

    # === グルメ・食文化 ===
    if cat == 'gourmet':
        if any(k in text for k in ['うどん', 'さぬき', '讃岐うどん']):
            return ('グルメ・食文化', 'うどん')
        if any(k in text for k in ['酒', '金陵', '醸造', '酒造', 'ワイン', '地酒']):
            return ('グルメ・食文化', '酒・醸造')
        if any(k in text for k in ['和三盆', '砂糖', '菓子', 'スイーツ', 'おいり', '甘味', 'ソフトクリーム', '豆', '飴', 'CAFE', 'カフェ']):
            return ('グルメ・食文化', '和菓子・スイーツ')
        if any(k in text for k in ['骨付鳥', '鶏', '焼鳥', '肉']):
            return ('グルメ・食文化', '骨付鳥・肉料理')
        if any(k in text for k in ['醤油', '味噌', '調味料', 'オリーブ']):
            return ('グルメ・食文化', '調味料・特産品')
        return ('グルメ・食文化', '飲食店・その他')

    # === 生活・文化 ===
    if cat == 'life':
        if any(k in text for k in ['学校', '教育', '小学校', '中学校', '高校']):
            return ('生活・文化', '教育')
        if any(k in text for k in ['方言', '言葉', '讃岐弁']):
            return ('生活・文化', '方言・言葉')
        if any(k in text for k in ['病院', '急病', '医療', '診療']):
            return ('生活・文化', '医療・福祉')
        if any(k in text for k in ['銀行', '百十四']):
            return ('生活・文化', '金融・経済')
        if any(k in text for k in ['人口', '面積', '郡', '駐車場', '高速', 'IC', 'アクセス', '移動', '車']):
            return ('生活・文化', '生活インフラ')
        if any(k in text for k in ['こんぴーくん', 'マスコット', 'キャラクター']):
            return ('生活・文化', 'マスコットキャラクター')
        if any(k in text for k in ['移住', '支援', '消滅可能性', '過疎', '高齢化', '町花']):
            return ('生活・文化', '町政・定住促進')
        if any(k in text for k in ['丸尾醸造', '文化財']):
            return ('生活・文化', '文化財')
        return ('生活・文化', 'その他')

    # === 現代・メディア ===
    if cat == 'modern':
        if any(k in text for k in ['映画', 'ドラマ', '撮影', 'ロケ']):
            return ('現代・メディア', '映画・ドラマ')
        if any(k in text for k in ['アニメ', '漫画', 'マンガ']):
            return ('現代・メディア', 'アニメ・漫画')
        if any(k in text for k in ['こんぴら十帖', '十帖']):
            return ('現代・メディア', 'こんぴら十帖')
        if any(k in text for k in ['敷島館', '宿泊', 'ホテル', '旅館', '客室']):
            return ('現代・メディア', '新規宿泊施設')
        if any(k in text for k in ['わん詣', '犬']):
            return ('現代・メディア', 'わん詣')
        if any(k in text for k in ['街ガチャ', 'ガチャ']):
            return ('現代・メディア', '街ガチャ')
        if any(k in text for k in ['観光', '参拝者', '年間', '魅力', '強み']):
            return ('現代・メディア', '観光振興・まちづくり')
        return ('現代・メディア', 'その他')

    return ('その他', cat)

classified = defaultdict(lambda: defaultdict(list))
for q in qs:
    theme, sub = classify(q)
    classified[theme][sub].append(q)

def extract_urls(items):
    urls = set()
    for q in items:
        src = q.get('source', '')
        if src.startswith('http'):
            urls.add(src)
        exp = q.get('explanation', '')
        for match in re.findall(r'https?://[^\s\)]+', exp):
            urls.add(match.rstrip(')'))
    return sorted(urls)

lines = []
lines.append("# 既存問題分析")
lines.append("")
lines.append("## 全体サマリー")
total = len(qs)
enabled_count = sum(1 for q in qs if q.get('enabled', True))
disabled_count = total - enabled_count
lines.append(f"- 総問題数: {total}問（有効: {enabled_count}問、無効化: {disabled_count}問）")

cats = Counter(q['category'] for q in qs)
cat_str = ", ".join(f"{c} {n}問" for c, n in cats.most_common())
lines.append(f"- カテゴリ別: {cat_str}")

lines.append("")
lines.append("### 大テーマ別問題数")
lines.append("")
lines.append("| 大テーマ | 有効 | 無効 | 合計 |")
lines.append("|----------|------|------|------|")
theme_order = [
    '金刀比羅宮', '金丸座・歌舞伎', '歴史・文化', '祭り・イベント',
    '琴平町・地理', '建築・建造物', '観光・宿泊', 'グルメ・食文化',
    '生活・文化', '現代・メディア', 'その他'
]
all_themes = list(theme_order)
for theme in sorted(classified.keys()):
    if theme not in all_themes:
        all_themes.append(theme)

for theme in all_themes:
    if theme not in classified:
        continue
    subs = classified[theme]
    t_total = sum(len(v) for v in subs.values())
    t_dis = sum(1 for sub in subs.values() for q in sub if not q.get('enabled', True))
    t_en = t_total - t_dis
    lines.append(f"| {theme} | {t_en} | {t_dis} | {t_total} |")

lines.append("")

def write_theme(theme):
    subs = classified[theme]
    t_total = sum(len(v) for v in subs.values())
    lines.append(f"## 大テーマ: {theme}（{t_total}問）")
    lines.append("")
    for sub in sorted(subs.keys()):
        items = subs[sub]
        dis_items = [q for q in items if not q.get('enabled', True)]
        en_items = [q for q in items if q.get('enabled', True)]
        dis_note = f"（うち無効化: {len(dis_items)}問）" if dis_items else ""
        lines.append(f"### サブトピック: {sub}")
        lines.append(f"- 問題数: {len(items)}問 {dis_note}")
        examples = en_items[:2] if en_items else dis_items[:2]
        for ex in examples:
            lines.append(f"- 例: 「{ex['question'][:70]}」({ex['id']})")
        if dis_items:
            dis_ids = ", ".join(q['id'] for q in dis_items)
            lines.append(f"- 無効化済みID: {dis_ids}")
        urls = extract_urls(items)
        if urls:
            lines.append(f"- 出典URL ({len(urls)}件):")
            for url in urls:
                lines.append(f"  - {url}")
        else:
            src_types = set(q.get('source', '') for q in items if q.get('source', ''))
            non_url = [s for s in src_types if not s.startswith('http')]
            if non_url:
                lines.append(f"- 出典: {', '.join(sorted(non_url))}")
        lines.append("")

for theme in all_themes:
    if theme in classified:
        write_theme(theme)

# Duplicate detection
lines.append("## 重複・類似問題の可能性")
lines.append("")
lines.append("同一事実について複数の問題がある可能性のあるグループ:")
lines.append("")

keyword_groups = defaultdict(list)
for q in qs:
    text = q['question']
    exp = q.get('explanation', '')
    both = text + ' ' + exp
    if '石段' in text and ('何段' in text or '段' in text):
        keyword_groups['石段の段数'].append(q['id'])
    if '主祭神' in text:
        keyword_groups['主祭神'].append(q['id'])
    if '通称' in text and 'こんぴら' in both:
        keyword_groups['通称こんぴらさん'].append(q['id'])
    if '奥社' in text and '段' in text:
        keyword_groups['奥社の段数'].append(q['id'])
    if '五人百姓' in text:
        keyword_groups['五人百姓'].append(q['id'])
    if '例大祭' in text and ('月' in text or 'いつ' in text):
        keyword_groups['例大祭の時期'].append(q['id'])
    if '回り舞台' in text:
        keyword_groups['回り舞台'].append(q['id'])
    if '重要文化財' in text and '金丸座' in both:
        keyword_groups['金丸座重要文化財'].append(q['id'])
    if '天保' in text:
        keyword_groups['天保年間'].append(q['id'])
    if '高燈籠' in text and ('高さ' in text or '何メートル' in text):
        keyword_groups['高灯籠の高さ'].append(q['id'])

for topic, ids in sorted(keyword_groups.items()):
    if len(ids) >= 2:
        lines.append(f"- {topic}: {', '.join(ids)}")

lines.append("")

output = "\n".join(lines)
outpath = 'C:/Users/user/kotohira-quiz/docs/draft/existing_analysis.md'

os.makedirs(os.path.dirname(outpath), exist_ok=True)
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Written to {outpath}")
print(f"Total lines: {len(lines)}")

# Print summary of classification
print("\n=== Classification Summary ===")
for theme in all_themes:
    if theme not in classified:
        continue
    subs = classified[theme]
    t_total = sum(len(v) for v in subs.values())
    print(f"\n{theme} ({t_total})")
    for sub in sorted(subs.keys()):
        print(f"  {sub}: {len(subs[sub])}")

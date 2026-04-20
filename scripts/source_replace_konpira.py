# -*- coding: utf-8 -*-
"""
金刀比羅宮公式サイトで検証可能な問題の出典を置換するスクリプト
"""
import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'web', 'public', 'data', 'kotohira_questions.json')
SUMMARY_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'draft', 'source_replace_2_summary.txt')

OFFICIAL_URL = "https://www.konpira.or.jp/"

# Target question IDs (Wikipedia金刀比羅宮 single source, reviewed+enabled)
TARGET_IDS = {
    'kotohira_001','kotohira_005','kotohira_006','kotohira_007','kotohira_009',
    'kotohira_014','kotohira_015','kotohira_084','kotohira_086','kotohira_087',
    'kotohira_099','kotohira_103','kotohira_106','kotohira_108','kotohira_109',
    'kotohira_113','kotohira_119','kotohira_138','kotohira_153','kotohira_169',
    'kotohira_212','kotohira_229','kotohira_230','kotohira_271','kotohira_272',
    'kotohira_284','kotohira_285','kotohira_288','kotohira_289','kotohira_299',
    'kotohira_313','kotohira_314','kotohira_317','kotohira_320','kotohira_324',
    'kotohira_325','kotohira_328','kotohira_330','kotohira_337','kotohira_339',
    'kotohira_340','kotohira_344','kotohira_347','kotohira_351','kotohira_352',
    'kotohira_353','kotohira_358','kotohira_379','kotohira_383','kotohira_399',
    'kotohira_400','kotohira_402','kotohira_409','kotohira_417','kotohira_424',
    'kotohira_436','kotohira_439','kotohira_448','kotohira_450','kotohira_456',
    'kotohira_457','kotohira_465','kotohira_466','kotohira_467','kotohira_473',
    'kotohira_476','kotohira_478','kotohira_481','kotohira_482','kotohira_487',
    'kotohira_498','kotohira_500'
}

# Questions that CANNOT be verified on official site (skip with reasons)
SKIP_REASONS = {
    'kotohira_007': '五人百姓の700年以上の歴史は公式サイトに記載なし',
    'kotohira_009': '重要文化財15件という具体的件数は公式サイトで確認不可（2024年に12棟指定の記載のみ）',
    'kotohira_015': '上り45分という所要時間は公式サイトと異なる可能性（公式は片道30分程度と記載）',
    'kotohira_084': '鞘橋の情報は公式サイトに記載なし',
    'kotohira_086': '紫銅鳥居の建立年(1788年)は公式サイトに記載なし',
    'kotohira_087': '鴻池儀兵衛の情報は公式サイトに記載なし',
    'kotohira_103': '国登録有形文化財1件という情報は公式サイトで確認不可',
    'kotohira_106': '石段の下り所要時間30分は公式サイトで明確に確認不可',
    'kotohira_108': '別宮本殿・中殿・拝殿の重要文化財情報は公式サイトで部分的にしか確認不可',
    'kotohira_113': '書院建築2件(奥書院・表書院及四脚門)の分類は公式サイトで確認不可',
    'kotohira_119': '御鉾楯及び御台船は公式サイトに記載なし',
    'kotohira_138': '与謝蕪村の句碑は公式サイトに記載なし',
    'kotohira_169': '金丸座の建設年・重要文化財指定は公式サイトに記載なし（金刀比羅宮の施設ではない）',
    'kotohira_229': 'JR琴平駅から参道入口まで10分は公式サイトに明確な記載なし',
    'kotohira_230': 'JR琴平駅から奥社まで90分は公式サイトに明確な記載なし',
    'kotohira_271': '海の科学館の開館年(1966年)は公式サイトに記載なし',
    'kotohira_272': '海の科学館の入場料は公式サイトに記載なし',
    'kotohira_284': '鞘橋の構造詳細は公式サイトに記載なし',
    'kotohira_285': '鞘橋の建設時代は公式サイトに記載なし',
    'kotohira_288': '紫銅鳥居の読み方は公式サイトに記載なし',
    'kotohira_289': '鴻池儀兵衛の出身地は公式サイトに記載なし',
    'kotohira_299': '高燈籠の詳細は公式サイトに記載なし',
    'kotohira_324': '祓除殿の用途は公式サイトに記載なし',
    'kotohira_325': '神庫の用途は公式サイトに記載なし',
    'kotohira_328': 'ご利益3種類の表現が公式サイトと異なる（公式は農業・殖産・医薬・海上守護）',
    'kotohira_330': '神饌幣帛料供進神社の重要文化財情報は公式サイトで確認不可',
    'kotohira_337': '5つの街道(こんぴら街道)の詳細は公式サイトに記載なし',
    'kotohira_340': '加美代飴の700年の歴史は公式サイトに記載なし',
    'kotohira_344': '鞘橋の文化財登録は公式サイトに記載なし',
    'kotohira_351': '重要文化財15件の完全リストは公式サイトで確認不可',
    'kotohira_352': '重要文化財15件の完全リストは公式サイトで確認不可',
    'kotohira_353': '海の科学館の開館時間は公式サイトに記載なし',
    'kotohira_358': '上り45分・下り30分は公式サイトと異なる可能性（公式は片道30分程度）',
    'kotohira_383': '鞘橋は公式サイトに記載なし',
    'kotohira_399': '紫銅鳥居(1788年)は公式サイトに記載なし',
    'kotohira_402': '高燈籠の建設目的は公式サイトに記載なし',
    'kotohira_424': '重要文化財の完全リストは公式サイトで確認不可',
    'kotohira_436': '高燈籠は公式サイトに記載なし',
    'kotohira_448': '紫銅鳥居(1788年)と高燈籠(1860年)は公式サイトに記載なし',
    'kotohira_450': '石段以外に参拝方法なしは公式サイトと矛盾（お車参拝予約あり）',
    'kotohira_456': '3大スポット(金丸座含む)は公式サイトで確認不可',
    'kotohira_457': '重要文化財の完全リストは公式サイトで確認不可',
    'kotohira_466': '車での参拝不可は公式サイトと矛盾（お車参拝予約あり）',
    'kotohira_478': '鞘橋と大宮橋の比較は公式サイトに記載なし',
    'kotohira_482': '重要文化財の完全リストは公式サイトで確認不可',
    'kotohira_487': '神楽殿は公式サイトに記載なし',
}

# Verifiable IDs
VERIFIABLE_IDS = TARGET_IDS - set(SKIP_REASONS.keys())

def main():
    # Read JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    updated_ids = []

    for q in data['questions']:
        if q['id'] not in VERIFIABLE_IDS:
            continue

        qid = q['id']
        old_source = q['source']
        old_explanation = q['explanation']

        # Find the existing Wikipedia citation in explanation (if any)
        # Pattern: （出典: [金刀比羅宮 - Wikipedia](URL)）
        # Some explanations may not have explicit citation text
        wiki_citation = None
        wiki_url = old_source  # Use source URL as wiki URL

        # Check if explanation already has a citation
        if '（出典:' in old_explanation or '（出典：' in old_explanation:
            # Already has citation - should not happen for single-source questions
            # but handle gracefully
            print(f"WARNING: {qid} already has citation in explanation, skipping")
            continue

        # Build new explanation: append official site citation + Wikipedia citation
        new_explanation = (
            old_explanation
            + '（出典: [金刀比羅宮 公式サイト](https://www.konpira.or.jp/)）'
            + '\n（出典: [金刀比羅宮 - Wikipedia](' + wiki_url + ')）'
        )

        # Update source to official URL
        q['source'] = OFFICIAL_URL
        q['explanation'] = new_explanation

        updated_count += 1
        updated_ids.append(qid)

    # Write JSON
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    # Write summary
    os.makedirs(os.path.dirname(SUMMARY_PATH), exist_ok=True)
    with open(SUMMARY_PATH, 'w', encoding='utf-8') as f:
        f.write('出典置換結果サマリー (Wikipedia「金刀比羅宮」→ 公式サイト)\n')
        f.write('=' * 60 + '\n\n')
        f.write(f'対象問題数: {len(TARGET_IDS)}\n')
        f.write(f'更新した問題数: {updated_count}\n')
        f.write(f'スキップした問題数: {len(SKIP_REASONS)}\n\n')
        f.write('--- 更新した問題 ---\n')
        for uid in sorted(updated_ids):
            f.write(f'  {uid}\n')
        f.write(f'\n--- スキップした問題 ({len(SKIP_REASONS)}件) ---\n')
        for sid in sorted(SKIP_REASONS.keys()):
            f.write(f'  {sid}: {SKIP_REASONS[sid]}\n')
        f.write('\n--- 変更内容 ---\n')
        f.write('- source: Wikipedia URL → https://www.konpira.or.jp/\n')
        f.write('- explanation: 末尾に公式サイト出典を追加し、Wikipedia出典を2番目に追加\n')

    print(f'Updated: {updated_count} questions')
    print(f'Skipped: {len(SKIP_REASONS)} questions')
    print(f'JSON written to: {JSON_PATH}')
    print(f'Summary written to: {SUMMARY_PATH}')

if __name__ == '__main__':
    main()

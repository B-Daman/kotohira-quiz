"""問題データの読み込みと選出（読み取り専用）"""

import json
import random
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from config import Config

JST = ZoneInfo("Asia/Tokyo")


def _load_json(filepath: Path) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def load_questions(question_type: str) -> list[dict]:
    """有効な問題を全件取得"""
    data_dir = Path(Config.QUIZ_DATA_DIR)
    if question_type == "kotohira":
        filepath = data_dir / "kotohira_questions.json"
    else:
        filepath = data_dir / "english_questions.json"

    data = _load_json(filepath)
    return [
        q
        for q in data.get("questions", [])
        if q.get("reviewed", False) and q.get("enabled", True)
    ]


def select_questions(question_type: str, count: int = 1) -> list[dict]:
    """問題を選出する"""
    pool = load_questions(question_type)
    if not pool:
        return []

    if question_type == "kotohira":
        return _select_kotohira(pool, count)
    return _select_english(pool, count)


def _select_kotohira(pool: list[dict], count: int) -> list[dict]:
    """カテゴリ分散で選出"""
    by_cat: dict[str, list[dict]] = {}
    for q in pool:
        cat = q.get("category", "other")
        by_cat.setdefault(cat, []).append(q)

    selected: list[dict] = []
    selected_ids: set[str] = set()
    categories = list(by_cat.keys())
    random.shuffle(categories)

    while len(selected) < count:
        added = False
        for cat in categories:
            if len(selected) >= count:
                break
            candidates = [
                q for q in by_cat[cat] if q["id"] not in selected_ids
            ]
            if candidates:
                pick = random.choice(candidates)
                selected.append(pick)
                selected_ids.add(pick["id"])
                added = True
        if not added:
            remaining = [q for q in pool if q["id"] not in selected_ids]
            if not remaining:
                break
            pick = random.choice(remaining)
            selected.append(pick)
            selected_ids.add(pick["id"])

    return selected


def _select_english(pool: list[dict], count: int) -> list[dict]:
    """en_to_ja / ja_to_en を交互に選出"""
    en_to_ja = [q for q in pool if q.get("pattern") == "en_to_ja"]
    ja_to_en = [q for q in pool if q.get("pattern") == "ja_to_en"]
    random.shuffle(en_to_ja)
    random.shuffle(ja_to_en)

    selected: list[dict] = []
    i_en, i_ja = 0, 0
    use_en = True

    while len(selected) < count:
        if use_en and i_en < len(en_to_ja):
            selected.append(en_to_ja[i_en])
            i_en += 1
        elif not use_en and i_ja < len(ja_to_en):
            selected.append(ja_to_en[i_ja])
            i_ja += 1
        elif i_en < len(en_to_ja):
            selected.append(en_to_ja[i_en])
            i_en += 1
        elif i_ja < len(ja_to_en):
            selected.append(ja_to_en[i_ja])
            i_ja += 1
        else:
            break
        use_en = not use_en

    return selected


def get_today_jst() -> str:
    return datetime.now(JST).strftime("%Y-%m-%d")

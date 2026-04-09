export interface ThemeSub {
  label: string;
  categories: string[];
}

export interface ThemeGroup {
  id: string;
  icon: string;
  label: string;
  categories: string[];
  subs: ThemeSub[];
}

export const THEME_GROUPS: ThemeGroup[] = [
  {
    id: "shrine",
    icon: "⛩️",
    label: "金刀比羅宮",
    categories: ["shrine", "architecture"],
    subs: [
      { label: "参拝・信仰", categories: ["shrine"] },
      { label: "建造物・美術", categories: ["architecture"] },
    ],
  },
  {
    id: "history",
    icon: "📜",
    label: "歴史・人物",
    categories: ["history"],
    subs: [],
  },
  {
    id: "theater",
    icon: "🎭",
    label: "金丸座・歌舞伎",
    categories: ["theater"],
    subs: [],
  },
  {
    id: "geography",
    icon: "🗺️",
    label: "地理・観光",
    categories: ["geography", "tourism"],
    subs: [
      { label: "地理・行政", categories: ["geography"] },
      { label: "観光スポット", categories: ["tourism"] },
    ],
  },
  {
    id: "food",
    icon: "🍜",
    label: "グルメ・名産品",
    categories: ["gourmet", "food"],
    subs: [
      { label: "讃岐うどん・名店", categories: ["gourmet"] },
      { label: "お菓子・地酒", categories: ["food"] },
    ],
  },
  {
    id: "culture",
    icon: "🎨",
    label: "文化・伝統",
    categories: ["culture"],
    subs: [],
  },
  {
    id: "event",
    icon: "🎪",
    label: "祭り・イベント",
    categories: ["event"],
    subs: [],
  },
  {
    id: "modern",
    icon: "🏘️",
    label: "現代の琴平",
    categories: ["modern", "life"],
    subs: [
      { label: "まちの取り組み", categories: ["modern"] },
      { label: "暮らし・施設", categories: ["life"] },
    ],
  },
];

/** JSON category key → 日本語ラベル */
const CATEGORY_LABELS: Record<string, string> = {};
for (const group of THEME_GROUPS) {
  for (const cat of group.categories) {
    // サブカテゴリがある場合はサブのラベルを使う
    const sub = group.subs.find((s) => s.categories.includes(cat));
    CATEGORY_LABELS[cat] = sub ? sub.label : group.label;
  }
}

export function getCategoryLabel(category: string): string {
  return CATEGORY_LABELS[category] ?? category;
}

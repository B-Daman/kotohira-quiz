import { useEffect, useRef, useState } from "react";
import type { QuizConfig } from "../types";
import { THEME_GROUPS } from "../config/categories";

interface Props {
  onStart: (config: QuizConfig) => void;
  questionCounts: Record<string, number>;
  difficultyCounts: Record<string, Record<string, number>>;
}

type Difficulty = "all" | "easy" | "medium" | "hard";

const DIFFICULTY_OPTIONS: {
  value: Difficulty;
  label: string;
}[] = [
  { value: "all", label: "すべて" },
  { value: "easy", label: "やさしい" },
  { value: "medium", label: "ふつう" },
  { value: "hard", label: "むずかしい" },
];

function Popover({
  group,
  selectedCategories,
  onToggle,
  onClose,
  questionCounts,
}: {
  group: (typeof THEME_GROUPS)[0];
  selectedCategories: Set<string>;
  onToggle: (categories: string[]) => void;
  onClose: () => void;
  questionCounts: Record<string, number>;
}) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClick(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        onClose();
      }
    }
    document.addEventListener("mousedown", handleClick);
    return () => document.removeEventListener("mousedown", handleClick);
  }, [onClose]);

  const allCount = group.categories.reduce(
    (s, c) => s + (questionCounts[c] ?? 0),
    0,
  );
  const allSelected = group.categories.every((c) =>
    selectedCategories.has(c),
  );

  return (
    <div
      ref={ref}
      className="absolute top-full right-0 sm:left-0 sm:right-auto mt-1 z-20 bg-white rounded-lg shadow-lg border border-gray-200 py-1 min-w-[200px]"
    >
      <button
        onClick={() => onToggle(group.categories)}
        className="w-full text-left px-4 py-3 hover:bg-gray-50 flex items-center justify-between"
      >
        <span className="text-sm font-medium text-gray-700">
          すべて
        </span>
        <span className="flex items-center gap-2">
          <span className="text-xs text-gray-500">
            {allCount}問
          </span>
          {allSelected && (
            <span className="text-amber-600 text-sm">✓</span>
          )}
        </span>
      </button>
      {group.subs.map((sub) => {
        const subCount = sub.categories.reduce(
          (s, c) => s + (questionCounts[c] ?? 0),
          0,
        );
        const subSelected = sub.categories.every((c) =>
          selectedCategories.has(c),
        );
        return (
          <button
            key={sub.label}
            onClick={() => onToggle(sub.categories)}
            className="w-full text-left px-4 py-3 hover:bg-gray-50 flex items-center justify-between"
          >
            <span className="text-sm text-gray-600">
              {sub.label}
            </span>
            <span className="flex items-center gap-2">
              <span className="text-xs text-gray-500">
                {subCount}問
              </span>
              {subSelected && (
                <span className="text-amber-600 text-sm">✓</span>
              )}
            </span>
          </button>
        );
      })}
    </div>
  );
}

export function StartScreen({
  onStart,
  questionCounts,
  difficultyCounts,
}: Props) {
  const [difficulty, setDifficulty] = useState<Difficulty>("all");
  const [selectedCategories, setSelectedCategories] = useState<
    Set<string>
  >(new Set());
  const [openPopover, setOpenPopover] = useState<string | null>(null);
  const hoverTimeout = useRef<ReturnType<typeof setTimeout> | null>(
    null,
  );

  // Compute effective question counts based on difficulty filter
  const effectiveCounts: Record<string, number> = {};
  if (difficulty === "all") {
    Object.assign(effectiveCounts, questionCounts);
  } else {
    for (const [cat, count] of Object.entries(
      difficultyCounts[difficulty] ?? {},
    )) {
      effectiveCounts[cat] = count;
    }
  }

  // Compute total matching questions
  const allJsonCategories = THEME_GROUPS.flatMap((g) => g.categories);
  const activeCategories =
    selectedCategories.size === 0
      ? new Set(allJsonCategories)
      : selectedCategories;

  const totalMatching = [...activeCategories].reduce(
    (s, c) => s + (effectiveCounts[c] ?? 0),
    0,
  );

  function toggleCategories(cats: string[]) {
    setSelectedCategories((prev) => {
      const next = new Set(prev);
      const allIn = cats.every((c) => next.has(c));
      if (allIn) {
        cats.forEach((c) => next.delete(c));
      } else {
        cats.forEach((c) => next.add(c));
      }
      return next;
    });
  }

  function handleStart() {
    const config: QuizConfig = { mode: "free", label: "フリーモード" };

    // Difficulty
    if (difficulty !== "all") {
      config.mode = "difficulty";
      config.difficulty = difficulty;
      const diffLabels: Record<string, string> = {
        easy: "やさしい",
        medium: "ふつう",
        hard: "むずかしい",
      };
      config.label = diffLabels[difficulty];
    }

    // Categories
    if (selectedCategories.size > 0) {
      config.categories = [...selectedCategories];
      if (config.mode === "free") {
        config.mode = "theme";
      }
      // Build label from selected theme groups
      const groupLabels = THEME_GROUPS.filter((g) =>
        g.categories.some((c) => selectedCategories.has(c)),
      ).map((g) => g.label);
      if (groupLabels.length <= 2) {
        config.label = groupLabels.join(" + ");
      } else {
        config.label = `${groupLabels.length}テーマ選択`;
      }
      if (difficulty !== "all") {
        const diffLabels: Record<string, string> = {
          easy: "やさしい",
          medium: "ふつう",
          hard: "むずかしい",
        };
        config.label += ` / ${diffLabels[difficulty]}`;
      }
    }

    onStart(config);
  }

  function handleEnglishMix() {
    onStart({ mode: "english_mix", label: "英語もまぜる" });
  }

  function handleMouseEnter(groupId: string, hasSubs: boolean) {
    if (!hasSubs) return;
    if (hoverTimeout.current) clearTimeout(hoverTimeout.current);
    setOpenPopover(groupId);
  }

  function handleMouseLeave() {
    hoverTimeout.current = setTimeout(() => {
      setOpenPopover(null);
    }, 200);
  }

  function handleChipClick(group: (typeof THEME_GROUPS)[0]) {
    if (group.subs.length === 0) {
      toggleCategories(group.categories);
    } else {
      // Mobile: toggle popover on tap
      setOpenPopover(openPopover === group.id ? null : group.id);
    }
  }

  function isGroupSelected(group: (typeof THEME_GROUPS)[0]): boolean {
    return group.categories.some((c) => selectedCategories.has(c));
  }

  return (
    <div className="w-full max-w-lg mx-auto">
      <div className="text-center mb-6">
        <div className="text-5xl mb-3">⛩️</div>
        <h2 className="text-2xl font-bold text-gray-800">
          琴平クイズ
        </h2>
      </div>

      {/* Difficulty */}
      <div className="mb-5">
        <p className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">
          難易度
        </p>
        <div className="flex flex-wrap gap-2">
          {DIFFICULTY_OPTIONS.map((opt) => (
            <button
              key={opt.value}
              onClick={() => setDifficulty(opt.value)}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                difficulty === opt.value
                  ? "bg-amber-600 text-white shadow-sm"
                  : "bg-white text-gray-600 border border-gray-200 hover:border-gray-400"
              }`}
            >
              {opt.label}
            </button>
          ))}
        </div>
      </div>

      {/* Theme */}
      <div className="mb-6">
        <p className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">
          テーマ
        </p>
        <div className="flex flex-wrap gap-2">
          {/* "すべて" chip */}
          <button
            onClick={() => setSelectedCategories(new Set())}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
              selectedCategories.size === 0
                ? "bg-amber-600 text-white shadow-sm"
                : "bg-white text-gray-600 border border-gray-200 hover:border-gray-400"
            }`}
          >
            すべて
          </button>

          {THEME_GROUPS.map((group) => {
            const selected = isGroupSelected(group);
            const hasSubs = group.subs.length > 0;
            const count = group.categories.reduce(
              (s, c) => s + (effectiveCounts[c] ?? 0),
              0,
            );

            return (
              <div
                key={group.id}
                className="relative"
                onMouseEnter={() =>
                  handleMouseEnter(group.id, hasSubs)
                }
                onMouseLeave={handleMouseLeave}
              >
                <button
                  onClick={() => handleChipClick(group)}
                  className={`px-4 py-2 rounded-full text-sm font-medium transition-all flex items-center gap-1 ${
                    selected
                      ? "bg-amber-600 text-white shadow-sm"
                      : "bg-white text-gray-600 border border-gray-200 hover:border-gray-400"
                  }`}
                >
                  <span>{group.icon}</span>
                  <span>{group.label}</span>
                  {hasSubs && (
                    <span
                      className={`text-xs ml-0.5 ${selected ? "text-amber-200" : "text-gray-500"}`}
                    >
                      ▾
                    </span>
                  )}
                  <span
                    className={`text-xs ${selected ? "text-amber-200" : "text-gray-500"}`}
                  >
                    {count}
                  </span>
                </button>

                {openPopover === group.id && hasSubs && (
                  <Popover
                    group={group}
                    selectedCategories={selectedCategories}
                    onToggle={toggleCategories}
                    onClose={() => setOpenPopover(null)}
                    questionCounts={effectiveCounts}
                  />
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Start button */}
      <button
        onClick={handleStart}
        disabled={totalMatching === 0}
        className="w-full py-4 rounded-xl bg-amber-600 text-white font-bold text-lg hover:bg-amber-700 active:scale-[0.98] transition-all disabled:bg-gray-300 disabled:cursor-not-allowed mb-3"
      >
        🎯 10問スタート
        <span className="text-amber-200 text-sm ml-2">
          ({totalMatching}問から出題)
        </span>
      </button>

      {/* English mix */}
      <button
        onClick={handleEnglishMix}
        className="w-full py-3 rounded-xl bg-blue-50 text-blue-700 font-medium border border-blue-200 hover:border-blue-400 active:scale-[0.98] transition-all text-sm mb-4"
      >
        🔤 英語もまぜる（琴平5問 + 英語5問）
      </button>
    </div>
  );
}

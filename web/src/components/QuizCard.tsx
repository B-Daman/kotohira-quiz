import { useState } from "react";
import type { Question } from "../types";
import {
  isKotohiraQuestion,
  isEnglishQuestion,
  isJapaneseQuestion,
} from "../types";
import { getCategoryLabel } from "../config/categories";

const DIFFICULTY_BADGE: Record<
  string,
  { label: string; color: string; bg: string }
> = {
  easy: { label: "やさしい", color: "#16a34a", bg: "#f0fdf4" },
  medium: { label: "ふつう", color: "#d97706", bg: "#fffbeb" },
  hard: { label: "むずかしい", color: "#dc2626", bg: "#fef2f2" },
};

interface Props {
  question: Question;
  index: number;
  onAnswer: (selected: string) => void;
}

export function QuizCard({ question, index, onAnswer }: Props) {
  const [selected, setSelected] = useState<string | null>(null);

  const isKotohira = isKotohiraQuestion(question);
  const isJapanese = isJapaneseQuestion(question);
  const accentColor = isKotohira
    ? "#D4A574"
    : isJapanese
      ? "#10B981"
      : "#5B8DEF";

  let tag = "";
  if (isKotohiraQuestion(question)) {
    tag = getCategoryLabel(question.category);
  } else if (isEnglishQuestion(question)) {
    tag = question.pattern === "en_to_ja" ? "英→日" : "日→英";
  } else if (isJapaneseQuestion(question)) {
    tag =
      question.pattern === "kanji_to_reading" ? "漢字→読み" : "読み→漢字";
  }

  const badge =
    isKotohiraQuestion(question)
      ? DIFFICULTY_BADGE[question.difficulty]
      : isJapaneseQuestion(question)
        ? DIFFICULTY_BADGE[question.level]
        : null;

  const labels = ["A", "B", "C", "D"];

  function handleSelect(label: string) {
    if (selected !== null) return; // prevent double tap
    setSelected(label);

    const isCorrect = label === question.answer;

    setTimeout(() => {
      onAnswer(label);
      setSelected(null);
    }, isCorrect ? 400 : 600);
  }

  function getChoiceStyle(label: string): string {
    if (selected === null) {
      return "border-gray-200 bg-white hover:border-gray-400";
    }
    if (label === question.answer) {
      return "border-green-400 bg-green-50";
    }
    if (label === selected) {
      return "border-red-400 bg-red-50";
    }
    return "border-gray-200 bg-white opacity-50";
  }

  return (
    <div className="w-full max-w-lg mx-auto animate-fadeIn">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-xs font-bold tracking-wider text-stone-500">
          {isKotohira ? "🏛️ " : isJapanese ? "📝 " : "🔤 "}
          {tag}
        </span>
        {badge && (
          <span
            className="text-xs font-bold px-2 py-0.5 rounded-full"
            style={{
              color: badge.color,
              backgroundColor: badge.bg,
            }}
          >
            {badge.label}
          </span>
        )}
      </div>

      <h2 className="text-xl font-bold text-gray-800 mb-1">
        Q{index + 1}.
      </h2>
      <p className="text-xl text-gray-700 mb-6 leading-relaxed">
        {question.question}
      </p>

      <div className="flex flex-col gap-3">
        {question.choices.map((choice, i) => {
          const text =
            choice.includes(". ")
              ? choice.split(". ").slice(1).join(". ")
              : choice;
          const label = labels[i];
          return (
            <button
              key={label}
              onClick={() => handleSelect(label)}
              disabled={selected !== null}
              className={`w-full text-left px-4 py-3 rounded-lg border-2 transition-all duration-200 text-gray-700 font-medium ${getChoiceStyle(label)} ${selected !== null ? "" : "active:scale-[0.98]"}`}
            >
              <span
                className="inline-block w-8 font-bold"
                style={{ color: selected === null ? accentColor : undefined }}
              >
                {label}.
              </span>
              {text}
            </button>
          );
        })}
      </div>
    </div>
  );
}

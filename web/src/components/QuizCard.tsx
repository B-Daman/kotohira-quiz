import type { Question } from "../types";
import { isKotohiraQuestion, isEnglishQuestion } from "../types";

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
  const isKotohira = isKotohiraQuestion(question);
  const accentColor = isKotohira ? "#D4A574" : "#5B8DEF";

  let tag = "";
  if (isKotohiraQuestion(question)) {
    tag = question.category;
  } else if (isEnglishQuestion(question)) {
    tag = question.pattern === "en_to_ja" ? "英→日" : "日→英";
  }

  const badge =
    isKotohiraQuestion(question)
      ? DIFFICULTY_BADGE[question.difficulty]
      : null;

  const labels = ["A", "B", "C", "D"];

  return (
    <div className="w-full max-w-lg mx-auto">
      <div className="flex items-center gap-2 mb-2">
        <span
          className="text-xs font-bold uppercase tracking-wider"
          style={{ color: accentColor }}
        >
          {isKotohira ? "🏛️ " : "🔤 "}
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
      <p className="text-lg text-gray-700 mb-6 leading-relaxed">
        {question.question}
      </p>

      <div className="flex flex-col gap-3">
        {question.choices.map((choice, i) => {
          const text =
            choice.includes(". ") ?
              choice.split(". ").slice(1).join(". ")
            : choice;
          return (
            <button
              key={labels[i]}
              onClick={() => onAnswer(labels[i])}
              className="w-full text-left px-4 py-3 rounded-lg border-2 border-gray-200 bg-white hover:border-gray-400 active:scale-[0.98] transition-all text-gray-700 font-medium"
            >
              <span
                className="inline-block w-8 font-bold"
                style={{ color: accentColor }}
              >
                {labels[i]}.
              </span>
              {text}
            </button>
          );
        })}
      </div>
    </div>
  );
}

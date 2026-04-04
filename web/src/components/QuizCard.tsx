import type { Question } from "../types";
import { isKotohiraQuestion, isEnglishQuestion } from "../types";

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

  const labels = ["A", "B", "C", "D"];

  return (
    <div className="w-full max-w-lg mx-auto">
      <div
        className="text-xs font-bold uppercase tracking-wider mb-2"
        style={{ color: accentColor }}
      >
        {isKotohira ? "🏛️ 琴平町クイズ" : "🔤 英単語クイズ"} ・{" "}
        {tag}
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

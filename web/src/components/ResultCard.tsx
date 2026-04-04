import type { Question, AnswerRecord } from "../types";
import { isKotohiraQuestion, isEnglishQuestion } from "../types";

function RichText({ text }: { text: string }) {
  const parts = text.split(/(\[[^\]]+\]\([^)]+\))/g);
  return (
    <>
      {parts.map((part, i) => {
        const m = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
        if (m) {
          return (
            <a
              key={i}
              href={m[2]}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-500 underline"
            >
              {m[1]}
            </a>
          );
        }
        return <span key={i}>{part}</span>;
      })}
    </>
  );
}

function splitSource(text: string): {
  body: string;
  source: { label: string; url: string } | null;
} {
  // （出典: [label](url)） を分離
  const m = text.match(
    /（出典: \[([^\]]+)\]\(([^)]+)\)）$/,
  );
  if (m) {
    return {
      body: text.replace(m[0], "").trim(),
      source: { label: m[1], url: m[2] },
    };
  }
  return { body: text, source: null };
}

function SourceLink({
  source,
}: {
  source: { label: string; url: string };
}) {
  return (
    <>
      <p className="text-sm text-gray-500 mt-3 mb-1 font-bold">
        📎 出典
      </p>
      <a
        href={source.url}
        target="_blank"
        rel="noopener noreferrer"
        className="text-blue-500 underline text-sm"
      >
        {source.label}
      </a>
    </>
  );
}

function EnglishExplanation({
  explanation,
  pronunciation,
}: {
  explanation: string;
  pronunciation?: string;
}) {
  // "word = 意味。例: English sentence.（日本語訳）"
  // → 答え行と例文行に分割
  const exampleMatch = explanation.match(
    /^(.+?)(?:。\s*例:\s*|。\s*例：\s*)(.+)$/,
  );

  const meaningLine = exampleMatch ? exampleMatch[1] : explanation;
  const exampleLine = exampleMatch ? exampleMatch[2] : null;

  return (
    <>
      <p className="text-sm text-gray-500 mb-1 font-bold">
        💡 答え
      </p>
      <p className="text-gray-700 font-medium">
        <RichText text={meaningLine} />
      </p>
      {pronunciation && (
        <p className="text-sm text-gray-400 italic mt-1">
          発音: {pronunciation}
        </p>
      )}
      {exampleLine && (
        <>
          <p className="text-sm text-gray-500 mt-3 mb-1 font-bold">
            📝 例文
          </p>
          <p className="text-gray-700 leading-relaxed">
            <RichText text={exampleLine} />
          </p>
        </>
      )}
    </>
  );
}

interface Props {
  question: Question;
  answer: AnswerRecord;
  onNext: () => void;
  isLast: boolean;
}

export function ResultCard({
  question,
  answer,
  onNext,
  isLast,
}: Props) {
  const isKotohira = isKotohiraQuestion(question);
  const accentColor = isKotohira ? "#D4A574" : "#5B8DEF";

  return (
    <div className="w-full max-w-lg mx-auto">
      <div
        className={`text-center text-4xl mb-4 ${
          answer.correct ? "animate-bounce" : ""
        }`}
      >
        {answer.correct ? "✅" : "❌"}
      </div>

      <h2
        className={`text-2xl font-bold text-center mb-2 ${
          answer.correct ? "text-green-600" : "text-red-500"
        }`}
      >
        {answer.correct ? "正解！" : "不正解…"}
      </h2>

      {!answer.correct && (
        <p className="text-center text-gray-600 mb-4">
          正解は <strong>{question.answer}</strong>
        </p>
      )}

      <div
        className="rounded-lg p-4 mb-6"
        style={{ backgroundColor: `${accentColor}15` }}
      >
        {isEnglishQuestion(question) ? (
          <EnglishExplanation
            explanation={question.explanation}
            pronunciation={question.pronunciation}
          />
        ) : (
          (() => {
            const { body, source } = splitSource(
              question.explanation,
            );
            return (
              <>
                <p className="text-sm text-gray-500 mb-1 font-bold">
                  💡 解説
                </p>
                <p className="text-gray-700 leading-relaxed">
                  <RichText text={body} />
                </p>
                {source && (
                  <SourceLink source={source} />
                )}
              </>
            );
          })()
        )}
      </div>

      <button
        onClick={onNext}
        className="w-full py-3 rounded-lg text-white font-bold text-lg transition-all hover:opacity-90 active:scale-[0.98]"
        style={{ backgroundColor: accentColor }}
      >
        {isLast ? "結果を見る" : "次の問題へ →"}
      </button>
    </div>
  );
}

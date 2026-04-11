import type { Question, AnswerRecord } from "../types";
import {
  isKotohiraQuestion,
  isEnglishQuestion,
  isJapaneseQuestion,
} from "../types";
import { RichText, SourceLinks } from "./ExplanationParts";
import { splitSources } from "../utils/explanation";

function EnglishExplanation({
  explanation,
  pronunciation,
  searchUrl,
  translateUrl,
}: {
  explanation: string;
  pronunciation?: string;
  searchUrl: string;
  translateUrl: string;
}) {
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
        <p className="text-sm text-gray-500 italic mt-1">
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
      <div className="flex gap-3 mt-3">
        <a
          href={searchUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs text-blue-500 hover:text-blue-700 underline"
        >
          🔍 Google検索
        </a>
        <a
          href={translateUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs text-blue-500 hover:text-blue-700 underline"
        >
          🌐 Google翻訳
        </a>
      </div>
    </>
  );
}

function JapaneseExplanation({
  explanation,
  word,
  reading,
  english,
  searchUrl,
  translateUrl,
}: {
  explanation: string;
  word: string;
  reading: string;
  english: string;
  searchUrl: string;
  translateUrl: string;
}) {
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
      <p className="text-sm text-gray-500 italic mt-1">
        英訳: {english}
      </p>
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
      <div className="flex gap-3 mt-3">
        <a
          href={searchUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs text-blue-500 hover:text-blue-700 underline"
        >
          🔍 Google検索
        </a>
        <a
          href={translateUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs text-blue-500 hover:text-blue-700 underline"
        >
          🌐 Google翻訳
        </a>
      </div>
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
  const isJapanese = isJapaneseQuestion(question);
  const accentColor = isKotohira
    ? "#D4A574"
    : isJapanese
      ? "#10B981"
      : "#5B8DEF";

  const bgClass = answer.correct
    ? "bg-green-50 border-green-200"
    : "bg-red-50 border-red-200";

  return (
    <div
      className={`w-full max-w-lg mx-auto animate-fadeIn ${answer.correct ? "" : "animate-shake"}`}
    >
      {/* Result header with colored background */}
      <div
        className={`rounded-xl border-2 ${bgClass} p-6 mb-4 text-center`}
      >
        <div
          className={`text-4xl mb-2 ${answer.correct ? "animate-bounce" : ""}`}
        >
          {answer.correct ? "✅" : "❌"}
        </div>

        <h2
          className={`text-2xl font-bold mb-1 ${
            answer.correct ? "text-green-600" : "text-red-500"
          }`}
        >
          {answer.correct ? "正解！" : "不正解…"}
        </h2>

        {!answer.correct && (
          <p className="text-gray-600">
            正解は <strong>{question.answer}</strong>
          </p>
        )}
      </div>

      {/* Explanation */}
      <div className="rounded-xl bg-white border border-gray-200 p-4 mb-4">
        {isEnglishQuestion(question) ? (
          <EnglishExplanation
            explanation={question.explanation}
            pronunciation={question.pronunciation}
            searchUrl={question.search_url}
            translateUrl={question.translate_url}
          />
        ) : isJapaneseQuestion(question) ? (
          <JapaneseExplanation
            explanation={question.explanation}
            word={question.word}
            reading={question.reading}
            english={question.english}
            searchUrl={question.search_url}
            translateUrl={question.translate_url}
          />
        ) : (
          (() => {
            const { body, sources } = splitSources(
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
                <SourceLinks sources={sources} />
              </>
            );
          })()
        )}
      </div>

      <button
        onClick={onNext}
        autoFocus
        className="w-full py-3 rounded-lg text-white font-bold text-lg transition-all hover:opacity-90 active:scale-[0.98]"
        style={{ backgroundColor: accentColor }}
      >
        {isLast ? "結果を見る" : "次の問題へ →"}
      </button>
    </div>
  );
}

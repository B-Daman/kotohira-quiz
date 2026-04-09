import { useState } from "react";
import type { AnswerRecord, Question } from "../types";
import { isKotohiraQuestion } from "../types";
import { getTodayJST } from "../utils/date";
import { getDailyScores } from "../data/history";
import { splitSources } from "../utils/explanation";
import { RichText, SourceLinks } from "./ExplanationParts";

interface Props {
  answers: AnswerRecord[];
  questions: Question[];
  onRestart: () => void;
  onGoToStart: () => void;
}

function ReviewItem({
  question,
  answer,
  index,
}: {
  question: Question;
  answer: AnswerRecord;
  index: number;
}) {
  const [open, setOpen] = useState(false);
  const { body, sources } = splitSources(question.explanation);

  const correctChoice = question.choices.find((c) =>
    c.startsWith(`${question.answer}.`),
  );
  const selectedChoice = question.choices.find((c) =>
    c.startsWith(`${answer.selected}.`),
  );

  return (
    <div
      className={`rounded-lg border-2 ${answer.correct ? "border-green-200 bg-green-50/50" : "border-red-200 bg-red-50/50"}`}
    >
      <button
        onClick={() => setOpen(!open)}
        className="w-full text-left px-4 py-3 flex items-start gap-3"
      >
        <span className="text-lg mt-0.5 shrink-0">
          {answer.correct ? "✅" : "❌"}
        </span>
        <div className="flex-1 min-w-0">
          <p className="text-sm font-bold text-gray-800">
            Q{index + 1}. {question.question}
          </p>
          {!answer.correct && (
            <p className="text-xs text-gray-500 mt-1">
              あなた: {selectedChoice ?? answer.selected} → 正解:{" "}
              {correctChoice ?? question.answer}
            </p>
          )}
        </div>
        <span className="text-gray-500 text-xs shrink-0 mt-1">
          {open ? "▲" : "▼"}
        </span>
      </button>

      {open && (
        <div className="px-4 pb-4 border-t border-gray-200 pt-3">
          <p className="text-sm text-gray-700 leading-relaxed">
            <RichText text={body} />
          </p>
          <SourceLinks sources={sources} />
        </div>
      )}
    </div>
  );
}

export function ScoreSummary({
  answers,
  questions,
  onRestart,
  onGoToStart,
}: Props) {
  const total = answers.length;
  const correct = answers.filter((a) => a.correct).length;
  const pct = total > 0 ? Math.round((correct / total) * 100) : 0;
  const today = getTodayJST();
  const scores = getDailyScores();

  const streak = (() => {
    let count = 0;
    const sorted = [...scores].sort((a, b) =>
      b.date.localeCompare(a.date),
    );
    for (const s of sorted) {
      if (s.correct > 0) count++;
      else break;
    }
    return count;
  })();

  // Difficulty breakdown (kotohira questions only)
  const diffStats: Record<string, { total: number; correct: number }> =
    {};
  for (let i = 0; i < answers.length; i++) {
    const q = questions[i];
    if (q && isKotohiraQuestion(q)) {
      const d = q.difficulty;
      if (!diffStats[d]) diffStats[d] = { total: 0, correct: 0 };
      diffStats[d].total++;
      if (answers[i].correct) diffStats[d].correct++;
    }
  }

  const diffOrder = ["easy", "medium", "hard"];
  const diffLabels: Record<string, string> = {
    easy: "😊 やさしい",
    medium: "🤔 ふつう",
    hard: "😤 むずかしい",
  };

  const hasKotohira = answers.some((a) =>
    a.questionId.startsWith("kotohira"),
  );
  const hasEnglish = answers.some((a) =>
    a.questionId.startsWith("eng"),
  );

  return (
    <div className="w-full max-w-lg mx-auto text-center">
      <div className="text-6xl mb-4">
        {pct >= 80 ? "🎉" : pct >= 50 ? "👍" : "💪"}
      </div>

      <h2 className="text-2xl font-bold text-gray-800 mb-2">
        {today} のクイズ結果
      </h2>

      <div className="text-5xl font-bold my-6">
        <span className="text-green-600">{correct}</span>
        <span className="text-gray-400"> / </span>
        <span className="text-gray-600">{total}</span>
      </div>

      <p className="text-lg text-gray-500 mb-6">
        正答率 {pct}%
      </p>

      {/* Difficulty breakdown */}
      {hasKotohira && Object.keys(diffStats).length > 0 && (
        <div className="flex justify-center gap-3 mb-6">
          {diffOrder.map((d) => {
            const s = diffStats[d];
            if (!s) return null;
            return (
              <div
                key={d}
                className="bg-gray-50 rounded-lg px-4 py-2 text-sm"
              >
                <p className="text-gray-500">{diffLabels[d]}</p>
                <p className="text-lg font-bold text-gray-700">
                  {s.correct}/{s.total}
                </p>
              </div>
            );
          })}
        </div>
      )}

      {/* English/Kotohira split (only in mixed mode) */}
      {hasKotohira && hasEnglish && (
        <div className="grid grid-cols-2 gap-4 mb-6">
          <div className="bg-amber-50 rounded-lg p-4">
            <p className="text-sm text-gray-500">🏛️ 琴平町</p>
            <p className="text-2xl font-bold text-amber-700">
              {answers.filter((a) => a.questionId.startsWith("kotohira") && a.correct).length}
              /
              {answers.filter((a) => a.questionId.startsWith("kotohira")).length}
            </p>
          </div>
          <div className="bg-blue-50 rounded-lg p-4">
            <p className="text-sm text-gray-500">🔤 英単語</p>
            <p className="text-2xl font-bold text-blue-600">
              {answers.filter((a) => a.questionId.startsWith("eng") && a.correct).length}
              /
              {answers.filter((a) => a.questionId.startsWith("eng")).length}
            </p>
          </div>
        </div>
      )}

      {streak > 1 && (
        <p className="text-sm text-gray-500 mb-6">
          🔥 {streak}日連続チャレンジ中！
        </p>
      )}

      {/* Action buttons */}
      <div className="flex flex-col gap-3 mb-8">
        <button
          onClick={onRestart}
          className="w-full py-3 rounded-lg bg-amber-600 text-white font-bold text-lg hover:bg-amber-700 active:scale-[0.98] transition-all"
        >
          次の10問へ →
        </button>
        <button
          onClick={onGoToStart}
          className="w-full py-3 rounded-lg bg-gray-200 text-gray-700 font-bold hover:bg-gray-300 active:scale-[0.98] transition-all"
        >
          モードを変えて遊ぶ
        </button>
      </div>

      {/* Review list */}
      <div className="text-left">
        <h3 className="text-sm font-bold text-gray-500 uppercase tracking-wider mb-3">
          問題のふりかえり
        </h3>
        <div className="flex flex-col gap-2">
          {questions.map((q, i) => {
            const a = answers[i];
            if (!a) return null;
            return (
              <ReviewItem
                key={q.id}
                question={q}
                answer={a}
                index={i}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
}

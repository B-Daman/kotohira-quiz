import type { AnswerRecord } from "../types";
import { getTodayJST } from "../utils/date";
import { getDailyScores } from "../data/history";

interface Props {
  answers: AnswerRecord[];
}

export function ScoreSummary({ answers }: Props) {
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

      <p className="text-lg text-gray-500 mb-8">
        正答率 {pct}%
      </p>

      <div className="grid grid-cols-2 gap-4 mb-8">
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

      {streak > 1 && (
        <p className="text-sm text-gray-500">
          🔥 {streak}日連続チャレンジ中！
        </p>
      )}

      <p className="text-xs text-gray-400 mt-4">
        明日もチャレンジしよう！毎朝7時に新しい問題が届きます。
      </p>
    </div>
  );
}

import { useEffect, useState } from "react";
import type { KotohiraQuestion, Question, AnswerRecord } from "../types";
import { useQuiz } from "../hooks/useQuiz";
import { StartScreen } from "../components/StartScreen";
import { ProgressBar } from "../components/ProgressBar";
import { QuizCard } from "../components/QuizCard";
import { ResultCard } from "../components/ResultCard";
import { ScoreSummary } from "../components/ScoreSummary";
import { ErrorMessage } from "../components/ErrorMessage";
import { loadAllQuestions } from "../data/questions";

/** ?preview=kotohira_001 で特定問題の解説表示をプレビュー */
function usePreview() {
  const [preview, setPreview] = useState<{
    question: Question;
    answer: AnswerRecord;
  } | null>(null);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("preview");
    if (!id) return;

    loadAllQuestions().then((data) => {
      const all = [...data.kotohira, ...data.english];
      const q = all.find((x) => x.id === id);
      if (q) {
        setPreview({
          question: q,
          answer: {
            date: "",
            questionId: q.id,
            selected: q.answer,
            correct: true,
          },
        });
      }
    });
  }, []);

  return preview;
}

export function DailyQuiz() {
  const {
    phase,
    config,
    questions,
    currentIndex,
    answers,
    currentQuestion,
    lastAnswer,
    errorMessage,
    startQuiz,
    submitAnswer,
    nextQuestion,
    restartQuiz,
    goToStart,
  } = useQuiz();

  const preview = usePreview();

  const [questionCounts, setQuestionCounts] = useState<
    Record<string, number>
  >({});
  const [difficultyCounts, setDifficultyCounts] = useState<
    Record<string, Record<string, number>>
  >({});

  useEffect(() => {
    loadAllQuestions().then((data) => {
      const counts: Record<string, number> = {};
      const diffCounts: Record<string, Record<string, number>> = {
        easy: {},
        medium: {},
        hard: {},
      };
      for (const q of data.kotohira as KotohiraQuestion[]) {
        const cat = q.category || "other";
        counts[cat] = (counts[cat] ?? 0) + 1;
        if (diffCounts[q.difficulty]) {
          diffCounts[q.difficulty][cat] =
            (diffCounts[q.difficulty][cat] ?? 0) + 1;
        }
      }
      setQuestionCounts(counts);
      setDifficultyCounts(diffCounts);
    });
  }, []);

  return (
    <div className="min-h-screen bg-stone-50 px-4 py-8">
      {phase !== "start" && (
        <header className="mb-6 max-w-lg mx-auto">
          <div className="flex items-center justify-between">
            <button
              onClick={goToStart}
              className="text-sm text-gray-500 hover:text-amber-700 transition-colors flex items-center gap-1"
            >
              ← トップへ
            </button>
            <span className="text-sm font-bold text-gray-800">
              ⛩️ 琴平クイズ
            </span>
            <span className="w-12" />
          </div>
          {config?.label && (
            <p className="text-xs text-gray-500 text-right mt-1">
              {config.label}
            </p>
          )}
        </header>
      )}

      <main>
        {preview && (
          <div className="w-full max-w-lg mx-auto">
            <p className="text-xs text-gray-400 mb-4 text-center">
              プレビュー: {preview.question.id}
            </p>
            <ResultCard
              question={preview.question}
              answer={preview.answer}
              onNext={() => {
                window.history.replaceState(
                  null,
                  "",
                  window.location.pathname,
                );
                window.location.reload();
              }}
              isLast={true}
            />
          </div>
        )}

        {!preview && phase === "start" && (
          <StartScreen
            onStart={startQuiz}
            questionCounts={questionCounts}
            difficultyCounts={difficultyCounts}
          />
        )}

        {!preview && phase === "loading" && (
          <div className="text-center py-12">
            <div className="text-4xl animate-spin mb-4">⛩️</div>
            <p className="text-gray-500">問題を読み込み中...</p>
          </div>
        )}

        {phase === "error" && (
          <ErrorMessage
            message={errorMessage}
            onGoToStart={goToStart}
          />
        )}

        {phase === "question" && currentQuestion && (
          <>
            <ProgressBar
              current={currentIndex}
              total={questions.length}
            />
            <QuizCard
              question={currentQuestion}
              index={currentIndex}
              onAnswer={submitAnswer}
            />
          </>
        )}

        {phase === "result" &&
          currentQuestion &&
          lastAnswer && (
            <>
              <ProgressBar
                current={currentIndex}
                total={questions.length}
              />
              <ResultCard
                question={currentQuestion}
                answer={lastAnswer}
                onNext={nextQuestion}
                isLast={currentIndex >= questions.length - 1}
              />
            </>
          )}

        {phase === "summary" && (
          <ScoreSummary
            answers={answers}
            questions={questions}
            onRestart={restartQuiz}
            onGoToStart={goToStart}
          />
        )}
      </main>
    </div>
  );
}

import { useQuiz } from "../hooks/useQuiz";
import { ProgressBar } from "../components/ProgressBar";
import { QuizCard } from "../components/QuizCard";
import { ResultCard } from "../components/ResultCard";
import { ScoreSummary } from "../components/ScoreSummary";
import { ErrorMessage } from "../components/ErrorMessage";

export function DailyQuiz() {
  const {
    phase,
    questions,
    currentIndex,
    answers,
    currentQuestion,
    lastAnswer,
    errorMessage,
    submitAnswer,
    nextQuestion,
  } = useQuiz();

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-8">
      <header className="text-center mb-8">
        <h1 className="text-2xl font-bold text-gray-800">
          琴平デイリークイズ
        </h1>
        <p className="text-sm text-gray-400">
          毎日10問で琴平町と英語を学ぼう
        </p>
      </header>

      <main>
        {phase === "loading" && (
          <div className="text-center py-12">
            <div className="text-4xl animate-spin mb-4">⛩️</div>
            <p className="text-gray-500">
              問題を読み込み中...
            </p>
          </div>
        )}

        {phase === "error" && (
          <ErrorMessage message={errorMessage} />
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
                isLast={
                  currentIndex >= questions.length - 1
                }
              />
            </>
          )}

        {phase === "summary" && (
          <ScoreSummary answers={answers} />
        )}
      </main>
    </div>
  );
}

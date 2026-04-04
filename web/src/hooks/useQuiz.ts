import { useCallback, useEffect, useState } from "react";
import type {
  Question,
  KotohiraQuestion,
  EnglishQuestion,
  AnswerRecord,
  QuizPhase,
} from "../types";
import { loadAllQuestions } from "../data/questions";
import {
  getTodayAnsweredIds,
  getTodayAnswers,
  saveAnswer,
  saveDailyScore,
} from "../data/history";
import { getTodayJST } from "../utils/date";

function shuffled<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function selectKotohira(
  pool: KotohiraQuestion[],
  count: number,
): KotohiraQuestion[] {
  const byCategory: Record<string, KotohiraQuestion[]> = {};
  for (const q of pool) {
    const cat = q.category || "other";
    (byCategory[cat] ??= []).push(q);
  }

  const selected: KotohiraQuestion[] = [];
  const selectedIds = new Set<string>();
  const categories = shuffled(Object.keys(byCategory));
  const catCount: Record<string, number> = {};

  while (selected.length < count) {
    let added = false;
    for (const cat of categories) {
      if (selected.length >= count) break;
      if ((catCount[cat] ?? 0) >= 1) continue;
      const candidates = byCategory[cat].filter(
        (q) => !selectedIds.has(q.id),
      );
      if (candidates.length > 0) {
        const pick =
          candidates[Math.floor(Math.random() * candidates.length)];
        selected.push(pick);
        selectedIds.add(pick.id);
        catCount[cat] = (catCount[cat] ?? 0) + 1;
        added = true;
      }
    }
    if (!added) {
      const remaining = pool.filter((q) => !selectedIds.has(q.id));
      if (remaining.length === 0) break;
      const pick =
        remaining[Math.floor(Math.random() * remaining.length)];
      selected.push(pick);
      selectedIds.add(pick.id);
    }
  }
  return selected;
}

function selectEnglish(
  pool: EnglishQuestion[],
  count: number,
): EnglishQuestion[] {
  const enToJa = shuffled(
    pool.filter((q) => q.pattern === "en_to_ja"),
  );
  const jaToEn = shuffled(
    pool.filter((q) => q.pattern === "ja_to_en"),
  );

  const selected: EnglishQuestion[] = [];
  let iEn = 0;
  let iJa = 0;
  let useEn = true;

  while (selected.length < count) {
    if (useEn && iEn < enToJa.length) {
      selected.push(enToJa[iEn++]);
    } else if (!useEn && iJa < jaToEn.length) {
      selected.push(jaToEn[iJa++]);
    } else if (iEn < enToJa.length) {
      selected.push(enToJa[iEn++]);
    } else if (iJa < jaToEn.length) {
      selected.push(jaToEn[iJa++]);
    } else {
      break;
    }
    useEn = !useEn;
  }
  return selected;
}

export interface QuizState {
  phase: QuizPhase;
  questions: Question[];
  currentIndex: number;
  answers: AnswerRecord[];
  errorMessage: string;
}

export function useQuiz() {
  const [state, setState] = useState<QuizState>({
    phase: "loading",
    questions: [],
    currentIndex: 0,
    answers: [],
    errorMessage: "",
  });

  useEffect(() => {
    let cancelled = false;

    async function init() {
      try {
        const data = await loadAllQuestions();
        const answeredIds = getTodayAnsweredIds();

        const kotohiraPool = data.kotohira.filter(
          (q) => !answeredIds.has(q.id),
        );
        const englishPool = data.english.filter(
          (q) => !answeredIds.has(q.id),
        );

        const kotohiraQs = selectKotohira(kotohiraPool, 5);
        const englishQs = selectEnglish(englishPool, 5);
        const questions: Question[] = [
          ...kotohiraQs,
          ...englishQs,
        ];

        if (cancelled) return;

        if (questions.length === 0) {
          const existing = getTodayAnswers();
          if (existing.length > 0) {
            setState((s) => ({
              ...s,
              phase: "summary",
              answers: existing,
              questions: [],
            }));
          } else {
            setState((s) => ({
              ...s,
              phase: "error",
              errorMessage: "出題可能な問題がありません。",
            }));
          }
          return;
        }

        setState((s) => ({
          ...s,
          phase: "question",
          questions,
          currentIndex: 0,
          answers: [],
        }));
      } catch (e) {
        if (cancelled) return;
        setState((s) => ({
          ...s,
          phase: "error",
          errorMessage:
            e instanceof Error
              ? e.message
              : "問題データの読み込みに失敗しました",
        }));
      }
    }

    init();
    return () => {
      cancelled = true;
    };
  }, []);

  const submitAnswer = useCallback(
    (selected: string) => {
      const q = state.questions[state.currentIndex];
      if (!q) return;

      const correct = selected === q.answer;
      const record: AnswerRecord = {
        date: getTodayJST(),
        questionId: q.id,
        selected,
        correct,
      };

      saveAnswer(record);

      setState((s) => ({
        ...s,
        phase: "result",
        answers: [...s.answers, record],
      }));
    },
    [state.questions, state.currentIndex],
  );

  const nextQuestion = useCallback(() => {
    setState((s) => {
      const nextIdx = s.currentIndex + 1;
      if (nextIdx >= s.questions.length) {
        const total = s.answers.length;
        const correct = s.answers.filter((a) => a.correct).length;
        saveDailyScore({
          date: getTodayJST(),
          total,
          correct,
        });
        return { ...s, phase: "summary" };
      }
      return { ...s, phase: "question", currentIndex: nextIdx };
    });
  }, []);

  const currentQuestion =
    state.questions[state.currentIndex] ?? null;
  const lastAnswer =
    state.answers[state.answers.length - 1] ?? null;

  return {
    ...state,
    currentQuestion,
    lastAnswer,
    submitAnswer,
    nextQuestion,
  };
}

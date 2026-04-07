import { useCallback, useEffect, useRef, useState } from "react";
import type {
  Question,
  KotohiraQuestion,
  EnglishQuestion,
  AnswerRecord,
  QuizPhase,
  QuizConfig,
} from "../types";
import { loadAllQuestions } from "../data/questions";
import {
  getTodayAnsweredIds,
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
  applyDistribution?: boolean,
): KotohiraQuestion[] {
  if (!applyDistribution) {
    // Simple category-distributed selection
    return selectWithCategoryDistribution(pool, count);
  }
  return selectWithCategoryDistribution(pool, count);
}

function selectWithCategoryDistribution(
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
  const maxPerCat = 2;

  while (selected.length < count) {
    let added = false;
    for (const cat of categories) {
      if (selected.length >= count) break;
      if ((catCount[cat] ?? 0) >= maxPerCat) continue;
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

function selectMixDifficulty(
  pool: KotohiraQuestion[],
  count: number,
): KotohiraQuestion[] {
  const byDiff: Record<string, KotohiraQuestion[]> = {};
  for (const q of pool) {
    (byDiff[q.difficulty] ??= []).push(q);
  }

  // Random distribution: pick counts for each difficulty
  const easyCount = 2 + Math.floor(Math.random() * 3); // 2-4
  const hardCount = 2 + Math.floor(Math.random() * 3); // 2-4
  const mediumCount = count - easyCount - hardCount;

  const targets: [string, number][] = [
    ["easy", Math.min(easyCount, (byDiff["easy"] ?? []).length)],
    ["medium", Math.min(Math.max(mediumCount, 0), (byDiff["medium"] ?? []).length)],
    ["hard", Math.min(hardCount, (byDiff["hard"] ?? []).length)],
  ];

  const selected: KotohiraQuestion[] = [];
  for (const [diff, n] of targets) {
    const candidates = shuffled(byDiff[diff] ?? []);
    selected.push(...candidates.slice(0, n));
  }

  // Fill remaining if targets didn't reach count
  if (selected.length < count) {
    const selectedIds = new Set(selected.map((q) => q.id));
    const remaining = shuffled(
      pool.filter((q) => !selectedIds.has(q.id)),
    );
    selected.push(...remaining.slice(0, count - selected.length));
  }

  return shuffled(selected);
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

function buildQuestions(
  config: QuizConfig,
  kotohiraPool: KotohiraQuestion[],
  englishPool: EnglishQuestion[],
): Question[] {
  if (config.mode === "english_mix") {
    const kotohiraQs = selectKotohira(kotohiraPool, 5);
    const englishQs = selectEnglish(englishPool, 5);
    return [...kotohiraQs, ...englishQs];
  }

  let filtered = kotohiraPool;

  // Filter by categories
  if (config.categories && config.categories.length > 0) {
    const cats = new Set(config.categories);
    filtered = filtered.filter((q) => cats.has(q.category));
  }

  // Filter by difficulty
  if (config.difficulty && config.difficulty !== "mix") {
    filtered = filtered.filter((q) => q.difficulty === config.difficulty);
  }

  // Mix difficulty mode
  if (config.difficulty === "mix") {
    return selectMixDifficulty(filtered, 10);
  }

  // Theme/category selected: no category distribution
  if (config.categories && config.categories.length > 0) {
    const count = Math.min(10, filtered.length);
    return shuffled(filtered).slice(0, count);
  }

  return selectKotohira(filtered, 10);
}

export interface QuizState {
  phase: QuizPhase;
  config: QuizConfig | null;
  questions: Question[];
  currentIndex: number;
  answers: AnswerRecord[];
  errorMessage: string;
}

export function useQuiz() {
  const [state, setState] = useState<QuizState>({
    phase: "start",
    config: null,
    questions: [],
    currentIndex: 0,
    answers: [],
    errorMessage: "",
  });

  const sessionAnsweredIds = useRef(new Set<string>());
  const roundCounter = useRef(0);

  const startQuiz = useCallback((config: QuizConfig) => {
    setState((s) => ({
      ...s,
      phase: "loading",
      config,
      questions: [],
      currentIndex: 0,
      answers: [],
      errorMessage: "",
    }));
    roundCounter.current += 1;
  }, []);

  useEffect(() => {
    if (state.phase !== "loading" || !state.config) return;

    let cancelled = false;

    async function init() {
      try {
        const data = await loadAllQuestions();
        const todayIds = getTodayAnsweredIds();
        const excludeIds = new Set([
          ...todayIds,
          ...sessionAnsweredIds.current,
        ]);

        const kotohiraPool = data.kotohira.filter(
          (q) => !excludeIds.has(q.id),
        );
        const englishPool = data.english.filter(
          (q) => !excludeIds.has(q.id),
        );

        const questions = buildQuestions(
          state.config!,
          kotohiraPool,
          englishPool,
        );

        if (cancelled) return;

        if (questions.length === 0) {
          setState((s) => ({
            ...s,
            phase: "error",
            errorMessage:
              "出題可能な問題がありません。条件を変えて試してみてください。",
          }));
          return;
        }

        for (const q of questions) {
          sessionAnsweredIds.current.add(q.id);
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
  }, [state.phase, state.config, roundCounter.current]);

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

  const restartQuiz = useCallback(() => {
    if (state.config) {
      startQuiz(state.config);
    }
  }, [state.config, startQuiz]);

  const goToStart = useCallback(() => {
    setState({
      phase: "start",
      config: null,
      questions: [],
      currentIndex: 0,
      answers: [],
      errorMessage: "",
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
    startQuiz,
    submitAnswer,
    nextQuestion,
    restartQuiz,
    goToStart,
  };
}

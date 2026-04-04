import type { AnswerRecord, DailyScore } from "../types";
import { getTodayJST } from "../utils/date";

const HISTORY_KEY = "kotohira_quiz_history";
const SCORES_KEY = "kotohira_quiz_scores";

export function getTodayAnswers(): AnswerRecord[] {
  const today = getTodayJST();
  const all = getAllAnswers();
  return all.filter((r) => r.date === today);
}

export function getTodayAnsweredIds(): Set<string> {
  return new Set(getTodayAnswers().map((r) => r.questionId));
}

export function saveAnswer(record: AnswerRecord): void {
  const all = getAllAnswers();
  all.push(record);
  localStorage.setItem(HISTORY_KEY, JSON.stringify(all));
}

export function saveDailyScore(score: DailyScore): void {
  const scores = getDailyScores();
  const existing = scores.findIndex((s) => s.date === score.date);
  if (existing >= 0) {
    scores[existing] = score;
  } else {
    scores.push(score);
  }
  localStorage.setItem(SCORES_KEY, JSON.stringify(scores));
}

export function getDailyScores(): DailyScore[] {
  try {
    return JSON.parse(localStorage.getItem(SCORES_KEY) || "[]");
  } catch {
    return [];
  }
}

function getAllAnswers(): AnswerRecord[] {
  try {
    return JSON.parse(localStorage.getItem(HISTORY_KEY) || "[]");
  } catch {
    return [];
  }
}

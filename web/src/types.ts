export interface KotohiraQuestion {
  id: string;
  category: string;
  difficulty: "easy" | "medium" | "hard";
  question: string;
  choices: string[];
  answer: string;
  explanation: string;
  source?: string;
  reviewed: boolean;
  enabled: boolean;
}

export interface EnglishQuestion {
  id: string;
  level: "A2" | "B1";
  pattern: "en_to_ja" | "ja_to_en";
  question: string;
  choices: string[];
  answer: string;
  explanation: string;
  word: string;
  pronunciation: string;
  reviewed: boolean;
  enabled: boolean;
}

export type Question = KotohiraQuestion | EnglishQuestion;

export function isKotohiraQuestion(q: Question): q is KotohiraQuestion {
  return "category" in q;
}

export function isEnglishQuestion(q: Question): q is EnglishQuestion {
  return "pattern" in q;
}

export interface QuestionBank {
  version: number;
  questions: Question[];
}

export interface AnswerRecord {
  date: string;
  questionId: string;
  selected: string;
  correct: boolean;
}

export type QuizPhase = "loading" | "question" | "result" | "summary" | "error";

export interface DailyScore {
  date: string;
  total: number;
  correct: number;
}

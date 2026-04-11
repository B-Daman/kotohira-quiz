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
  search_url: string;
  translate_url: string;
  reviewed: boolean;
  enabled: boolean;
}

export interface JapaneseQuestion {
  id: string;
  level: "easy" | "medium" | "hard";
  pattern: "kanji_to_reading" | "reading_to_kanji";
  question: string;
  choices: string[];
  answer: string;
  explanation: string;
  word: string;
  reading: string;
  english: string;
  search_url: string;
  translate_url: string;
  reviewed: boolean;
  enabled: boolean;
}

export type Question = KotohiraQuestion | EnglishQuestion | JapaneseQuestion;

export function isKotohiraQuestion(q: Question): q is KotohiraQuestion {
  return "category" in q;
}

export function isEnglishQuestion(q: Question): q is EnglishQuestion {
  return "pattern" in q && "pronunciation" in q;
}

export function isJapaneseQuestion(q: Question): q is JapaneseQuestion {
  return "pattern" in q && "reading" in q;
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

export interface QuizConfig {
  mode: "free" | "english_mix" | "japanese_mix" | "english_only" | "japanese_only" | "difficulty" | "theme";
  difficulty?: "easy" | "medium" | "hard" | "mix";
  categories?: string[];
  label?: string;
}

export type QuizPhase = "start" | "loading" | "question" | "result" | "summary" | "error";

export interface DailyScore {
  date: string;
  total: number;
  correct: number;
}

import type {
  KotohiraQuestion,
  EnglishQuestion,
  JapaneseQuestion,
  QuestionBank,
} from "../types";

interface QuestionCache {
  kotohira: KotohiraQuestion[];
  english: EnglishQuestion[];
  japanese: JapaneseQuestion[];
}

let cache: QuestionCache | null = null;

export async function loadAllQuestions(): Promise<QuestionCache> {
  if (cache) return cache;

  const base = import.meta.env.BASE_URL;
  const [kotohiraRes, englishRes, japaneseRes] = await Promise.all([
    fetch(`${base}data/kotohira_questions.json`),
    fetch(`${base}data/english_questions.json`),
    fetch(`${base}data/japanese_questions.json`),
  ]);

  if (!kotohiraRes.ok || !englishRes.ok || !japaneseRes.ok) {
    throw new Error("問題データの読み込みに失敗しました");
  }

  const kotohiraData: QuestionBank = await kotohiraRes.json();
  const englishData: QuestionBank = await englishRes.json();
  const japaneseData: QuestionBank = await japaneseRes.json();

  cache = {
    kotohira: (kotohiraData.questions as KotohiraQuestion[]).filter(
      (q) => q.enabled && q.reviewed,
    ),
    english: (englishData.questions as EnglishQuestion[]).filter(
      (q) => q.enabled && q.reviewed,
    ),
    japanese: (japaneseData.questions as JapaneseQuestion[]).filter(
      (q) => q.enabled && q.reviewed,
    ),
  };

  return cache;
}

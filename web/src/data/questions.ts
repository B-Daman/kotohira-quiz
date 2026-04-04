import type {
  KotohiraQuestion,
  EnglishQuestion,
  QuestionBank,
} from "../types";

interface QuestionCache {
  kotohira: KotohiraQuestion[];
  english: EnglishQuestion[];
}

let cache: QuestionCache | null = null;

export async function loadAllQuestions(): Promise<QuestionCache> {
  if (cache) return cache;

  const [kotohiraRes, englishRes] = await Promise.all([
    fetch("/data/kotohira_questions.json"),
    fetch("/data/english_questions.json"),
  ]);

  if (!kotohiraRes.ok || !englishRes.ok) {
    throw new Error("問題データの読み込みに失敗しました");
  }

  const kotohiraData: QuestionBank = await kotohiraRes.json();
  const englishData: QuestionBank = await englishRes.json();

  cache = {
    kotohira: (kotohiraData.questions as KotohiraQuestion[]).filter(
      (q) => q.enabled && q.reviewed,
    ),
    english: (englishData.questions as EnglishQuestion[]).filter(
      (q) => q.enabled && q.reviewed,
    ),
  };

  return cache;
}

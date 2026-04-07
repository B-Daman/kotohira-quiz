/** Parse markdown links in text */
export function parseRichText(
  text: string,
): { type: "text" | "link"; content: string; url?: string }[] {
  const parts = text.split(/(\[[^\]]+\]\([^)]+\))/g);
  return parts
    .filter((p) => p.length > 0)
    .map((part) => {
      const m = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      if (m) {
        return { type: "link" as const, content: m[1], url: m[2] };
      }
      return { type: "text" as const, content: part };
    });
}

/** Extract all （出典: [label](url)） from explanation text */
export function splitSources(text: string): {
  body: string;
  sources: { label: string; url: string }[];
} {
  const sources: { label: string; url: string }[] = [];
  const pattern = /\n?（出典: \[([^\]]+)\]\(([^)]+)\)）/g;
  let m: RegExpExecArray | null;
  while ((m = pattern.exec(text)) !== null) {
    sources.push({ label: m[1], url: m[2] });
  }
  const body = text.replace(pattern, "").trim();
  return { body, sources };
}

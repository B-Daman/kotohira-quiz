import { parseRichText } from "../utils/explanation";

export function RichText({ text }: { text: string }) {
  const parts = parseRichText(text);
  return (
    <>
      {parts.map((part, i) => {
        if (part.type === "link" && part.url) {
          return (
            <a
              key={i}
              href={part.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-500 underline"
            >
              {part.content}
            </a>
          );
        }
        return <span key={i}>{part.content}</span>;
      })}
    </>
  );
}

export function SourceLinks({
  sources,
}: {
  sources: { label: string; url: string }[];
}) {
  if (sources.length === 0) return null;
  return (
    <>
      <p className="text-sm text-gray-500 mt-3 mb-1 font-bold">
        📎 出典
      </p>
      <ul className="list-none space-y-1">
        {sources.map((s, i) => (
          <li key={i}>
            <a
              href={s.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-500 underline text-sm"
            >
              {s.label}
            </a>
          </li>
        ))}
      </ul>
    </>
  );
}

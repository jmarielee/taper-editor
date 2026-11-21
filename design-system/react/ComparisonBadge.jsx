import "./ComparisonBadge.css";

// One fixed word per result. No icon: this check never produces a flag, so
// neither reserved shape belongs here, and the word carries the meaning.
const RESULTS = {
  lighter: "Lighter",
  heavier: "Heavier",
  same: "Same",
};

export default function ComparisonBadge({ result }) {
  const word = RESULTS[result];
  if (!word) {
    throw new Error(
      `ComparisonBadge: unknown result "${result}". Use one of: ${Object.keys(RESULTS).join(", ")}.`
    );
  }

  return <span className={`comparison-badge comparison-badge--${result}`}>{word}</span>;
}

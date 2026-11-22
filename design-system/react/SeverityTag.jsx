import "./SeverityTag.css";

// The word is the whole tag. Flag uses the findings colors (see the CSS),
// because flag findings are what produce a `findings` verdict.
const WORDS = {
  block: "Block",
  flag: "Flag",
};

export default function SeverityTag({ severity }) {
  const word = WORDS[severity];
  if (!word) {
    throw new Error(
      `SeverityTag: unknown severity "${severity}". Use one of: ${Object.keys(WORDS).join(", ")}.`
    );
  }

  return <span className={`severity-tag severity-tag--${severity}`}>{word}</span>;
}

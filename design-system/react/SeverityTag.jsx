import "./SeverityTag.css";
import VerdictIcon from "./VerdictIcon.jsx";

// Each severity reuses the matching VerdictBanner icon: flag findings are
// what produce a `findings` verdict, so flag shares the triangle.
const SEVERITIES = {
  block: { icon: "block", word: "Block" },
  flag: { icon: "findings", word: "Flag" },
};

export default function SeverityTag({ severity }) {
  const config = SEVERITIES[severity];
  if (!config) {
    throw new Error(
      `SeverityTag: unknown severity "${severity}". Use one of: ${Object.keys(SEVERITIES).join(", ")}.`
    );
  }

  return (
    <span className={`severity-tag severity-tag--${severity}`}>
      <VerdictIcon
        name={config.icon}
        width="var(--severity-tag-icon-width)"
        className="severity-tag__icon"
      />
      <span className="severity-tag__label">{config.word}</span>
    </span>
  );
}

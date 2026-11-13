import "./VerdictBanner.css";
import VerdictIcon, { ICONS } from "./VerdictIcon.jsx";

export default function VerdictBanner({ verdict, headline, message }) {
  if (!ICONS[verdict]) {
    throw new Error(
      `VerdictBanner: unknown verdict "${verdict}". Use one of: ${Object.keys(ICONS).join(", ")}.`
    );
  }

  return (
    <section className={`verdict-banner verdict-banner--${verdict}`}>
      <VerdictIcon
        name={verdict}
        width="var(--verdict-banner-icon-width)"
        className="verdict-banner__icon"
      />
      <div className="verdict-banner__body">
        <h2 className="verdict-banner__headline">{headline}</h2>
        <p className="verdict-banner__message">{message}</p>
      </div>
    </section>
  );
}

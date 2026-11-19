import { StrictMode, useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "../build/tokens.css";
import "./demo.css";
import VerdictBanner from "../react/VerdictBanner.jsx";
import SeverityTag from "../react/SeverityTag.jsx";
import QuoteBlock from "../react/QuoteBlock.jsx";

// Plan quotes copied word for word from report-detroit-half-pass.md,
// findings 3 and 4 (extracted by script, not retyped).
const QUOTE_SINGLE = "you will be positioned to cross the finish line comfortably.";
const QUOTE_LONG =
  "Keep it moderate. Avoid playing four hours or repeatedly chasing every difficult ball while your running volume is climbing.";
const QUOTE_FIRST =
  "You have 13 weeks until Sunday, October 18, 2026 — enough time to finish the Detroit half comfortably…";
const QUOTE_LATER = "you will be positioned to cross the finish line comfortably.";

const SEVERITIES = ["block", "flag"];

const EXAMPLES = [
  {
    verdict: "block",
    headline: "Blocked: this plan fails",
    message:
      "Your final week is the hardest stretch of the whole plan, with a 90-minute brick five days before your goal race.",
  },
  {
    verdict: "findings",
    headline: "Findings: passes, with three flags",
    message:
      "Your race week winds down well before November 1, but three risks below are yours to weigh.",
  },
  {
    verdict: "clean",
    headline: "Clean: this plan passes",
    message:
      "Race week averages about 14 minutes a day against about 34 before it, and nothing else needs your attention.",
  },
  {
    verdict: "hold",
    headline: "On hold: one question first",
    message: "Is your July 12 race the goal, or training for something else?",
  },
  {
    verdict: "decline",
    headline: "Not reviewed: outside what I check",
    message:
      "This is a strength program, not an AI-generated running or triathlon plan, so I didn't review it.",
  },
];

function systemTheme() {
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function Demo() {
  const [theme, setTheme] = useState(systemTheme);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
  }, [theme]);

  const next = theme === "dark" ? "light" : "dark";

  return (
    <main className="demo">
      <header className="demo__header">
        <h1>Design system</h1>
        <button type="button" onClick={() => setTheme(next)}>
          Switch to {next} mode
        </button>
      </header>
      <h2 className="demo__section">VerdictBanner</h2>
      {EXAMPLES.map((example) => (
        <div key={example.verdict} className="demo__item">
          <code>verdict="{example.verdict}"</code>
          <VerdictBanner {...example} />
        </div>
      ))}
      <h2 className="demo__section">SeverityTag</h2>
      {SEVERITIES.map((severity) => (
        <div key={severity} className="demo__item">
          <code>severity="{severity}"</code>
          <div>
            <SeverityTag severity={severity} />
          </div>
        </div>
      ))}
      <h2 className="demo__section">QuoteBlock</h2>
      <div className="demo__item">
        <code>One quote</code>
        <QuoteBlock quote={QUOTE_SINGLE} />
      </div>
      <div className="demo__item">
        <code>Long quote that wraps</code>
        <QuoteBlock quote={QUOTE_LONG} />
      </div>
      <div className="demo__item">
        <code>Two quotes, stacked</code>
        <div className="demo__stack">
          <QuoteBlock quote={QUOTE_FIRST} />
          <p className="demo__bridge">and later:</p>
          <QuoteBlock quote={QUOTE_LATER} />
        </div>
      </div>
    </main>
  );
}

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Demo />
  </StrictMode>
);

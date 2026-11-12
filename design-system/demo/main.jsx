import { StrictMode, useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "../build/tokens.css";
import "./demo.css";
import VerdictBanner from "../react/VerdictBanner.jsx";

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
        <h1>VerdictBanner</h1>
        <button type="button" onClick={() => setTheme(next)}>
          Switch to {next} mode
        </button>
      </header>
      {EXAMPLES.map((example) => (
        <div key={example.verdict} className="demo__item">
          <code>verdict="{example.verdict}"</code>
          <VerdictBanner {...example} />
        </div>
      ))}
    </main>
  );
}

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Demo />
  </StrictMode>
);

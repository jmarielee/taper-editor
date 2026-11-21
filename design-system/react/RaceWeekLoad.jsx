import { useId } from "react";
import "./RaceWeekLoad.css";
import ComparisonBadge from "./ComparisonBadge.jsx";

// The checker prints each race-week number as plain digits, with an optional
// decimal part ("47.1", "90"). Anything else (a unit, a sign, a blank) means
// the value didn't come straight from the receipt, so it is refused.
const RECEIPT_NUMBER = /^\d+(\.\d+)?$/;

function checkValue(prop, value) {
  if (typeof value !== "string" || !RECEIPT_NUMBER.test(value)) {
    throw new Error(
      `RaceWeekLoad: ${prop} must be the number only, as text, exactly as the receipt prints it (for example "47.1"). Got ${JSON.stringify(value)}.`
    );
  }
}

// Worked out from the two numbers beside the badge, never passed in, so the
// word can never contradict them.
function compare(raceWeek, before) {
  const a = Number(raceWeek);
  const b = Number(before);
  if (a < b) return "lighter";
  if (a > b) return "heavier";
  return "same";
}

function Group({ label, raceWeek, before }) {
  const labelId = useId();
  return (
    <div className="race-week-load__group">
      <p id={labelId} className="race-week-load__group-label">
        {label}
      </p>
      <dl className="race-week-load__list" aria-labelledby={labelId}>
        <div className="race-week-load__row race-week-load__row--number">
          <dt className="race-week-load__label">Race week</dt>
          {/* The value is shown exactly as passed. Only " min" is added. */}
          <dd className="race-week-load__value">{raceWeek} min</dd>
        </div>
        <div className="race-week-load__row race-week-load__row--number">
          <dt className="race-week-load__label">Before race week</dt>
          <dd className="race-week-load__value">{before} min</dd>
        </div>
        <div className="race-week-load__row race-week-load__row--result">
          <dt className="race-week-load__label">Race week is</dt>
          <dd className="race-week-load__badge">
            <ComparisonBadge result={compare(raceWeek, before)} />
          </dd>
        </div>
      </dl>
    </div>
  );
}

export default function RaceWeekLoad({
  raceWeekAverage,
  beforeAverage,
  raceWeekBiggestDay,
  beforeBiggestDay,
}) {
  checkValue("raceWeekAverage", raceWeekAverage);
  checkValue("beforeAverage", beforeAverage);
  checkValue("raceWeekBiggestDay", raceWeekBiggestDay);
  checkValue("beforeBiggestDay", beforeBiggestDay);

  return (
    <figure className="race-week-load">
      <figcaption className="race-week-load__header">
        <span className="race-week-load__name">Race-week load</span>
        {/* The divider is this span's left border, not a typed character,
            so screen readers don't announce it. */}
        <span className="race-week-load__source">Counted by the checker</span>
      </figcaption>
      <div className="race-week-load__box">
        <Group label="Average training a day" raceWeek={raceWeekAverage} before={beforeAverage} />
        <Group label="Biggest training day" raceWeek={raceWeekBiggestDay} before={beforeBiggestDay} />
      </div>
    </figure>
  );
}

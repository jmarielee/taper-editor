import "./VerdictBanner.css";

// Filled Material Symbols (FILL 1, weight 400, 24 opsz), viewBox 0 -960 960 960.
const ICONS = {
  // report (octagon). Only block uses the octagon.
  block:
    "M480-280q17 0 28.5-11.5T520-320q0-17-11.5-28.5T480-360q-17 0-28.5 11.5T440-320q0 17 11.5 28.5T480-280Zm-40-160h80v-240h-80v240ZM330-120 120-330v-300l210-210h300l210 210v300L630-120H330Z",
  // warning (triangle). Only findings uses the triangle.
  findings:
    "m40-120 440-760 440 760H40Zm440-120q17 0 28.5-11.5T520-280q0-17-11.5-28.5T480-320q-17 0-28.5 11.5T440-280q0 17 11.5 28.5T480-240Zm-40-120h80v-200h-80v200Z",
  // check_circle
  clean:
    "m424-296 282-282-56-56-226 226-114-114-56 56 170 170Zm56 216q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z",
  // help
  hold:
    "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z",
  // do_not_disturb_on
  decline:
    "M280-440h400v-80H280v80ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z",
};

export default function VerdictBanner({ verdict, headline, message }) {
  const icon = ICONS[verdict];
  if (!icon) {
    throw new Error(
      `VerdictBanner: unknown verdict "${verdict}". Use one of: ${Object.keys(ICONS).join(", ")}.`
    );
  }

  return (
    <section className={`verdict-banner verdict-banner--${verdict}`}>
      <svg
        className="verdict-banner__icon"
        viewBox="0 -960 960 960"
        aria-hidden="true"
        focusable="false"
      >
        <path d={icon} />
      </svg>
      <div className="verdict-banner__body">
        <h2 className="verdict-banner__headline">{headline}</h2>
        <p className="verdict-banner__message">{message}</p>
      </div>
    </section>
  );
}

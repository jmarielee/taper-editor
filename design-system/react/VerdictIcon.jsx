// Shared icons for VerdictBanner and SeverityTag. Each glyph is defined once.
// Filled Material Symbols (FILL 1, weight 400, 24 opsz), drawn on Material's
// 0 -960 960 960 grid. Each viewBox is cropped tightly to its shape (bounds
// measured from the path), so `width` sizes the shape itself, matching Figma,
// and the height follows the shape's proportions.
export const ICONS = {
  // report (octagon). Reserved: the octagon means block, in VerdictBanner
  // and SeverityTag. Don't use it for anything else.
  block: { viewBox: "120 -840 720 720", path: "M480-280q17 0 28.5-11.5T520-320q0-17-11.5-28.5T480-360q-17 0-28.5 11.5T440-320q0 17 11.5 28.5T480-280Zm-40-160h80v-240h-80v240ZM330-120 120-330v-300l210-210h300l210 210v300L630-120H330Z" },
  // warning (triangle). Reserved: the triangle means findings in VerdictBanner
  // and flag in SeverityTag. Don't use it for anything else.
  findings: { viewBox: "40 -880 880 760", path: "m40-120 440-760 440 760H40Zm440-120q17 0 28.5-11.5T520-280q0-17-11.5-28.5T480-320q-17 0-28.5 11.5T440-280q0 17 11.5 28.5T480-240Zm-40-120h80v-200h-80v200Z" },
  // check_circle
  clean: { viewBox: "80 -880 800 800", path: "m424-296 282-282-56-56-226 226-114-114-56 56 170 170Zm56 216q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z" },
  // help
  hold: { viewBox: "80 -880 800 800", path: "M478-240q21 0 35.5-14.5T528-290q0-21-14.5-35.5T478-340q-21 0-35.5 14.5T428-290q0 21 14.5 35.5T478-240Zm-36-154h74q0-33 7.5-52t42.5-52q26-26 41-49.5t15-56.5q0-56-41-86t-97-30q-57 0-92.5 30T342-618l66 26q5-18 22.5-39t53.5-21q32 0 48 17.5t16 38.5q0 20-12 37.5T506-526q-44 39-54 59t-10 73Zm38 314q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z" },
  // do_not_disturb_on
  decline: { viewBox: "80 -880 800 800", path: "M280-440h400v-80H280v80ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Z" },
};

export default function VerdictIcon({ name, width, className }) {
  const icon = ICONS[name];
  if (!icon) {
    throw new Error(
      `VerdictIcon: unknown icon "${name}". Use one of: ${Object.keys(ICONS).join(", ")}.`
    );
  }
  const [, , w, h] = icon.viewBox.split(" ");
  return (
    <svg
      className={className}
      viewBox={icon.viewBox}
      style={{ width, height: "auto", aspectRatio: `${w} / ${h}` }}
      aria-hidden="true"
      focusable="false"
    >
      <path d={icon.path} />
    </svg>
  );
}

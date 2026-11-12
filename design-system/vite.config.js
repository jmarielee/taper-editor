import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// The demo page lives in demo/ and imports ../react and ../build.
export default defineConfig({
  root: "demo",
  plugins: [react()],
  build: { outDir: "../dist", emptyOutDir: true },
});

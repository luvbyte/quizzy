const DEFAULT_THEME = "valentine";
export const VERSION = "0.0.1"

export function getTheme() {
  return localStorage.getItem("escapy-theme") || DEFAULT_THEME;
}

// Apply theme to #main
export const applyTheme = theme => {
  localStorage.setItem("escapy-theme", theme);
  document.getElementById("main")?.setAttribute("data-theme", theme);
};

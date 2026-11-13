let navigationHidden = false
try {
  navigationHidden = sessionStorage.getItem("pmg-navigation-hidden") === "true"
} catch {
  // Keep the setting in memory if browser storage is unavailable.
}

function updateNavigation() {
  document.documentElement.toggleAttribute("data-pmg-navigation-hidden", navigationHidden)
  const button = document.querySelector<HTMLButtonElement>(".pmg-navigation-toggle")
  if (button) {
    button.hidden = false
    button.setAttribute("aria-expanded", String(!navigationHidden))
  }
}

document.addEventListener("click", (event) => {
  if (!(event.target instanceof Element) || !event.target.closest(".pmg-navigation-toggle")) return
  navigationHidden = !navigationHidden
  try {
    sessionStorage.setItem("pmg-navigation-hidden", String(navigationHidden))
  } catch {
    // The toggle still works without browser storage.
  }
  updateNavigation()
})

document.addEventListener("nav", updateNavigation)
updateNavigation()

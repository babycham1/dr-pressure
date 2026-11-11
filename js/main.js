// Dr. Pressure: mobile menu, footer year, before/after sliders.
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("mobile-nav");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") menu.classList.remove("open");
    });
  }

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  document.querySelectorAll("[data-ba]").forEach(function (box) {
    var range = box.querySelector('input[type="range"]');
    if (!range) return;
    var set = function () { box.style.setProperty("--pos", range.value + "%"); };
    range.addEventListener("input", set);
    set();
  });
})();

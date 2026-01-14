// Reveal-on-scroll animation
const reveals = document.querySelectorAll(".reveal");
const obs = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) e.target.classList.add("show");
  });
}, { threshold: 0.15 });

reveals.forEach((el) => obs.observe(el));

// Active nav link while scrolling
const sections = ["bio","education","skills","experience","projects","contact"]
  .map(id => document.getElementById(id))
  .filter(Boolean);

const navLinks = document.querySelectorAll(".nav-link");

function setActive(id){
  navLinks.forEach(a => {
    const href = a.getAttribute("href") || "";
    a.classList.toggle("active", href === `#${id}`);
  });
}

window.addEventListener("scroll", () => {
  const y = window.scrollY + 120; // offset for sticky nav
  let current = "bio";
  for (const s of sections){
    if (s.offsetTop <= y) current = s.id;
  }
  setActive(current);
});

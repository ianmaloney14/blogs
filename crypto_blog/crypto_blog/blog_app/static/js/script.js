// UPDATE YEAR
const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
console.log(currentYear)
yearEl.textContent = currentYear;



// //STICKY NAVIGATION
// const sectionHeroEl = document.querySelector(".section-hero");

// const obs = new IntersectionObserver(
//     function (entries) {
//         const ent = entries[0];
//         console.log(ent);

//         if (ent.isIntersecting === false) {
//             document.body.classList.add("sticky");
//         }

//         if (ent.isIntersecting) {
//             document.body.classList.remove("sticky")
//         }
//     },
//     {
//         root: null,
//         threshold: 0,
//         rootMargin: "-80px",
//     }
// );

// obs.observe(sectionHeroEl);
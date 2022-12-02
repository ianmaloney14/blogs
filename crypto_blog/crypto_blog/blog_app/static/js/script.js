// UPDATE YEAR
const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
console.log(currentYear)
yearEl.textContent = currentYear;

// NAV DROPDOWN

document.addEventListener('click', e => {
    const isDropdownButton = e.target.matches("[data-dropdown-button]")
    if (!isDropdownButton && e.target.closest('[data-dropdown]') != null) return

    let currentDropdown
    if (isDropdownButton) {
        currentDropdown = e.target.closest('[data-dropdown]')
        currentDropdown.classList.toggle('active')
    }

    document.querySelectorAll("[data-dropdown].active").forEach(dropdown => {
        if (dropdown === currentDropdown) return 
        dropdown.classList.remove('active')
    })
})



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
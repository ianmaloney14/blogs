////////////////////////////////////////////////////////////////////////////////
// Hover effect for category_list page. 
//This function will apply filter: contrast effect when hovering the category links
function addHoverClass() {
    const categoryLinks = document.querySelectorAll('.category-links');
    const categoryImgs = document.querySelectorAll('.category-img');
  
    categoryLinks.forEach((link, index) => {
      link.addEventListener('mouseover', () => {
        categoryImgs[index].classList.add('hovered');
      });
      link.addEventListener('mouseout', () => {
        categoryImgs[index].classList.remove('hovered');
      });
    });
  }
  addHoverClass()
////////////////////////////////////////////////////////////////////////////////
// Make mobile nav work
const btnNavEl = document.querySelector(".btn-mobile-nav")
const headerEl = document.querySelector(".header")

btnNavEl.addEventListener('click', function() {
  headerEl.classList.toggle("nav-open")
})

////////////////////////////////////////////////////////////////////////////////
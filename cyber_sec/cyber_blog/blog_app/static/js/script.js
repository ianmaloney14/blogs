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
// Fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
  var flex = document.createElement("div");
  flex.style.display = "flex";
  flex.style.flexDirection = "column";
  flex.style.rowGap = "1px";

  flex.appendChild(document.createElement("div"));
  flex.appendChild(document.createElement("div"));

  document.body.appendChild(flex);
  var isSupported = flex.scrollHeight === 1;
  flex.parentNode.removeChild(flex);
  console.log(isSupported);

  if (!isSupported) document.body.classList.add("no-flexbox-gap");
}
checkFlexGap();
////////////////////////////////////////////////////////////////////////////////
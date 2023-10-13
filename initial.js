window.addEventListener("scroll", function () {
  var footer = document.querySelector("footer");
  var scrollHeight = window.scrollY + window.innerHeight;
  var documentHeight = document.body.scrollHeight;

  if (scrollHeight >= documentHeight) {
    footer.style.transform = "translateY(0)"; // Show the footer
  } else {
    footer.style.transform = "translateY(100%)"; // Hide the footer
  }
});

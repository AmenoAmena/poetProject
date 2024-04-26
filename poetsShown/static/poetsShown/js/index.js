document.addEventListener("click", function(event) {
    var dropdownMenu = document.getElementById("dropdownMenu");
    var menuToggle = document.querySelector(".menu-toggle");
    
    if (!menuToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
      dropdownMenu.style.display = "none";
    }
  });
  
  function toggleMenu() {
    var dropdownMenu = document.getElementById("dropdownMenu");
    if (dropdownMenu.style.display === "block") {
      dropdownMenu.style.display = "none";
    } else {
      dropdownMenu.style.display = "block";
    }
  }
  
window.addEventListener('scroll', function() {
  console.log("Scrolling...");
  var bottom = document.documentElement.scrollHeight - window.innerHeight;
  var scrollTop =  document.documentElement.scrollTop;
  var scrollPercentage = (scrollTop / bottom) * 100;

  if (scrollPercentage > 90) {
      document.querySelector('.pagination').style.visibility = 'visible';
  } else {
      document.querySelector('.pagination').style.visibility = 'hidden';
  }
});
  
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
  
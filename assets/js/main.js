// main.js
document.addEventListener("DOMContentLoaded", function () {
    const headers = document.querySelectorAll(".accordion-header");
  
    headers.forEach((header) => {
      header.addEventListener("click", function () {
        const item = this.parentElement;
        item.classList.toggle("active");
  
        document.querySelectorAll(".accordion-item").forEach((i) => {
          if (i !== item) i.classList.remove("active");
        });
      });
    });
  });
  
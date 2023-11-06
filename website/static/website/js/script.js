document.addEventListener("DOMContentLoaded", function () {
// JavaScript to toggle the dropdown menu on hover
var services = document.getElementById('services');
services.addEventListener('mouseenter', function() {
  console.log("Enter")
    var dropdownContent = document.querySelector('.hidden');
  dropdownContent.style.display = 'flex';
});
var div = document.getElementById('hidden');
div.addEventListener('mouseleave', function() {
  var dropdownContent = document.querySelector('.hidden');
  dropdownContent.style.display = 'none';
});

});

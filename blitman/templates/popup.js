function togglePopup() {
  var overlay = document.getElementById("overlay");
  var popup = document.getElementById("popup");

  overlay.style.display = "block";
  popup.style.display = "block";
}

function closePopup() {
  var overlay = document.getElementById("overlay");
  var popup = document.getElementById("popup");

  overlay.style.display = "none";
  popup.style.display = "none";
}

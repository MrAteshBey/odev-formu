const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileElem");

dropArea.addEventListener("click", () => fileInput.click());
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.style.background = "#e0e7ff";
});
dropArea.addEventListener("dragleave", () => {
  dropArea.style.background = "#fafafa";
});
dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  fileInput.files = e.dataTransfer.files;
  dropArea.style.background = "#fafafa";
});

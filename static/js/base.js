
const input = document.querySelector('input[type="tel"]');

input.addEventListener('input', () => {
  input.value = input.value.replace(/\D/g, '');
});

const passwordBtn = document.getElementById("password-btn");

const dashIcon = document.querySelector("#password-btn .dashicon");

passwordBtn.addEventListener("click", function () {
  dashIcon.classList.toggle("dashicon-hidden");
});

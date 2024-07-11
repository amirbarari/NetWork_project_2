const container = document.querySelector(".container");
const signupBtn = document.querySelector(".button-leftside");
signupBtn.addEventListener("click", doit);

function doit() {
    container.classList.toggle("change");
}
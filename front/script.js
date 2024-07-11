const container = document.querySelector(".container");
const signupBtn = document.querySelector(".show-signup-button");
signupBtn.addEventListener("click", doit);

function doit() {
    container.classList.toggle("change");
}
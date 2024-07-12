const container = document.querySelector(".container");

const signinBtn = document.querySelector(".show-signin-button");
const signupBtn = document.querySelector(".show-signup-button");
let is_showed = false;

signupBtn.addEventListener("click", doit);
signinBtn.addEventListener("click", doitt);
function doit() {
    if (!is_showed) {
        container.classList.toggle("change-signin-form");
        is_showed = true;
    }
    else
        container.classList.toggle("switch-bettwen-in-up");
}

function doitt() {
    if (!is_showed) {
        is_showed = true;
        container.classList.toggle("change-signup-form");
    }
    else
        container.classList.toggle("switch-bettwen-in-up");
}
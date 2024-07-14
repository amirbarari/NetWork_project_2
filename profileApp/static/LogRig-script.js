const container = document.querySelector(".container");

const signupBtn = document.querySelector(".show-signup-button");
const signinBtn = document.querySelector(".show-signin-button");
const title1 = document.querySelector("elegantshadow");
const title2 = document.querySelector("elegantshadow1");

let is_signin_form_close = true;
let is_signup_form_close = true;

signupBtn.addEventListener("click", signup_click);
signinBtn.addEventListener("click", signin_click);
function signin_click() {
    if (is_signup_form_close) {
        is_signin_form_close = !is_signin_form_close;
        title_state();
        container.classList.toggle("change-signin-form");
        container.classList.remove("switch-to-signup");
    }
    else {
        is_signup_form_close = true;
        is_signin_form_close = false;
        title_state();
        container.classList.remove("switch-to-signup");
        container.classList.toggle("switch-to-signin");
    }
}

function signup_click() {
    if (is_signin_form_close) {
        is_signup_form_close = !is_signup_form_close;
        title_state();
        container.classList.toggle("change-signup-form");
        container.classList.remove("switch-to-signup");
    }
    else {
        is_signin_form_close = true;
        is_signup_form_close = false;
        title_state();
        container.classList.remove("switch-to-signin");
        container.classList.toggle("switch-to-signup");
    }
}

function title_state() {
    if (!is_signin_form_close && is_signup_form_close) {
        container.classList.toggle("hide-title");
        container.classList.toggle("hide-title1");
    }
    else {
        container.classList.toggle("hide-title");
        container.classList.toggle("hide-title1");
    }
}
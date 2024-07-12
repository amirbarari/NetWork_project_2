const container = document.querySelector(".container");

const signupBtn = document.querySelector(".show-signup-button");
const signinBtn = document.querySelector(".show-signin-button");

let is_signin_form_close = true;
let is_signup_form_close = true;

signupBtn.addEventListener("click", signup_click);
signinBtn.addEventListener("click", signin_click);
function signin_click() {
    if (is_signup_form_close) {
        is_signin_form_close = !is_signin_form_close;
        container.classList.toggle("change-signin-form");
        Log(is_signin_form_close, is_signup_form_close);
    }
    else {
        is_signup_form_close = true;
        is_signin_form_close = false;
        container.classList.remove("switch-to-signup");
        container.classList.toggle("switch-to-signin");
        Log(is_signin_form_close, is_signup_form_close);
    }
}

function signup_click() {
    if (is_signin_form_close) {
        is_signup_form_close = !is_signup_form_close;
        container.classList.toggle("change-signup-form");
        Log(is_signin_form_close, is_signup_form_close);
    }
    else {
        is_signin_form_close = true;
        is_signup_form_close = false;
        container.classList.remove("switch-to-signin");
        container.classList.toggle("switch-to-signup");
        Log(is_signin_form_close, is_signup_form_close);
    }
}
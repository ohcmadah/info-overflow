const btnSignUp = document.querySelector(".btn-sign-up");
const btnSignIn = document.querySelector(".btn-sign-in");
const btnLogo = document.querySelector(".logo");

function setEvent() {
    if (btnSignIn) {
        btnSignIn.addEventListener('click', event => {
            event.preventDefault();
            location.href = '/login';
        });
    }
    if (btnSignUp) {
        btnSignUp.addEventListener('click', event => {
            event.preventDefault();
            location.href = '/signup';
        });
    }
    if (btnLogo) {
        btnLogo.addEventListener('click', event => {
            event.preventDefault();
            location.href = '/';
        })
    }
}

function init() {
    setEvent();
}

init();
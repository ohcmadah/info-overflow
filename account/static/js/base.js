const btnSignUp = document.querySelector(".btn-sign-up")
const btnSignIn = document.querySelector(".btn-sign-in")

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
}

function init() {
    setEvent();
}

init();
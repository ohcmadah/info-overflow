const btnSignUp = document.querySelector(".btn-sign-up");
const btnSignIn = document.querySelector(".btn-sign-in");
const btnLogo = document.querySelector(".logo");

const navUser = document.querySelector(".nav-user");
const dropdown = document.querySelector(".dropdown");
const dropdownList = document.querySelectorAll(".dropdown a");

function setEvent() {
    if (btnSignIn) {
        btnSignIn.addEventListener('click', evt => {
            evt.preventDefault();
            location.href = '/login';
        });
    }
    if (btnSignUp) {
        btnSignUp.addEventListener('click', evt => {
            evt.preventDefault();
            location.href = '/signup';
        });
    }
    if (btnLogo) {
        btnLogo.addEventListener('click', evt => {
            evt.preventDefault();
            location.href = '/';
        })
    }

    if (navUser) {
        navUser.addEventListener('click', evt => {
            dropdown.classList.toggle("dropdown-active");
        });
    }
    if (dropdownList) {
        dropdownList.forEach( menu => {
            menu.addEventListener('click', evt => {
                dropdown.classList.remove("dropdown-active");
                if (menu.innerText === "My page") {
                    location.href = '/my_page/';
                } else {
                    const result = confirm("로그아웃 하시겠습니까?");
                    if (result) {
                        location.href = '/logout/'
                    }
                }
            });
        })
    }
}

function init() {
    setEvent();
}

init();
const sortSelect = document.querySelector("#sort-select");

function setEvent() {
    if (sortSelect) {
        sortSelect.addEventListener('change', (evt) => {
            const value = sortSelect.value;
            if (value === 'popular') {
                location.href = `/${value}`
            } else {
                location.href = '/'
            }
        })
    }
}

function init() {
    setEvent();
    if (location.pathname === "/popular/") {
        sortSelect[1].selected = true;
    }
}

init();
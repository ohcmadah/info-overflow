const sortSelect = document.querySelector("#sort-select");

function setEvent() {
    if (sortSelect) {
        sortSelect.addEventListener('change', (evt) => {
            const value = sortSelect.value;
            if (value === 'popular') {
                if (location.search.includes('category')) {
                    location.href = `${location.search}&sort=popular`
                } else {
                    location.href = '?sort=popular'
                }
            } else {
                location.href = '/'
            }
        })
    }
}

function init() {
    setEvent();
    if (location.search.includes('popular')) {
        sortSelect[1].selected = true;
    }
}

init();
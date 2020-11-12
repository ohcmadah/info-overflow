const btnDeactivate = document.querySelector('.btn-deactivate');
const deactivateForm = document.querySelector('#deactivate_form');

function setEvent() {
    if (btnDeactivate) {
        btnDeactivate.addEventListener('click', event => {
            event.preventDefault();

            const isDeactivate = confirm('Deactivate');

            if (isDeactivate) {
                deactivateForm.submit();
            }
        });
    }
}

function init() {
    setEvent();
}

init();
const inputEditName = document.querySelector('#id_name');
const selectEditDepartment = document.querySelector('#id_department');
const btnNameCancel = document.querySelector('.profile-name .btn-cancel');
const btnDepartmentCancel = document.querySelector('.profile-department .btn-cancel');
const btnApplyAll = document.querySelectorAll('.btn-apply');

const spanName = document.querySelector('.profile-name span');
const spanDepartment = document.querySelector('.profile-department span');
const btnNameEdit = document.querySelector('.btn-name-edit');
const btnDepartmentEdit = document.querySelector('.btn-department-edit');

function setEvent() {
    if (btnApplyAll) {
        btnApplyAll.forEach(btnApply => {
                btnApply.addEventListener('click', event => {
                event.preventDefault();

                const form = event.target.parentNode.parentNode;
                form.submit();
            });
        })
    }

    if (btnNameEdit && btnDepartmentEdit) {
        btnNameEdit.addEventListener('click', event => {
            event.preventDefault();
            editToggle('name');
        });
        btnDepartmentEdit.addEventListener('click', event => {
            event.preventDefault();
            editToggle('department');
        });
    }

    if (btnNameCancel && btnDepartmentCancel) {
        btnNameCancel.addEventListener('click', event => {
            event.preventDefault();
            editToggle('name');
        });
        btnDepartmentCancel.addEventListener('click', event => {
            event.preventDefault();
            editToggle('department');
        });
    }
}

function editToggle(target) {
    if (target === 'name') {
        inputEditName.classList.toggle('invisible');
        btnNameEdit.classList.toggle('invisible');
        btnNameCancel.classList.toggle('invisible');
        btnApplyAll[0].classList.toggle('invisible');
        spanName.classList.toggle('invisible');
    } else {
        selectEditDepartment.classList.toggle('invisible');
        btnDepartmentEdit.classList.toggle('invisible');
        btnDepartmentCancel.classList.toggle('invisible');
        btnApplyAll[1].classList.toggle('invisible');
        spanDepartment.classList.toggle('invisible');
    }
}

function init() {
    setEvent();
}

init();
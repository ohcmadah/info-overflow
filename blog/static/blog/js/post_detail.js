const btnCommentEditAll = document.querySelectorAll(".btn-comment-edit");
let btnCommentSave;

function setEvent() {
    if (btnCommentEditAll) {
        btnCommentEditAll.forEach(btnCommentEdit => {
                btnCommentEdit.addEventListener('click', event => {
                event.preventDefault();

                btnCommentEdit.classList.toggle("invisible");

                const pk = btnCommentEdit.id.split('-')[2];

                myToggle(pk);
            });
        })
    }
    if (btnCommentSave) {
        btnCommentSave.addEventListener('click', event => {
            event.preventDefault();
            myToggle();
            commentEditForm.submit();
        });
    }
}

function myToggle(pk) {
    const editTextArea = document.querySelector(`#edit-textarea-${pk}`);
    const commentContent = document.querySelector(`#comment-content-${pk}`);
    btnCommentSave = document.querySelector(`#save-btn-${pk}`);
    const btnCommentRemove = document.querySelector(`#remove-btn-${pk}`);
    const line = document.querySelector(`#line-${pk}`);

    if (editTextArea && commentContent && btnCommentSave && btnCommentRemove && line) {
        editTextArea.classList.toggle("invisible");
        commentContent.classList.toggle("invisible");
        btnCommentSave.classList.toggle("invisible");
        btnCommentRemove.classList.toggle("invisible");
        line.classList.toggle("invisible");
    }
}

function init() {
    setEvent();
}

init();
const btnCommentEdit = document.querySelector(".btn-comment-edit");
const btnCommentSave = document.querySelector(".btn-comment-save");
const btnCommentRemove = document.querySelector(".btn-comment-remove");

const line = document.querySelector(".comment-buttons .line");
const commentEditForm = document.querySelector("#comment-edit-form");

const editTextArea = document.querySelector(".edit-textarea");
const commentContent = document.querySelector(".comment-content");

function setEvent() {
    if (btnCommentSave) {
        btnCommentSave.classList.add("invisible");
        editTextArea.classList.add("invisible");
    }
    if (btnCommentEdit) {
        btnCommentEdit.addEventListener('click', event => {
            event.preventDefault();
            myToggle();
        });
    }
    if (btnCommentSave) {
        btnCommentSave.addEventListener('click', event => {
            event.preventDefault();
            myToggle();
            commentEditForm.submit();
        });
    }
}

function myToggle() {
    btnCommentSave.classList.toggle("invisible");
    btnCommentRemove.classList.toggle("invisible");
    btnCommentEdit.classList.toggle("invisible");
    line.classList.toggle("invisible");
    editTextArea.classList.toggle("invisible");
    commentContent.classList.toggle("invisible");
}

function init() {
    setEvent();
}

init();
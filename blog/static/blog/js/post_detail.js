const btnCommentEditAll = document.querySelectorAll(".btn-comment-edit");
const btnCommentRemoveAll = document.querySelectorAll(".btn-comment-remove");
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

    if (btnCommentRemoveAll) {
        btnCommentRemoveAll.forEach(btnCommentRemove => {
            btnCommentRemove.addEventListener('click', evt => {
                evt.preventDefault();

                const result = confirm("댓글을 삭제하시겠습니까?");
                if (result) {
                    const removeUrl = evt.target.getAttribute("href");
                    location.href = removeUrl;
                }
            })
        })
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
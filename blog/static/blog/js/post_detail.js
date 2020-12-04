const btnCommentEditAll = document.querySelectorAll(".btn-comment-edit");
const btnCommentRemoveAll = document.querySelectorAll(".btn-comment-remove");
const btnPostRemove= document.querySelector(".btn-remove a");
let btnCommentSave;
let editing = false;
let pk;

const btnCommentTagAll = document.querySelectorAll('.tagable');

function setEvent() {
    if (btnCommentEditAll) {
        btnCommentEditAll.forEach(btnCommentEdit => {
            btnCommentEdit.addEventListener('click', event => {
                event.preventDefault();

                if (editing) {
                    myToggle();
                }
                pk = btnCommentEdit.id.split('-')[2];

                myToggle();
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

    if (btnPostRemove) {
        btnPostRemove.addEventListener('click', evt => {
             evt.preventDefault();

                const result = confirm("게시글을 삭제하시겠습니까?");
                if (result) {
                    const removeUrl = evt.target.getAttribute("href");
                    location.href = removeUrl;
                }
        })
    }

    if (btnCommentTagAll) {
        btnCommentTagAll.forEach(btnCommentTag => {
            btnCommentTag.addEventListener('click', evt => {
                const clickName = btnCommentTag.querySelector('.comment-info span').innerText;
                let textarea;
                if (editing) {
                    textarea = document.querySelector(`#edit-textarea-${pk} textarea`);
                } else {
                    textarea = document.querySelector('.textarea-comment');
                }

                if (textarea.value !== '') {
                    textarea.value += '\n';
                }
                textarea.value += `@${clickName}\n`;
                textarea.focus();
            })
        })
    }
}

function myToggle() {
    const editTextArea = document.querySelector(`#edit-textarea-${pk}`);
    const commentContent = document.querySelector(`#comment-content-${pk}`);
    btnCommentSave = document.querySelector(`#save-btn-${pk}`);
    const btnCommentEdit = document.querySelector(`#edit-btn-${pk}`);
    const btnCommentRemove = document.querySelector(`#remove-btn-${pk}`);
    const line = document.querySelector(`#line-${pk}`);

    if (editTextArea && commentContent && btnCommentSave && btnCommentRemove && line && btnCommentEdit) {
        editTextArea.classList.toggle("invisible");
        commentContent.classList.toggle("invisible");
        btnCommentSave.classList.toggle("invisible");
        btnCommentRemove.classList.toggle("invisible");
        line.classList.toggle("invisible");
        btnCommentEdit.classList.toggle("invisible");
    }

    if (editing) {
        const commentContent = document.querySelector(`#comment-content-${pk}`).childNodes[2].innerText;
        editTextArea.firstElementChild.value = commentContent;
    }

    editing = !editing;
}

function init() {
    setEvent();
}

init();
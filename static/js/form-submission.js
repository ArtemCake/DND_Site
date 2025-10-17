// form-submission.js

document.addEventListener('DOMContentLoaded', function() {
    const mainForm = document.getElementById('EditForm');

    if (!mainForm) {
        console.log('Форма не найдена. Скрипт не будет выполнен.');
        return;
    }

    mainForm.onsubmit = function(event) {
        const submitter = event.submitter;

        if (!(submitter.id === 'update' || submitter.id === 'closeOn')) {
            event.preventDefault();
        }
    };
});
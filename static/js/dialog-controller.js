// dialog-controller.js
document.addEventListener('DOMContentLoaded', function() {
    const dialog = document.querySelector('dialog');
    if (dialog) {
        document.querySelector('#open').addEventListener('click', () => dialog.showModal());
        document.querySelector('#closeOn').addEventListener('click', () => dialog.close());
        document.querySelector('#closeOff').addEventListener('click', () => dialog.close());
    }
});
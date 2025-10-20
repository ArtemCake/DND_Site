// dialog-controller.js

document.addEventListener('DOMContentLoaded', () => {
    const dialog = document.querySelector('dialog');
    const openButton = document.querySelector('#open');
    const closeButtons = document.querySelectorAll('#closeOn, #closeOff');

    if (!dialog) {
        console.warn('Диалоговое окно не найдено. Скрипт не будет выполнен.');
        return;
    }

    openButton?.addEventListener('click', () => dialog.showModal());

    closeButtons.forEach(button => {
        button?.addEventListener('click', () => dialog.close());
    });
});
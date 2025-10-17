// dialog-controller.js

document.addEventListener('DOMContentLoaded', function() {
    const dialog = document.querySelector('dialog');
    const openButton = document.querySelector('#open');
    const closeOnButton = document.querySelector('#closeOn');
    const closeOffButton = document.querySelector('#closeOff');

    if (!dialog || !openButton || !closeOnButton || !closeOffButton) {
        console.log('Один или несколько элементов не найдены. Скрипт не будет выполнен.');
        return;
    }

    openButton.addEventListener('click', () => dialog.showModal());
    closeOnButton.addEventListener('click', () => dialog.close());
    closeOffButton.addEventListener('click', () => dialog.close());
});
// buttons-return.js

document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.getElementById('back-button');

    if (!backButton) {
        console.log('Кнопка возврата не найдена. Скрипт не будет выполнен.');
        return;
    }

    backButton.addEventListener('click', function() {
        window.history.back();
    });
});
// forms.js

document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.querySelector('.registration-form');
    const errorMessage = document.querySelector('.error-message');
    const passwordField = document.getElementById('password-input');
    const confirmPasswordField = document.getElementById('password-input-confirm');

    if (!registrationForm || !errorMessage || !passwordField || !confirmPasswordField) {
        console.error('Один или несколько элементов не найдены.');
        return;
    }

    // Базовая проверка соответствия паролей
    function validatePasswords(event) {
        if (passwordField.value !== confirmPasswordField.value) {
            event.preventDefault(); // Предотвращение отправки формы
            errorMessage.style.display = 'block'; // Показываем сообщение об ошибке
        } else {
            errorMessage.style.display = 'none'; // Скрываем сообщение об ошибке
        }
    }

    // Обработчик отправки формы
    registrationForm.addEventListener('submit', validatePasswords);

    // Слежение за полем пароля
    passwordField.addEventListener('input', () => {
        errorMessage.style.display = 'none';
    });

    // Слежение за полем подтверждения пароля
    confirmPasswordField.addEventListener('input', () => {
        errorMessage.style.display = 'none';
    });

    // Возможность отключения отображения ошибки при очистке полей
    [passwordField, confirmPasswordField].forEach(input => {
        input.addEventListener('focus', () => {
            errorMessage.style.display = 'none';
        });
    });
});
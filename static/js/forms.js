// forms.js

document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.querySelector('.registration-form');
    const errorMessage = document.querySelector('.error-message');
    const passwordField = document.getElementById('password-input');
    const confirmPasswordField = document.getElementById('password-input-confirm');

    // Проверка совпадения паролей при отправке формы
    registrationForm.addEventListener('submit', event => {
        if (passwordField.value !== confirmPasswordField.value) {
            event.preventDefault(); // Предотвращаем отправку формы
            errorMessage.style.display = 'block'; // Показываем сообщение об ошибке
        } else {
            errorMessage.style.display = 'none'; // Скрываем сообщение об ошибке
        }
    });

    // Скрытие сообщения об ошибке при изменении полей пароля
    passwordField.addEventListener('input', () => {
        if (!passwordField.value || !confirmPasswordField.value) {
            errorMessage.style.display = 'none';
        }
    });

    confirmPasswordField.addEventListener('input', () => {
        if (!passwordField.value || !confirmPasswordField.value) {
            errorMessage.style.display = 'none';
        }
    });
});
// script.js

// Функция для переключения отображения пароля
function togglePasswordVisibility(spanElement, fieldID) {
    var passwordField = document.getElementById(fieldID);
    var imgElement = spanElement.querySelector('img');

    if (passwordField.type === 'password') {
        passwordField.type = 'text'; // Покажем пароль
        imgElement.src = '/static/logo/view.png'; // Установим иконку "Видеть"
    } else {
        passwordField.type = 'password'; // Скроем пароль
        imgElement.src = '/static/logo/no-view.png'; // Установим иконку "Невидеть"
    }
}

// Связывание событий с иконками
document.addEventListener("DOMContentLoaded", function() {
    // Формы регистрации
    document.querySelectorAll('.registration-form .toggle-password').forEach((element) => {
        element.addEventListener('click', function() {
            var fieldID = element.parentNode.querySelector('input').id; // Берём ID ближайшего поля пароля
            togglePasswordVisibility(element, fieldID);
        });
    });

    document.querySelectorAll('.registration-form .toggle-password-one').forEach((element) => {
        element.addEventListener('click', function() {
            var fieldID = element.parentNode.querySelector('input').id; // Берём ID ближайшего поля пароля
            togglePasswordVisibility(element, fieldID);
        });
    });

    // Форма входа
    document.querySelectorAll('.authentication-form .toggle-password').forEach((element) => {
        element.addEventListener('click', function() {
            var fieldID = element.parentNode.querySelector('input').id; // Берём ID ближайшего поля пароля
            togglePasswordVisibility(element, fieldID);
        });
    });
});
// form-switcher.js

document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');
    const signinForm = document.getElementById('signin-form');
    const registerLink = document.querySelector('.authentication-form .message a');
    const loginLink = document.querySelector('.registration-form .message a');

    if (!signupForm || !signinForm || !registerLink || !loginLink) {
        console.warn('Один или несколько элементов не найдены. Скрипт не будет выполнен.');
        return;
    }

    let hash = location.hash || '';

    // Изначально скрываем обе формы
    signupForm.classList.add('hidden');
    signinForm.classList.add('hidden');

    // Отображаем нужную форму в зависимости от хэша
    if (hash === '#login') {
        signinForm.classList.remove('hidden');
    } else if (hash === '#register' || !hash) {
        signupForm.classList.remove('hidden');
    }

    // Функции для переключения форм
    function showSignIn() {
        signupForm.classList.add('hidden');
        signinForm.classList.remove('hidden');
    }

    function showSignUp() {
        signupForm.classList.remove('hidden');
        signinForm.classList.add('hidden');
    }

    // Обработка кликов по ссылкам
    loginLink.addEventListener('click', function(event) {
        event.preventDefault();
        showSignIn();
    });

    registerLink.addEventListener('click', function(event) {
        event.preventDefault();
        showSignUp();
    });

    // Обновляем формы при изменении хэша
    window.addEventListener('hashchange', () => {
        hash = location.hash || '';
        if (hash === '#login') {
            showSignIn();
        } else if (hash === '#register' || !hash) {
            showSignUp();
        }
    });
});
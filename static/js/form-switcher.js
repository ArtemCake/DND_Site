// form-switcher.js
document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.getElementById("signup-form");
    const signinForm = document.getElementById("signin-form");

    let hash = location.hash || '';

    // Изначально скрываем обе формы
    signupForm?.classList.add("hidden");
    signinForm?.classList.add("hidden");

    // Показываем нужную форму в зависимости от хэша
    if (hash === '#login') {
        signinForm?.classList.remove("hidden");
    } else if (hash === '#register' || !hash) {
        signupForm?.classList.remove("hidden");
    }

    // Функции для ручного переключения
    function showSignIn() {
        signupForm?.classList.add("hidden");
        signinForm?.classList.remove("hidden");
    }

    function showSignUp() {
        signupForm?.classList.remove("hidden");
        signinForm?.classList.add("hidden");
    }

    // Найдем анкорные ссылки для переключения форм
    const registerLink = document.querySelector('.authentication-form .message a');
    const loginLink = document.querySelector('.registration-form .message a');

    // Обработка события кликов на анкоре "Войти"
    loginLink?.addEventListener("click", function(event) {
        event.preventDefault();
        showSignIn();
    });

    // Обработка события кликов на анкоре "Зарегистрироваться"
    registerLink?.addEventListener("click", function(event) {
        event.preventDefault();
        showSignUp();
    });

    // Добавляем обработчик хэш-механизма вручную (если понадобится)
    window.onhashchange = function() {
        hash = location.hash || '';
        if (hash === '#login') {
            showSignIn();
        } else if (hash === '#register' || !hash) {
            showSignUp();
        }
    };
});
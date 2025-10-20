// password-toggle.js

document.addEventListener('DOMContentLoaded', () => {
    // Обобщенный обработчик переключателей пароля
    document.querySelectorAll('.toggle-password').forEach((spanElement) => {
        const fieldID = spanElement.getAttribute('data-for-field'); // Получаем ID поля пароля

        if (!fieldID) {
            console.error('Не задан атрибут data-for-field на переключателе пароля');
            return;
        }

        const passwordField = document.getElementById(fieldID);
        const imgElement = spanElement.querySelector('img');

        if (!passwordField || !imgElement) {
            console.error('Элементы не найдены для переключателя пароля');
            return;
        }

        spanElement.addEventListener('click', () => {
            if (passwordField.type === 'password') {
                passwordField.type = 'text'; // Пароль отображается открыто
                imgElement.src = '/static/logo/view.png'; // Меняем иконку на "видеть"
            } else {
                passwordField.type = 'password'; // Пароль снова маскируется
                imgElement.src = '/static/logo/no-view.png'; // Меняем иконку на "не видеть"
            }
        });
    });
});
// universal_filter_script.js

document.addEventListener('DOMContentLoaded', () => {
    // Получаем все зависимые выпадающие списки
    const dependentDropdowns = document.querySelectorAll('[data-dependent-on]');

    dependentDropdowns.forEach(dependentDropdown => {
        // Получаем родительский элемент
        const parentFieldSelector = `[data-param-id="${dependentDropdown.getAttribute('data-dependent-on')}"]`;
        const parentField = document.querySelector(parentFieldSelector);

        // Проверяем существование родительского поля
        if (!parentField) {
            console.error(`Родительское поле (${parentFieldSelector}) не найдено.`);
            return;
        }

        // Получаем контейнер с опциями
        const dropdownContainer = dependentDropdown.querySelector('.dropdown-content');
        if (!dropdownContainer) {
            console.error(`Контейнер (.dropdown-content) не найден в ${dependentDropdown}.`);
            return;
        }

        // Получаем доступные опции
        const childOptions = dropdownContainer.querySelectorAll('ul li');

        // Получаем поля для хранения значений и текста
        const relatedFields = [
            dependentDropdown.querySelector('.values-input'),
            dependentDropdown.querySelector('.texts-input')
        ];

        // Изначально скрываем все опции
        childOptions.forEach(option => option.style.display = 'none');

        // Обработчик кликов по родительскому элементу
        parentField.addEventListener('change', () => {
            const selectedParentValue = parentField.value;

            // Обновляем отображаемые опции
            childOptions.forEach(option => {
                if (option.getAttribute('data-parent-id') === selectedParentValue) {
                    option.style.display = '';
                } else {
                    option.style.display = 'none';
                }
            });

            // Сбрасываем значения зависимых полей
            relatedFields.forEach(field => field.value = '');
        });
    });
});
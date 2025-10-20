document.addEventListener('DOMContentLoaded', () => {
    // Ищем все зависимые выпадающие списки
    const dependentDropdowns = document.querySelectorAll('[data-dependent-on]');

    dependentDropdowns.forEach(dependentDropdown => {
        // Идентификатор родительского поля
        const parentFieldSelector = '#' + dependentDropdown.getAttribute('data-dependent-on');
        const parentField = document.querySelector(parentFieldSelector);

        // Контейнер зависимого выпадающего списка
        const dropdownContainer = dependentDropdown.querySelector('.dropdown-content');

        // Только элементы <li> в контейнере
        const childOptions = dropdownContainer.querySelectorAll('ul li');

        // Формируем массив ссылок на связанные поля
        const relatedFields = [
            dependentDropdown.querySelector('.values-input'),
            dependentDropdown.querySelector('.texts-input')
        ];

        // Изначально скрываем все опции зависимого списка
        childOptions.forEach(option => {
            option.style.display = 'none';
        });

        // Обработчик кликов по элементам родительского списка
        parentField.closest('.dropdown').addEventListener('click', e => {
            const clickedItem = e.target.closest('li');
            if (clickedItem) {
                const selectedParentValue = clickedItem.getAttribute('data-value');
                parentField.value = selectedParentValue;

                // Сбрасываем выбор зависимых полей
                relatedFields.forEach(field => field.value = '');

                // Обновляем отображаемые опции зависимого списка
                childOptions.forEach(option => {
                    if (option.getAttribute('data-parent-id') === selectedParentValue) {
                        option.style.display = '';
                    } else {
                        option.style.display = 'none';
                    }
                });
            }
        });
    });
});
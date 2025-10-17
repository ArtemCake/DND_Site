// script.js

document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');

    if (dropdowns.length === 0) {
        console.log('Выпадающие списки не найдены. Скрипт не будет выполнен.');
        return;
    }

    dropdowns.forEach(dropdown => {
        const content = dropdown.querySelector('.dropdown-content');          // Содержимое выпадающего списка
        const valuesInput = dropdown.querySelector('.values-input');         // Скрытое поле для хранения значений
        const textsInput = dropdown.querySelector('.texts-input');           // Видимое поле для отображения текста
        const items = Array.from(content.querySelectorAll('ul li'));         // Доступные элементы для выбора
        const fixedMode = dropdown.dataset.fixed === 'true';                 // Режим фиксации (невозможность редактирования)
        const selectionType = dropdown.classList.contains('multiple-select') ? 'multiple' : 'single'; // Тип выбора (одиночный/множественный)

        if (!content || !valuesInput || !textsInput || items.length === 0) {
            console.log('Один или несколько элементов не найдены. Скрипт не будет выполнен.');
            return;
        }

        // Предварительное выделение элементов
        let preselectedValues = [];
        if (valuesInput.value !== '') {
            preselectedValues = valuesInput.value.split(',').map(value => value.trim());
        }

        // Установка классов "selected" для предварительно выбранных элементов
        items.forEach(item => {
            if (preselectedValues.includes(item.dataset.value)) {
                item.classList.add('selected');
            }
        });

        // Первоначальное обновление полей
        updateDropdownDisplay();

        // Обработка кликов по элементам списка
        content.addEventListener('click', event => {
            const target = event.target.closest('li');

            if (!target || fixedMode) return; // Ничего не делаем, если клик вне зоны или в режиме фиксации

            switch (selectionType) {
                case 'single':
                    // Удаляем все предыдущие выборы и добавляем новый
                    items.forEach(item => item.classList.remove('selected'));
                    target.classList.add('selected');
                    break;
                case 'multiple':
                    // Переключаем статус выбора текущего пункта
                    target.classList.toggle('selected');
                    break;
            }

            // Обновляем состояние полей
            updateDropdownDisplay();
        });

        // Функция обновления состояний полей
        function updateDropdownDisplay() {
            const selectedItems = items.filter(item => item.classList.contains('selected')).map(item => ({
                value: item.dataset.value,
                text: item.textContent
            }));

            // Сохраняем значения в скрытом поле
            valuesInput.value = selectedItems.map(i => i.value).join(', ');

            // Обновляем отображаемое поле
            textsInput.value = selectedItems.map(i => i.text).join(', ');
        }
    });
});
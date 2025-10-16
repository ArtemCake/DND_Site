document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.dropdown').forEach(dropdown => {
        const content = dropdown.querySelector('.dropdown-content');
        const valuesInput = dropdown.querySelector('.values-input');
        const textsInput = dropdown.querySelector('.texts-input');
        const items = Array.from(content.querySelectorAll('ul li'));
        const fixedMode = dropdown.dataset.fixed === 'true'; // Фиксированный режим
        const selectionType = dropdown.classList.contains('multiple-select') ? 'multiple' : 'single';

        // Предварительно выбираемые элементы
        let preselectedValues = [];
        if (valuesInput.value !== '') {
            preselectedValues = valuesInput.value.split(',').map(v => v.trim());
        }

        // Применяем классы для предварительного выделения
        items.forEach(item => {
            if (preselectedValues.includes(item.dataset.value)) {
                item.classList.add('selected');
            }
        });

        // Подготавливаем отображение текста и значений
        updateDropdownDisplay();

        // Клик обработчик
        content.addEventListener('click', event => {
            const target = event.target.closest('li');

            if (!target || fixedMode) return; // Игнорируем события для фиксированных элементов

            switch (selectionType) {
                case 'single': // Одинарный выбор
                    items.forEach(item => item.classList.remove('selected'));
                    target.classList.add('selected');
                    break;
                case 'multiple': // Многократный выбор
                    target.classList.toggle('selected');
                    break;
            }

            // Обновляем поля ввода и отображаемый текст
            updateDropdownDisplay();
        });

        // Функция обновления состояния полей
        function updateDropdownDisplay() {
            const selectedItems = items.filter(item => item.classList.contains('selected')).map(item => ({
                value: item.dataset.value,
                text: item.textContent
            }));

            valuesInput.value = selectedItems.map(i => i.value).join(', ');
            textsInput.value = selectedItems.map(i => i.text).join(', ');
        }
    });
});
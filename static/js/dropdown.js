// dropdown.js

document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');

    if (dropdowns.length === 0) {
        console.log('Выпадающие списки не найдены. Скрипт не будет выполнен.');
        return;
    }

    dropdowns.forEach(dropdown => {
        const content = dropdown.querySelector('.dropdown-content');
        const valuesInput = dropdown.querySelector('.values-input');
        const textsInput = dropdown.querySelector('.texts-input');
        const items = Array.from(content.querySelectorAll('ul li'));
        const modeFixed = dropdown.dataset.fixed === 'true';
        const selectionType = dropdown.classList.contains('multiple-select') ? 'multiple' : 'single';

        if (!content || !valuesInput || !textsInput || items.length === 0) {
            console.log('Один или несколько элементов не найдены. Скрипт не будет выполнен.');
            return;
        }

        // Начальная подготовка состояния элементов
        let initialSelectedValues = [];
        if (valuesInput.value) {
            initialSelectedValues = valuesInput.value.split(',').map(v => v.trim());
        }

        // Отмечаем предварительно выбранные пункты
        items.forEach(item => {
            if (initialSelectedValues.includes(item.dataset.value)) {
                item.classList.add('selected');
            }
        });

        // Обновляем отображение
        updateDropdownDisplay();

        // Обработка кликов по пунктам списка
        content.addEventListener('click', event => {
            const target = event.target.closest('li');

            if (!target || modeFixed) return;

            switch (selectionType) {
                case 'single':
                    items.forEach(item => item.classList.remove('selected'));
                    target.classList.add('selected');
                    break;
                case 'multiple':
                    target.classList.toggle('selected');
                    break;
            }

            updateDropdownDisplay();
        });

        // Вспомогательная функция для обновления отображения
        function updateDropdownDisplay() {
            const selectedItems = items.filter(item => item.classList.contains('selected'))
                                      .map(item => ({
                                          value: item.dataset.value,
                                          text: item.textContent
                                      }));

            valuesInput.value = selectedItems.map(i => i.value).join(', ');
            textsInput.value = selectedItems.map(i => i.text).join(', ');
        }
    });
});
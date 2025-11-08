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

            // Получаем необходимые атрибуты
            const elementValue = target.dataset.value;
            const hasCategoryAttr = target.hasAttribute('data-category'); // Проверка наличия атрибута
            const category = hasCategoryAttr ? target.dataset.category : null;

            // Обновляем выбранный элемент и категорию
	        if (selectionType === 'single') {
		        valuesInput.value = elementValue;
		        textsInput.value = target.textContent;

		        // Только если есть категория, обновляем скрытое поле
		        if (hasCategoryAttr) {
			        const categoriesInput = dropdown.querySelector('.categories-input');
			        if (categoriesInput) {
				        categoriesInput.value = category;
			        }
		        }

		        // Обновляем визуальное состояние (класс selected)
		        items.forEach(item => item.classList.remove('selected'));
		        target.classList.add('selected');
	        } else if (selectionType === 'multiple') {
		        // Для множественного выбора
		        target.classList.toggle('selected');

		        // Обновляем значения и текст
		        const selectedItems = items.filter(item => item.classList.contains('selected'));
		        valuesInput.value = selectedItems.map(item => item.dataset.value).join(', ');
		        textsInput.value = selectedItems.map(item => item.textContent).join(', ');

		        // Обновляем категории
		        if (hasCategoryAttr) {
			        const categoriesInput = dropdown.querySelector('.categories-input');
			        if (categoriesInput) {
				        categoriesInput.value = selectedItems.map(item => item.dataset.category).filter(Boolean).join(', ');
			        }
		        }
	        }
        });

        // Вспомогательная функция для обновления отображения
        function updateDropdownDisplay() {
            const selectedItems = items.filter(item => item.classList.contains('selected'))
                .map(item => ({
                value: item.dataset.value,
                text: item.textContent,
                category: item.dataset.category || ''
            }));

            valuesInput.value = selectedItems.map(i => i.value).join(', ');      // Заполняем скрытые поля
            textsInput.value = selectedItems.map(i => i.text).join(', ');        // Текущие названия элементов

            // Если имеется хотя бы один элемент с категорией, обновляем поле категорий
            const hasAnyCategory = selectedItems.some(item => item.category);
            if (hasAnyCategory) {
                const categoriesInput = dropdown.querySelector('.categories-input');
                if (categoriesInput) {
                    categoriesInput.value = selectedItems.map(i => i.category).filter(Boolean).join(', ');
                }
            }
        }
    });
});
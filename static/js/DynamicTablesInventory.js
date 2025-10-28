// DynamicTablesInventory.js

document.addEventListener('DOMContentLoaded', function() {
    // Получаем все таблицы с классом "inventory"
    const tables = document.querySelectorAll('.inventory');

    tables.forEach(table => {
        const addRowButton = table.querySelector('span');
        addRowButton.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвращаем переход по ссылке

            const items = JSON.parse(table.getAttribute('data-items'));
            const tableBody = table.querySelector('tbody');
            const row = document.createElement('tr');

            // Создаем ячейки для каждой колонки
            const cell1 = document.createElement('td');
            cell1.setAttribute('colspan', '2');
            const cell2 = document.createElement('td');
            const cell3 = document.createElement('td');
            const cell4 = document.createElement('td');
            const cell5 = document.createElement('td'); // Добавляем ячейку для удаления

            // Добавляем элемент span для удаления строки
            const deleteSpan = document.createElement('span');
            deleteSpan.textContent = '-';
            deleteSpan.className = 'delete-row';
            cell5.appendChild(deleteSpan);

            // Добавляем всплывающий список в первую ячейку
            const dropdown1 = document.createElement('div');
            dropdown1.className = 'dropdown single-select';
            dropdown1.dataset.type = 'single';
            dropdown1.dataset.fixed = 'false';

            const hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.className = 'values-input class-select';
            hiddenInput.name = 'StorageBag';
            hiddenInput.id = 'StorageBag';
            hiddenInput.placeholder = 'Выберете предмет...';
            hiddenInput.readOnly = true;
            hiddenInput.value = '';
            dropdown1.appendChild(hiddenInput);

            // Новое скрытое поле для хранения категории
            const categoryHiddenInput = document.createElement('input');
            categoryHiddenInput.type = 'hidden';
            categoryHiddenInput.className = 'categories-input';              // Новая категория
            categoryHiddenInput.name = 'StorageBagCategory';               // Имя поля
            categoryHiddenInput.id = 'StorageBagCategory';                 // Идентификатор
            categoryHiddenInput.readOnly = true;
            categoryHiddenInput.value = '';                                 // Изначально пустое
            dropdown1.appendChild(categoryHiddenInput);                     // Добавляем скрытое поле

            const textInput = document.createElement('input');
            textInput.type = 'text';
            textInput.className = 'texts-input';
            textInput.id = 'StorageBagPrint';
            textInput.placeholder = 'Выберете предмет...';
            textInput.readOnly = true;
            dropdown1.appendChild(textInput);

            const dropdownContent1 = document.createElement('div');
            dropdownContent1.className = 'dropdown-content';

            const ul = document.createElement('ul');
            dropdownContent1.appendChild(ul);

            // Добавляем элементы списка из массива items
            items.forEach(function(itemParam) {
                const li = document.createElement('li');
                li.dataset.value = itemParam.id;
                li.textContent = itemParam.Name;
                li.setAttribute('data-category', itemParam.Category);     // Сохраняем категорию
                ul.appendChild(li);
            });

            dropdown1.appendChild(dropdownContent1);
            cell1.appendChild(dropdown1);

            // Создаем инпуты для колонок 2-4
            const input2 = document.createElement('input');
            input2.type = 'number';
            input2.placeholder = 'Количество';
            input2.className = "interactivElement";
            input2.name = 'Quantity';
            input2.value = 1;
            cell2.appendChild(input2);

            const input3 = document.createElement('input');
            input3.type = 'number';
            input3.name = 'Cost';
            input3.className = "interactivElement";
            input3.placeholder = 'Цена';
            cell3.appendChild(input3);

            const input4 = document.createElement('input');
            input4.type = 'number';
            input4.name = 'Weight';
            input4.className = "interactivElement";
            input4.placeholder = 'Вес';
            cell4.appendChild(input4);

            // Добавляем ячейки в строку
            row.appendChild(cell5); // Ячейка с кнопкой удаления
            row.appendChild(cell1);
            row.appendChild(cell2);
            row.appendChild(cell3);
            row.appendChild(cell4);

            // Добавляем строку в таблицу
            tableBody.appendChild(row);

            // Обработчик выбора элемента в выпадающем списке
            dropdownContent1.addEventListener('click', function(event) {
                if (event.target.tagName === 'LI') {
                    const selectedItemId = event.target.dataset.value;
                    const selectedItemcategory = event.target.dataset.category;
                    const selectedItem = items.find(item =>
                    item.id === parseInt(selectedItemId) && item.Category === selectedItemcategory); // ищем элемент по сочетанию ID и категории

                    if (selectedItem) {
                        input3.value = selectedItem.Cost;
                        input4.value = selectedItem.Weight;
                        textInput.value = selectedItem.Name;
                        hiddenInput.value = selectedItem.id;

                        // Устанавливаем категорию в новом скрытом поле
                        categoryHiddenInput.value = selectedItem.Category; // Присваиваем категорию

                        // Расчёт суммы значений в колонке "Вес" с учетом количества
                        const weightInputs = tableBody.querySelectorAll('input[name="Weight"]');
                        const quantityInputs = tableBody.querySelectorAll('input[name="Quantity"]');
                        let totalWeight = 0;
                        weightInputs.forEach((input, index) => {
                            const value = parseFloat(input.value);
                            const quantity = parseFloat(quantityInputs[index].value);
                            if (!isNaN(value) && !isNaN(quantity)) {
                                totalWeight += value * quantity;
                            }
                        });

                        // Записываем сумму в поле "значение веса"
                        const totalWeightInput = document.querySelector('input[name="TotalWeight"]');
                        if (totalWeightInput) {
                            totalWeightInput.value = totalWeight;
                        }
                    }
                }
            });

            // Обработчик кликов для удаления строки
            deleteSpan.addEventListener('click', function() {
                row.remove();

                // Пересчет суммы значений в колонке "Вес" после удаления строки
                const weightInputs = tableBody.querySelectorAll('input[name="Weight"]');
                const quantityInputs = tableBody.querySelectorAll('input[name="Quantity"]');
                let totalWeight = 0;
                weightInputs.forEach((input, index) => {
                    const value = parseFloat(input.value);
                    const quantity = parseFloat(quantityInputs[index].value);
                    if (!isNaN(value) && !isNaN(quantity)) {
                        totalWeight += value * quantity;
                    }
                });

                // Записываем сумму в поле "значение веса"
                const totalWeightInput = document.querySelector('input[name="TotalWeight"]');
                if (totalWeightInput) {
                    totalWeightInput.value = totalWeight;
                }
            });

            // Обработчик изменения веса
            input4.addEventListener('input', function() {
                // Пересчитываем сумму значений в колонке "Вес" после изменения веса
                const weightInputs = tableBody.querySelectorAll('input[name="Weight"]');
                const quantityInputs = tableBody.querySelectorAll('input[name="Quantity"]');
                let totalWeight = 0;
                weightInputs.forEach((input, index) => {
                    const value = parseFloat(input.value);
                    const quantity = parseFloat(quantityInputs[index].value);
                    if (!isNaN(value) && !isNaN(quantity)) {
                        totalWeight += value * quantity;
                    }
                });

                // Записываем сумму в поле "значение веса"
                const totalWeightInput = document.querySelector('input[name="TotalWeight"]');
                if (totalWeightInput) {
                    totalWeightInput.value = totalWeight;
                }
            });

            // Обработчик изменения количества
            input2.addEventListener('input', function() {
                // Пересчитываем сумму значений в колонке "Вес" после изменения количества
                const weightInputs = tableBody.querySelectorAll('input[name="Weight"]');
                const quantityInputs = tableBody.querySelectorAll('input[name="Quantity"]');
                let totalWeight = 0;
                weightInputs.forEach((input, index) => {
                    const value = parseFloat(input.value);
                    const quantity = parseFloat(quantityInputs[index].value);
                    if (!isNaN(value) && !isNaN(quantity)) {
                        totalWeight += value * quantity;
                    }
                });

                // Записываем сумму в поле "значение веса"
                const totalWeightInput = document.querySelector('input[name="TotalWeight"]');
                if (totalWeightInput) {
                    totalWeightInput.value = totalWeight;
                }
            });

        });
    });
});
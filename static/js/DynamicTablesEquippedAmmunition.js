// DynamicTablesEquippedAmmunition.js

document.addEventListener('DOMContentLoaded', function() {
	// Получаем все таблицы с классом "inventory"
	const tables = document.querySelectorAll('.EquippedAmmunition');

	tables.forEach(table => {
		const addRowButton = table.querySelector('span');
		addRowButton.addEventListener('click', function(event) {
			event.preventDefault(); // Предотвращаем переход по ссылке

			const items = JSON.parse(table.getAttribute('data-items-Ammunition'));
			const tableBody = table.querySelector('tbody');
			const row = document.createElement('tr');

			// Создаем ячейки для каждой колонки
			const cell1 = document.createElement('td');
			const cell2 = document.createElement('td');
			const cell3 = document.createElement('td');
			const cell4 = document.createElement('td');
			const cell5 = document.createElement('td'); // Добавляем ячейку для удаления

			// Добавляем элемент span для удаления строки
			const divDeleteSpan = document.createElement('div');
			divDeleteSpan.className = "Blok-delete-row"
			const deleteSpan = document.createElement('span');
			deleteSpan.textContent = '🗑️';
			deleteSpan.className = 'delete-row';
			divDeleteSpan.appendChild(deleteSpan);
			cell5.appendChild(divDeleteSpan);

			// Добавляем всплывающий список в первую ячейку
			const dropdown1 = document.createElement('div');
			dropdown1.className = 'dropdown single-select';
			dropdown1.dataset.type = 'single';
			dropdown1.dataset.fixed = 'false';

			const hiddenInput = document.createElement('input');
			hiddenInput.type = 'hidden';
			hiddenInput.className = 'values-input class-select';
			hiddenInput.name = 'EquippedAmmunition';
			hiddenInput.id = 'EquippedAmmunition';
			hiddenInput.placeholder = 'Выберете предмет...';
			hiddenInput.readOnly = true;
			hiddenInput.value = '';
			dropdown1.appendChild(hiddenInput);

			// Новое скрытое поле для хранения категории
			const categoryHiddenInput = document.createElement('input');
			categoryHiddenInput.type = 'hidden';
			categoryHiddenInput.className = 'categories-input';            // Новая категория
			categoryHiddenInput.name = 'EquippedAmmunition';               // Имя поля
			categoryHiddenInput.id = 'EquippedAmmunition';                 // Идентификатор
			categoryHiddenInput.readOnly = true;
			categoryHiddenInput.value = '';                                 // Изначально пустое
			dropdown1.appendChild(categoryHiddenInput);                     // Добавляем скрытое поле

			const textInput = document.createElement('input');
			textInput.type = 'text';
			textInput.className = 'texts-input';
			textInput.id = 'EquippedAmmunitionPrint';
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
			input2.type = 'text';
			input2.placeholder = 'Тип снаряжения';
			input2.name = 'AmmunitionTypePrint';
			cell2.appendChild(input2);

			const input4 = document.createElement('input');
			input4.type = 'text';
			input4.placeholder = 'Вид снаряжения';
			input4.name = 'AmmunitionType';
			cell3.appendChild(input4);

			const input3 = document.createElement('input');
			input3.type = 'checkbox';
			input3.name = 'Setting';
			input3.className = "interactivElement";
			input3.placeholder = 'Требуется растройка';
			cell4.appendChild(input3);

			// Добавляем ячейки в строку
			row.appendChild(cell5); // Ячейка с кнопкой удаления
			row.appendChild(cell1);
			row.appendChild(cell3);
			row.appendChild(cell2);
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
						input2.value = selectedItem.CategoryName;
						input4.value = selectedItem.Category;
						textInput.value = selectedItem.Name;
						hiddenInput.value = selectedItem.id;

						// Устанавливаем категорию в новом скрытом поле
						categoryHiddenInput.value = selectedItem.Category; // Присваиваем категорию
					}
				}
			});

			// Обработчик кликов для удаления строки
			deleteSpan.addEventListener('click', function() {
				row.remove();
			});

		});
	});
});
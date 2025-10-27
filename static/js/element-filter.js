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

		// Обновляем отображаемые опции при загрузке страницы
		const initialParentValue = parentField.value;
		console.log('Initial parent value:', initialParentValue);
		childOptions.forEach(option => {
			const parentId = option.getAttribute('data-parent-id');
			if (parentId === initialParentValue) {
				option.style.display = '';
			}
		});

		// Обработчик кликов по элементам списка родительского выпадающего списка
		const parentOptions = parentField.querySelectorAll('.dropdown-content ul li');
		parentOptions.forEach(option => {
			option.addEventListener('click', () => {
				const selectedParentValue = option.getAttribute('data-value');

				// Обновляем отображаемые опции
				childOptions.forEach(childOption => {
					const parentId = childOption.getAttribute('data-parent-id');
					console.log('Child option parent ID:', parentId);
					if (parentId === selectedParentValue) {
						childOption.style.display = '';
					} else {
						childOption.style.display = 'none';
					}
				});

				// Сбрасываем значения зависимых полей
				relatedFields.forEach(field => field.value = '');
			});
		});
	});
});
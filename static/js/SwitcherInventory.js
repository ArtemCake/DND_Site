// SwitcherInventory.js

document.addEventListener('DOMContentLoaded', () => {
	// Получаем доступ к переключателю и обеим таблицам
	const toggleBtn = document.getElementById('inventory_Ammunition');
	const EquippedAmmunitionBlock = document.querySelector('.EquippedAmmunition');
	const inventoryBlock = document.querySelector('.inventory');
	const labelLeft = document.querySelector('.tables-center .label-left');
	const labelRight = document.querySelector('.tables-center .label-right');

	// Функция переключения видимости
	function switchTables() {
		if (toggleBtn.checked) {
			EquippedAmmunitionBlock.classList.add('hide');      // Скрываем таблицу
			inventoryBlock.classList.remove('hide');    // Показываем таблицу
			// Меняем активный статус надписей
			labelLeft.classList.remove('active-label');
			labelRight.classList.add('active-label');
		} else {
			EquippedAmmunitionBlock.classList.remove('hide');   // Показываем таблицу
			inventoryBlock.classList.add('hide');       // Скрываем таблицу
			// Меняем активный статус надписей
			labelLeft.classList.add('active-label');
			labelRight.classList.remove('active-label');
		}
	}

	// Присваиваем обработчик события клика
	toggleBtn.addEventListener('click', switchTables);
});
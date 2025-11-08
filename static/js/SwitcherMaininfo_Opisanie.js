// SwitcherMaininfo_Opisanie.js

document.addEventListener('DOMContentLoaded', () => {
	// Получаем доступ к переключателю и обеим таблицам
	const toggleBtn = document.getElementById('MainInfo');
	const MainDateBlock = document.querySelector('.MainDate-blok');
	const OpisanieBlock = document.querySelector('.Opisanie-blok');
	const labelLeft = document.querySelector('.tables-left .label-left');
	const labelRight = document.querySelector('.tables-left .label-right');

	// Функция переключения видимости
	function switchTables() {
		if (toggleBtn.checked) {
			MainDateBlock.classList.add('hide');      // Скрываем таблицу
			OpisanieBlock.classList.remove('hide');    // Показываем таблицу
			// Меняем активный статус надписей
			labelLeft.classList.remove('active-label');
			labelRight.classList.add('active-label');
		} else {
			MainDateBlock.classList.remove('hide');   // Показываем таблицу
			OpisanieBlock.classList.add('hide');       // Скрываем таблицу
			// Меняем активный статус надписей
			labelLeft.classList.add('active-label');
			labelRight.classList.remove('active-label');
		}
	}

	// Присваиваем обработчик события клика
	toggleBtn.addEventListener('click', switchTables);
});
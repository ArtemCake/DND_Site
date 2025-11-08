// SwitcherSkills_Spass.js

document.addEventListener('DOMContentLoaded', () => {
	// Получаем доступ к переключателю и обеим таблицам
	const toggleBtn = document.getElementById('Spass_Skill');
	const skillsBlock = document.querySelector('.Skills-blok');
	const spassBlock = document.querySelector('.Spass-blok');
	const labelLeft = document.querySelector('.tables-right .label-left');
	const labelRight = document.querySelector('.tables-right .label-right');

	// Функция переключения видимости
	function switchTables() {
		if (toggleBtn.checked) {
			skillsBlock.classList.add('hide');      // Скрываем таблицу навыков
			spassBlock.classList.remove('hide');    // Показываем таблицу спасбросков
			// Меняем активный статус надписей
			labelLeft.classList.remove('active-label');
			labelRight.classList.add('active-label');
		} else {
			skillsBlock.classList.remove('hide');   // Показываем таблицу навыков
			spassBlock.classList.add('hide');       // Скрываем таблицу спасбросков
			// Меняем активный статус надписей
			labelLeft.classList.add('active-label');
			labelRight.classList.remove('active-label');
		}
	}

	// Присваиваем обработчик события клика
	toggleBtn.addEventListener('click', switchTables);
});
// MasteryrCalculation.js

import { calculateSkills } from './CharacteristicSkillsCalculation.js';

document.addEventListener('DOMContentLoaded', () => {
	// Проверка наличия jQuery
	if (typeof $ === 'undefined') {
		console.error('jQuery не загружена. Скрипт не будет выполнен.');
		return;
	}
	const levelPers = document.querySelectorAll('#LevelPersonages');
	if (!levelPers) {
		console.error('Элементы для расчёта мастерства не найдены.');
		return;
	}
	// Функция для расчёта модификаторов
	function MasteryrCalculation() {
		const MasteryInput = $('#Mastery-block input[name="Mastery"]');
		MasteryInput.val(1 + Math.ceil(levelPers[0].value*0.25));
	}

	// Регистрация обработки событий
	$('input[name="LevelPersonages"]').on('change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		MasteryrCalculation();
		calculateSkills();
	});

	// Изначально вычисляем модификаторы и навыки при загрузке страницы
	MasteryrCalculation();
	calculateSkills();
});
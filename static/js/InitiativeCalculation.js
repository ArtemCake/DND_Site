// InitiativeCalculation.js.js

document.addEventListener('DOMContentLoaded', () => {
	// Проверка наличия jQuery
	if (typeof $ === 'undefined') {
		console.error('jQuery не загружена. Скрипт не будет выполнен.');
		return;
	}
	const dexterityMod = document.querySelectorAll('input[data-Initiative-param]');
	if (!dexterityMod) {
		console.error('Элементы для расчёта пассивного внимания не найдены.');
		return;
	}
	// Функция для расчёта модификаторов
	function InitiativeCalculation() {
		const Initiative = $('#Initiative-block input[name="Initiative"]');
		var value = dexterityMod[0].value;
		Initiative.val(-5 + Math.floor(0.5 * Number(value)));
	}

	// Регистрация обработки событий
	dexterityMod.forEach(function(element) {
		element.addEventListener('change', InitiativeCalculation); // Запускаем пересчет при завершении редактирования поля
	});

	// Изначально вычисляем пассивное внимание и навыки при загрузке страницы
	InitiativeCalculation();
});
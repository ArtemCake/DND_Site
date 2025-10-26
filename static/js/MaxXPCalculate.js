document.addEventListener('DOMContentLoaded', function() {
	// Элементы списка классов
	const classesListItems = document.querySelectorAll('#classes-list li[data-BoneHealth]');
	// Поле для опыта героя
	const experienceField = document.querySelector('input[data-MaxXP-param]');
	// Поле для отображения максимального здоровья
	const maxHpField = document.getElementById('MaxHP');

	// Обработчик для подсчета Maximum Health
	function calculateMaxHealth() {
		// Получаем опыт героя
		const xp = parseFloat(experienceField.value) || 0;

		// Находим текущий выбранный класс (если ни один не выбран, берём первый по умолчанию)
		const selectedClassItem = document.querySelector('#classes-list li.selected') ||
		classesListItems[0]; // Обратите внимание, объявили переменную внутри функции!

		// Извлекаем число из атрибута data-BoneHealth
		const match = selectedClassItem.dataset.bonehealth.match(/\d+/);
		const boneHealth = match ? parseFloat(match[0]) : 0;

		// Рассчитываем максимальное здоровье
		const maxHealth = boneHealth + xp;
		maxHpField.value = maxHealth.toFixed(0); // Округляем до целого числа
	}

	// Назначаем обработчик кликов на выбор класса
	classesListItems.forEach(item => {
		item.addEventListener('click', function(event) {
			// Очищаем ранее выделенный класс
			document.querySelector('#classes-list li.selected')?.classList.remove('selected');
			// Выделяем текущий класс
			event.target.classList.add('selected');
			// Пересчитываем здоровье
			calculateMaxHealth();
		});
	});

	// Следим за изменениями в поле опыта
	experienceField.addEventListener('input', calculateMaxHealth);

	// Первичное заполнение при загрузке страницы
	calculateMaxHealth();
});
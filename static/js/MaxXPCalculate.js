//MaxXPCalculate.js

document.addEventListener('DOMContentLoaded', function() {
	// Поле для опыта героя
	const experienceField = document.querySelector('input[data-MaxXP-param]');
	// Поле для отображения максимального здоровья
	const maxHpField = document.getElementById('MaxHP');
	const HpField = document.getElementById('HP');
	// Элементы списка классов
	const classesListItems = document.querySelectorAll('#classes-list li[data-BoneHealth]');

	// Обработчик для подсчета Maximum Health
	function calculateMaxHealth() {
		// Получаем опыт героя
		const xp = parseFloat(experienceField.value) || 0;

		// Находим текущий выбранный класс (если ни один не выбран, берем первый по умолчанию)
		let selectedClassItem = document.querySelector('#classes-list li.selected');

		// Проверяем, существует ли selectedClassItem, чтобы избежать ошибки
		if (selectedClassItem) {
			// Извлекаем число из атрибута data-BoneHealth
			const match = selectedClassItem.dataset.bonehealth.match(/\d+/);
			const boneHealth = match ? parseFloat(match[0]) : 0;

			// Рассчитываем максимальное здоровье
			const maxHealth = boneHealth + xp;
			maxHpField.value = maxHealth.toFixed(0); // Округляем до целого числа
			HpField.value = maxHealth.toFixed(0);
		} else {
			// Если класс не выбран, оставляем значение MaxHP пустым или устанавливаем нулевое значение
			maxHpField.value = "";
			HpField.value = "";
		}
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
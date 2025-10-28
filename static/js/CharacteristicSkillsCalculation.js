// CharacteristicSkillsCalculation.js
import { PassivAttentionCalculation } from './PassivAttentionCalculation.js';

// Основной цикл расчёта навыков
export function calculateSkills() {
	const characteristicsInputs = $('.CharacteristicsValue input[name="CharacteristicsValue"]');
	if (characteristicsInputs.length === 0) {
		console.error('Элементы для расчёта модификаторов не найдены.');
		return;
	}

	characteristicsInputs.each(function() {
		const characteristicId = $(this).siblings('.ParamId').val(); // ID характеристики
		const characteristicValue = parseFloat($(this).val());       // Значение характеристики

		if (isNaN(characteristicValue)) {
			console.error('Некорректное значение характеристики:', $(this).attr('name'), characteristicValue);
			return;
		}

		// Модификатор характеристики
		const modifier = -5 + Math.floor(0.5 * characteristicValue);

		// Находим связанные навыки и определяем коэффициент владения
		const relatedSkills = $('.SkillValue input[name="SkillValue"]')
			.filter(function() {
			return $(this).parent().find('.ParamId').val() === characteristicId;
		});

		relatedSkills.each(function() {
			const possessionCheckbox = $(this).parent().find('input[name="SkillPossession"]');
			const isProficient = possessionCheckbox.prop('checked');
			const masteryValue = Number($('#Mastery-block input[name="Mastery"]').val());

			// Применяем формулу исходя из статуса владения навыком
			let skillValue = isProficient
			? 1 * masteryValue + modifier
			: 0 * masteryValue + modifier;

			$(this).val(skillValue);
		});
	});
}

document.addEventListener('DOMContentLoaded', () => {
	// Проверка наличия jQuery
	if (typeof $ === 'undefined') {
		console.error('jQuery не загружена. Скрипт не будет выполнен.');
		return;
	}

	// Обработчики событий
	$('.CharacteristicsValue input[name="CharacteristicsValue"]').on('input change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		calculateSkills();
		PassivAttentionCalculation();
	});

	$('#Mastery-block input[name="Mastery"]').on('input change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		calculateSkills();
		PassivAttentionCalculation();
	});

	$('.SkillValue input[name="SkillPossession"]').on('change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		calculateSkills();
		PassivAttentionCalculation();
	});

	// Изначально вычисляем навыки при загрузке страницы
	calculateSkills();
	PassivAttentionCalculation();
});
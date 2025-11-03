// CharacteristicSpassCalculation.js

// Основной цикл расчёта навыков
export function calculateSpass() {
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
		const relatedSpass = $('.SpassValue input[name="SpassValue"]')
			.filter(function() {
			return $(this).parent().find('.ParamId').val() === characteristicId;
		});

		const relatedSpasschar = $('.SpassCharacteristicsValue input[name="CharacteristicId"]')
			.filter(function() {
			return $(this).parent().find('.ParamId').val() === characteristicId;
		});

		console.log(relatedSpasschar[0]);
		var skillValue = 0;
		relatedSpasschar.each(function() {
			const possessionCheckbox = $('.SkillPossession').filter(function() {
				return $(this).parent().find('.ParamId').val() === characteristicId;
			});
			const MasteryCheckbox = $('.SkillMastery').filter(function() {
				return $(this).parent().find('.ParamId').val() === characteristicId;
			});
			const isProficient = possessionCheckbox.prop('checked');
			const isMasteryient = MasteryCheckbox.prop('checked');
			const masteryValue = Number($('#Mastery-block input[name="Mastery"]').val());

			// Применяем формулу исходя из статуса владения навыком
			if (!isProficient){
				possessionCheckbox[0].checked   = false;
				MasteryCheckbox[0].checked      = false;
				skillValue = 0 * masteryValue + modifier;
			} else if (!isMasteryient){
				skillValue = 1 * masteryValue + modifier;
			} else {
				skillValue = 2 * masteryValue + modifier;
			};
		});
		relatedSpass.val(skillValue);
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
		calculateSpass();
	});

	$('#Mastery-block input[name="Mastery"]').on('input change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		calculateSpass();
	});

	$('.SkillPossession').on('change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		calculateSpass();
	});

	$('.SkillMastery').on('change', function() {
		console.log('Обработчик вызван для:', $(this).attr('name'));
		calculateSpass();
	});

	// Изначально вычисляем навыки при загрузке страницы
	calculateSpass();
});
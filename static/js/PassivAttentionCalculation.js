// PassivAttentionCalculation.js

// Функция для расчёта модификаторов
export function PassivAttentionCalculation() {
	const PassivAttention = $('#PassivAttentionField input[name="PassivAttention"]');
	const Attention = document.querySelectorAll('input[data-attention-param]');
	if (!Attention) {
		console.error('Элементы для расчёта пассивного внимания не найдены.');
		return;
	}
	var result = 10 + Number(Attention[0].value);
	PassivAttention.val(result);

}

document.addEventListener('DOMContentLoaded', () => {
	// Проверка наличия jQuery
	if (typeof $ === 'undefined') {
		console.error('jQuery не загружена. Скрипт не будет выполнен.');
		return;
	}

	// Регистрация обработки событий
	document.querySelectorAll('input[data-attention-param]').forEach(function(el) {
		el.addEventListener('change', PassivAttentionCalculation); // Запускаем пересчет при завершении редактирования поля
	});

	// Изначально вычисляем пассивное внимание и навыки при загрузке страницы
	PassivAttentionCalculation();
});
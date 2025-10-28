// ChekedSettingsAmunition.js

document.addEventListener('DOMContentLoaded', () => {
	const container = document.querySelector('.EquippedAmmunition');

	// Функция для отображения временного сообщения
	function flashMessage(message) {
		const toast = document.getElementById('flash-message');
		toast.innerText = message;
		toast.style.opacity = '1';
		toast.style.display = 'block';
		setTimeout(() => {
			toast.style.opacity = '0';
			setTimeout(() => toast.style.display = 'none', 500);
		}, 3000);
	}

	// Обработчик событий на контейнере
	container.addEventListener('click', function(e) {
		if (e.target.matches('input[name="Setting"]')) {
			const checkedCount = document.querySelectorAll('input[name="Setting"]:checked').length;
			if (checkedCount > 3 && e.target.checked) {
				e.preventDefault(); // Останавливаем действие по умолчанию
				flashMessage('Максимум можно быть настроенным на 3 предмета'); // Показываем временную надпись
			}
		}
	});
});
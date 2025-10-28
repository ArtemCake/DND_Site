// MaxWeightCalculate.js

document.addEventListener('DOMContentLoaded', function() {
    // Начинаем исполнение кода только после полной загрузки страницы

    // Получаем элементы с атрибутом data-maxweight-param
    const elementsToWatch = document.querySelectorAll('[data-maxweight-param]');
	const outputElement = document.querySelector('input[name="MaxWeight"]'); // Поле для вывода результата

    // Если нужных элементов нет, выводим предупреждение в консоль
    if(elementsToWatch.length === 0 || !outputElement) {
        console.warn('Внимание! Необходимые элементы для расчёта не найдены.');
        return;
    }

    // Обработчик для пересчета итогового значения
    function recalculateResult() {
        let totalSum = 0;

        elementsToWatch.forEach(function(el) {
            const currentVal = el.value.trim(); // Удаляем лишние пробелы
            if(currentVal !== '' && !isNaN(parseFloat(currentVal))) {
                totalSum += parseFloat(currentVal); // Суммируем валидные значения
            }
        });

        // Ваша формула расчета итогового значения
        const finalResult = Math.round(totalSum * 15); // Измените формулу при необходимости

        // Выводим результат в поле вывода
        outputElement.value = finalResult;
    }

    // Присваиваем обработчик события change каждому элементу
    elementsToWatch.forEach(function(el) {
        el.addEventListener('change', recalculateResult); // Запускаем пересчет при завершении редактирования поля
    });

    // Первый расчет при загрузке страницы
    recalculateResult();
});
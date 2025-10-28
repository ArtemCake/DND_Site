// CharacteristicModificatorCalculation.js

document.addEventListener('DOMContentLoaded', () => {
    // Проверка наличия jQuery
    if (typeof $ === 'undefined') {
        console.error('jQuery не загружена. Скрипт не будет выполнен.');
        return;
    }

    // Функция для расчёта модификаторов
    function calculateModifiers() {
        const characteristicsInputs = $('.CharacteristicsValue input[name="CharacteristicsValue"]');
        if (characteristicsInputs.length === 0) {
            console.error('Элементы для расчёта модификаторов не найдены.');
            return;
        }
        characteristicsInputs.each(function() {
            const characteristicId = $(this).siblings('.ParamId').val(); // ID характеристики
            const value = parseFloat($(this).val());                      // Значение характеристики

            if (isNaN(value)) {
                console.error('Некорректное значение характеристики:', $(this).attr('name'), value);
                return;
            }

            // Формула расчёта модификатора
            const modifier = -5 + Math.floor(0.5 * value);
            // Находим соответствующий модификатор и устанавливаем новое значение
            $('.CharacteristicsModificator input[name="CharacteristicsModificator"]')
                .filter(function() {
                    return $(this).siblings('.ParamId').val() === characteristicId;
                })
                .val(modifier);

        });
    }

    // Регистрация обработки событий
    $('.CharacteristicsValue input[name="CharacteristicsValue"]').on('input change', function() {
        console.log('Обработчик вызван для:', $(this).attr('name'));
        calculateModifiers();
    });


    // Изначально вычисляем модификаторы и навыки при загрузке страницы
    calculateModifiers();
});
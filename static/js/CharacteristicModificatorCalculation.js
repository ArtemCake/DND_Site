// CharacteristicModificatorCalculation.js

document.addEventListener('DOMContentLoaded', () => {
    // Функция для расчёта модификаторов
    function calculateModifiers() {
        $('.CharacteristicsValue input[name="CharacteristicsValue"]').each(function() {
            const characteristicId = $(this).siblings('.ParamId').val(); // ID характеристики
            const value = parseFloat($(this).val());                      // Значение характеристики

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
    $('.CharacteristicsValue input[name="CharacteristicsValue"]').on('input change', calculateModifiers);

    // Изначально вычисляем модификаторы при загрузке страницы
    calculateModifiers();
});
// Обработчик события DOMContentLoaded
if (window.jQuery) {
    // Убедились, что jQuery доступна
    $(document).ready(function() {
document.addEventListener('DOMContentLoaded', () => {
    // Подождём полную загрузку DOM и убедимся, что jQuery доступна

    // Функция для расчёта модификаторов
    function calculateModifiers() {
        $('.CharacteristicsValue input[name="CharacteristicsValue"]').each(function() {
            var characteristicId = $(this).siblings('.ParamId').val(); // ID характеристики
            var value = parseFloat($(this).val());                      // Значение характеристики

            // Формула расчёта модификатора
            var modifier = -5 + Math.floor(0.5 * value);

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
    });
} else {
    console.error("jQuery не найдена!");
}
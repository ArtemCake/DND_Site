// healthCalculator.js

// Ждём загрузки DOM
document.addEventListener('DOMContentLoaded', function() {
    // Тело нашего скрипта начинается отсюда

    // Связываем элементы с DOM
    const maxHealthInput = document.querySelector('input[name="MaxHP"]');
    const tempHealthInput = document.querySelector('input[name="TimedHP"]');
    const damageInput = document.querySelector('input[name="Damage"]');
    const currentHealthOutput = document.querySelector('input[name="HP"]');

    // Проверим, найдены ли элементы
    if (!maxHealthInput || !tempHealthInput || !damageInput || !currentHealthOutput) {
        console.error('Один или несколько элементов не найдены');
        return;
    }

    // Функция для пересчета текущего здоровья
    function recalculateCurrentHealth() {
        // Проверим, вызвали ли события (для диагностики)
        console.log('Function called');

        // Получаем введённые значения
        const maxHealth = parseFloat(maxHealthInput.value) || 0;
        const tempHealth = parseFloat(tempHealthInput.value) || 0;
        const damage = parseFloat(damageInput.value) || 0;

        // Посмотрим полученные значения (для диагностики)
        console.log('Max HP:', maxHealth);
        console.log('Temp HP:', tempHealth);
        console.log('Damage:', damage);

        // Вычислим текущее здоровье
        const currentHealth = Math.max(0, maxHealth + tempHealth - damage);

        // Установим новое значение в поле текущего здоровья
        currentHealthOutput.value = currentHealth.toFixed(0); // Округляем до целых
    }

    // Присвоим обработчики событий
    maxHealthInput.addEventListener('input', recalculateCurrentHealth);
    tempHealthInput.addEventListener('input', recalculateCurrentHealth);
    damageInput.addEventListener('input', recalculateCurrentHealth);

    // Первоначально пересчитаем здоровье при загрузке страницы
    recalculateCurrentHealth();
});
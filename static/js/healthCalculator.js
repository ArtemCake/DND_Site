// healthCalculator.js

document.addEventListener('DOMContentLoaded', () => {
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
        // Получаем введённые значения
        const maxHealth = parseFloat(maxHealthInput.value) || 0;
        const tempHealth = parseFloat(tempHealthInput.value) || 0;
        const damage = parseFloat(damageInput.value) || 0;

        // Проверка корректности ввода
        if (isNaN(maxHealth) || isNaN(tempHealth) || isNaN(damage)) {
            alert('Введите корректные численные значения!');
            return;
        }

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
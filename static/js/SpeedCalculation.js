// SpeedCalculation.js

document.addEventListener('DOMContentLoaded', () => {
    // Связываем элементы с DOM
    const raceSelect = document.querySelector('#Race');
    const bonusesContainers = document.querySelectorAll('.bonuses-dropdown');
    const outputFields = {
        walk: document.getElementById('Speed'),
        fly: document.getElementById('Fly'),
        swim: document.getElementById('Swim'),
        climb: document.getElementById('Climb')
    };

    // Проверим наличие всех элементов
    if (!raceSelect || !bonusesContainers.length || Object.values(outputFields).some(f => !f)) {
        console.error('Один или несколько элементов не найдены');
        return;
    }

    // Основная функция расчета скоростей
    function updateSpeeds() {
        const raceItem = raceSelect.value;
        const bonuses = aggregateBonuses(bonusesContainers);
        const finalSpeeds = calculateFinalSpeeds(raceItem, bonuses);

        // Обновляем поля с результатами
        outputFields.walk.value = finalSpeeds.walk;
        outputFields.fly.value = finalSpeeds.fly;
        outputFields.swim.value = finalSpeeds.swim;
        outputFields.climb.value = finalSpeeds.climb;
    }

    // Функция агрегации бонусов
    function aggregateBonuses(elements) {
        const bonuses = { walk: 0, fly: 0, swim: 0, climb: 0 };

        elements.forEach(container => {
            const selectedOption = container.querySelector('.dropdown-content ul li.selected');
            if (selectedOption) {
                bonuses.walk += parseFloat(selectedOption.dataset.bonusSpeed) || 0;
                bonuses.fly += parseFloat(selectedOption.dataset.bonusFly) || 0;
                bonuses.swim += parseFloat(selectedOption.dataset.bonusSwim) || 0;
                bonuses.climb += parseFloat(selectedOption.dataset.bonusClimb) || 0;
            }
        });

        return bonuses;
    }

    // Функция расчета финальной скорости
    function calculateFinalSpeeds(raceItem, bonuses) {
        const raceData = getRaceData(raceItem);
        const finalSpeeds = {
            walk: applyBonusToBase(raceData.speed, bonuses.walk),
            fly: applyBonusToBase(raceData.fly, bonuses.fly),
            swim: applyBonusToBase(raceData.swim, bonuses.swim),
            climb: applyBonusToBase(raceData.climb, bonuses.climb)
        };

        return finalSpeeds;
    }

    // Функция получения данных расы
    function getRaceData(value) {
        const races = document.querySelectorAll('#Race ~ .dropdown-content ul li');
        for (const race of races) {
            if (race.dataset.value === value) {
                return {
                    speed: parseFloat(race.dataset.speed) || 0,
                    fly: parseFloat(race.dataset.fly) || 0,
                    swim: parseFloat(race.dataset.swim) || 0,
                    climb: parseFloat(race.dataset.climb) || 0
                };
            }
        }
        return {};
    }

    // Функция применения бонуса к базовым характеристикам
    function applyBonusToBase(base, bonus) {
        if (base === undefined || base === null || base === "") {
            return Math.max(parseFloat(bonus), 0);
        }
        return Math.max(parseFloat(base) + parseFloat(bonus), 0);
    }

    // Вызов при загрузке страницы
    updateSpeeds();

    // Реакция на изменения формы
    raceSelect.addEventListener('change', updateSpeeds);
    bonusesContainers.forEach(container => {
        container.addEventListener('change', updateSpeeds);
    });
});
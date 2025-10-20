// calculator.js

// Функция расчета скоростей
function updateSpeeds() {
    const raceItem = document.querySelector('#Race').value; // Выбираем выбранную расу
    const bonusesElements = document.querySelectorAll('.bonuses-dropdown'); // Берём все блоки бонусов
    const finalSpeeds = calculateFinalSpeeds(raceItem, bonusesElements);

    // Обновляем поля с результатами
    document.getElementById('Speed').value = finalSpeeds.walk;
    document.getElementById('Fly').value = finalSpeeds.fly;
    document.getElementById('Swim').value = finalSpeeds.swim;
    document.getElementById('Climb').value = finalSpeeds.climb;
}

// Основная функция расчета итоговых скоростей
function calculateFinalSpeeds(raceItem, bonusesElements) {
    const raceData = getRaceData(raceItem); // Получаем базовые скорости расы
    const bonusesSum = aggregateBonuses(bonusesElements); // Суммируем бонусы всех блоков

    // Общая формула расчета
    const finalSpeeds = {
        walk: applyBonusToBase(raceData.speed, bonusesSum.walk),
        fly: applyBonusToBase(raceData.fly, bonusesSum.fly),
        swim: applyBonusToBase(raceData.swim, bonusesSum.swim),
        climb: applyBonusToBase(raceData.climb, bonusesSum.climb)
    };

    return finalSpeeds;
}

// Получение данных расы
function getRaceData(value) {
    const races = document.querySelectorAll('#Race ~ .dropdown-content ul li');
    for (const race of races) {
        if (race.dataset.value === value) {
            return {
                speed: parseFloat(race.dataset.speed),
                fly: parseFloat(race.dataset.fly),
                swim: parseFloat(race.dataset.swim),
                climb: parseFloat(race.dataset.climb)
            };
        }
    }
    return {};
}

// Агрегация бонусов
function aggregateBonuses(elements) {
    const bonuses = { walk: 0, fly: 0, swim: 0, climb: 0 };

    elements.forEach(element => {
        const bonusesInput = element.querySelector('.dropdown-content ul li.selected');
        if (bonusesInput) {
            bonuses.walk += parseFloat(bonusesInput.dataset.bonusSpeed) || 0;
            bonuses.fly += parseFloat(bonusesInput.dataset.bonusFly) || 0;
            bonuses.swim += parseFloat(bonusesInput.dataset.bonusSwim) || 0;
            bonuses.climb += parseFloat(bonusesInput.dataset.bonusClimb) || 0;
        }
    });

    return bonuses;
}

// Новое правило применения бонуса: если у расы нет данной характеристики, то берем сам бонус
function applyBonusToBase(base, bonus) {
    // Если базовая характеристика не указана у расы, принимаем бонус как отдельную величину
    if (base === "" || typeof base === 'undefined' || base === null) {
        return Math.max(parseFloat(bonus), 0);
    }
    return Math.max(parseFloat(base) + parseFloat(bonus), 0);
}
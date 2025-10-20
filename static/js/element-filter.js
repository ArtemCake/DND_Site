// element-filter.js

document.addEventListener('DOMContentLoaded', () => {
    // 1. Собираем ключевые элементы
    const keys = document.querySelectorAll('[data-param-id]');

    keys.forEach(keyEl => {
        const paramId = keyEl.getAttribute('data-param-id');
        const delay = parseInt(keyEl.getAttribute('data-delay')) || 0; // Задержка перед изменениями
        const hideUnmatched = keyEl.hasAttribute('data-hide-unmatched'); // Признак скрытия неподходящих элементов

        // 2. Определяем зависимые элементы
        const relatedDeps = document.querySelectorAll(`input.CharacteristicId[value="${paramId}"]`);

        if (relatedDeps.length === 0) {
            console.warn(`Нет зависимых элементов для ключа "${paramId}".`);
            return;
        }

        // 3. Устанавливаем начальное состояние
        showRelated(relatedDeps, hideUnmatched);

        // 4. Реакция на изменения значения ключевого элемента
        keyEl.addEventListener('change', () => {
            setTimeout(() => {
                showRelated(relatedDeps, hideUnmatched);
            }, delay);
        });
    });
});

// Вспомогательная функция для показа/сокрытия зависимых элементов
function showRelated(elements, hideUnmatched) {
    elements.forEach(el => {
        el.closest('[data-dependent-on]').style.display = ''; // Показываем подходящие элементы

        if (hideUnmatched) {
            const container = el.closest('[data-dependent-on]');
            const siblings = [...container.parentNode.children].filter(child =>
                child !== container && child.matches('[data-dependent-on]')
            );
            siblings.forEach(sibling => sibling.style.display = 'none'); // Прячем неподходящие
        }
    });
}
//element-filter.js

document.addEventListener('DOMContentLoaded', function() {
    // 2. Теперь берем ключевые элементы и ищем зависимые элементы
    const keys = document.querySelectorAll('[data-param-id]');
    keys.forEach(keyEl => {
        const paramId = keyEl.getAttribute('data-param-id');

        // Находим все зависимые элементы, чьи значения скрытых полей совпадают с нашим key
        const relatedDeps = document.querySelectorAll(`input[class="CharacteristicId"][value="${paramId}"]`);

        // Просматриваем список найденных зависимых элементов и показываем их
        relatedDeps.forEach(dep => dep.closest('[data-dependent-on]').style.display = '');
    });
});
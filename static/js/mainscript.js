// app.js
import { loadExternalLibraries } from './external-libraries.js';

// Загрузка внешних библиотек
loadExternalLibraries()
    .then(() => {
        console.log('Внешние библиотеки загружены успешно.');
        // Здесь можно разместить код, который зависит от внешних библиотек
    })
    .catch((error) => {
        console.error('Ошибка при загрузке внешних библиотек:', error);
    });
import'./external-libraries.js';            // Загрузка внешних библиотек
import './password-toggle.js';              // Подключение модуля управления видимостью паролей
import './form-switcher.js';                // Модуль переключения форм
import './dropdown.js';                     // Выпадающие списки
import './form-submission.js';              // Управление формой отправки
import './forms.js';                        // Управление формами
import './dialog-controller.js';            // Контроль диалогового окна
import './image-canvas.js';                 // Работа с изображением на холсте
import './buttons-return.js';               // Работа с кнопками возврата
import './universal_filter_script.js';      // Работа со связанными списками
import './element-filter.js';               // Работа фильтр значений для связанных объектов
import './SpeedCalculation.js';             // Расчёт скоростей перстонажа
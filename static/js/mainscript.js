// mainscript.js
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
import'https://code.jquery.com/jquery-3.6.0.min.js';
import'./external-libraries.js';                    // Загрузка внешних библиотек
import './password-toggle.js';                      // Подключение модуля управления видимостью паролей
import './form-switcher.js';                        // Модуль переключения форм
import './dropdown.js';                             // Выпадающие списки
import './form-submission.js';                      // Управление формой отправки
import './forms.js';                                // Управление формами
import './dialog-controller.js';                    // Контроль диалогового окна
import './image-canvas.js';                         // Работа с изображением на холсте
import './buttons-return.js';                       // Работа с кнопками возврата
import './element-filter.js';                       // Работа фильтр значений для связанных объектов
import './SpeedCalculation.js';                     // Расчёт скоростей перстонажа
import './healthCalculator.js';                     // Расчёт текущего здоровья персонажа
import './CharacteristicModificatorCalculation.js'; // Расчёт модификаторов характеристик
import './DynamicTables.js';                        // Динамическое создание таблицы
import './MaxWeightCalculate.js';                   // Расчет масксимального веса исходя из силы
import './MaxXPCalculate.js';                       // Расчет масксимального здоровья при создании персонажа
import './CharacteristicSkillsCalculation.js';      // Расчёт навыков характеристик
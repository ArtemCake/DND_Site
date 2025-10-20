// mainscript.js
import { loadExternalLibraries } from './external-libraries.js';

// Список наших собственных скриптов
const internalScripts = [
    './password-toggle.js',
    './form-switcher.js',
    './dropdown.js',
    './form-submission.js',
    './forms.js',
    './dialog-controller.js',
    './image-canvas.js',
    './buttons-return.js',
    './universal_filter_script.js',
    './element-filter.js',
    './SpeedCalculation.js',
    './healthCalculator.js',
    './CharacteristicModificatorCalculation.js'
];

// Функция для загрузки скриптов
async function loadInternalScripts() {
    for (const scriptPath of internalScripts) {
        try {
            await import(scriptPath);
            console.log(`Скрипт ${scriptPath} загружен`);
        } catch (err) {
            console.error(`Ошибка при загрузке скрипта ${scriptPath}:`, err);
        }
    }
}

// Загрузка внешних библиотек
loadExternalLibraries()
    .then(async () => {
        console.log('Внешние библиотеки загружены успешно.');

        // Начинаем асинхронную загрузку внутренних скриптов
        await loadInternalScripts();
    })
    .catch((error) => {
        console.error('Ошибка при загрузке внешних библиотек:', error);
    });
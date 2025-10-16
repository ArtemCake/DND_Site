// external-libraries.js
export function loadExternalLibraries() {
    return new Promise((resolve, reject) => {
        const head = document.head || document.getElementsByTagName('head')[0];
        const firstScript = document.createElement('script');
        const secondScript = document.createElement('script');

        firstScript.src = 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js';
        firstScript.onload = () => {
            secondScript.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
            secondScript.onload = () => {
                resolve();
            };
            secondScript.onerror = () => {
                reject(new Error('Ошибка загрузки второго скрипта.'));
            };
            head.appendChild(secondScript);
        };
        firstScript.onerror = () => {
            reject(new Error('Ошибка загрузки первого скрипта.'));
        };
        head.appendChild(firstScript);
    });
}
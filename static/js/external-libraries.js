// external-libraries.js

export function loadExternalLibraries(libraries) {
    return new Promise((resolve, reject) => {
        const head = document.head || document.getElementsByTagName('head')[0];
        const totalScripts = libraries.length;
        let loadedCount = 0;

        libraries.forEach(src => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = () => {
                loadedCount++;
                if (loadedCount >= totalScripts) {
                    resolve();
                }
            };
            script.onerror = () => {
                reject(new Error(`Ошибка загрузки библиотеки ${src}`));
            };
            head.appendChild(script);
        });
    });
}

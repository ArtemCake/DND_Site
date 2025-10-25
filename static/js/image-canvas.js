// image-canvas.js

document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('imageDate');
    const imageInput = document.getElementById('image_uploads');
    const oldImageName = document.getElementById('oldimageName');

    if (!canvas || !imageInput || !oldImageName) {
        console.error('Один или несколько элементов не найдены');
        return;
    }

    const ctx = canvas.getContext('2d');
    const oldImageSrc = 'static/image/' + oldImageName.value;
    let uploadedImage = null;

    // Функция для прорисовки изображения с поддержкой масштабирования
    function drawFittingImage(image, canvasWidth, canvasHeight) {
        const aspectRatio = image.width / image.height;
        let scaledWidth = canvasWidth;
        let scaledHeight = canvasHeight;

        // Сохраняем полную площадь изображения
        if ((canvasWidth / canvasHeight) >= aspectRatio) {
            scaledWidth = canvasHeight * aspectRatio;
        } else {
            scaledHeight = canvasWidth / aspectRatio;
        }

        // Рассчитываем смещение для центрального расположения
        const xOffset = Math.floor((canvasWidth - scaledWidth) / 2);
        const yOffset = Math.floor((canvasHeight - scaledHeight) / 2);

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(image, xOffset, yOffset, scaledWidth, scaledHeight);
    }

    // Загрузка первоначального изображения
    const pic = new Image();
    pic.src = oldImageSrc;
    pic.onload = function() {
        drawFittingImage(pic, canvas.width, canvas.height);
    };

    // Обработчик загрузки файла
    imageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() {
                uploadedImage = img;
                drawFittingImage(img, canvas.width, canvas.height);
            };
        };

        reader.readAsDataURL(file);
    });
});
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

    // Рисуем изначальное изображение
    const pic = new Image();
    pic.src = oldImageSrc;
    pic.onload = function() {
        ctx.drawImage(pic, 0, 0, canvas.width, canvas.height);
    };

    // Обработка изменения файла
    imageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() {
                uploadedImage = img;
                requestAnimationFrame(redrawCanvas); // Используем анимационный кадр для плавной перерисовки
            };
        };

        reader.readAsDataURL(file);
    });

    // Перерисовка изображения на канвасе
    function redrawCanvas() {
        if (uploadedImage) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(uploadedImage, 0, 0, canvas.width, canvas.height);
        }
    }
});
// image-canvas.js

document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('imageDate');
    const imageInput = document.getElementById('image_uploads');
    const oldImageName = document.getElementById('oldimageName');

    if (!canvas || !imageInput || !oldImageName) {
        console.log('Один или несколько элементов не найдены. Скрипт не будет выполнен.');
        return;
    }

    const ctx = canvas.getContext('2d');
    const oldImageSrc = 'static/image/' + oldImageName.value;
    let uploadedImage = null;

    const pic = new Image();
    pic.src = oldImageSrc;
    pic.onload = function() {
        ctx.drawImage(this, 0, 0, canvas.width, canvas.height);
    };

    imageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() {
                uploadedImage = img;
                redrawCanvas();
            };
        };

        reader.readAsDataURL(file);
    });

    function redrawCanvas() {
        if (uploadedImage) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(uploadedImage, 0, 0, canvas.width, canvas.height);
        }
    }
});
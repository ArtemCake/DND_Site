// image-canvas.js
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('imageDate');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        const oldImageSrc = 'static/image/' + document.getElementById("oldimageName").value;
        const imageInput = document.getElementById('image_uploads');
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
    }
});
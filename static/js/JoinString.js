$(function() {
    $('input[class="checkboxUpdate"]').on('click', function() {
        var values = [];
        $('input:checked').each(function() {
            values.push($(this).val());
        });
        $('[class="hiddenUpdate"]').attr({value: values.join(', ')});
    });
});

window.onload = function(){
    const mainForm = document.getElementById('EditForm')
    mainForm.onsubmit = function(event){
    if (document.getElementById('update') != event.submitter && document.getElementById('closeOn')!= event.submitter){
    event.preventDefault();
    }
    }
};

  var dialog = document.querySelector('dialog')
  document.querySelector('#open').onclick = function () {
    dialog.showModal()
  };

  document.querySelector('#closeOn').onclick = function () {
  dialog.close()
};

  document.querySelector('#closeOff').onclick = function () {
  dialog.close()
};

const canvas = document.getElementById('imageDate');
const ctx = canvas.getContext('2d');
pic       = new Image();              // "Создаём" изображение
pic.src    = 'static/image/'+document.getElementById("oldimageName").value;  // Источник изображения, позаимствовано на хабре

const imageInput = document.getElementById('image_uploads');
let uploadedImage = null;

// Load the image onto the canvas
imageInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    const img = new Image();
    img.src = e.target.result;
    img.onload = () => {
      uploadedImage = img;
      drawImage();
    };
  };

  reader.readAsDataURL(file);
});

// Draw image and text on canvas
function drawImage() {
  if (uploadedImage) {
    // Clear canvas and set canvas dimensions to fit the image
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(uploadedImage, 0, 0, canvas.width, canvas.height);

  }
};

pic.onload = function() {    // Событие onLoad, ждём момента пока загрузится изображение
ctx.drawImage(pic, 0, 0, canvas.width, canvas.height);  // Рисуем изображение от точки с координатами 0, 0
 }




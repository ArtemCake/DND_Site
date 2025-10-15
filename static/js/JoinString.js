// Инициализация выбранных значений при загрузке страницы
document.querySelectorAll('.dropdown').forEach(dropdown => {
    const valuesInput = dropdown.querySelector('.values-input');
    const textsInput = dropdown.querySelector('.texts-input');

    // собираем предварительно выбранные элементы
    const preselectedItems = dropdown.querySelectorAll('.dropdown-content li.selected');

    // заполняем поля ввода значениями и текстами выбранных элементов
    const initialValues = [...preselectedItems].map(item => item.dataset.value);
    const initialTexts = [...preselectedItems].map(item => item.textContent);

    valuesInput.value = initialValues.join(', ').trim();
    textsInput.value = initialTexts.join(', ').trim();
});

// Универсальная обработка кликов для всех выпадающих списков
document.querySelectorAll('.dropdown-content ul').forEach((list) => {
    list.addEventListener('click', function(event) {
        const target = event.target.closest('li');

        if (!target || target.parentNode.parentNode.parentNode.classList.contains('fixed-selected')) return;

        // определяем ближайшее окружение ".dropdown" и связанные input
        const dropdownParent = target.closest('.dropdown');
        const isSingleSelect = dropdownParent.classList.contains('single-select');
        const valuesInput = dropdownParent.querySelector('.values-input');
        const textsInput = dropdownParent.querySelector('.texts-input');

        if (isSingleSelect) {
            // Режим одиночного выбора

            // очищаем выделение предыдущих элементов
            dropdownParent.querySelectorAll('.dropdown-content li').forEach(li => li.classList.remove('selected'));

            // делаем текущий элемент активным
            target.classList.add('selected');

            // обновляем поля ввода
            valuesInput.value = target.dataset.value;
            textsInput.value = target.textContent;
        } else {
            // Режим множественного выбора

            // собираем текущие выбранные значения
            let currentSelectedValues = valuesInput.value ? valuesInput.value.split(',').map(v => v.trim()) : [];
            let currentSelectedTexts = textsInput.value ? textsInput.value.split(',').map(t => t.trim()) : [];

            // проверяем наличие элемента в списке
            const indexOfTarget = currentSelectedValues.indexOf(target.dataset.value);

            if (indexOfTarget !== -1) {
                // если элемент уже выбран, удаляем его
                currentSelectedValues.splice(indexOfTarget, 1);
                currentSelectedTexts.splice(indexOfTarget, 1);
                target.classList.remove('selected');
            } else {
                // иначе добавляем элемент
                currentSelectedValues.push(target.dataset.value);
                currentSelectedTexts.push(target.textContent);
                target.classList.add('selected');
            }

            // обновляем поля ввода
            valuesInput.value = currentSelectedValues.join(', ').trim();
            textsInput.value = currentSelectedTexts.join(', ').trim();
        }
    });
});

window.onload = function() {
    const mainForm = document.getElementById('EditForm')
    if (mainForm != null) {
        mainForm.onsubmit = function(event) {
            if (document.getElementById('update') != event.submitter && document.getElementById('closeOn') != event.submitter) {
                event.preventDefault();
            };
        };
    };
};

var dialog = document.querySelector('dialog')
if (dialog != null) {
    document.querySelector('#open').onclick = function() {
        dialog.showModal()
    };

    document.querySelector('#closeOn').onclick = function() {
        dialog.close()
    };

    document.querySelector('#closeOff').onclick = function() {
        dialog.close()
    };
};

const canvas = document.getElementById('imageDate');
if (canvas != null) {
    const ctx = canvas.getContext('2d');
    pic = new Image(); // "Создаём" изображение
    pic.src = 'static/image/' + document.getElementById("oldimageName").value; // Источник изображения, позаимствовано на хабре
    console.log("13123");
    const imageInput = document.getElementById('image_uploads');
    let uploadedImage = null;
    console.log("Усп312ех");
    // Load the image onto the canvas
    imageInput.addEventListener('change', (event) => {
        console.log("1");
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = (e) => {
            console.log("2");
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
            console.log("Успех");
        };
    };

    pic.onload = function() { // Событие onLoad, ждём момента пока загрузится изображение
        ctx.drawImage(pic, 0, 0, canvas.width, canvas.height); // Рисуем изображение от точки с координатами 0, 0
        console.log("Успех");
    };
};
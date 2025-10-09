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
    if (document.getElementById('open')== event.submitter || document.getElementById('closeOff')== event.submitter){
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
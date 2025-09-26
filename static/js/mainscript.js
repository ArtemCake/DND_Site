$('body').on('click', '.password-control', function(){
	if ($('#password-input').attr('type') == 'password'){
		$(this).addClass('view');
		$('#password-input').attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$('#password-input').attr('type', 'password');
	}
});
$('body').on('click', '.password-control-1', function(){
	if ($('#password-input-1').attr('type') == 'password'){
		$(this).addClass('view');
		$('#password-input-1').attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$('#password-input-1').attr('type', 'password');
	}
});
$('body').on('click', '.password-control-2', function(){
	if ($('#password-input-2').attr('type') == 'password'){
		$(this).addClass('view');
		$('#password-input-2').attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$('#password-input-2').attr('type', 'password');
	}
	return false;
});

$('body').on('click', '.password-control-3', function(){
	if ($('#password-input-3').attr('type') == 'password'){
		$(this).addClass('view');
		$('#password-input-3').attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$('#password-input-3').attr('type', 'password');
	}
	return false;
});

$('body').on('click', '.password-control-4', function(){
	if ($('#password-input-4').attr('type') == 'password'){
		$(this).addClass('view');
		$('#password-input-4').attr('type', 'text');
	} else {
		$(this).removeClass('view');
		$('#password-input-4').attr('type', 'password');
	}
	return false;
});
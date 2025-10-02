var fields = $('#CreateCharacteristicesForm').find('input.add-to-tags, select.SkillsPrint');
fields.on('change keyup', function(){
	var tags = [];
	fields.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Skills]', '#CreateCharacteristicesForm').val(tags.join(','));
});

var fields1 = $('#CharacteristicesForm').find('input.add-to-tags, select.SkillPrint');
fields1.on('change keyup', function(){
	var tags = [];
	fields1.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Skill]', '#CharacteristicesForm').val(tags.join(','));
});
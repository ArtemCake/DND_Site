var fields = $('#CreateArchetypeForm').find('input.add-to-tags, select.PossessionArmorPrint');
fields.on('change keyup', function(){
	var tags = [];
	fields.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=PossessionArmor]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields1 = $('#CreateArchetypeForm').find('input.add-to-tags, select.GunOwnershipPrint');
fields1.on('change keyup', function(){
	var tags = [];
	fields1.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=GunOwnership]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields2 = $('#CreateArchetypeForm').find('input.add-to-tags, select.ToolOwnershipPrint');
fields2.on('change keyup', function(){
	var tags = [];
	fields2.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=ToolOwnership]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields3 = $('#CreateArchetypeForm').find('input.add-to-tags, select.SpellsPrint');
fields3.on('change keyup', function(){
	var tags = [];
	fields3.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Spells]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields4 = $('#CreateArchetypeForm').find('input.add-to-tags, select.SkillsNamePrint');
fields4.on('change keyup', function(){
	var tags = [];
	fields4.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=SkillsName]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields4 = $('#CreateArchetypeForm').find('input.add-to-tags, select.DamageResistancePrint');
fields4.on('change keyup', function(){
	var tags = [];
	fields4.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageResistance]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields5 = $('#CreateArchetypeForm').find('input.add-to-tags, select.DamageImmunityPrint');
fields5.on('change keyup', function(){
	var tags = [];
	fields5.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageImmunity]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields6 = $('#CreateArchetypeForm').find('input.add-to-tags, select.CharacteristicesPrint');
fields6.on('change keyup', function(){
	var tags = [];
	fields6.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Characteristices]', '#CreateArchetypeForm').val(tags.join(','));
});

var fields7 = $('#CreateAttributeForm').find('input.add-to-tags, select.GunOwnershipPrint');
fields7.on('change keyup', function(){
	var tags = [];
	fields7.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=GunOwnership]', '#CreateAttributeForm').val(tags.join(','));
});

var fields8 = $('#CreateAttributeForm').find('input.add-to-tags, select.ToolOwnershipPrint');
fields8.on('change keyup', function(){
	var tags = [];
	fields8.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=ToolOwnership]', '#CreateAttributeForm').val(tags.join(','));
});

var fields9 = $('#CreateAttributeForm').find('input.add-to-tags, select.SpellsPrint');
fields9.on('change keyup', function(){
	var tags = [];
	fields9.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Spells]', '#CreateAttributeForm').val(tags.join(','));
});

var fields10 = $('#CreateAttributeForm').find('input.add-to-tags, select.SkillsNamePrint');
fields10.on('change keyup', function(){
	var tags = [];
	fields10.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=SkillsName]', '#CreateAttributeForm').val(tags.join(','));
});

var fields11 = $('#CreateAttributeForm').find('input.add-to-tags, select.DamageResistancePrint');
fields11.on('change keyup', function(){
	var tags = [];
	fields11.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageResistance]', '#CreateAttributeForm').val(tags.join(','));
});

var fields12 = $('#CreateAttributeForm').find('input.add-to-tags, select.DamageImmunityPrint');
fields12.on('change keyup', function(){
	var tags = [];
	fields12.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageImmunity]', '#CreateAttributeForm').val(tags.join(','));
});

var fields13 = $('#CreateAttributeForm').find('input.add-to-tags, select.PossessionArmorPrint');
fields13.on('change keyup', function(){
	var tags = [];
	fields13.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=PossessionArmor]', '#CreateAttributeForm').val(tags.join(','));
});

var fields14 = $('#CreateAttributeForm').find('input.add-to-tags, select.CharacteristicesPrint');
fields14.on('change keyup', function(){
	var tags = [];
	fields14.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Characteristices]', '#CreateAttributeForm').val(tags.join(','));
});

var fields15 = $('#CreateBackgroundForm').find('input.add-to-tags, select.PossessionArmorPrint');
fields15.on('change keyup', function(){
	var tags = [];
	fields15.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=PossessionArmor]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields16 = $('#CreateBackgroundForm').find('input.add-to-tags, select.GunOwnershipPrint');
fields16.on('change keyup', function(){
	var tags = [];
	fields16.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=GunOwnership]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields17 = $('#CreateBackgroundForm').find('input.add-to-tags, select.ToolOwnershipPrint');
fields17.on('change keyup', function(){
	var tags = [];
	fields17.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=ToolOwnership]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields18 = $('#CreateBackgroundForm').find('input.add-to-tags, select.SpellsPrint');
fields18.on('change keyup', function(){
	var tags = [];
	fields18.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Spells]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields19 = $('#CreateBackgroundForm').find('input.add-to-tags, select.SkillsNamePrint');
fields19.on('change keyup', function(){
	var tags = [];
	fields19.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=SkillsName]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields20 = $('#CreateBackgroundForm').find('input.add-to-tags, select.DamageResistancePrint');
fields20.on('change keyup', function(){
	var tags = [];
	fields20.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageResistance]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields21 = $('#CreateBackgroundForm').find('input.add-to-tags, select.DamageImmunityPrint');
fields21.on('change keyup', function(){
	var tags = [];
	fields21.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageImmunity]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields22 = $('#CreateBackgroundForm').find('input.add-to-tags, select.CharacteristicesPrint');
fields22.on('change keyup', function(){
	var tags = [];
	fields22.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Characteristices]', '#CreateBackgroundForm').val(tags.join(','));
});

var fields23 = $('#CreateClassDNDForm').find('input.add-to-tags, select.PossessionArmorPrint');
fields23.on('change keyup', function(){
	var tags = [];
	fields23.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=PossessionArmor]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields24 = $('#CreateClassDNDForm').find('input.add-to-tags, select.GunOwnershipPrint');
fields24.on('change keyup', function(){
	var tags = [];
	fields24.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=GunOwnership]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields25 = $('#CreateClassDNDForm').find('input.add-to-tags, select.ToolOwnershipPrint');
fields25.on('change keyup', function(){
	var tags = [];
	fields25.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=ToolOwnership]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields26 = $('#CreateClassDNDForm').find('input.add-to-tags, select.SpellsPrint');
fields26.on('change keyup', function(){
	var tags = [];
	fields26.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Spells]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields27 = $('#CreateClassDNDForm').find('input.add-to-tags, select.SkillsNamePrint');
fields27.on('change keyup', function(){
	var tags = [];
	fields27.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=SkillsName]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields28 = $('#CreateClassDNDForm').find('input.add-to-tags, select.DamageResistancePrint');
fields28.on('change keyup', function(){
	var tags = [];
	fields28.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageResistance]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields29 = $('#CreateClassDNDForm').find('input.add-to-tags, select.DamageImmunityPrint');
fields29.on('change keyup', function(){
	var tags = [];
	fields29.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageImmunity]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields30 = $('#CreateClassDNDForm').find('input.add-to-tags, select.CharacteristicesPrint');
fields30.on('change keyup', function(){
	var tags = [];
	fields30.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Characteristices]', '#CreateClassDNDForm').val(tags.join(','));
});

var fields31 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.PossessionArmorPrint');
fields31.on('change keyup', function(){
	var tags = [];
	fields31.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=PossessionArmor]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields32 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.GunOwnershipPrint');
fields32.on('change keyup', function(){
	var tags = [];
	fields32.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=GunOwnership]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields33 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.ToolOwnershipPrint');
fields33.on('change keyup', function(){
	var tags = [];
	fields33.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=ToolOwnership]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields34 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.SpellsPrint');
fields34.on('change keyup', function(){
	var tags = [];
	fields34.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Spells]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields35 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.SkillsNamePrint');
fields35.on('change keyup', function(){
	var tags = [];
	fields35.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=SkillsName]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields36 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.DamageResistancePrint');
fields36.on('change keyup', function(){
	var tags = [];
	fields36.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageResistance]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields37 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.DamageImmunityPrint');
fields37.on('change keyup', function(){
	var tags = [];
	fields37.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageImmunity]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields38 = $('#CreateRaceDNDForm').find('input.add-to-tags, select.CharacteristicesPrint');
fields38.on('change keyup', function(){
	var tags = [];
	fields38.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Characteristices]', '#CreateRaceDNDForm').val(tags.join(','));
});

var fields39 = $('#CreateSpellForm').find('input.add-to-tags, select.DamageImmunityPrint');
fields39.on('change keyup', function(){
	var tags = [];
	fields39.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=DamageImmunity]', '#CreateSpellForm').val(tags.join(','));
});

var fields40 = $('#CreateSpellForm').find('input.add-to-tags, select.SubclassesPrint');
fields40.on('change keyup', function(){
	var tags = [];
	fields40.each(function(){
		if ($(this).val().length)
		{
			tags.push($(this).val());
		}
	});
	$('input[name=Subclasses]', '#CreateSpellForm').val(tags.join(','));
});
def parametrsoutput(Resultrequest, Tabledates, TabelsParametrs):
    languagesName = Resultrequest['languagesName']
    if languagesName == '' or languagesName == None:
        languages = []
    else:
        languages = languagesName.split(sep=',')
    SpellsName = Resultrequest['Spells']
    if SpellsName == '' or SpellsName == None:
        SpellsDND = []
    else:
        SpellsDND = SpellsName.split(sep=',')
    PossessionArmorsName = Resultrequest['PossessionArmors']
    if PossessionArmorsName == '' or PossessionArmorsName == None:
        PossessionArmors = []
    else:
        PossessionArmors = PossessionArmorsName.split(sep=',')
    GunsOwnershipName = Resultrequest['GunsOwnership']
    if GunsOwnershipName == '' or GunsOwnershipName == None:
        GunsOwnership = []
    else:
        GunsOwnership = GunsOwnershipName.split(sep=',')
    ToolsOwnershipName = Resultrequest['ToolsOwnership']
    if ToolsOwnershipName == '' or ToolsOwnershipName == None:
        ToolsOwnership = []
    else:
        ToolsOwnership = ToolsOwnershipName.split(sep=',')
    SkillsName = Resultrequest["SkillsName"]
    if SkillsName == '' or SkillsName == None:
        SkillsDND = []
    else:
        SkillsDND = SkillsName.split(sep=',')
    damageresistanceName = Resultrequest["DamageResistance"]
    if damageresistanceName == '' or damageresistanceName == None:
        damageresistances = []
    else:
        damageresistances = damageresistanceName.split(sep=',')
    damageimmunityName = Resultrequest["DamageImmunity"]
    if damageimmunityName == '' or damageimmunityName == None:
        damageimmunitys = []
    else:
        damageimmunitys = damageimmunityName.split(sep=',')
    CharacteristicesDND = Resultrequest["Characteristices"]
    if CharacteristicesDND == '' or CharacteristicesDND == None:
        Characteristics = []
    else:
        Characteristics = CharacteristicesDND.split(sep=',')

    MasivDates = [languages,SpellsDND,PossessionArmors,GunsOwnership,ToolsOwnership,SkillsDND,damageresistances,damageimmunitys,Characteristics]
    resultdate = appenddatas(MasivDates, Tabledates, TabelsParametrs)
    return resultdate

def appenddatas(MasivDates,Tabledates,TabelsParametrs):
    languages       = MasivDates['languages']
    SpellsDND           = MasivDates['SpellsDND']
    PossessionArmors    = MasivDates['PossessionArmors']
    GunsOwnership       = MasivDates['GunsOwnership']
    ToolsOwnership      = MasivDates['ToolsOwnership']
    SkillsDND           = MasivDates['SkillsDND']
    damageresistances   = MasivDates['damageresistances']
    damageimmunitys     = MasivDates['damageimmunitys']
    Characteristics     = MasivDates['Characteristics']
    LanguageDND              = TabelsParametrs['LanguageDND']
    Skills              = TabelsParametrs['Skills']
    SpellDND            = TabelsParametrs['SpellDND']
    ArmorTypes          = TabelsParametrs['ArmorTypes']
    Weapoons            = TabelsParametrs['Weapoons']
    Tools               = TabelsParametrs['Tools']
    DamageTypes         = TabelsParametrs['DamageTypes']
    Characteristices    = TabelsParametrs['Characteristices']
    try:
        for language in languages:
            languagednd = LanguageDND.query.filter_by(LanguageName=language).first()
            Tabledates.Language.append(languagednd)
        for SkillName in SkillsDND:
            SkillDND = Skills.query.filter_by(SkillName=SkillName).first()
            Tabledates.Skill.append(SkillDND)
        for Spellame in SpellsDND:
            Spell = SpellDND.query.filter_by(Spellame=Spellame).first()
            Tabledates.Spell.append(Spell)
        for PossessionArmor in PossessionArmors:
            Armor = ArmorTypes.query.filter_by(ArmorTypeName=PossessionArmor).first()
            Tabledates.PossessionArmor.append(Armor)
        for GunOwnership in GunsOwnership:
            Weapoon = Weapoons.query.filter_by(WeapoonName=GunOwnership).first()
            Tabledates.GunOwnership.append(Weapoon)
        for ToolOwnership in ToolsOwnership:
            Tool = Tools.query.filter_by(ToolName=ToolOwnership).first()
            Tabledates.ToolOwnership.append(Tool)
        for damageresistance in damageresistances:
            resistance = DamageTypes.query.filter_by(DamageTypeName=damageresistance).first()
            Tabledates.DamageResistance.append(resistance)
        for damageimmunity in damageimmunitys:
            immunity = DamageTypes.query.filter_by(DamageTypeName=damageimmunity).first()
            Tabledates.DamageImmunity.append(immunity)
        for Characteristic in Characteristics:
            characteristic = Characteristices.query.filter_by(CharacteristicName=Characteristic).first()
            Tabledates.Characteristic.append(characteristic)

        return True
    except:
        return False


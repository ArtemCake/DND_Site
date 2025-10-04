from flask import (Flask, render_template, request, redirect)
from flask_login import login_user, login_required, logout_user, LoginManager
from flask_security import (roles_accepted, Security, SQLAlchemySessionUserDatastore)
from functions.functions import appenddatas, parametrsoutput, OpenVeiwPost, OpenEditPost, UpdateTable, RemoveTable
import logging
from functions.Classes import *

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
app.config['SECRET_KEY'] = 'MY_SECRET'
app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
db.init_app(app)
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)


logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


user_datastore  = SQLAlchemySessionUserDatastore(db.session, User, Role)
security        = Security(app, user_datastore)


@app.before_first_request
def create_tables():
    db.create_all()
    roles = Role.query.all()
    if len(roles) == 0:
        role1 = Role(RoleName='Gamer'   , name='Gamer'  , NameUser='Игрок')
        role2 = Role(RoleName='Master'  , name='Master' , NameUser='Мастер')
        role3 = Role(RoleName='Admin'   , name='Admin'  , NameUser='Администратор')
        db.session.add(role1)
        db.session.add(role2)
        db.session.add(role3)
        db.session.commit()
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if len(magicalItemsTypes) == 0:
        magicalItemsType1 = MagicalItemsTypes(Name='Доспех', Discription='')
        magicalItemsType2 = MagicalItemsTypes(Name='Оружие', Discription='')
        db.session.add(magicalItemsType1)
        db.session.add(magicalItemsType2)
        db.session.commit()


@app.route("/CreateAbilities", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateAbilities():
    DateTabels = [['AbilitieName', 'Название способности', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        AbilitiesName   = request.form['AbilitieName']
        Discription     = request.form['Discription']
        abilities       = Abilities(Name=AbilitiesName, Discription=Discription)
        try:
            db.session.add(abilities)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Abilities',Title='Создание способности')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Abilities', Title='Создание способности')


@app.route("/CreateArchetypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArchetypes():
    characteristices = Characteristices.query.all()
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    PossessionArmor  = ArmorTypes.query.all()
    GunOwnership     = Weapoons.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    classes          = Classes.query.all()
    DateTabels = [['ArchetypeName', 'Название подкласса', False], ['Discription', 'Описание', False], ['NotArmorSafe', 'Защита без доспехов', True]
        , ['ArmorClass', 'Класс брони без доспехов', False], [[characteristices, 'Characteristices', 'Владение характеристиками', False]]
        , [[damageTypes, 'DamageResistance', 'Сопративление к урону', False]], [[damageTypes, 'DamageImmunity', 'Имунитет к урону', False]]
        , [[effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False]], [[spells, 'Spells', 'Дополнительные заклинания', False]]
        , [[skills, 'Skills', 'Владение навыками', False]], [[PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]]
        , [[GunOwnership, 'GunOwnership', 'Владение оружием', False]], [[ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]]
        , [[languages, 'Languages', 'Владение языками', False]], [[abilities, 'Abilities', 'Особые способности', False]]
        , [[classes, 'Classes', 'Класс', True]]]
    if request.method == 'POST':
        ArchetypeName   = request.form['ArchetypeName']
        Discription     = request.form['Discription']
        ArmorClass      = request.form['ArmorClass']
        if 'NotArmorSafe' in request.form:
            NotArmorSafe=True
        else:
            NotArmorSafe=False
        Archetype = Archetypes(Name=ArchetypeName, Discription=Discription, NotArmorSafe=NotArmorSafe
                                , ArmorClass=ArmorClass)
        ClassesParam                = parametrsoutput(request.form['Classes'])
        MassivClasses               = [''] if ClassesParam is None or ClassesParam =='' else ClassesParam
        MassivClassesApd            = [MassivClasses, Classes, Archetype.Class]
        CharacteristicesParam       = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristices      = [''] if CharacteristicesParam is None or CharacteristicesParam =='' else CharacteristicesParam
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Archetype.Characteristic]
        DamageResistanceParam       =  parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistance      = [''] if DamageResistanceParam is None or DamageResistanceParam =='' else DamageResistanceParam
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, Archetype.DamageResistance]
        DamageImmunityParam         = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunity        = [''] if DamageImmunityParam is None or DamageImmunityParam =='' else DamageImmunityParam
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, Archetype.DamageImmunity]
        EffectsResistanceParam      = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistance     = [''] if EffectsResistanceParam is None or EffectsResistanceParam =='' else EffectsResistanceParam
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Archetype.EffectsResistance]
        SpellsParam                 = parametrsoutput(request.form['Spells'])
        MassivSpells                = [''] if SpellsParam is None or SpellsParam == '' else SpellsParam
        MassivSpellsApd             = [MassivSpells, Spells, Archetype.Spell]
        SkillsParam                 = parametrsoutput(request.form['Skills'])
        MassivSkills                = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd             = [MassivSkills, Skills, Archetype.Skill]
        PossessionArmorParam        = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmor       = [''] if PossessionArmorParam is None or PossessionArmorParam == '' else PossessionArmorParam
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Archetype.PossessionArmor]
        GunOwnershipParam           = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnership          = [''] if GunOwnershipParam is None or GunOwnershipParam == '' else GunOwnershipParam
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Archetype.GunOwnership]
        ToolOwnershipParam          = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnership         = [''] if ToolOwnershipParam is None or ToolOwnershipParam == '' else ToolOwnershipParam
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Archetype.ToolOwnership]
        LanguagesParam              = parametrsoutput(request.form['Languages'])
        MassivLanguages             = [''] if LanguagesParam is None or LanguagesParam == '' else LanguagesParam
        MassivLanguagesApd          = [MassivLanguages, Languages, Archetype.Language]
        AbilitiesParam              = parametrsoutput(request.form['Abilities'])
        MassivAbilities             = [''] if AbilitiesParam is None or AbilitiesParam == '' else AbilitiesParam
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Archetype.Abilities]
        MassivDates                 = [MassivClassesApd,MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Archetype)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Archetypes', Title='Создание подкласса (архетипа)')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Archetypes', Title='Создание подкласса (архетипа)')


@app.route("/CreateArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmors():
    armorTypes = ArmorTypes.query.all()
    DateTabels = [['ArmorName', 'Название доспеха', False], ['Discription', 'Описание', False],['Hindrance', 'Помеха', True]
                , ['Weight', 'Вес', False], ['Power', 'Сила', False], ['Cost', 'Цена', False], ['ArmorClass', 'Классс доспеха', False]
                , ['ArmorClass', 'Класс брони без доспехов', False], [[armorTypes, 'ArmorTypes', 'Тип доспеха', True]]]
    if request.method == 'POST':
        ArmorName   = request.form['ArmorName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Power       = request.form['Power']
        Cost        = request.form['Cost']
        ArmorClass  = request.form['ArmorClass']

        if 'Hindrance' in request.form:
            Hindrance = True
        else:
            Hindrance = False
        armors = Armors(Name=ArmorName, Discription=Discription, Weight=Weight, Power=Power
                             , Cost=Cost, ArmorClass=ArmorClass, Hindrance=Hindrance)
        ArmorTypesParam     = parametrsoutput(request.form['ArmorTypes'])
        MassivArmorTypes    = ['']  if ArmorTypesParam is None or ArmorTypesParam == '' else ArmorTypesParam
        MassivArmorTypesApd = [MassivArmorTypes, ArmorTypes, armors.ArmorType]
        MassivDates         = [MassivArmorTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(armors)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Armors', Title='Создание доспеха')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Armors', Title='Создание доспеха')


@app.route("/CreateArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmorTypes():
    DateTabels = [['ArmorTypeName', 'Название способности', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        ArmorTypeName   = request.form['ArmorTypeName']
        Discription     = request.form['Discription']
        ArmorType       = ArmorTypes(Name=ArmorTypeName, Discription=Discription)
        try:
            db.session.add(ArmorType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Armors', Title='Создание типа доспеха')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='ArmorTypes', Title='Создание типа доспеха')


@app.route("/CreateAtributes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateAtributes():
    characteristices = Characteristices.query.all()
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    PossessionArmor  = ArmorTypes.query.all()
    GunOwnership     = Weapoons.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    DateTabels = [['AttributeName', 'Название черты', False], ['Discription', 'Описание', False], [[characteristices, 'Characteristices', 'Владение характеристиками', False]]
        , [[damageTypes, 'DamageResistance', 'Сопративление к урону', False]], [[damageTypes, 'DamageImmunity', 'Имунитет к урону', False]]
        , [[damageTypes, 'DamageResistance', 'Сопративление к урону', False]], [[effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False]]
        , [[spells, 'Spells', 'Дополнительные заклинания', False]]           , [[skills, 'Skills', 'Владение навыками', False]]
        , [[PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]], [[GunOwnership, 'GunOwnership', 'Владение оружием', False]]
        , [[ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]], [[languages, 'Languages', 'Владение языками', False]]
        , [[abilities, 'Abilities', 'Особые способности', False]]]
    if request.method == 'POST':
        AttributeName               = request.form['AttributeName']
        Discription                 = request.form['Discription']
        Attribute                   = Atributes(Name=AttributeName, Discription=Discription)
        CharacteristicesParam       = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristices      = ['']  if CharacteristicesParam is None or CharacteristicesParam == '' else CharacteristicesParam
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Attribute.Characteristic]
        DamageResistanceParam       =  parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistance      = [''] if DamageResistanceParam is None or DamageResistanceParam =='' else DamageResistanceParam
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, Attribute.DamageResistance]
        DamageImmunityParam         = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunity        = [''] if DamageImmunityParam is None or DamageImmunityParam =='' else DamageImmunityParam
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, Attribute.DamageImmunity]
        EffectsResistanceParam      = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistance     = [''] if EffectsResistanceParam is None or EffectsResistanceParam =='' else EffectsResistanceParam
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Attribute.EffectsResistance]
        SpellsParam                 = parametrsoutput(request.form['Spells'])
        MassivSpells                = [''] if SpellsParam is None or SpellsParam == '' else SpellsParam
        MassivSpellsApd             = [MassivSpells, Spells, Attribute.Spell]
        SkillsParam                 = parametrsoutput(request.form['Skills'])
        MassivSkills                = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd             = [MassivSkills, Skills, Attribute.Skill]
        PossessionArmorParam        = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmor       = [''] if PossessionArmorParam is None or PossessionArmorParam == '' else PossessionArmorParam
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Attribute.PossessionArmor]
        GunOwnershipParam           = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnership          = [''] if GunOwnershipParam is None or GunOwnershipParam == '' else GunOwnershipParam
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Attribute.GunOwnership]
        ToolOwnershipParam          = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnership         = [''] if ToolOwnershipParam is None or ToolOwnershipParam == '' else ToolOwnershipParam
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Attribute.ToolOwnership]
        LanguagesParam              = parametrsoutput(request.form['Languages'])
        MassivLanguages             = [''] if LanguagesParam is None or LanguagesParam == '' else LanguagesParam
        MassivLanguagesApd          = [MassivLanguages, Languages, Attribute.Language]
        AbilitiesParam              = parametrsoutput(request.form['Abilities'])
        MassivAbilities             = [''] if AbilitiesParam is None or AbilitiesParam == '' else AbilitiesParam
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Attribute.Abilities]
        MassivDates                 = [MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Attribute)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Atributes', Title='Создание черты')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Atributes', Title='Создание черты')


@app.route("/CreateBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateBackgrounds():
    characteristices = Characteristices.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    DateTabels = [['BackgroundName', 'Название предыстрории', False], ['Discription', 'Описание', False], [[characteristices, 'Characteristices', 'Владение характеристиками', False]]
        , [[spells, 'Spells', 'Дополнительные заклинания', False]]           , [[skills, 'Skills', 'Владение навыками', False]]
        , [[ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]], [[languages, 'Languages', 'Владение языками', False]]]
    if request.method == 'POST':
        BackgroundName   = request.form['BackgroundName']
        Discription     = request.form['Discription']
        Background                  = Backgrounds(Name=BackgroundName, Discription=Discription)
        CharacteristicesParam       = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristices      = ['']  if CharacteristicesParam is None or CharacteristicesParam == '' else CharacteristicesParam
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Background.Characteristic]
        SpellsParam                 = parametrsoutput(request.form['Spells'])
        MassivSpells                = [''] if SpellsParam is None or SpellsParam == '' else SpellsParam
        MassivSpellsApd             = [MassivSpells, Spells, Background.Spell]
        SkillsParam                 = parametrsoutput(request.form['Skills'])
        MassivSkills                = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd             = [MassivSkills, Skills, Background.Skill]
        ToolOwnershipParam          = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnership         = [''] if ToolOwnershipParam is None or ToolOwnershipParam == '' else ToolOwnershipParam
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Background.ToolOwnership]
        LanguagesParam              = parametrsoutput(request.form['Languages'])
        MassivLanguages             = [''] if LanguagesParam is None or LanguagesParam == '' else LanguagesParam
        MassivLanguagesApd          = [MassivLanguages, Languages, Background.Language]
        MassivDates                 = [MassivCharacteristicesApd,MassivSpellsApd,MassivSkillsApd
                                        ,MassivToolOwnershipApd,MassivLanguagesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Background)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Atributes', Title='Создание черты')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Backgrounds', Title='Создание предыстории')


@app.route("/CreateCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateCharacteristices():
    skills = Skills.query.all()
    DateTabels = [['CharacteristicName', 'Название характеристики', False], ['Discription', 'Описание', False]
                , [[skills, 'Skills', 'Владение навыками', False]]]
    if request.method == 'POST':
        CharacteristicName   = request.form['CharacteristicName']
        Discription          = request.form['Discription']
        Characteristic       = Characteristices(Name=CharacteristicName, Discription=Discription)
        SkillsParam          = parametrsoutput(request.form['Skills'])
        MassivSkills         = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd      = [MassivSkills, Skills, Characteristic.Skill]
        MassivDates          = [MassivSkillsApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Characteristic)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Characteristices', Title='Создание характеристики')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Characteristices', Title='Создание характеристики')


@app.route("/CreateClasses", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateClasses():
    characteristices = Characteristices.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    PossessionArmor  = ArmorTypes.query.all()
    GunOwnership     = Weapoons.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    DateTabels = [['ArchetypeName', 'Название подкласса', False], ['Discription', 'Описание', False], ['NotArmorSafe', 'Защита без доспехов', True]
                , ['ArmorClass', 'Класс брони без доспехов', False], [[characteristices, 'Characteristices', 'Владение характеристиками', False]]
                , [[spells, 'Spells', 'Дополнительные заклинания', False]], [[skills, 'Skills', 'Владение навыками', False]]
                , [[PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]], [[GunOwnership, 'GunOwnership', 'Владение оружием', False]]
                , [[ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]], [[languages, 'Languages', 'Владение языками', False]]]
    if request.method == 'POST':
        ArmorClass  = request.form['ArmorClass']
        Discription = request.form['Discription']
        ClassName   = request.form['ClassName']
        if 'NotArmorSafe' in request.form:
            NotArmorSafe = True
        else:
            NotArmorSafe = False
        Class = Classes(Name=ClassName, Discription=Discription, NotArmorSafe=NotArmorSafe
                                , ArmorClass=ArmorClass)
        CharacteristicesParam       = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristices      = [''] if CharacteristicesParam is None or CharacteristicesParam =='' else CharacteristicesParam
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Class.Characteristic]
        SpellsParam                 = parametrsoutput(request.form['Spells'])
        MassivSpells                = [''] if SpellsParam is None or SpellsParam == '' else SpellsParam
        MassivSpellsApd             = [MassivSpells, Spells, Class.Spell]
        SkillsParam                 = parametrsoutput(request.form['Skills'])
        MassivSkills                = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd             = [MassivSkills, Skills, Class.Skill]
        PossessionArmorParam        = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmor       = [''] if PossessionArmorParam is None or PossessionArmorParam == '' else PossessionArmorParam
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Class.PossessionArmor]
        GunOwnershipParam           = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnership          = [''] if GunOwnershipParam is None or GunOwnershipParam == '' else GunOwnershipParam
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Class.GunOwnership]
        ToolOwnershipParam          = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnership         = [''] if ToolOwnershipParam is None or ToolOwnershipParam == '' else ToolOwnershipParam
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Class.ToolOwnership]
        LanguagesParam              = parametrsoutput(request.form['Languages'])
        MassivLanguages             = [''] if LanguagesParam is None or LanguagesParam == '' else LanguagesParam
        MassivLanguagesApd          = [MassivLanguages, Languages, Class.Language]
        MassivDates                 = [MassivCharacteristicesApd
                           ,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Class)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Classes', Title='Создание класса')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Classes', Title='Создание класса')


@app.route("/CreateDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateDamageTypes():
    DateTabels = [['DamageTypeName', 'Название типа урона', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        DamageTypeName  = request.form['DamageTypeName']
        Discription     = request.form['Discription']
        DamageType      = DamageTypes(Name=DamageTypeName, Discription=Discription)
        try:
            db.session.add(DamageType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='DamageTypes', Title='Создание типа урона')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='DamageTypes', Title='Создание типа урона')


@app.route("/CreateEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEffects():
    DateTabels = [['EffectName', 'Название эффекта', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        EffectName  = request.form['EffectName']
        Discription = request.form['Discription']
        Effect      = Effects(Name=EffectName, Discription=Discription)
        try:
            db.session.add(Effect)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Effects', Title='Создание эффекта')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Effects', Title='Создание эффекта')


@app.route("/CreateEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipments():
    equipmentTypes = EquipmentTypes.query.all()
    DateTabels = [['EquipmentName', 'Название предыстрории', False], ['Discription', 'Описание', False]
                    , ['Weight', 'Вес', False], ['Cost', 'Цена', False]
                    , [[equipmentTypes, 'EquipmentTypes', 'Тип снаряжения', False]]]
    if request.method == 'POST':
        EquipmentName   = request.form['EquipmentName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Cost        = request.form['Cost']
        Equipment = Equipments(Name=EquipmentName, Discription=Discription, Weight=Weight, Cost=Cost)
        EquipmentTypesParam     = parametrsoutput(request.form['EquipmentTypes'])
        MassivEquipmentTypes    = ['']  if EquipmentTypesParam is None or EquipmentTypesParam == '' else EquipmentTypesParam
        MassivEquipmentTypesApd = [MassivEquipmentTypes, EquipmentTypes, Equipment.EquipmentType]
        MassivDates             = [MassivEquipmentTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Equipment)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Equipments', Title='Создание снаряжения')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Equipments', Title='Создание снаряжения')


@app.route("/CreateEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipmentTypes():
    DateTabels = [['EquipmentTypeName', 'Название типа снаряжения', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        EquipmentTypeName   = request.form['EquipmentTypeName']
        Discription         = request.form['Discription']
        EquipmentType       = EquipmentTypes(Name=EquipmentTypeName, Discription=Discription)
        try:
            db.session.add(EquipmentType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='EquipmentTypes', Title='Создание типа снаряжения')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='EquipmentTypes', Title='Создание типа снаряжения')


@app.route("/CreateFeatures", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateFeatures():
    DateTabels = [['FeaturesName', 'Название свойства оружия', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        FeaturesName = request.form['FeaturesName']
        Discription  = request.form['Discription']
        features     = Features(Name=FeaturesName, Discription=Discription)
        try:
            db.session.add(features)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Features', Title='Создание свойства оружия')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Features', Title='Создание свойства оружия')


@app.route("/CreateLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateLanguages():
    DateTabels = [['LanguageName', 'Название языка', False], ['Discription', 'Описание', False]
                  ,['TypicalRepresentative', 'Типичные представители', False],['Writing', 'Письменность', False]]
    if request.method == 'POST':
        LanguageName            = request.form['LanguageName']
        Discription             = request.form['Discription']
        TypicalRepresentative   = request.form['TypicalRepresentative']
        Writing                 = request.form['Writing']
        Language                = Languages(Name=LanguageName, Discription=Discription
                                             , TypicalRepresentative=TypicalRepresentative, Writing=Writing)
        try:
            db.session.add(Language)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Languages', Title='Создание языка')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Languages', Title='Создание языка')


@app.route("/CreateMagicalItems", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateMagicalItems():
    characteristices = Characteristices.query.all()
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    PossessionArmor  = ArmorTypes.query.all()
    GunOwnership     = Weapoons.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    armors           = Armors.query.all()
    magicalItemTypes = MagicalItemsTypes.query.all()
    DateTabels = [['MagicalItemsName', 'Название магического предмета', False], ['Discription', 'Описание', False], ['ArmorBonus', 'Бонус защиты', False]
        , ['PowerBonus', 'Бонус атаки', False], [[characteristices, 'Characteristices', 'Владение характеристиками', False]]
        , [[damageTypes, 'DamageResistance', 'Сопративление к урону', False]], [[damageTypes, 'DamageImmunity', 'Имунитет к урону', False]]
        , [[effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False]], [[effects, 'Effects', 'Эффекты', False]]
        , [[spells, 'Spells', 'Дополнительные заклинания', False]], [[skills, 'Skills', 'Владение навыками', False]]
        , [[PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]], [[GunOwnership, 'GunOwnership', 'Владение оружием', False]]
        , [[ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]], [[languages, 'Languages', 'Владение языками', False]]
        , [[abilities, 'Abilities', 'Особые способности', False]], [[armors, 'ArmorTypes', 'Доспех основа магического предмета', True]]
        , [[GunOwnership, 'WeapoonTypes', 'Оружие основа магического предмета', True]], [[magicalItemTypes, 'MagicalItemTypes', 'Тип магического предмета', True]]]
    if request.method == 'POST':
        MagicalItemsName    = request.form['MagicalItemsName']
        Discription         = request.form['Discription']
        PowerBonus          = request.form['PowerBonus']
        ArmorBonus          = request.form['ArmorBonus']
        MagicalItem         = MagicalItems(Name=MagicalItemsName, Discription=Discription, ArmorBonus=ArmorBonus
                                , PowerBonus=PowerBonus)
        MagicalItemTypesParam       = parametrsoutput(request.form['MagicalItemTypes'])
        MassivMagicalItemTypes      = ['']  if MagicalItemTypesParam is None or MagicalItemTypesParam == '' else MagicalItemTypesParam
        MassivMagicalItemTypesApd   = [MassivMagicalItemTypes, MagicalItemsTypes, MagicalItem.Class]
        CharacteristicesParam       = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristices      = [''] if CharacteristicesParam is None or CharacteristicesParam =='' else CharacteristicesParam
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, MagicalItem.Characteristic]
        DamageResistanceParam       =  parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistance      = [''] if DamageResistanceParam is None or DamageResistanceParam =='' else DamageResistanceParam
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, MagicalItem.DamageResistance]
        DamageImmunityParam         = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunity        = [''] if DamageImmunityParam is None or DamageImmunityParam =='' else DamageImmunityParam
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, MagicalItem.DamageImmunity]
        EffectsResistanceParam      = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistance     = [''] if EffectsResistanceParam is None or EffectsResistanceParam =='' else EffectsResistanceParam
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, MagicalItem.EffectResistance]
        EffectsParam                = parametrsoutput(request.form['Effects'])
        MassivEffects               = ['']  if EffectsParam is None or EffectsParam == '' else EffectsParam
        MassivEffectsApd            = [MassivEffects, Effects, MagicalItem.Effect]
        SpellsParam                 = parametrsoutput(request.form['Spells'])
        MassivSpells                = [''] if SpellsParam is None or SpellsParam == '' else SpellsParam
        MassivSpellsApd             = [MassivSpells, Spells, MagicalItem.Spell]
        SkillsParam                 = parametrsoutput(request.form['Skills'])
        MassivSkills                = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd             = [MassivSkills, Skills, MagicalItem.Skill]
        PossessionArmorParam        = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmor       = [''] if PossessionArmorParam is None or PossessionArmorParam == '' else PossessionArmorParam
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, MagicalItem.PossessionArmor]
        GunOwnershipParam           = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnership          = [''] if GunOwnershipParam is None or GunOwnershipParam == '' else GunOwnershipParam
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, MagicalItem.GunOwnership]
        ToolOwnershipParam          = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnership         = [''] if ToolOwnershipParam is None or ToolOwnershipParam == '' else ToolOwnershipParam
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, MagicalItem.ToolOwnership]
        LanguagesParam              = parametrsoutput(request.form['Languages'])
        MassivLanguages             = [''] if LanguagesParam is None or LanguagesParam == '' else LanguagesParam
        MassivLanguagesApd          = [MassivLanguages, Languages, MagicalItem.Language]
        AbilitiesParam              = parametrsoutput(request.form['Abilities'])
        MassivAbilities             = [''] if AbilitiesParam is None or AbilitiesParam == '' else AbilitiesParam
        MassivAbilitiesApd          = [MassivAbilities, Abilities, MagicalItem.Abilitie]
        ArmorTypesPAram             = parametrsoutput(request.form['ArmorTypes'])
        MassivArmorTypes            = ['']  if ArmorTypesPAram is None or ArmorTypesPAram == '' else ArmorTypesPAram
        MassivArmorTypesApd         = [MassivArmorTypes, Armors, MagicalItem.ArmorTypeItem]
        WeapoonTypesParam           = parametrsoutput(request.form['WeapoonTypes'])
        MassivWeapoonTypes          = ['']  if WeapoonTypesParam is None or WeapoonTypesParam == '' else WeapoonTypesParam
        MassivWeapoonTypesApd       = [MassivWeapoonTypes, Weapoons, MagicalItem.WeapoonTypeItem]
        MassivDates                 = [MassivMagicalItemTypesApd,MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivEffectsApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd
                            ,MassivGunOwnershipApd,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd,MassivArmorTypesApd,MassivWeapoonTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(MagicalItem)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItems', Title='Создание магического предмета')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItems', Title='Создание магического предмета')


@app.route("/CreateMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateMagicalItemTypes():
    DateTabels = [['MagicalItemTypeName', 'Название типа магического предмета', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        MagicalItemTypeName = request.form['MagicalItemTypeName']
        Discription         = request.form['Discription']
        MagicalItemsType    = MagicalItemsTypes(Name=MagicalItemTypeName, Discription=Discription)
        try:
            db.session.add(MagicalItemsType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItemsTypes', Title='Создание типа магического предмета')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItemsTypes', Title='Создание типа магического предмета')


@app.route("/CreateRaces", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateRaces():
    characteristices = Characteristices.query.all()
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    PossessionArmor  = ArmorTypes.query.all()
    GunOwnership     = Weapoons.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    DateTabels = [['RaceName', 'Название расы', False], ['Discription', 'Описание', False], ['Speed', 'Скорость бега', False]
        , ['Fly', 'Скорость полёта', False], ['Climb', 'Скорость лазания', False], ['Swim', 'Скорость плавания', False]
        , ['Fight', 'Безоружная атака', False], ['Armor', 'Бонус к классу брони', False], [[characteristices, 'Characteristices', 'Владение характеристиками', False]]
        , [[damageTypes, 'DamageResistance', 'Сопративление к урону', False]], [[damageTypes, 'DamageImmunity', 'Имунитет к урону', False]]
        , [[effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False]], [[spells, 'Spells', 'Дополнительные заклинания', False]]
        , [[skills, 'Skills', 'Владение навыками', False]], [[PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]]
        , [[GunOwnership, 'GunOwnership', 'Владение оружием', False]], [[ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]]
        , [[languages, 'Languages', 'Владение языками', False]], [[abilities, 'Abilities', 'Особые способности', False]]]
    if request.method == 'POST':
        RaceName        = request.form['RaceName']
        Discription     = request.form['Discription']
        Speed           = request.form['Speed']
        Fly             = request.form['Fly']
        Climb           = request.form['Climb']
        Swim            = request.form['Swim']
        Fight           = request.form['Fight']
        Armor           = request.form['Armor']
        Race            = Races(Name=RaceName, Discription=Discription
                                , Speed=Speed, Fly=Fly, Climb=Climb, Swim=Swim, Fight=Fight, Armor=Armor)
        CharacteristicesParam       = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristices      = [''] if CharacteristicesParam is None or CharacteristicesParam =='' else CharacteristicesParam
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Race.Characteristic]
        DamageResistanceParam       =  parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistance      = [''] if DamageResistanceParam is None or DamageResistanceParam =='' else DamageResistanceParam
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, Race.DamageResistance]
        DamageImmunityParam         = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunity        = [''] if DamageImmunityParam is None or DamageImmunityParam =='' else DamageImmunityParam
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, Race.DamageImmunity]
        EffectsResistanceParam      = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistance     = [''] if EffectsResistanceParam is None or EffectsResistanceParam =='' else EffectsResistanceParam
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Race.EffectsResistance]
        SpellsParam                 = parametrsoutput(request.form['Spells'])
        MassivSpells                = [''] if SpellsParam is None or SpellsParam == '' else SpellsParam
        MassivSpellsApd             = [MassivSpells, Spells, Race.Spell]
        SkillsParam                 = parametrsoutput(request.form['Skills'])
        MassivSkills                = [''] if SkillsParam is None or SkillsParam == '' else SkillsParam
        MassivSkillsApd             = [MassivSkills, Skills, Race.Skill]
        PossessionArmorParam        = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmor       = [''] if PossessionArmorParam is None or PossessionArmorParam == '' else PossessionArmorParam
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Race.PossessionArmor]
        GunOwnershipParam           = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnership          = [''] if GunOwnershipParam is None or GunOwnershipParam == '' else GunOwnershipParam
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Race.GunOwnership]
        ToolOwnershipParam          = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnership         = [''] if ToolOwnershipParam is None or ToolOwnershipParam == '' else ToolOwnershipParam
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Race.ToolOwnership]
        MassivLanguages             = ['']  if parametrsoutput(request.form['Languages']) is None else parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, Race.Language]
        AbilitiesParam              = parametrsoutput(request.form['Abilities'])
        MassivAbilities             = [''] if AbilitiesParam is None or AbilitiesParam == '' else AbilitiesParam
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Race.Abilities]
        MassivDates                 = [MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Race)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Races', Title='Создание расы')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Races', Title='Создание расы')


@app.route("/CreateSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSkills():
    DateTabels = [['SkillName', 'Название навыка', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        SkillName   = request.form['SkillName']
        Discription = request.form['Discription']
        Skill       = Skills(Name=SkillName, Discription=Discription)
        try:
            db.session.add(Skill)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Skills', Title='Создание навыка')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Skills', Title='Создание навыка')


@app.route("/CreateSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSpells():
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    classes          = Classes.query.all()
    archetypes       = Archetypes.query.all()
    DateTabels = [['SpellName', 'Название заклинания', False], ['Discription', 'Описание', False]
        , ['LevelSpell', 'Уровень заклинания', False], ['Damage', 'Атака заклинания', False]
        , ['ApplicationTime', 'Время накладывания', False], ['Distance', 'Дистанция', False]
        , ['Components', 'Компоненты', False], ['Duration', 'Продолжительность', False], ['Ritual', 'Ритуал', True]
        , ['ArmorClass', 'Класс брони без доспехов', False], [[damageTypes, 'DamageTypes', 'Тип урона', False]]
        , [[effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False]], [[effects, 'Effects', 'Эффекты', False]]
        , [[languages, 'Languages', 'Владение языками', False]], [[abilities, 'Abilities', 'Особые способности', False]]
        , [[classes, 'Classes', 'Доступно для классов', True]] , [[archetypes, 'Archetypes', 'Доступно для подклассов', True]]]
    if request.method == 'POST':
        SpellName           = request.form['SpellName']
        Discription         = request.form['Discription']
        LevelSpell          = request.form['LevelSpell']
        Damage              = request.form['Damage']
        ApplicationTime     = request.form['ApplicationTime']
        Distance            = request.form['Distance']
        Components          = request.form['Components']
        Duration            = request.form['Duration']
        if'Ritual' in request.form:
            Ritual = True
        else:
            Ritual = False
        Spell               = Spells(Name=SpellName, Discription=Discription, Damage=Damage
                                , LevelSpell=LevelSpell, ApplicationTime=ApplicationTime, Distance=Distance
                                ,Components=Components,Duration=Duration, Ritual=Ritual)
        ClassesParam                = parametrsoutput(request.form['Classes'])
        MassivClasses               = [''] if ClassesParam is None or ClassesParam =='' else ClassesParam
        MassivClassesApd            = [MassivClasses, Classes, Spell.Class]
        ArchetypesParam             = parametrsoutput(request.form['Archetypes'])
        MassivArchetypes            = [''] if ArchetypesParam is None or ArchetypesParam == '' else ArchetypesParam
        MassivArchetypesApd         = [MassivArchetypes, Archetypes, Spell.Archetype]
        DamageTypesParam            = parametrsoutput(request.form['DamageTypes'])
        MassivDamageTypes           = [''] if DamageTypesParam is None or DamageTypesParam == '' else DamageTypesParam
        MassivDamageTypessApd       = [MassivDamageTypes, DamageTypes, Spell.DamageType]
        LanguagesParam              = parametrsoutput(request.form['Languages'])
        MassivLanguages             = [''] if LanguagesParam is None or LanguagesParam == '' else LanguagesParam
        MassivLanguagesApd          = [MassivLanguages, Languages, Spell.Language]
        AbilitiesParam              = parametrsoutput(request.form['Abilities'])
        MassivAbilities             = [''] if AbilitiesParam is None or AbilitiesParam == '' else AbilitiesParam
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Spell.Abilitie]
        EffectsResistanceParam      = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistance     = [''] if EffectsResistanceParam is None or EffectsResistanceParam =='' else EffectsResistanceParam
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Spell.EffectResistance]
        EffectsParam                = parametrsoutput(request.form['Effects'])
        MassivEffects               = ['']  if EffectsParam is None or EffectsParam == '' else EffectsParam
        MassivEffectsApd            = [MassivEffects, Effects, Spell.Effect]
        MassivDates                 = [MassivClassesApd,MassivArchetypesApd,MassivDamageTypessApd,MassivLanguagesApd
                                       ,MassivAbilitiesApd,MassivEffectsResistanceApd,MassivEffectsApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Spell)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Spells', Title='Создание заклинания')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Spells', Title='Создание заклинания')


@app.route("/CreateTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateTools():
    toolTypes = ToolTypes.query.all()
    DateTabels = [['ToolName', 'Название предыстрории', False], ['Discription', 'Описание', False]
                    , ['Weight', 'Вес', False], ['Cost', 'Цена', False]
                    , [[toolTypes, 'ToolTypes', 'Тип инструмента', True]]]
    if request.method == 'POST':
        ToolName            = request.form['ToolName']
        Discription         = request.form['Discription']
        Weight              = request.form['Weight']
        Cost                = request.form['Cost']
        Tool                = Tools(Name=ToolName, Discription=Discription, Weight=Weight, Cost=Cost)
        ToolTypesParam      = parametrsoutput(request.form['ToolTypes'])
        MassivToolTypes     = [''] if ToolTypesParam is None or ToolTypesParam == '' else ToolTypesParam
        MassivToolTypesApd  = [MassivToolTypes, ToolTypes, Tool.ToolType]
        MassivDates         = [MassivToolTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Tool)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Tools', Title='Создание инструмента')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Tools', Title='Создание инструмента')


@app.route("/CreateToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateToolTypes():
    DateTabels = [['ToolTypeName', 'Название типа инструмента', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        ToolTypeName  = request.form['ToolTypeName']
        Discription   = request.form['Discription']
        ToolType      = ToolTypes(Name=ToolTypeName, Discription=Discription)
        try:
            db.session.add(ToolType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='ToolTypes', Title='Создание типа инструмента')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='ToolTypes', Title='Создание типа инструмента')


@app.route("/CreateWeapoons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoons():
    features     = Features.query.all()
    damageTypes  = DamageTypes.query.all()
    weapoonTypes = WeapoonTypes.query.all()
    DateTabels = [['WeapoonName', 'Название оружия', False], ['Discription', 'Описание', False]
                    , ['Weight', 'Вес', False], ['Cost', 'Цена', False], ['Damage', 'Урон', False]
                    , [[features, 'Features', 'Свойство оружия', True]], [[damageTypes, 'DamageTypes', 'Тип урона', True]]
                    , [[weapoonTypes, 'WeapoonTypes', 'Тип оружия', True]]]
    if request.method == 'POST':
        WeapoonName    = request.form['WeapoonName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Cost        = request.form['Cost']
        Damage      = request.form['Damage']
        Weapoon               = Weapoons(Name=WeapoonName, Discription=Discription, Weight=Weight
                                         , Cost=Cost, Damage=Damage)
        WeapoonTypesParam     = parametrsoutput(request.form['WeapoonTypes'])
        MassivWeapoonTypes    = ['']  if WeapoonTypesParam is None or WeapoonTypesParam == '' else WeapoonTypesParam
        MassivWeapoonTypesApd = [MassivWeapoonTypes, WeapoonTypes, Weapoon.WeapoonType]
        FeaturesParam         = parametrsoutput(request.form['Features'])
        MassivFeatures        = [''] if FeaturesParam is None or FeaturesParam == '' else FeaturesParam
        MassivFeaturesApd     = [MassivFeatures, Features, Weapoon.Feature]
        DamageTypesParam      = parametrsoutput(request.form['DamageTypes'])
        MassivDamageTypes     = [''] if DamageTypesParam is None or DamageTypesParam == '' else DamageTypesParam
        MassivDamageTypesApd  = [MassivDamageTypes, DamageTypes, Weapoon.DamageType]
        MassivDates           = [MassivWeapoonTypesApd,MassivDamageTypesApd,MassivFeaturesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Weapoon)
                db.session.commit()
                return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Weapoons', Title='Создание оружия')
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Weapoons', Title='Создание оружия')


@app.route("/CreateWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoonTypes():
    DateTabels = [['WeapoonTypeName', 'Название типа оружия', False], ['Discription', 'Описание', False]]
    if request.method == 'POST':
        WeapoonTypeName  = request.form['WeapoonTypeName']
        Discription      = request.form['Discription']
        WeapoonType      = WeapoonTypes(Name=WeapoonTypeName, Discription=Discription)
        try:
            db.session.add(WeapoonType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='WeapoonTypes', Title='Создание типа оружия')
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='WeapoonTypes', Title='Создание типа оружия')


@app.route("/VeiwAbilities", methods=['GET', 'POST'])
def VeiwAbilities():
    abilities = Abilities.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Abilities', Date_id])
    return render_template("VeiwElementPage.html", Dates=abilities
                           , TableName='VeiwAbilities', TitlePage='Способности')


@app.route("/VeiwArchetypes", methods=['GET', 'POST'])
def VeiwArchetypes():
    archetypes = Archetypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Archetypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=archetypes
                           , TableName='VeiwArchetypes', TitlePage='Подклассы (Архетипы)')


@app.route("/VeiwArmors", methods=['GET', 'POST'])
def VeiwArmors():
    armors = Armors.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Armors', Date_id])
    return render_template("VeiwElementPage.html", Dates=armors
                           , TableName='VeiwArmors', TitlePage='Доспехи')


@app.route("/VeiwArmorTypes", methods=['GET', 'POST'])
def VeiwArmorTypes():
    armorTypes = ArmorTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['ArmorTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=armorTypes
                           , TableName='VeiwArmorTypes', TitlePage='Типы доспехов')


@app.route("/VeiwAtributes", methods=['GET', 'POST'])
def VeiwAtributes():
    atributes = Atributes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Atributes', Date_id])
    return render_template("VeiwElementPage.html", Dates=atributes
                           , VeiwAtributes='VeiwAtributes', TitlePage='Черты')


@app.route("/VeiwBackgrounds", methods=['GET', 'POST'])
def VeiwBackgrounds():
    backgrounds = Backgrounds.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Backgrounds', Date_id])
    return render_template("VeiwElementPage.html", Dates=backgrounds
                           , VeiwAtributes='VeiwBackgrounds', TitlePage='Предыстории')


@app.route("/VeiwCharacteristices", methods=['GET', 'POST'])
def VeiwCharacteristices():
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Characteristices', Date_id])
    return render_template("VeiwElementPage.html", Dates=characteristices
                           , VeiwAtributes='VeiwCharacteristices', TitlePage='Характеристики')


@app.route("/VeiwClasses", methods=['GET', 'POST'])
def VeiwClasses():
    classes = Classes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Classes', Date_id])
    return render_template("VeiwElementPage.html", Dates=classes
                           , VeiwAtributes='VeiwClasses', TitlePage='Классы')


@app.route("/VeiwDamageTypes", methods=['GET', 'POST'])
def VeiwDamageTypes():
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['DamageTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=damageTypes
                           , VeiwAtributes='VeiwDamageTypes', TitlePage='Типы урона')


@app.route("/VeiwEffects", methods=['GET', 'POST'])
def VeiwEffects():
    effects = Effects.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Effects', Date_id])
    return render_template("VeiwElementPage.html", Dates=effects
                           , VeiwAtributes='VeiwEffects', TitlePage='Эффекты')


@app.route("/VeiwEquipments", methods=['GET', 'POST'])
def VeiwEquipments():
    equipments = Equipments.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Equipments', Date_id])
    return render_template("VeiwElementPage.html", Dates=equipments
                           , VeiwAtributes='VeiwEquipments', TitlePage='Снаряжения')


@app.route("/VeiwEquipmentTypes", methods=['GET', 'POST'])
def VeiwEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['EquipmentTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=equipmentTypes
                           , VeiwAtributes='VeiwEquipmentTypes', TitlePage='Типы снаряжения')


@app.route("/VeiwFeatures", methods=['GET', 'POST'])
def VeiwFeatures():
    features = Features.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Features', Date_id])
    return render_template("VeiwElementPage.html", Dates=features
                           , VeiwAtributes='VeiwFeatures', TitlePage='Особенности')


@app.route("/VeiwLanguages", methods=['GET', 'POST'])
def VeiwLanguages():
    languages = Languages.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Languages', Date_id])
    return render_template("VeiwElementPage.html", Dates=languages
                           , VeiwAtributes='VeiwLanguages', TitlePage='Языки')


@app.route("/VeiwMagicalItems", methods=['GET', 'POST'])
def VeiwMagicalItems():
    magicalItems = MagicalItems.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['MagicalItems', Date_id])
    return render_template("VeiwElementPage.html", Dates=magicalItems
                           , VeiwAtributes='VeiwMagicalItems', TitlePage='Магические предметы')


@app.route("/VeiwMagicalItemTypes", methods=['GET', 'POST'])
def VeiwMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['MagicalItemsTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=magicalItemsTypes
                           , VeiwAtributes='VeiwMagicalItemTypes', TitlePage='Типы магических предметов')


@app.route("/VeiwRaces", methods=['GET', 'POST'])
def VeiwRaces():
    races = Races.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Races', Date_id])
    return render_template("VeiwElementPage.html", Dates=races
                           , VeiwAtributes='VeiwRaces', TitlePage='Расы')


@app.route("/VeiwSkills", methods=['GET', 'POST'])
def VeiwSkills():
    skills = Skills.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Skills', Date_id])
    return render_template("VeiwElementPage.html", Dates=skills
                           , VeiwAtributes='VeiwSkills', TitlePage='Навыки')


@app.route("/VeiwSpells", methods=['GET', 'POST'])
def VeiwSpells():
    spells = Spells.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Spells', Date_id])
    return render_template("VeiwElementPage.html", Dates=spells
                           , VeiwAtributes='VeiwSpells', TitlePage='Заклинания')


@app.route("/VeiwTools", methods=['GET', 'POST'])
def VeiwTools():
    tools = Tools.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Tools', Date_id])
    return render_template("VeiwElementPage.html", Dates=tools
                           , VeiwAtributes='VeiwTools', TitlePage='Инструменты')


@app.route("/VeiwToolTypes", methods=['GET', 'POST'])
def VeiwToolTypes():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['ToolTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=toolTypes
                           , VeiwAtributes='VeiwToolTypes', TitlePage='Типы инструментов')


@app.route("/VeiwWeapoons", methods=['GET', 'POST'])
def VeiwWeapoons():
    weapoons = Weapoons.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Weapoons', Date_id])
    return render_template("VeiwElementPage.html", Dates=weapoons
                           , VeiwAtributes='VeiwWeapoons', TitlePage='Оружия')


@app.route("/VeiwWeapoonTypes", methods=['GET', 'POST'])
def VeiwWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['WeapoonTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=weapoonTypes
                           , VeiwAtributes='VeiwWeapoonTypes', TitlePage='Типы оружия')


@app.route("/EditAbilities", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditAbilities():
    abilities = Abilities.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Abilities', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=abilities
                           , TableName='EditAbilities', TitlePage='Изменить способности')


@app.route("/EditArchetypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArchetypes():
    archetypes = Archetypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Archetypes', Date_id, ['Class']])
    return render_template("EditElementPage.html", Dates=archetypes
                           , TableName='EditArchetypes', TitlePage='Изменить подклассы (Архетипы)')


@app.route("/EditArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArmors():
    armors = Armors.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Armors', Date_id, ['ArmorType']])
    return render_template("EditElementPage.html", Dates=armors
                           , TableName='EditArmors', TitlePage='Изменить доспехи')


@app.route("/EditArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArmorTypes():
    armorTypes = ArmorTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['ArmorTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=armorTypes
                           , TableName='EditArmorTypes', TitlePage='Изменить типы доспехов')


@app.route("/EditAtributes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditAtributes():
    atributes = Atributes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Atributes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=atributes
                           , TableName='EditAtributes', TitlePage='Изменить черты')


@app.route("/EditBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditBackgrounds():
    backgrounds = Backgrounds.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Backgrounds', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=backgrounds
                           , TableName='EditBackgrounds', TitlePage='Изменить предыстории')


@app.route("/EditCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditCharacteristices():
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Characteristices', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=characteristices
                           , TableName='EditCharacteristices', TitlePage='Изменить характеристики')


@app.route("/EditClasses", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditClasses():
    classes = Classes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Classes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=classes
                           , TableName='EditClasses', TitlePage='Изменить классы')


@app.route("/EditDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditDamageTypes():
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['DamageTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=damageTypes
                           , TableName='EditDamageTypes', TitlePage='Изменить типы урона')


@app.route("/EditEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEffects():
    effects = Effects.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Effects', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=effects
                           , TableName='EditEffects', TitlePage='Изменить эффекты')


@app.route("/EditEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEquipments():
    equipments = Equipments.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Equipments', Date_id, ['EquipmentType']])
    return render_template("EditElementPage.html", Dates=equipments
                           , TableName='EditEquipments', TitlePage='Изменить снаряжения')


@app.route("/EditEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['EquipmentTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=equipmentTypes
            , TableName='EditEquipmentTypes', TitlePage='Изменить типы снаряжений')


@app.route("/EditFeatures", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditFeatures():
    features = Features.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['EquipmentTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=features
        , TableName='EditFeatures', TitlePage='Изменить особенности')


@app.route("/EditLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditLanguages():
    languages = Languages.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Languages', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=languages
        , TableName='EditLanguages', TitlePage='Изменить языки')


@app.route("/EditMagicalItems", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMagicalItems():
    magicalItems = MagicalItems.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['MagicalItems', Date_id, ['ArmorTypeItem','WeapoonTypeItem','MagicalItemType']])
    return render_template("EditElementPage.html", Dates=magicalItems
        , TableName='EditMagicalItems', TitlePage='Изменить магические предметы')


@app.route("/EditMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['MagicalItemsTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=magicalItemsTypes
        , TableName='EditMagicalItemTypes', TitlePage='Изменить типы магических предметов')


@app.route("/EditRaces", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditRaces():
    races = Races.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Races', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=races
        , TableName='EditRaces', TitlePage='Изменить расы')


@app.route("/EditSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditSkills():
    skills = Skills.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Skills', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=skills
        , TableName='EditSkills', TitlePage='Изменить навыки')


@app.route("/EditSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditSpells():
    spells = Spells.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Spells', Date_id, ['DamageType']])
    return render_template("EditElementPage.html", Dates=spells
        , TableName='EditSpells', TitlePage='Изменить заклинания')


@app.route("/EditTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditTools():
    tools = Tools.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Tools', Date_id, ['ToolType']])
    return render_template("EditElementPage.html", Dates=tools
        , TableName='EditTools', TitlePage='Изменить инструменты')


@app.route("/EditToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditToolTypes():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['ToolTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=toolTypes
        , TableName='EditToolTypes', TitlePage='Изменить типы инструментов')


@app.route("/EditWeapoons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditWeapoons():
    weapoons = Weapoons.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Weapoons', Date_id, ['Features','DamageType','WeapoonType']])
    return render_template("EditElementPage.html", Dates=weapoons
                           , TableName='EditWeapoons', TitlePage='Изменить оружия')


@app.route("/EditWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['WeapoonTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=weapoonTypes
                           , TableName='EditWeapoonTypes', TitlePage='Изменить типы оружия')


@app.route("/EditPost", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditPost():
    if request.method == 'POST':
        Parametrs = request.form
        if request.form['two_buttons'] == "update":
            updateTrue = UpdateTable(Parametrs)
            if type(updateTrue) != bool:
                db.session.add(updateTrue)
                db.session.commit()
            else:
                db.session.rollback()
            return render_template("EditMaterial.html")
        elif request.form['two_buttons'] == "remove":
            removeTrue = RemoveTable(Parametrs)
            if removeTrue:
                db.session.commit()
            else:
                db.session.rollback()
        return render_template("EditMaterial.html")
    return render_template("EditMaterial.html")


@app.route("/Index")
@app.route("/")
def Index():
    return render_template("Index.html")


@app.route("/AdminPanel")
@roles_accepted('Admin')
def AdminPanel():
    return render_template("AdminPanel.html")


@app.route("/CreateMaterial", methods=['POST','GET'])
@roles_accepted('Admin', 'Master')
def CreateMaterial():
    return render_template("CreateMaterial.html")


@app.route("/VeiwMaterial", methods=['GET', 'POST'])
def VeiwMaterial():
    return render_template("VeiwMaterial.html")


@app.route("/EditMaterial", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMaterial():
    return render_template("EditMaterial.html")


@app.route('/CreateUsers', methods=['GET', 'POST'])
def CreateUsers():
    msg = ""
    Roles = Role.query.all()
    if request.method == 'POST':
        user = User.query.filter_by(login=request.form['login']).first()
        if user:
            msg = "Пользователь уже существует"
            return render_template('CreateUsers.html', msg=msg)
        user = User(login=request.form['login'], active=1, password=request.form['password'])
        role = Role.query.filter_by(NameUser=request.form['Role']).first()
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        return render_template("Index.html")
    else:
        return render_template("CreateUsers.html", msg=msg, roles=Roles)


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


@app.route('/LoginUsers', methods=['GET', 'POST'])
def LoginUsers():
    msg = ""
    if request.method == 'POST':
        user = User.query.filter_by(login=request.form['login']).first()
        if user:
            if user.password == request.form['password']:
                login_user(user)
                return render_template('Index.html')
            else:
                msg = "Неверный пароль"
        else:
            msg = "Пользователь не существует"
        return render_template('LoginUsers.html', msg=msg)

    else:
        return render_template("LoginUsers.html", msg=msg)


@app.route('/Logout')
@login_required
def logout():
    logout_user()
    return render_template("Index.html")


if __name__ == "__main__":
    app.run(debug=True,passthrough_errors=True,
    use_debugger=False, use_reloader=False)

from flask import (Flask, render_template, request, redirect)
from flask_login import login_user, login_required, logout_user, LoginManager, current_user
from flask_security import (roles_accepted, Security, SQLAlchemySessionUserDatastore)
import json
from functions.functions import (OpenVeiwPost, OpenEditPost, UpdateTable, RemoveTable, FileDelete, CreateDate)
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
    DateTabels = [['Name', 'Название способности', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        abilities = CreateDate([Abilities(), request, MassivDates])
        try:
            db.session.add(abilities)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Abilities',
                                   Title='Создание способности', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Abilities',
                               Title='Создание способности', show_back_button=True)


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
    DateTabels = [['Name', 'Название подкласса', False], ['Discription', 'Описание', False]
        , ['ArmorClass', 'Класс брони без доспехов', False],
                  [characteristices, 'Characteristices', 'Владение характеристиками', False]
        , [damageTypes, 'DamageResistance', 'Сопративление к урону', False],
                  [damageTypes, 'DamageImmunity', 'Имунитет к урону', False]
        , [effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False],
                  [spells, 'Spell', 'Дополнительные заклинания', False]
        , [skills, 'Skill', 'Владение навыками', False],
                  [PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]
        , [GunOwnership, 'GunOwnership', 'Владение оружием', False],
                  [ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]
        , [languages, 'Language', 'Владение языками', False], [abilities, 'Abilitie', 'Особые способности', False]
        , [classes, 'Class', 'Класс', True], ['imageName', 'Картинка', False]
        , ['NotArmorSafe', 'Защита без доспехов', True]]
    if request.method == 'POST':
        MassivDates = [['Classes', 'Class', Archetypes().Class],
                       ['Characteristices', 'Characteristic', Archetypes().Characteristic]
            , ['DamageTypes', 'DamageResistance', Archetypes().DamageResistance],
                       ['DamageTypes', 'DamageImmunity', Archetypes().DamageImmunity]
            , ['Effects', 'EffectsResistance', Archetypes().EffectsResistance], ['Spells', 'Spell', Archetypes().Spell]
            , ['Skills', 'Skill', Archetypes().Skill], ['ArmorTypes', 'PossessionArmor', Archetypes().PossessionArmor],
                       ['Weapoons', 'GunOwnership', Archetypes().GunOwnership]
            , ['Tools', 'ToolOwnership', Archetypes().ToolOwnership], ['Languages', 'Language', Archetypes().Language]
            , ['Abilities', 'Abilitie', Archetypes().Abilitie]]
        Archetype = CreateDate([Archetypes(), request, MassivDates])
        try:
            db.session.add(Archetype)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Archetypes',
                                   Title='Создание подкласса (архетипа)', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Archetypes',
                               Title='Создание подкласса (архетипа)', show_back_button=True)


@app.route("/CreateArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmors():
    armorTypes = ArmorTypes.query.all()
    DateTabels = [['Name', 'Название доспеха', False], ['Discription', 'Описание', False], ['Hindrance', 'Помеха', True]
        , ['Weight', 'Вес', False], ['Power', 'Сила', False], ['Cost', 'Цена', False],
                  ['ArmorClass', 'Классс доспеха', False]
        , [armorTypes, 'ArmorTypes', 'Тип доспеха', True], ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['ArmorTypes', 'ArmorType', Armors().ArmorType]]
        armors = CreateDate([Armors(), request, MassivDates])
        try:
            db.session.add(armors)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Armors',
                                   Title='Создание доспеха', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Armors', Title='Создание доспеха',
                               show_back_button=True)


@app.route("/CreateArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmorTypes():
    DateTabels = [['Name', 'Название способности', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        ArmorType = CreateDate([ArmorTypes(), request, MassivDates])
        try:
            db.session.add(ArmorType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Armors',
                                   Title='Создание типа доспеха', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='ArmorTypes',
                               Title='Создание типа доспеха', show_back_button=True)


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
    DateTabels = [['Name', 'Название черты', False], ['Discription', 'Описание', False]
        , [damageTypes, 'DamageResistance', 'Сопративление к урону', False],
                  [damageTypes, 'DamageImmunity', 'Имунитет к урону', False]
        , [damageTypes, 'DamageResistance', 'Сопративление к урону', False],
                  [effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False]
        , [spells, 'Spells', 'Дополнительные заклинания', False], [skills, 'Skills', 'Владение навыками', False]
        , [PossessionArmor, 'PossessionArmor', 'Владение доспехами', False],
                  [GunOwnership, 'GunOwnership', 'Владение оружием', False]
        , [ToolOwnership, 'ToolOwnership', 'Владение инструментами', False],
                  [languages, 'Languages', 'Владение языками', False]
        , [abilities, 'Abilities', 'Особые способности', False], ['imageName', 'Картинка', False]
        , [characteristices, 'Characteristices', 'Владение характеристиками', False]]
    if request.method == 'POST':
        MassivDates = [['Characteristices', 'Characteristic', Atributes().Characteristic],
                       ['DamageTypes', 'DamageResistance', Atributes().DamageResistance]
            , ['DamageTypes', 'DamageImmunity', Atributes().DamageImmunity],
                       ['Effects', 'EffectsResistance', Atributes().EffectsResistance]
            , ['Spells', 'Spell', Atributes().Spell], ['Skills', 'Skill', Atributes().Skill]
            , ['ArmorTypes', 'PossessionArmor', Atributes().PossessionArmor],
                       ['Abilities', 'Abilitie', Atributes().Abilitie]
            , ['Weapoons', 'GunOwnership', Atributes().GunOwnership],
                       ['Tools', 'ToolOwnership', Atributes().ToolOwnership]
            , ['Languages', 'Language', Atributes().Language]]
        Attribute = CreateDate([Atributes(), request, MassivDates])
        try:
            db.session.add(Attribute)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Atributes',
                                   Title='Создание черты', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Atributes', Title='Создание черты',
                               show_back_button=True)


@app.route("/CreateBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateBackgrounds():
    characteristices = Characteristices.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    DateTabels = [['Name', 'Название предыстрории', False], ['Discription', 'Описание', False]
        , [characteristices, 'Characteristices', 'Владение характеристиками', False],
                  [spells, 'Spells', 'Дополнительные заклинания', False]
        , [skills, 'Skills', 'Владение навыками', False],
                  [ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]
        , [languages, 'Languages', 'Владение языками', False], ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['Characteristices', 'Characteristic', Backgrounds().Characteristic],
                       ['Spells', 'Spell', Backgrounds().Spell]
            , ['Skills', 'Skill', Backgrounds().Skill], ['Tools', 'ToolOwnership', Backgrounds().ToolOwnership]
            , ['Languages', 'Language', Backgrounds().Language]]
        Background = CreateDate([Backgrounds(), request, MassivDates])
        try:
            db.session.add(Background)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Atributes',
                                   Title='Создание черты', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Backgrounds',
                               Title='Создание предыстории', show_back_button=True)


@app.route("/CreateCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateCharacteristices():
    skills = Skills.query.all()
    DateTabels = [['Name', 'Название характеристики', False], ['Discription', 'Описание', False]
        , [skills, 'Skill', 'Владение навыками', False], ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['Skills', 'Skill', Characteristices().Skill]]
        Characteristic = CreateDate([Characteristices(), request, MassivDates])
        try:
            db.session.add(Characteristic)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Characteristices',
                                   Title='Создание характеристики', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Characteristices',
                               Title='Создание характеристики', show_back_button=True)


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
    DateTabels = [['Name', 'Название подкласса', False], ['Discription', 'Описание', False]
        , ['ArmorClass', 'Класс брони без доспехов', False], ['BoneHealth', 'Кость хитов', False],
                  [characteristices, 'Characteristices', 'Владение характеристиками', False]
        , [spells, 'Spells', 'Дополнительные заклинания', False], [skills, 'Skills', 'Владение навыками', False]
        , [PossessionArmor, 'PossessionArmor', 'Владение доспехами', False],
                  [GunOwnership, 'GunOwnership', 'Владение оружием', False]
        , [ToolOwnership, 'ToolOwnership', 'Владение инструментами', False],
                  [languages, 'Languages', 'Владение языками', False]
        , ['imageName', 'Картинка', False], ['NotArmorSafe', 'Защита без доспехов', True]]
    if request.method == 'POST':
        MassivDates = [['Characteristices', 'Characteristic', Classes().Characteristic],
                       ['Languages', 'Language', Classes().Language]
            , ['Spells', 'Spell', Classes().Spell], ['Skills', 'Skill', Classes().Skill]
            , ['ArmorTypes', 'PossessionArmor', Classes().PossessionArmor],
                       ['Tools', 'ToolOwnership', Classes().ToolOwnership]
            , ['Weapoons', 'GunOwnership', Classes().GunOwnership]]
        Class = CreateDate([Classes(), request, MassivDates])
        try:
            db.session.add(Class)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Classes',
                                   Title='Создание класса', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Classes', Title='Создание класса',
                               show_back_button=True)


@app.route("/CreateDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateDamageTypes():
    DateTabels = [['Name', 'Название типа урона', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        DamageType = CreateDate([DamageTypes(), request, MassivDates])
        try:
            db.session.add(DamageType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='DamageTypes',
                                   Title='Создание типа урона', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='DamageTypes',
                               Title='Создание типа урона', show_back_button=True)


@app.route("/CreateEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEffects():
    DateTabels = [['Name', 'Название эффекта', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        Effect = CreateDate([Effects(), request, MassivDates])
        try:
            db.session.add(Effect)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Effects',
                                   Title='Создание эффекта', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Effects', Title='Создание эффекта',
                               show_back_button=True)


@app.route("/CreateEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipments():
    equipmentTypes = EquipmentTypes.query.all()
    DateTabels = [['Name', 'Название предыстрории', False], ['Discription', 'Описание', False]
        , ['Weight', 'Вес', False], ['Cost', 'Цена', False], [equipmentTypes, 'EquipmentTypes', 'Тип снаряжения', False]
        , ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['EquipmentTypes', 'EquipmentType', Equipments().EquipmentType]]
        Equipment = CreateDate([Equipments(), request, MassivDates])
        try:
            db.session.add(Equipment)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Equipments',
                                   Title='Создание снаряжения', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Equipments',
                               Title='Создание снаряжения', show_back_button=True)


@app.route("/CreateEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipmentTypes():
    DateTabels = [['Name', 'Название типа снаряжения', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        EquipmentType = CreateDate([EquipmentTypes(), request, MassivDates])
        try:
            db.session.add(EquipmentType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='EquipmentTypes',
                                   Title='Создание типа снаряжения', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='EquipmentTypes',
                               Title='Создание типа снаряжения', show_back_button=True)


@app.route("/CreateFeatures", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateFeatures():
    DateTabels = [['Name', 'Название свойства оружия', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False], ['Distanse', 'Дистанция', False],
                  ['DopDamage', 'Дополнительный урон', False]]
    if request.method == 'POST':
        MassivDates = []
        features = CreateDate([Features(), request, MassivDates])
        try:
            db.session.add(features)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Features',
                                   Title='Создание свойства оружия', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Features',
                               Title='Создание свойства оружия', show_back_button=True)


@app.route("/CreateLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateLanguages():
    rases = Races.query.all()
    DateTabels = [['Name', 'Название языка', False], ['Discription', 'Описание', False]
        , [rases, 'TypicalRepresentative', 'Типичные представители', False], ['Writing', 'Письменность', False]
        , ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['Races', 'TypicalRepresentative', Languages().TypicalRepresentative]]
        Language = CreateDate([Languages(), request, MassivDates])
        try:
            db.session.add(Language)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Languages',
                                   Title='Создание языка', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Languages', Title='Создание языка',
                               show_back_button=True)


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
    DateTabels = [['Name', 'Название магического предмета', False], ['Discription', 'Описание', False]
        , ['PowerBonus', 'Бонус атаки', False],
                  [characteristices, 'Characteristices', 'Владение характеристиками', False]
        , [damageTypes, 'DamageResistance', 'Сопративление к урону', False],
                  [damageTypes, 'DamageImmunity', 'Имунитет к урону', False]
        , [effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False], [effects, 'Effects', 'Эффекты', False]
        , [spells, 'Spells', 'Дополнительные заклинания', False], [skills, 'Skills', 'Владение навыками', False]
        , [PossessionArmor, 'PossessionArmor', 'Владение доспехами', False],
                  [GunOwnership, 'GunOwnership', 'Владение оружием', False]
        , [ToolOwnership, 'ToolOwnership', 'Владение инструментами', False],
                  [languages, 'Languages', 'Владение языками', False]
        , [abilities, 'Abilities', 'Особые способности', False],
                  [armors, 'ArmorTypes', 'Доспех основа магического предмета', True]
        , [GunOwnership, 'WeapoonTypes', 'Оружие основа магического предмета', True],
                  [magicalItemTypes, 'MagicalItemTypes', 'Тип магического предмета', True]
        , ['imageName', 'Картинка', False], ['ArmorBonus', 'Бонус защиты', False]]
    if request.method == 'POST':
        MassivDates = [['Characteristices', 'Characteristic', MagicalItems().Characteristic],
                       ['DamageTypes', 'DamageResistance', MagicalItems().DamageResistance]
            , ['DamageTypes', 'DamageImmunity', MagicalItems().DamageImmunity],
                       ['Effects', 'EffectsResistance', MagicalItems().EffectsResistance]
            , ['Spells', 'Spell', MagicalItems().Spell], ['Skills', 'Skill', MagicalItems().Skill]
            , ['ArmorTypes', 'PossessionArmor', MagicalItems().PossessionArmor],
                       ['Abilities', 'Abilitie', MagicalItems().Abilitie]
            , ['Weapoons', 'GunOwnership', MagicalItems().GunOwnership],
                       ['Tools', 'ToolOwnership', MagicalItems().ToolOwnership]
            , ['Languages', 'Language', MagicalItems().Language],
                       ['MagicalItemTypes', 'MagicalItemType', MagicalItems().MagicalItemType]
            , ['Effects', 'Effect', MagicalItems().Effect], ['Armors', 'ArmorTypeItem', MagicalItems().ArmorTypeItem]
            , ['Weapoons', 'WeapoonTypeItem', MagicalItems().WeapoonTypeItem]]
        MagicalItem = CreateDate([MagicalItems(), request, MassivDates])
        try:
            db.session.add(MagicalItem)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItems',
                                   Title='Создание магического предмета', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItems',
                               Title='Создание магического предмета', show_back_button=True)


@app.route("/CreateMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateMagicalItemTypes():
    DateTabels = [['Name', 'Название типа магического предмета', False],
                  ['Discription', 'Описание', False], ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        MagicalItemsType = CreateDate([MagicalItemsTypes(), request, MassivDates])
        try:
            db.session.add(MagicalItemsType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItemsTypes',
                                   Title='Создание типа магического предмета', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='MagicalItemsTypes',
                               Title='Создание типа магического предмета', show_back_button=True)


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
    DateTabels = [['Name', 'Название расы', False], ['Discription', 'Описание', False]
        , ['Fly', 'Скорость полёта', False], ['Climb', 'Скорость лазания', False]
        , ['Fight', 'Безоружная атака', False], ['Armor', 'Бонус к классу брони', False]
        , [damageTypes, 'DamageResistance', 'Сопративление к урону', False],
                  [damageTypes, 'DamageImmunity', 'Имунитет к урону', False]
        , [effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False],
                  [spells, 'Spells', 'Дополнительные заклинания', False]
        , [skills, 'Skills', 'Владение навыками', False],
                  [PossessionArmor, 'PossessionArmor', 'Владение доспехами', False]
        , [GunOwnership, 'GunOwnership', 'Владение оружием', False],
                  [ToolOwnership, 'ToolOwnership', 'Владение инструментами', False]
        , [languages, 'Languages', 'Владение языками', False], [abilities, 'Abilities', 'Особые способности', False]
        , ['imageName', 'Картинка', False], ['Speed', 'Скорость бега', False]
        , ['Swim', 'Скорость плавания', False],
                  [characteristices, 'Characteristices', 'Владение характеристиками', False]]
    if request.method == 'POST':
        MassivDates = [['Characteristices', 'Characteristic', Races().Characteristic],
                       ['DamageTypes', 'DamageResistance', Races().DamageResistance]
            , ['DamageTypes', 'DamageImmunity', Races().DamageImmunity],
                       ['Effects', 'EffectsResistance', Races().EffectsResistance]
            , ['Spells', 'Spell', Races().Spell], ['Abilities', 'Abilitie', Races().Abilitie]
            , ['Skills', 'Skill', Races().Skill], ['ArmorTypes', 'PossessionArmor', Races().PossessionArmor],
                       ['Weapoons', 'GunOwnership', Races().GunOwnership]
            , ['Tools', 'ToolOwnership', Races().ToolOwnership], ['Languages', 'Language', Races().Language]]
        Race = CreateDate([Races(), request, MassivDates])
        try:
            db.session.add(Race)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Races', Title='Создание расы',
                                   show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Races', Title='Создание расы',
                               show_back_button=True)


@app.route("/CreateSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSkills():
    DateTabels = [['Name', 'Название навыка', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        Skill = CreateDate([Skills(), request, MassivDates])
        try:
            db.session.add(Skill)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Skills',
                                   Title='Создание навыка', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Skills', Title='Создание навыка',
                               show_back_button=True)


@app.route("/CreateSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSpells():
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    classes          = Classes.query.all()
    archetypes       = Archetypes.query.all()
    DateTabels = [['Name', 'Название заклинания', False], ['Discription', 'Описание', False]
        , ['LevelSpell', 'Уровень заклинания', False], ['Damage', 'Атака заклинания', False]
        , ['ApplicationTime', 'Время накладывания', False], ['Distance', 'Дистанция', False]
        , ['Components', 'Компоненты', False], ['Duration', 'Продолжительность', False], ['Ritual', 'Ритуал', True]
        , ['ArmorClass', 'Класс брони без доспехов', False], [damageTypes, 'DamageTypes', 'Тип урона', False]
        , [effects, 'EffectsResistance', 'Невосприимчивость к эффектам', False], [effects, 'Effects', 'Эффекты', False]
        , [languages, 'Languages', 'Владение языками', False], [abilities, 'Abilities', 'Особые способности', False]
        , [classes, 'Classes', 'Доступно для классов', True],
                  [archetypes, 'Archetypes', 'Доступно для подклассов', True]
        , ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['Classes', 'Class', Spells().Class],
                       ['Characteristices', 'Characteristic', Spells().Characteristic]
            , ['Abilities', 'Abilitie', Spells().Abilitie], ['DamageTypes', 'DamageType', Spells().DamageType]
            , ['Effects', 'EffectsResistance', Spells().EffectsResistance],
                       ['Archetypes', 'Archetype', Spells().Archetype]
            , ['Skills', 'Skill', Spells().Skill], ['ArmorTypes', 'ArmorType', Spells().ArmorType]
            , ['ArmorTypes', 'PossessionArmor', Spells().PossessionArmor],
                       ['Weapoons', 'GunOwnership', Spells().GunOwnership]
            , ['Tools', 'ToolOwnership', Spells().ToolOwnership], ['Languages', 'Language', Spells().Language]
            , ['Effects', 'Effect', Spells().Effect]]
        Spell = CreateDate([Spells(), request, MassivDates])
        try:
            db.session.add(Spell)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Spells',
                                   Title='Создание заклинания', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Spells',
                               Title='Создание заклинания', show_back_button=True)


@app.route("/CreateTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateTools():
    toolTypes = ToolTypes.query.all()
    DateTabels = [['Name', 'Название инструмента', False], ['Discription', 'Описание', False]
        , ['Weight', 'Вес', False], ['Cost', 'Цена', False]
        , [toolTypes, 'ToolTypes', 'Тип инструмента', True], ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = [['ToolTypes', 'ToolType', Tools().ToolType]]
        Tool = CreateDate([Tools(), request, MassivDates])
        try:
            db.session.add(Tool)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Tools',
                                   Title='Создание инструмента', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Tools',
                               Title='Создание инструмента', show_back_button=True)


@app.route("/CreateToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateToolTypes():
    DateTabels = [['Name', 'Название типа инструмента', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        ToolType = CreateDate([ToolTypes(), request, MassivDates])
        try:
            db.session.add(ToolType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='ToolTypes',
                                   Title='Создание типа инструмента', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='ToolTypes',
                               Title='Создание типа инструмента', show_back_button=True)


@app.route("/CreateWeapoons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoons():
    features     = Features.query.all()
    damageTypes  = DamageTypes.query.all()
    weapoonTypes = WeapoonTypes.query.all()
    DateTabels = [['Name', 'Название оружия', False], ['Discription', 'Описание', False]
        , ['Weight', 'Вес', False], ['Cost', 'Цена', False]
        , [features, 'Features', 'Свойство оружия', False], [damageTypes, 'DamageTypes', 'Тип урона', True]
        , [weapoonTypes, 'WeapoonTypes', 'Тип оружия', True], ['imageName', 'Картинка', False]
        , ['Damage', 'Урон', False]]
    if request.method == 'POST':
        MassivDates = [['WeapoonTypes', 'WeapoonType', Weapoons().WeapoonType],
                       ['Features', 'Feature', Weapoons().Feature]
            , ['DamageTypes', 'DamageType', Weapoons().DamageType]]
        Weapoon = CreateDate([Weapoons(), request, MassivDates])
        try:
            db.session.add(Weapoon)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Weapoons',
                                   Title='Создание оружия', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='Weapoons', Title='Создание оружия',
                               show_back_button=True)


@app.route("/CreateWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoonTypes():
    DateTabels = [['Name', 'Название типа оружия', False], ['Discription', 'Описание', False],
                  ['imageName', 'Картинка', False]]
    if request.method == 'POST':
        MassivDates = []
        WeapoonType = CreateDate([WeapoonTypes(), request, MassivDates])
        try:
            db.session.add(WeapoonType)
            db.session.commit()
            return render_template("CreatePost.html", DateTabels=DateTabels, TableName='WeapoonTypes',
                                   Title='Создание типа оружия', show_back_button=True)
        except Exception as msg:
            print(msg)
            db.session.rollback()
            return render_template("CreateMaterial.html", msg=msg, show_back_button=True)
    else:
        return render_template("CreatePost.html", DateTabels=DateTabels, TableName='WeapoonTypes',
                               Title='Создание типа оружия', show_back_button=True)


@app.route("/VeiwAbilities", methods=['GET', 'POST'])
def VeiwAbilities():
    abilities = Abilities.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Abilities', Date_id])
    return render_template("VeiwElementPage.html", Dates=abilities
                           , TableName='VeiwAbilities', TitlePage='Способности', show_back_button=True)


@app.route("/VeiwArchetypes", methods=['GET', 'POST'])
def VeiwArchetypes():
    archetypes = Archetypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Archetypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=archetypes
                           , TableName='VeiwArchetypes', TitlePage='Подклассы (Архетипы)', show_back_button=True)


@app.route("/VeiwArmors", methods=['GET', 'POST'])
def VeiwArmors():
    armors = Armors.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Armors', Date_id])
    return render_template("VeiwElementPage.html", Dates=armors
                           , TableName='VeiwArmors', TitlePage='Доспехи', show_back_button=True)


@app.route("/VeiwArmorTypes", methods=['GET', 'POST'])
def VeiwArmorTypes():
    armorTypes = ArmorTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['ArmorTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=armorTypes
                           , TableName='VeiwArmorTypes', TitlePage='Типы доспехов', show_back_button=True)


@app.route("/VeiwAtributes", methods=['GET', 'POST'])
def VeiwAtributes():
    atributes = Atributes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Atributes', Date_id])
    return render_template("VeiwElementPage.html", Dates=atributes
                           , VeiwAtributes='VeiwAtributes', TitlePage='Черты', show_back_button=True)


@app.route("/VeiwBackgrounds", methods=['GET', 'POST'])
def VeiwBackgrounds():
    backgrounds = Backgrounds.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Backgrounds', Date_id])
    return render_template("VeiwElementPage.html", Dates=backgrounds
                           , VeiwAtributes='VeiwBackgrounds', TitlePage='Предыстории', show_back_button=True)


@app.route("/VeiwCharacteristices", methods=['GET', 'POST'])
def VeiwCharacteristices():
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Characteristices', Date_id])
    return render_template("VeiwElementPage.html", Dates=characteristices
                           , VeiwAtributes='VeiwCharacteristices', TitlePage='Характеристики', show_back_button=True)


@app.route("/VeiwClasses", methods=['GET', 'POST'])
def VeiwClasses():
    classes = Classes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Classes', Date_id])
    return render_template("VeiwElementPage.html", Dates=classes
                           , VeiwAtributes='VeiwClasses', TitlePage='Классы', show_back_button=True)


@app.route("/VeiwDamageTypes", methods=['GET', 'POST'])
def VeiwDamageTypes():
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['DamageTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=damageTypes
                           , VeiwAtributes='VeiwDamageTypes', TitlePage='Типы урона', show_back_button=True)


@app.route("/VeiwEffects", methods=['GET', 'POST'])
def VeiwEffects():
    effects = Effects.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Effects', Date_id])
    return render_template("VeiwElementPage.html", Dates=effects
                           , VeiwAtributes='VeiwEffects', TitlePage='Эффекты', show_back_button=True)


@app.route("/VeiwEquipments", methods=['GET', 'POST'])
def VeiwEquipments():
    equipments = Equipments.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Equipments', Date_id])
    return render_template("VeiwElementPage.html", Dates=equipments
                           , VeiwAtributes='VeiwEquipments', TitlePage='Снаряжения', show_back_button=True)


@app.route("/VeiwEquipmentTypes", methods=['GET', 'POST'])
def VeiwEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['EquipmentTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=equipmentTypes
                           , VeiwAtributes='VeiwEquipmentTypes', TitlePage='Типы снаряжения', show_back_button=True)


@app.route("/VeiwFeatures", methods=['GET', 'POST'])
def VeiwFeatures():
    features = Features.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Features', Date_id])
    return render_template("VeiwElementPage.html", Dates=features
                           , VeiwAtributes='VeiwFeatures', TitlePage='Особенности', show_back_button=True)


@app.route("/VeiwLanguages", methods=['GET', 'POST'])
def VeiwLanguages():
    languages = Languages.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Languages', Date_id])
    return render_template("VeiwElementPage.html", Dates=languages
                           , VeiwAtributes='VeiwLanguages', TitlePage='Языки', show_back_button=True)


@app.route("/VeiwMagicalItems", methods=['GET', 'POST'])
def VeiwMagicalItems():
    magicalItems = MagicalItems.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['MagicalItems', Date_id])
    return render_template("VeiwElementPage.html", Dates=magicalItems
                           , VeiwAtributes='VeiwMagicalItems', TitlePage='Магические предметы', show_back_button=True)


@app.route("/VeiwMagicalItemTypes", methods=['GET', 'POST'])
def VeiwMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['MagicalItemsTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=magicalItemsTypes
                           , VeiwAtributes='VeiwMagicalItemTypes', TitlePage='Типы магических предметов',
                           show_back_button=True)


@app.route("/VeiwRaces", methods=['GET', 'POST'])
def VeiwRaces():
    races = Races.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Races', Date_id])
    return render_template("VeiwElementPage.html", Dates=races
                           , VeiwAtributes='VeiwRaces', TitlePage='Расы', show_back_button=True)


@app.route("/VeiwSkills", methods=['GET', 'POST'])
def VeiwSkills():
    skills = Skills.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Skills', Date_id])
    return render_template("VeiwElementPage.html", Dates=skills
                           , VeiwAtributes='VeiwSkills', TitlePage='Навыки', show_back_button=True)


@app.route("/VeiwSpells", methods=['GET', 'POST'])
def VeiwSpells():
    spells = Spells.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Spells', Date_id])
    return render_template("VeiwElementPage.html", Dates=spells
                           , VeiwAtributes='VeiwSpells', TitlePage='Заклинания', show_back_button=True)


@app.route("/VeiwTools", methods=['GET', 'POST'])
def VeiwTools():
    tools = Tools.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Tools', Date_id])
    return render_template("VeiwElementPage.html", Dates=tools
                           , VeiwAtributes='VeiwTools', TitlePage='Инструменты', show_back_button=True)


@app.route("/VeiwToolTypes", methods=['GET', 'POST'])
def VeiwToolTypes():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['ToolTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=toolTypes
                           , VeiwAtributes='VeiwToolTypes', TitlePage='Типы инструментов', show_back_button=True)


@app.route("/VeiwWeapoons", methods=['GET', 'POST'])
def VeiwWeapoons():
    weapoons = Weapoons.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['Weapoons', Date_id])
    return render_template("VeiwElementPage.html", Dates=weapoons
                           , VeiwAtributes='VeiwWeapoons', TitlePage='Оружия', show_back_button=True)


@app.route("/VeiwWeapoonTypes", methods=['GET', 'POST'])
def VeiwWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenVeiwPost(['WeapoonTypes', Date_id])
    return render_template("VeiwElementPage.html", Dates=weapoonTypes
                           , VeiwAtributes='VeiwWeapoonTypes', TitlePage='Типы оружия', show_back_button=True)


@app.route("/EditAbilities", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditAbilities():
    abilities = Abilities.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Abilities', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=abilities
                           , TableName='EditAbilities', TitlePage='Изменить способности', show_back_button=True)


@app.route("/EditArchetypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArchetypes():
    archetypes = Archetypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Archetypes', Date_id, ['Class']])
    return render_template("EditElementPage.html", Dates=archetypes
                           , TableName='EditArchetypes', TitlePage='Изменить подклассы (Архетипы)',
                           show_back_button=True)


@app.route("/EditArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArmors():
    armors = Armors.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Armors', Date_id, ['ArmorType']])
    return render_template("EditElementPage.html", Dates=armors
                           , TableName='EditArmors', TitlePage='Изменить доспехи', show_back_button=True)


@app.route("/EditArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArmorTypes():
    armorTypes = ArmorTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['ArmorTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=armorTypes
                           , TableName='EditArmorTypes', TitlePage='Изменить типы доспехов', show_back_button=True)


@app.route("/EditAtributes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditAtributes():
    atributes = Atributes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Atributes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=atributes
                           , TableName='EditAtributes', TitlePage='Изменить черты', show_back_button=True)


@app.route("/EditBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditBackgrounds():
    backgrounds = Backgrounds.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Backgrounds', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=backgrounds
                           , TableName='EditBackgrounds', TitlePage='Изменить предыстории', show_back_button=True)


@app.route("/EditCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditCharacteristices():
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Characteristices', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=characteristices
                           , TableName='EditCharacteristices', TitlePage='Изменить характеристики',
                           show_back_button=True)


@app.route("/EditClasses", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditClasses():
    classes = Classes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Classes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=classes
                           , TableName='EditClasses', TitlePage='Изменить классы', show_back_button=True)


@app.route("/EditDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditDamageTypes():
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['DamageTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=damageTypes
                           , TableName='EditDamageTypes', TitlePage='Изменить типы урона', show_back_button=True)


@app.route("/EditEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEffects():
    effects = Effects.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Effects', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=effects
                           , TableName='EditEffects', TitlePage='Изменить эффекты', show_back_button=True)


@app.route("/EditEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEquipments():
    equipments = Equipments.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Equipments', Date_id, ['EquipmentType']])
    return render_template("EditElementPage.html", Dates=equipments
                           , TableName='EditEquipments', TitlePage='Изменить снаряжения', show_back_button=True)


@app.route("/EditEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['EquipmentTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=equipmentTypes
                           , TableName='EditEquipmentTypes', TitlePage='Изменить типы снаряжений',
                           show_back_button=True)


@app.route("/EditFeatures", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditFeatures():
    features = Features.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Features', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=features
                           , TableName='EditFeatures', TitlePage='Изменить особенности', show_back_button=True)


@app.route("/EditLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditLanguages():
    languages = Languages.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Languages', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=languages
                           , TableName='EditLanguages', TitlePage='Изменить языки', show_back_button=True)


@app.route("/EditMagicalItems", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMagicalItems():
    magicalItems = MagicalItems.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['MagicalItems', Date_id, ['ArmorTypeItem','WeapoonTypeItem','MagicalItemType']])
    return render_template("EditElementPage.html", Dates=magicalItems
                           , TableName='EditMagicalItems', TitlePage='Изменить магические предметы',
                           show_back_button=True)


@app.route("/EditMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['MagicalItemsTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=magicalItemsTypes
                           , TableName='EditMagicalItemTypes', TitlePage='Изменить типы магических предметов',
                           show_back_button=True)


@app.route("/EditRaces", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditRaces():
    races = Races.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Races', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=races
                           , TableName='EditRaces', TitlePage='Изменить расы', show_back_button=True)


@app.route("/EditSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditSkills():
    skills = Skills.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Skills', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=skills
                           , TableName='EditSkills', TitlePage='Изменить навыки', show_back_button=True)


@app.route("/EditSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditSpells():
    spells = Spells.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Spells', Date_id, ['DamageType']])
    return render_template("EditElementPage.html", Dates=spells
                           , TableName='EditSpells', TitlePage='Изменить заклинания', show_back_button=True)


@app.route("/EditTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditTools():
    tools = Tools.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Tools', Date_id, ['ToolType']])
    return render_template("EditElementPage.html", Dates=tools
                           , TableName='EditTools', TitlePage='Изменить инструменты', show_back_button=True)


@app.route("/EditToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditToolTypes():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['ToolTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=toolTypes
                           , TableName='EditToolTypes', TitlePage='Изменить типы инструментов', show_back_button=True)


@app.route("/EditWeapoons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditWeapoons():
    weapoons = Weapoons.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['Weapoons', Date_id, ['Features','DamageType','WeapoonType']])
    return render_template("EditElementPage.html", Dates=weapoons
                           , TableName='EditWeapoons', TitlePage='Изменить оружия', show_back_button=True)


@app.route("/EditWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form.get('Date_id')
        return OpenEditPost(['WeapoonTypes', Date_id, ['']])
    return render_template("EditElementPage.html", Dates=weapoonTypes
                           , TableName='EditWeapoonTypes', TitlePage='Изменить типы оружия', show_back_button=True)


@app.route("/EditPost", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditPost():
    if request.method == 'POST':
        Parametrs = [request.form, request.files['image_uploads']]
        if 'two_buttons' in request.form:
            oldimageName = request.form['oldimageName']
            if request.form['two_buttons'] == "update":
                updateTrue = UpdateTable(Parametrs)
                if type(updateTrue) != bool:
                    db.session.add(updateTrue)
                    db.session.commit()
                else:
                    db.session.rollback()
                FileDelete([oldimageName])
                return render_template("EditMaterial.html", show_back_button=True)
            elif request.form['two_buttons'] == "remove":
                removeTrue = RemoveTable(Parametrs)
                if removeTrue:
                    db.session.commit()
                else:
                    db.session.rollback()
            return render_template("EditMaterial.html", show_back_button=True)
        else:
            return render_template("EditMaterial.html", show_back_button=True)
    return render_template("EditMaterial.html", show_back_button=True)


@app.route("/Index")
@app.route("/")
def Index():
    return render_template("Index.html")


@app.route("/AdminPanel")
@roles_accepted('Admin')
def AdminPanel():
    return render_template("AdminPanel.html", show_back_button=True)


@app.route("/CreateMaterial", methods=['POST','GET'])
@roles_accepted('Admin', 'Master')
def CreateMaterial():
    return render_template("CreateMaterial.html", show_back_button=True)


@app.route("/VeiwMaterial", methods=['GET', 'POST'])
def VeiwMaterial():
    return render_template("VeiwMaterial.html", show_back_button=True)


@app.route("/EditMaterial", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMaterial():
    return render_template("EditMaterial.html", show_back_button=True)


@roles_accepted('Gamer')
@app.route("/CreatePersonage", methods=['GET', 'POST'])
def CreatePersonage():
    MagicalItem = MagicalItems.query.all()
    Armor = Armors.query.all()
    TypeMagic = TypesMagic.query.all()
    Spell = Spells.query.all()
    PossessionArmor = ArmorTypes.query.all()
    Weapoon = Weapoons.query.all()
    Equipment = Equipments.query.all()
    ToolOwnership = Tools.query.all()
    DamageType = DamageTypes.query.all()
    Skill = Skills.query.all()
    Language = Languages.query.all()
    Effect = Effects.query.all()
    Abilitie = Abilities.query.all()
    Characteristic = Characteristices.query.all()
    Class = Classes.query.all()
    Archetype = Archetypes.query.all()
    Background = Backgrounds.query.all()
    Race = Races.query.all()
    Atribute = Atributes.query.all()
    Clan = Clans.query.all()
    arrayitems = []

    for armor in Armor:
        arrayitems.append(
            {"id": armor.id, "Name": armor.Name, "Cost": armor.Cost, "Weight": armor.Weight, "Category": "Доспехи",
             "CategoryName": armor.ArmorType})
    for magicalItem in MagicalItem:
        arrayitems.append(
            {"id": magicalItem.id, "Name": magicalItem.Name, "Cost": magicalItem.Cost, "Weight": magicalItem.Weight,
             "Category": "Магические предметы", "CategoryName": magicalItem.MagicalItemType})
    for weapoon in Weapoon:
        arrayitems.append({"id": weapoon.id, "Name": weapoon.Name, "Cost": weapoon.Cost, "Weight": weapoon.Weight,
                           "Category": "Оружие", "CategoryName": weapoon.WeapoonType})
    for equipment in Equipment:
        arrayitems.append(
            {"id": equipment.id, "Name": equipment.Name, "Cost": equipment.Cost, "Weight": equipment.Weight,
             "Category": "Снаряжение", "CategoryName": equipment.EquipmentType})
    for Tool in ToolOwnership:
        arrayitems.append(
            {"id": Tool.id, "Name": Tool.Name, "Cost": Tool.Cost, "Weight": Tool.Weight, "Category": "Инструменты",
             "CategoryName": Tool.ToolType})

    if current_user.is_authenticated:
        user = current_user
    else:
        user = []
    if request.method == 'POST':
        requestForm = request.form
        requestFiles = request.files
        return render_template("Index.html")
    else:
        return render_template("CreatePersonage.html", ActiveMagicalItems=MagicalItem, ActiveAromrs=Armor
                               , ActiveWeapoons=Weapoon, TypesMagic=TypeMagic,
                               SpellcastingCharacteristicses=Characteristic
                               , Spells=Spell, PossessionArmor=PossessionArmor, arrayitems=json.dumps(arrayitems),
                               GunOwnership=Weapoon,
                               ToolOwnership=ToolOwnership, Equipments=Equipment
                               , DamageResistance=DamageType, DamageImmunity=DamageType, Skills=Skill,
                               Languages=Language, Armors=Armor, Weapoons=Weapoon, MagicalItems=MagicalItem
                               , EffectsResistance=Effect, Effects=Effect, Abilities=Abilitie,
                               Characteristices=Characteristic
                               , Archetypes=Archetype, Classes=Class, Backgrounds=Background, Races=Race, user=user,
                               Atributes=Atribute, Clans=Clan, show_back_button=True)


@roles_accepted('Gamer')
@app.route("/EditPersonage", methods=['GET', 'POST'])
def EditPersonage():
    return render_template("EditPersonage.html", show_back_button=True)


@roles_accepted('Gamer')
@app.route("/VeiwPersonage", methods=['GET', 'POST'])
def VeiwPersonage():
    return render_template("VeiwPersonage.html", show_back_button=True)


@app.route("/VeiwMyGames", methods=['GET', 'POST'])
def VeiwMyGames():
    return render_template("VeiwMyGames.html", show_back_button=True)


@app.route("/ActiveGames", methods=['GET', 'POST'])
def ActiveGames():
    return render_template("ActiveGames.html", show_back_button=True)


@app.route("/CloseGames", methods=['GET', 'POST'])
def CloseGames():
    return render_template("CloseGames.html", show_back_button=True)


@roles_accepted('Master')
@app.route("/CreateNewGames", methods=['GET', 'POST'])
def CreateNewGames():
    return render_template("CreateNewGames.html", show_back_button=True)


@roles_accepted('Master')
@app.route("/EditMyGames", methods=['GET', 'POST'])
def EditMyGames():
    return render_template("EditMyGames.html", show_back_button=True)


@roles_accepted('Master')
@app.route("/PersonagesMyGames", methods=['GET', 'POST'])
def PersonagesMyGames():
    return render_template("PersonagesMyGames.html", show_back_button=True)


@app.route('/CreateUsers', methods=['GET', 'POST'])
def CreateUsers():
    msg = ""
    Roles = Role.query.all()
    if request.method == 'POST':
        user = User.query.filter_by(login=request.form['login']).first()
        if user:
            msg = "Пользователь уже существует"
            return render_template('LoginUsers.html', msg=msg)

        user = User(login=request.form['login'], active=1, password=request.form['password'])
        role = Role.query.filter_by(id=request.form['Role']).first()
        user.roles.append(role)
        db.session.add(user)
        db.session.commit()
        return render_template("Index.html")
    else:
        return render_template("LoginUsers.html", msg=msg, roles=Roles)


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


@app.route('/LoginUsers', methods=['GET', 'POST'])
def LoginUsers():
    msg = ""
    Roles = Role.query.all()
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
        return render_template('LoginUsers.html', msg=msg, roles=Roles, show_back_button=True)
    else:
        return render_template("LoginUsers.html", msg=msg, roles=Roles, show_back_button=True)


@app.route('/Logout')
@login_required
def logout():
    logout_user()
    return render_template("Index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, passthrough_errors=True,
            use_debugger=False, use_reloader=False)

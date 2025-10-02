from flask import (Flask, render_template, request, redirect)
from flask_login import login_user, login_required, logout_user, LoginManager
from flask_security import (roles_accepted, Security, SQLAlchemySessionUserDatastore, UserMixin, RoleMixin)
from functions.functions import appenddatas, parametrsoutput, OpenVeiwPost, OpenEditPost
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


Roles_Users = db.Table('Roles_Users',
        db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('Role.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id          = db.Column(db.Integer, autoincrement=True, primary_key=True)
    login       = db.Column(db.String, unique=True)
    password    = db.Column(db.String(255), nullable=False, server_default='')
    active      = db.Column(db.Boolean())
    roles       = db.relationship('Role', secondary=Roles_Users, backref='roled')


class Role(db.Model, RoleMixin):
    __tablename__ = 'Role'
    id       = db.Column(db.Integer(), primary_key=True)
    RoleName = db.Column(db.String(80), unique=True)
    name     = db.Column(db.String(80), unique=True)
    NameUser = db.Column(db.String(80), unique=True)


user_datastore  = SQLAlchemySessionUserDatastore(db.session, User, Role)
security        = Security(app, user_datastore)


@app.before_first_request
def create_tables():
    db.create_all()
    roles = Role.query.all()
    if len(roles) == 0:
        role1 = Role(RoleName='Gamer', name='Gamer', NameUser='Игрок')
        role2 = Role(RoleName='Master', name='Master', NameUser='Мастер')
        role3 = Role(RoleName='Admin', name='Admin', NameUser='Администратор')
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
    if request.method == 'POST':
        AbilitiesName   = request.form['AbilitieName']
        Discription     = request.form['Discription']
        abilities       = Abilities(Name=AbilitiesName, Discription=Discription)
        try:
            db.session.add(abilities)
            db.session.commit()
            return render_template("CreatePosts/CreateAbilities.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateAbilities.html")


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
    if request.method == 'POST':
        ArchetypeName   = request.form['ArchetypeName']
        Discription     = request.form['Discription']
        ArmorClass      = request.form['ArmorClass']
        if 'NotArmorSafe' in request.form:
            NotArmorSafe=True
        else:
            NotArmorSafe=False
        archetypes = Archetypes(Name=ArchetypeName, Discription=Discription, NotArmorSafe=NotArmorSafe
                                , ArmorClass=ArmorClass)
        MassivClasses               = parametrsoutput(request.form['ClassName'])
        MassivClassApd              = [MassivClasses, Classes, archetypes.R_Class]
        MassivCharacteristices      = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, archetypes.Characteristic]
        MassivDamageResistance      = parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, archetypes.DamageResistance]
        MassivDamageImmunity        = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, archetypes.DamageImmunity]
        MassivEffectsResistance     = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, archetypes.EffectsResistance]
        MassivSpells                = parametrsoutput(request.form['Spells'])
        MassivSpellsApd             = [MassivSpells, Spells, archetypes.Spell]
        MassivSkills                = parametrsoutput(request.form['Skills'])
        MassivSkillsApd             = [MassivSkills, Skills, archetypes.Skill]
        MassivPossessionArmor       = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, archetypes.PossessionArmor]
        MassivGunOwnership          = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, archetypes.GunOwnership]
        MassivToolOwnership         = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, archetypes.ToolOwnership]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, archetypes.Language]
        MassivAbilities             = parametrsoutput(request.form['Abilities'])
        MassivAbilitiesApd          = [MassivAbilities, Abilities, archetypes.Abilities]
        MassivDates                 = [MassivClassApd,MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(archetypes)
                db.session.commit()
                return render_template("CreatePosts/CreateArchetypes.html", Characteristices=characteristices
                                       , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                       , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities, Classes=classes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateArchetypes.html", Characteristices=characteristices
                                   , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                   , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities, Classes=classes)


@app.route("/CreateArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmors():
    armorTypes = ArmorTypes.query.all()
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
        MassivArmorTypes    = parametrsoutput(request.form['ArmorTypes'])
        MassivArmorTypesApd = [MassivArmorTypes, ArmorTypes, armors.ArmorType]
        MassivDates         = [MassivArmorTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(armors)
                db.session.commit()
                return render_template("CreatePosts/CreateArmors.html", ArmorTypes=armorTypes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateArmors.html", ArmorTypes=armorTypes)


@app.route("/CreateArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmorTypes():
    if request.method == 'POST':
        ArmorTypeName   = request.form['ArmorTypeName']
        Discription     = request.form['Discription']
        ArmorType       = ArmorTypes(Name=ArmorTypeName, Discription=Discription)
        try:
            db.session.add(ArmorType)
            db.session.commit()
            return render_template("CreatePosts/CreateArmorTypes.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateArmorTypes.html")


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
    if request.method == 'POST':
        AttributeName   = request.form['AttributeName']
        Discription     = request.form['Discription']
        Attribute                   = Atributes(Name=AttributeName, Discription=Discription)
        MassivCharacteristices      = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Attribute.Characteristic]
        MassivDamageResistance      = parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, Attribute.DamageResistance]
        MassivDamageImmunity        = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, Attribute.DamageImmunity]
        MassivEffectsResistance     = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Attribute.EffectsResistance]
        MassivSpells                = parametrsoutput(request.form['Spells'])
        MassivSpellsApd             = [MassivSpells, Spells, Attribute.Spell]
        MassivSkills                = parametrsoutput(request.form['Skills'])
        MassivSkillsApd             = [MassivSkills, Skills, Attribute.Skill]
        MassivPossessionArmor       = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Attribute.PossessionArmor]
        MassivGunOwnership          = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Attribute.GunOwnership]
        MassivToolOwnership         = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Attribute.ToolOwnership]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, Attribute.Language]
        MassivAbilities             = parametrsoutput(request.form['Abilities'])
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Attribute.Abilities]
        MassivDates                 = [MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Attribute)
                db.session.commit()
                return render_template("CreatePosts/CreateAtributes.html", Characteristices=characteristices
                                           , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                           , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateAtributes.html", Characteristices=characteristices
                                       , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                       , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities)


@app.route("/CreateBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateBackgrounds():
    characteristices = Characteristices.query.all()
    spells           = Spells.query.all()
    skills           = Skills.query.all()
    ToolOwnership    = Tools.query.all()
    languages        = Languages.query.all()
    if request.method == 'POST':
        BackgroundName   = request.form['BackgroundName']
        Discription     = request.form['Discription']
        Background                   = Backgrounds(Name=BackgroundName, Discription=Discription)
        MassivCharacteristices      = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Background.Characteristic]
        MassivSpells                = parametrsoutput(request.form['Spells'])
        MassivSpellsApd             = [MassivSpells, Spells, Background.Spell]
        MassivSkills                = parametrsoutput(request.form['Skills'])
        MassivSkillsApd             = [MassivSkills, Skills, Background.Skill]
        MassivToolOwnership         = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Background.ToolOwnership]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, Background.Language]
        MassivDates                 = [MassivCharacteristicesApd,MassivSpellsApd,MassivSkillsApd
                                        ,MassivToolOwnershipApd,MassivLanguagesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Background)
                db.session.commit()
                return render_template("CreatePosts/CreateBackgrounds.html", Characteristices=characteristices
                                           , Spells=spells, Skills=skills, Tools=ToolOwnership, Languages=languages)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateBackgrounds.html", Characteristices=characteristices
                                           , Spells=spells, Skills=skills, Tools=ToolOwnership, Languages=languages)


@app.route("/CreateCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateCharacteristices():
    skills = Skills.query.all()
    if request.method == 'POST':
        CharacteristicName   = request.form['CharacteristicName']
        Discription          = request.form['Discription']
        Characteristic       = Characteristices(Name=CharacteristicName, Discription=Discription)
        MassivSkills         = parametrsoutput(request.form['Skills'])
        MassivSkillsApd      = [MassivSkills, Skills, Characteristic.Skill]
        MassivDates          = [MassivSkillsApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Characteristic)
                db.session.commit()
                return render_template("CreatePosts/CreateCharacteristices.html", Skills=skills)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateCharacteristices.html", Skills=skills)


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
        MassivCharacteristices      = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Class.Characteristic]
        MassivSpells                = parametrsoutput(request.form['Spells'])
        MassivSpellsApd             = [MassivSpells, Spells, Class.Spell]
        MassivSkills                = parametrsoutput(request.form['Skills'])
        MassivSkillsApd             = [MassivSkills, Skills, Class.Skill]
        MassivPossessionArmor       = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Class.PossessionArmor]
        MassivGunOwnership          = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Class.GunOwnership]
        MassivToolOwnership         = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Class.ToolOwnership]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, Class.Language]
        MassivDates                 = [MassivCharacteristicesApd
                           ,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Class)
                db.session.commit()
                return render_template("CreatePosts/CreateClasses.html", Characteristices=characteristices
                                   , Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                   , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateClasses.html", Characteristices=characteristices
                                   , Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                   , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages)


@app.route("/CreateDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateDamageTypes():
    if request.method == 'POST':
        DamageTypeName  = request.form['DamageTypeName']
        Discription     = request.form['Discription']
        DamageType      = DamageTypes(Name=DamageTypeName, Discription=Discription)
        try:
            db.session.add(DamageType)
            db.session.commit()
            return render_template("CreatePosts/CreateDamageTypes.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateDamageTypes.html")


@app.route("/CreateEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEffects():
    if request.method == 'POST':
        EffectName  = request.form['EffectName']
        Discription = request.form['Discription']
        Effect      = Effects(Name=EffectName, Discription=Discription)
        try:
            db.session.add(Effect)
            db.session.commit()
            return render_template("CreatePosts/CreateEffects.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateEffects.html")


@app.route("/CreateEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipments():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        EquipmentName   = request.form['EquipmentName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Cost        = request.form['Cost']
        Equipment = Equipments(Name=EquipmentName, Discription=Discription, Weight=Weight, Cost=Cost)
        MassivEquipmentTypes    = parametrsoutput(request.form['EquipmentTypes'])
        MassivEquipmentTypesApd = [MassivEquipmentTypes, EquipmentTypes, Equipment.EquipmentType]
        MassivDates             = [MassivEquipmentTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Equipment)
                db.session.commit()
                return render_template("CreatePosts/CreateEquipments.html", EquipmentTypes=equipmentTypes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateEquipments.html", EquipmentTypes=equipmentTypes)


@app.route("/CreateEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipmentTypes():
    if request.method == 'POST':
        EquipmentTypeName   = request.form['EquipmentTypeName']
        Discription         = request.form['Discription']
        EquipmentType       = EquipmentTypes(Name=EquipmentTypeName, Discription=Discription)
        try:
            db.session.add(EquipmentType)
            db.session.commit()
            return render_template("CreatePosts/CreateEquipmentTypes.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateEquipmentTypes.html")


@app.route("/CreateFeatures", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateFeatures():
    if request.method == 'POST':
        FeaturesName     = request.form['FeaturesName']
        Discription      = request.form['Discription']
        WeapoonType      = WeapoonTypes(Name=FeaturesName, Discription=Discription)
        try:
            db.session.add(WeapoonType)
            db.session.commit()
            return render_template("CreatePosts/CreateFeatures.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateFeatures.html")


@app.route("/CreateLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateLanguages():
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
            return render_template("CreatePosts/CreateLanguages.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateLanguages.html")


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
    if request.method == 'POST':
        MagicalItemsName    = request.form['MagicalItemsName']
        Discription         = request.form['Discription']
        PowerBonus          = request.form['PowerBonus']
        ArmorBonus          = request.form['ArmorBonus']
        MagicalItem         = MagicalItems(Name=MagicalItemsName, Discription=Discription, ArmorBonus=ArmorBonus
                                , PowerBonus=PowerBonus)
        MassivMagicalItemTypes      = parametrsoutput(request.form['MagicalItemTypeName'])
        MassivMagicalItemTypesApd   = [MassivMagicalItemTypes, MagicalItemsTypes, MagicalItem.Class]
        MassivCharacteristices      = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, MagicalItem.Characteristic]
        MassivDamageResistance      = parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, MagicalItem.DamageResistance]
        MassivDamageImmunity        = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, MagicalItem.DamageImmunity]
        MassivEffectsResistance     = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, MagicalItem.EffectsResistance]
        MassivEffects               = parametrsoutput(request.form['Effects'])
        MassivEffectsApd            = [MassivEffects, Effects, MagicalItem.EffectsResistance]
        MassivSpells                = parametrsoutput(request.form['Spells'])
        MassivSpellsApd             = [MassivSpells, Spells, MagicalItem.Spell]
        MassivSkills                = parametrsoutput(request.form['Skills'])
        MassivSkillsApd             = [MassivSkills, Skills, MagicalItem.Skill]
        MassivPossessionArmor       = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, MagicalItem.PossessionArmor]
        MassivGunOwnership          = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, MagicalItem.GunOwnership]
        MassivToolOwnership         = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, MagicalItem.ToolOwnership]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, MagicalItem.Language]
        MassivAbilities             = parametrsoutput(request.form['Abilities'])
        MassivAbilitiesApd          = [MassivAbilities, Abilities, MagicalItem.Abilities]
        MassivArmorTypes            = parametrsoutput(request.form['ArmorTypes'])
        MassivArmorTypesApd         = [MassivArmorTypes, Armors, MagicalItem.ArmorTypeItem]
        MassivWeapoonTypes          = parametrsoutput(request.form['WeapoonTypes'])
        MassivWeapoonTypesApd       = [MassivWeapoonTypes, Weapoons, MagicalItem.WeapoonTypeItem]
        MassivDates                 = [MassivMagicalItemTypesApd,MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivEffectsApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd
                            ,MassivGunOwnershipApd,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd,MassivArmorTypesApd,MassivWeapoonTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(MagicalItem)
                db.session.commit()
                return render_template("CreatePosts/CreateMagicalItems.html", Characteristices=characteristices
                                       , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                       , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities
                                       ,Armors=armors)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateMagicalItems.html", Characteristices=characteristices
                                   , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                   , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities
                                   ,  Armors=armors)


@app.route("/CreateMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateMagicalItemTypes():
    if request.method == 'POST':
        MagicalItemTypeName = request.form['MagicalItemTypeName']
        Discription         = request.form['Discription']
        MagicalItemsType    = MagicalItemsTypes(Name=MagicalItemTypeName, Discription=Discription)
        try:
            db.session.add(MagicalItemsType)
            db.session.commit()
            return render_template("CreatePosts/CreateMagicalItemTypes.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateMagicalItemTypes.html")


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
    classes          = Classes.query.all()
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
        MassivCharacteristices      = parametrsoutput(request.form['Characteristices'])
        MassivCharacteristicesApd   = [MassivCharacteristices, Characteristices, Race.Characteristic]
        MassivDamageResistance      = parametrsoutput(request.form['DamageResistance'])
        MassivDamageResistanceApd   = [MassivDamageResistance, DamageTypes, Race.DamageResistance]
        MassivDamageImmunity        = parametrsoutput(request.form['DamageImmunity'])
        MassivDamageImmunityApd     = [MassivDamageImmunity, DamageTypes, Race.DamageImmunity]
        MassivEffectsResistance     = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Race.EffectsResistance]
        MassivSpells                = parametrsoutput(request.form['Spells'])
        MassivSpellsApd             = [MassivSpells, Spells, Race.Spell]
        MassivSkills                = parametrsoutput(request.form['Skills'])
        MassivSkillsApd             = [MassivSkills, Skills, Race.Skill]
        MassivPossessionArmor       = parametrsoutput(request.form['PossessionArmor'])
        MassivPossessionArmorApd    = [MassivPossessionArmor, ArmorTypes, Race.PossessionArmor]
        MassivGunOwnership          = parametrsoutput(request.form['GunOwnership'])
        MassivGunOwnershipApd       = [MassivGunOwnership, Weapoons, Race.GunOwnership]
        MassivToolOwnership         = parametrsoutput(request.form['ToolOwnership'])
        MassivToolOwnershipApd      = [MassivToolOwnership, Tools, Race.ToolOwnership]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, Race.Language]
        MassivAbilities             = parametrsoutput(request.form['Abilities'])
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Race.Abilities]
        MassivDates                 = [MassivCharacteristicesApd,MassivDamageResistanceApd,MassivDamageImmunityApd
                           ,MassivEffectsResistanceApd,MassivSpellsApd,MassivSkillsApd,MassivPossessionArmorApd,MassivGunOwnershipApd
                           ,MassivToolOwnershipApd,MassivLanguagesApd,MassivAbilitiesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Race)
                db.session.commit()
                return render_template("CreatePosts/CreateRaces.html", Characteristices=characteristices
                                       , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                       , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities, Classes=classes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateRaces.html", Characteristices=characteristices
                                   , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                   , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities, Classes=classes)


@app.route("/CreateSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSkills():
    if request.method == 'POST':
        SkillName   = request.form['SkillName']
        Discription = request.form['Discription']
        Skill       = Skills(Name=SkillName, Discription=Discription)
        try:
            db.session.add(Skill)
            db.session.commit()
            return render_template("CreatePosts/CreateSkills.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateSkills.html")


@app.route("/CreateSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSpells():
    damageTypes      = DamageTypes.query.all()
    effects          = Effects.query.all()
    languages        = Languages.query.all()
    abilities        = Abilities.query.all()
    classes          = Classes.query.all()
    archetypes       = Archetypes.query.all()
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
        MassivClasses               = parametrsoutput(request.form['Classes'])
        MassivClassesApd            = [MassivClasses, Classes, Spell.Class]
        MassivArchetypes            = parametrsoutput(request.form['Archetypes'])
        MassivArchetypesApd         = [MassivArchetypes, Archetypes, Spell.Archetype]
        MassivDamageTypes           = parametrsoutput(request.form['DamageTypes'])
        MassivDamageTypessApd       = [MassivDamageTypes, DamageTypes, Spell.DamageType]
        MassivLanguages             = parametrsoutput(request.form['Languages'])
        MassivLanguagesApd          = [MassivLanguages, Languages, Spell.Language]
        MassivAbilities             = parametrsoutput(request.form['Abilities'])
        MassivAbilitiesApd          = [MassivAbilities, Abilities, Spell.Abilities]
        MassivEffectsResistance     = parametrsoutput(request.form['EffectsResistance'])
        MassivEffectsResistanceApd  = [MassivEffectsResistance, Effects, Spell.EffectsResistance]
        MassivEffects               = parametrsoutput(request.form['Effects'])
        MassivEffectsApd            = [MassivEffects, Effects, Spell.Effects]
        MassivDates                 = [MassivClassesApd,MassivArchetypesApd,MassivDamageTypessApd,MassivLanguagesApd
                                       ,MassivAbilitiesApd,MassivEffectsResistanceApd,MassivEffectsApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Spell)
                db.session.commit()
                return render_template("CreatePosts/CreateSpells.html", Archetypes=archetypes
                                       , DamageTypes=damageTypes, Effects=effects, Languages=languages, Abilities=abilities
                                       , Classes=classes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateSpells.html", Archetypes=archetypes
                                       , DamageTypes=damageTypes, Effects=effects, Languages=languages, Abilities=abilities
                                       , Classes=classes)


@app.route("/CreateTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateTools():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        ToolName    = request.form['ToolName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Cost        = request.form['Cost']
        Tool        = Tools(Name=ToolName, Discription=Discription, Weight=Weight, Cost=Cost)
        MassivToolTypes    = parametrsoutput(request.form['ToolTypes'])
        MassivToolTypesApd = [MassivToolTypes, ToolTypes, Tool.ToolType]
        MassivDates         = [MassivToolTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Tool)
                db.session.commit()
                return render_template("CreatePosts/CreateTools.html", ToolTypes=toolTypes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateTools.html", ToolTypes=toolTypes)


@app.route("/CreateToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateToolTypes():
    if request.method == 'POST':
        ToolTypeName  = request.form['ToolTypeName']
        Discription   = request.form['Discription']
        ToolType      = ToolTypes(Name=ToolTypeName, Discription=Discription)
        try:
            db.session.add(ToolType)
            db.session.commit()
            return render_template("CreatePosts/CreateToolTypes.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateToolTypes.html")


@app.route("/CreateWeapoons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoons():
    toolTypes   = ToolTypes.query.all()
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        WeapoonName    = request.form['WeapoonName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Cost        = request.form['Cost']
        Damage      = request.form['Damage']
        Weapoon               = Weapoons(Name=WeapoonName, Discription=Discription, Weight=Weight
                                         , Cost=Cost, Damage=Damage)
        MassivWeapoonTypes    = parametrsoutput(request.form['WeapoonTypes'])
        MassivWeapoonTypesApd = [MassivWeapoonTypes, WeapoonTypes, Weapoon.WeapoonType]
        MassivDamageTypes     = parametrsoutput(request.form['DamageTypes'])
        MassivDamageTypesApd  = [MassivDamageTypes, DamageTypes, Weapoon.DamageType]
        MassivDates           = [MassivWeapoonTypesApd,MassivDamageTypesApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Weapoon)
                db.session.commit()
                return render_template("CreatePosts/CreateWeapoons.html", ToolTypes=toolTypes, DamageTypes=damageTypes)
            except:
                return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateWeapoons.html", ToolTypes=toolTypes, DamageTypes=damageTypes)


@app.route("/CreateWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoonTypes():
    if request.method == 'POST':
        WeapoonTypeName  = request.form['WeapoonTypeName']
        Discription      = request.form['Discription']
        WeapoonType      = WeapoonTypes(Name=WeapoonTypeName, Discription=Discription)
        try:
            db.session.add(WeapoonType)
            db.session.commit()
            return render_template("CreatePosts/CreateWeapoonTypes.html")
        except:
            return render_template("CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateWeapoonTypes.html")


@app.route("/VeiwAbilities", methods=['GET', 'POST'])
def VeiwAbilities():
    abilities = Abilities.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Abilities', Date_id)
    return render_template("VeiwPosts/VeiwAbilities.html", Abilities=abilities)


@app.route("/VeiwArchetypes", methods=['GET', 'POST'])
def VeiwArchetypes():
    archetypes = Archetypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Archetypes', Date_id)
    return render_template("VeiwPosts/VeiwArchetypes.html", Archetypes=archetypes)


@app.route("/VeiwArmors", methods=['GET', 'POST'])
def VeiwArmors():
    armors = Armors.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Armors', Date_id)
    return render_template("VeiwPosts/VeiwArmors.html", Armors=armors)


@app.route("/VeiwArmorTypes", methods=['GET', 'POST'])
def VeiwArmorTypes():
    armorTypes = ArmorTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('ArmorTypes', Date_id)
    return render_template("VeiwPosts/VeiwArmorTypes.html", ArmorTypes=armorTypes)


@app.route("/VeiwAtributes", methods=['GET', 'POST'])
def VeiwAtributes():
    atributes = Atributes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Atributes', Date_id)
    return render_template("VeiwPosts/VeiwAtributes.html", Atributes=atributes)


@app.route("/VeiwBackgrounds", methods=['GET', 'POST'])
def VeiwBackgrounds():
    backgrounds = Backgrounds.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Backgrounds', Date_id)
    return render_template("VeiwPosts/VeiwBackgrounds.html", Backgrounds=backgrounds)


@app.route("/VeiwCharacteristices", methods=['GET', 'POST'])
def VeiwCharacteristices():
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Characteristices', Date_id)
    return render_template("VeiwPosts/VeiwCharacteristices.html", Characteristices=characteristices)


@app.route("/VeiwClasses", methods=['GET', 'POST'])
def VeiwClasses():
    classes = Classes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Classes', Date_id)
    return render_template("VeiwPosts/VeiwClasses.html", Classes=classes)


@app.route("/VeiwDamageTypes", methods=['GET', 'POST'])
def VeiwDamageTypes():
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('DamageTypes', Date_id)
    return render_template("VeiwPosts/VeiwDamageTypes.html", DamageTypes=damageTypes)


@app.route("/VeiwEffects", methods=['GET', 'POST'])
def VeiwEffects():
    effects = Effects.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Effects', Date_id)
    return render_template("VeiwPosts/VeiwEffects.html", Effects=effects)


@app.route("/VeiwEquipments", methods=['GET', 'POST'])
def VeiwEquipments():
    equipments = Equipments.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Equipments', Date_id)
    return render_template("VeiwPosts/VeiwEquipments.html", Equipments=equipments)


@app.route("/VeiwEquipmentTypes", methods=['GET', 'POST'])
def VeiwEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('EquipmentTypes', Date_id)
    return render_template("VeiwPosts/VeiwEquipmentTypes.html", EquipmentTypes=equipmentTypes)


@app.route("/VeiwFeatures", methods=['GET', 'POST'])
def VeiwFeatures():
    features = Features.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Features', Date_id)
    return render_template("VeiwPosts/VeiwFeatures.html", Features=features)


@app.route("/VeiwLanguages", methods=['GET', 'POST'])
def VeiwLanguages():
    languages = Languages.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Languages', Date_id)
    return render_template("VeiwPosts/VeiwLanguages.html", Languages=languages)


@app.route("/VeiwMagicalItems", methods=['GET', 'POST'])
def VeiwMagicalItems():
    magicalItems = MagicalItems.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('MagicalItems', Date_id)
    return render_template("VeiwPosts/VeiwMagicalItems.html", MagicalItems=magicalItems)


@app.route("/VeiwMagicalItemTypes", methods=['GET', 'POST'])
def VeiwMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('MagicalItemsTypes', Date_id)
    return render_template("VeiwPosts/VeiwMagicalItemTypes.html", MagicalItemsTypes=magicalItemsTypes)


@app.route("/VeiwRaces", methods=['GET', 'POST'])
def VeiwRaces():
    races = Races.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Races', Date_id)
    return render_template("VeiwPosts/VeiwRaces.html", Races=races)


@app.route("/VeiwSkills", methods=['GET', 'POST'])
def VeiwSkills():
    skills = Skills.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Skills', Date_id)
    return render_template("VeiwPosts/VeiwSkills.html", Skills=skills)


@app.route("/VeiwSpells", methods=['GET', 'POST'])
def VeiwSpells():
    spells = Spells.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Spells', Date_id)
    return render_template("VeiwPosts/VeiwSpells.html", Spells=spells)


@app.route("/VeiwTools", methods=['GET', 'POST'])
def VeiwTools():
    tools = Tools.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Tools', Date_id)
    return render_template("VeiwPosts/VeiwTools.html", Tools=tools)


@app.route("/VeiwToolTypes", methods=['GET', 'POST'])
def VeiwToolTypes():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('ToolTypes', Date_id)
    return render_template("VeiwPosts/VeiwToolTypes.html", ToolTypes=toolTypes)


@app.route("/VeiwWeapoons", methods=['GET', 'POST'])
def VeiwWeapoons():
    weapoons = Weapoons.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('Weapoons', Date_id)
    return render_template("VeiwPosts/VeiwWeapoons.html", Weapoons=weapoons)


@app.route("/VeiwWeapoonTypes", methods=['GET', 'POST'])
def VeiwWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenVeiwPost('WeapoonTypes', Date_id)
    return render_template("VeiwPosts/VeiwWeapoonTypes.html", WeapoonTypes=weapoonTypes)


@app.route("/EditAbilities", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditAbilities():
    abilities = Abilities.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Abilities', Date_id)
    return render_template("EditPosts/EditAbilities.html", Abilities=abilities)


@app.route("/EditArchetypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArchetypes():
    archetypes = Archetypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Archetypes', Date_id)
    return render_template("EditPosts/EditArchetypes.html", Archetypes=archetypes)


@app.route("/EditArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArmors():
    armors = Armors.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Armors', Date_id)
    return render_template("EditPosts/EditArmors.html", Armors=armors)


@app.route("/EditArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditArmorTypes():
    armorTypes = ArmorTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('ArmorTypes', Date_id)
    return render_template("EditPosts/EditArmorTypes.html", ArmorTypes=armorTypes)


@app.route("/EditAtributes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditAtributes():
    atributes = Atributes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Atributes', Date_id)
    return render_template("EditPosts/EditAtributes.html", Atributes=atributes)


@app.route("/EditBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditBackgrounds():
    backgrounds = Backgrounds.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Backgrounds', Date_id)
    return render_template("EditPosts/EditBackgrounds.html", Backgrounds=backgrounds)


@app.route("/EditCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditCharacteristices():
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Characteristices', Date_id)
    return render_template("EditPosts/EditCharacteristices.html", Characteristices=characteristices)


@app.route("/EditClasses", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditClasses():
    classes = Classes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Classes', Date_id)
    return render_template("EditPosts/EditClasses.html", Classes=classes)


@app.route("/EditDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditDamageTypes():
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('DamageTypes', Date_id)
    return render_template("EditPosts/EditDamageTypes.html", DamageTypes=damageTypes)


@app.route("/EditEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEffects():
    effects = Effects.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Effects', Date_id)
    return render_template("EditPosts/EditEffects.html", Effects=effects)


@app.route("/EditEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEquipments():
    equipments = Equipments.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Equipments', Date_id)
    return render_template("EditPosts/EditEquipments.html", Equipments=equipments)


@app.route("/EditEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('EquipmentTypes', Date_id)
    return render_template("EditPosts/EditEquipmentTypes.html", EquipmentTypes=equipmentTypes)


@app.route("/EditFeatures", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditFeatures():
    features = Features.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Features', Date_id)
    return render_template("EditPosts/EditFeatures.html", Features=features)


@app.route("/EditLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditLanguages():
    languages = Languages.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Languages', Date_id)
    return render_template("EditPosts/EditLanguages.html", Languages=languages)


@app.route("/EditMagicalItems", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMagicalItems():
    magicalItems = MagicalItems.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('MagicalItems', Date_id)
    return render_template("EditPosts/EditMagicalItems.html", MagicalItems=magicalItems)


@app.route("/EditMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('MagicalItemsTypes', Date_id)
    return render_template("EditPosts/EditMagicalItemTypes.html", MagicalItemsTypes=magicalItemsTypes)


@app.route("/EditRaces", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditRaces():
    races = Races.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Races', Date_id)
    return render_template("EditPosts/EditRaces.html", Races=races)


@app.route("/EditSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditSkills():
    skills = Skills.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Skills', Date_id)
    return render_template("EditPosts/EditSkills.html", Skills=skills)


@app.route("/EditSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditSpells():
    spells = Spells.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Spells', Date_id)
    return render_template("EditPosts/EditSpells.html", Spells=spells)


@app.route("/EditTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditTools():
    tools = Tools.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Tools', Date_id)
    return render_template("EditPosts/EditTools.html", Tools=tools)


@app.route("/EditToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditToolTypes():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('ToolTypes', Date_id)
    return render_template("EditPosts/EditToolTypes.html", ToolTypes=toolTypes)


@app.route("/EditWeapoons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditWeapoons():
    weapoons = Weapoons.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('Weapoons', Date_id)
    return render_template("EditPosts/EditWeapoons.html", Weapoons=weapoons)


@app.route("/EditWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def EditWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    if request.method == 'POST':
        Date_id = request.form['Date_id']
        return OpenEditPost('WeapoonTypes', Date_id)
    return render_template("EditPosts/EditWeapoonTypes.html", WeapoonTypes=weapoonTypes)


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

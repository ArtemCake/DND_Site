from flask import (Flask, render_template, request, redirect)
from flask_login import login_user, login_required, logout_user, LoginManager
from flask_security import (roles_accepted, Security, SQLAlchemySessionUserDatastore, UserMixin, RoleMixin)
from functions.functions import parametrsoutput

import logging
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
app.config['SECRET_KEY'] = 'MY_SECRET'
app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)


logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


Roles_Users = db.Table('Roles_Users',
        db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('Role.id')))


Attributes_Skills = db.Table('Attributes_Skills',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Archetypes_Skills = db.Table('Archetypes_Skills',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Attributes_ResistanceDamageTypes = db.Table('Attributes_ResistanceDamageTypes',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Attributes_ImmunityDamageTypes = db.Table('Attributes_ImmunityDamageTypes',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Attributes_ArmorTypes = db.Table('Attributes_ArmorTypes',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Attributes_Weapoons = db.Table('Attributes_Weapoons',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Attributes_Tools = db.Table('Attributes_Tools',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')))

Archetypes_ArmorTypes = db.Table('Archetypes_ArmorTypes',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Archetypes_Weapoons = db.Table('Archetypes_Weapoons',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Archetypes_Tools = db.Table('Archetypes_Tools',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')))


Archetypes_ResistanceDamageTypes = db.Table('Archetypes_ResistanceDamageTypes',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Archetypes_ImmunityDamageTypes = db.Table('Archetypes_ImmunityDamageTypes',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Archetypes_Characteristices = db.Table('Archetypes_Characteristices',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


MagicalItems_Characteristices = db.Table('MagicalItems_Characteristices',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


RaceDND_Characteristices = db.Table('RaceDND_Characteristices',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


BackgroundDND_Characteristices = db.Table('BackgroundDND_Characteristices',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


BackgroundDND_ResistanceDamageTypes = db.Table('BackgroundDND_ResistanceDamageTypes',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


BackgroundDND_ImmunityDamageTypes = db.Table('BackgroundDND_ImmunityDamageTypes',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Attributes_Characteristices = db.Table('Attributes_Characteristices',
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


ClassPersonDND_Characteristices = db.Table('ClassPersonDND_Characteristices',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


RaceDND_LanguageDND = db.Table('RaceDND_LanguageDND',
        db.Column('LanguageDND_id', db.Integer(), db.ForeignKey('LanguageDND.id')),
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')))


Archetypes_LanguageDND = db.Table('Archetypes_LanguageDND',
        db.Column('LanguageDND_id', db.Integer(), db.ForeignKey('LanguageDND.id')),
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')))


BackgroundDND_LanguageDND = db.Table('BackgroundDND_LanguageDND',
        db.Column('LanguageDND_id', db.Integer(), db.ForeignKey('LanguageDND.id')),
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')))


BackgroundDND_SpellDND = db.Table('BackgroundDND_SpellDND',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')))


Attributes_LanguageDND = db.Table('Attributes_LanguageDND',
        db.Column('LanguageDND_id', db.Integer(), db.ForeignKey('LanguageDND.id')),
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')))


ClassPersonDND_LanguageDND = db.Table('ClassPersonDND_LanguageDND',
        db.Column('LanguageDND_id', db.Integer(), db.ForeignKey('LanguageDND.id')),
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')))


MagicalItems_LanguageDND = db.Table('MagicalItems_LanguageDND',
        db.Column('LanguageDND_id', db.Integer(), db.ForeignKey('LanguageDND.id')),
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')))


SpellDND_MagicalItems = db.Table('SpellDND_MagicalItems',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')))


RaceDND_SpellDND = db.Table('RaceDND_SpellDND',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('Race_id', db.Integer(), db.ForeignKey('RaceDND.id')))


Attributes_SpellDND = db.Table('Attributes_SpellDND',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('Attributes_id', db.Integer(), db.ForeignKey('Attributes.id')))


SpellDND_ClassPerson = db.Table('SpellDND_ClassPerson',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('ClassPerson_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')))


SpellDND_Archetypes = db.Table('SpellDND_Archetypes',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')))


ClassPersonDND_Archetypes = db.Table('ClassPersonDND_Archetypes',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')))


Armor_ArmorTypes = db.Table('Armors_ArmorTypes',
        db.Column('Armors_id', db.Integer(), db.ForeignKey('Armors.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Tool_ToolTypes = db.Table('Tool_ToolTypes',
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')),
        db.Column('ToolTypes_id', db.Integer(), db.ForeignKey('ToolTypes.id')))


Equipments_EquipmentTypes = db.Table('Equipments_EquipmentTypes',
        db.Column('Equipments_id', db.Integer(), db.ForeignKey('Equipments.id')),
        db.Column('EquipmentTypes_id', db.Integer(), db.ForeignKey('EquipmentTypes.id')))


Weapoon_WeapoonTypes = db.Table('Weapoon_WeapoonTypes',
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')),
        db.Column('WeapoonTypes_id', db.Integer(), db.ForeignKey('WeapoonTypes.id')))


Weapoons_DamageTypes = db.Table('Weapoons_DamageTypes',
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


BackgroundDND_Skills = db.Table('BackgroundDND_Skills',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


MagicalItems_Skills = db.Table('MagicalItems_Skills',
        db.Column('BMagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


ClassPersonDND_Skills = db.Table('ClassPersonDND_Skills',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


RaceDND_Skills = db.Table('RaceDND_Skills',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


SpellDND_DamageTypes = db.Table('SpellDND_DamageTypes',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


ClassPersonDND_SpellDND = db.Table('ClassPersonDND_SpellDND',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')))


Archetypes_SpellDND = db.Table('Archetypes_SpellDND',
        db.Column('SpellDND_id', db.Integer(), db.ForeignKey('SpellDND.id')),
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')))


RaceDND_ResistanceDamageTypes = db.Table('RaceDND_ResistanceDamageTypes',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


RaceDND_ImmunityDamageTypes = db.Table('RaceDND_ImmunityDamageTypes',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


ClassPersonDND_ResistanceDamageTypes = db.Table('ClassPersonDND_ResistanceDamageTypes',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


ClassPersonDND_ArmorTypes = db.Table('ClassPersonDND_ArmorTypes',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


ClassPersonDND_Weapoons = db.Table('ClassPersonDND_Weapoons',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


ClassPersonDND_Tools = db.Table('ClassPersonDND_Tools',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')))


RaceDND_ArmorTypes = db.Table('RaceDND_ArmorTypes',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


RaceDND_Weapoons = db.Table('RaceDND_Weapoons',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


RaceDND_Tools = db.Table('RaceDND_Tools',
        db.Column('RaceDND_id', db.Integer(), db.ForeignKey('RaceDND.id')),
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')))


BackgroundDND_ArmorTypes = db.Table('BackgroundDND_ArmorTypes',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


BackgroundDND_Weapoons = db.Table('BackgroundDND_Weapoons',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


BackgroundDND_Tools = db.Table('BackgroundDND_Tools',
        db.Column('BackgroundDND_id', db.Integer(), db.ForeignKey('BackgroundDND.id')),
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')))


MagicalItems_ArmorTypes = db.Table('MagicalItems_ArmorTypes',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


MagicalItems_Weapoons = db.Table('MagicalItems_Weapoons',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


MagicalItems_Tools = db.Table('MagicalItems_Tools',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')))


ClassPersonDND_ImmunityDamageTypes = db.Table('ClassPersonDND_ImmunityDamageTypes',
        db.Column('ClassPersonDND_id', db.Integer(), db.ForeignKey('ClassPersonDND.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


MagicalItems_ResistanceDamageTypes = db.Table('MagicalItems_ResistanceDamageTypes',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


MagicalItems_ImmunityDamageTypes = db.Table('MagicalItems_ImmunityDamageTypes',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


class Archetypes(db.Model):
    __tablename__ = 'Archetypes'
    id                  = db.Column(db.Integer, primary_key=True)
    ArchetypeName       = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    ArmorClass          = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Archetypes_Characteristices, backref='ArchetypesCharacteristices')
    DamageResistance    = db.relationship('DamageTypes', secondary=Archetypes_ResistanceDamageTypes, backref='ArchetypesResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=Archetypes_ImmunityDamageTypes, backref='ArchetypesImmunityDamageTypesDND')
    ClassPerson         = db.relationship('ClassPersonDND', secondary=ClassPersonDND_Archetypes, backref='ArchetypesDND')
    Spell               = db.relationship('SpellDND', secondary=SpellDND_Archetypes, backref='ArchetypesDND')
    Skill               = db.relationship('Skills', secondary=Archetypes_Skills, backref='ArchetypesSkills')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=Archetypes_ArmorTypes, backref='ArchetypesPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=Archetypes_Weapoons, backref='ArchetypesWeapoons')
    ToolOwnership       = db.relationship('Tools', secondary=Archetypes_Tools, backref='ArchetypesTools')
    Language            = db.relationship('LanguageDND', secondary=Archetypes_LanguageDND, backref='ArchetypesLanguageDND')


class Armors(db.Model):
    __tablename__ = 'Armors'
    id          = db.Column(db.Integer, primary_key=True)
    ArmorName   = db.Column(db.String(300), nullable=False, unique=True)
    Hindrance   = db.Column(db.Boolean)
    ArmorClass  = db.Column(db.Text, nullable=True)
    Cost        = db.Column(db.Integer, nullable=True)
    Power       = db.Column(db.Text, nullable=True)
    Weight      = db.Column(db.Integer, nullable=True)
    ArmorType   = db.relationship('ArmorTypes', secondary=Armor_ArmorTypes, backref='ArmorTypesDND')


class ArmorTypes(db.Model):
    __tablename__ = 'ArmorTypes'
    id              = db.Column(db.Integer, primary_key=True)
    ArmorTypeName   = db.Column(db.String(300), nullable=False, unique=True)


class Attributes(db.Model):
    __tablename__ = 'Attributes'
    id               = db.Column(db.Integer, primary_key=True)
    AttributeName    = db.Column(db.String(300), nullable=False, unique=True)
    Discription      = db.Column(db.Text, nullable=True)
    Characteristic   = db.relationship('Characteristices', secondary=Attributes_Characteristices, backref='AttributesCharacteristices')
    DamageResistance = db.relationship('DamageTypes', secondary=Attributes_ResistanceDamageTypes, backref='AttributesResistanceDamageTypesDND')
    DamageImmunity   = db.relationship('DamageTypes', secondary=Attributes_ImmunityDamageTypes, backref='AttributesImmunityDamageTypesDND')
    Language         = db.relationship('LanguageDND', secondary=Attributes_LanguageDND, backref='LanguageAttributes')
    Spell            = db.relationship('SpellDND', secondary=Attributes_SpellDND, backref='AttributesSpell')
    Skill            = db.relationship('Skills', secondary=Attributes_Skills, backref='AttributeSkills')
    PossessionArmor  = db.relationship('ArmorTypes', secondary=Attributes_ArmorTypes, backref='AttributesPossessionArmor')
    GunOwnership     = db.relationship('Weapoons', secondary=Attributes_Weapoons, backref='AttributesWeapoons')
    ToolOwnership    = db.relationship('Tools', secondary=Attributes_Tools, backref='AttributesTools')


class BackgroundDND(db.Model):
    __tablename__ = 'BackgroundDND'
    id               = db.Column(db.Integer, primary_key=True)
    BackgroundName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription      = db.Column(db.Text, nullable=True)
    Characteristic   = db.relationship('Characteristices', secondary=BackgroundDND_Characteristices, backref='BackgroundDNDCharacteristices')
    Language         = db.relationship('LanguageDND', secondary=BackgroundDND_LanguageDND, backref='LanguageDNDBackgroundDND')
    Skill            = db.relationship('Skills', secondary=BackgroundDND_Skills, backref='BackgroundDNDSkills')
    PossessionArmor  = db.relationship('ArmorTypes', secondary=BackgroundDND_ArmorTypes, backref='BackgroundDNDPossessionArmor')
    GunOwnership     = db.relationship('Weapoons', secondary=BackgroundDND_Weapoons, backref='BackgroundDNDGunOwnership')
    ToolOwnership    = db.relationship('Tools', secondary=BackgroundDND_Tools, backref='BackgroundDNDToolOwnership')
    DamageResistance = db.relationship('DamageTypes', secondary=BackgroundDND_ResistanceDamageTypes, backref='BackgroundDNDResistanceDamageTypesDND')
    DamageImmunity   = db.relationship('DamageTypes', secondary=BackgroundDND_ImmunityDamageTypes, backref='BackgroundDNDImmunityDamageTypesDND')
    Spell            = db.relationship('SpellDND', secondary=BackgroundDND_SpellDND, backref='BackgroundDNDSpell')


class ClassPersonDND(db.Model):
    __tablename__ = 'ClassPersonDND'
    id                  = db.Column(db.Integer, primary_key=True)
    ClassPersonName     = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    ArmorClass          = db.Column(db.Text, nullable=True)
    NotArmorSafe        = db.Column(db.Boolean, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=ClassPersonDND_Characteristices, backref='ClassPersonDNDCharacteristices')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=ClassPersonDND_ArmorTypes, backref='ClassPersonDNDPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=ClassPersonDND_Weapoons, backref='ClassPersonDNDGunOwnership')
    ToolOwnership       = db.relationship('Tools', secondary=ClassPersonDND_Tools, backref='ClassPersonDNDToolOwnership')
    Skill               = db.relationship('Skills', secondary=ClassPersonDND_Skills, backref='ClassPersonSkills')
    DamageResistance    = db.relationship('DamageTypes', secondary=ClassPersonDND_ResistanceDamageTypes, backref='ClassPersonDNDResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=ClassPersonDND_ImmunityDamageTypes, backref='ClassPersonDNDImmunityDamageTypesDND')
    Spell               = db.relationship('SpellDND', secondary=SpellDND_ClassPerson, backref='ClassPersonDND')
    Language            = db.relationship('LanguageDND', secondary=ClassPersonDND_LanguageDND, backref='ClassPersonDNDLanguageDND')


class DamageTypes(db.Model):
    __tablename__ = 'DamageTypes'
    id              = db.Column(db.Integer, primary_key=True)
    DamageTypeName  = db.Column(db.String(300), nullable=False, unique=True)


class Equipments(db.Model):
    __tablename__ = 'Equipments'
    id              = db.Column(db.Integer, primary_key=True)
    EquipmentName   = db.Column(db.String(300), nullable=False, unique=True)
    Cost            = db.Column(db.Integer, nullable=True)
    Weight          = db.Column(db.Integer, nullable=True)
    EquipmentType   = db.relationship('EquipmentTypes', secondary=Equipments_EquipmentTypes, backref='EquipmentsEquipmentTypes')


class EquipmentTypes(db.Model):
    __tablename__ = 'EquipmentTypes'
    id                  = db.Column(db.Integer, primary_key=True)
    EquipmentTypeName   = db.Column(db.String(300), nullable=False, unique=True)


class Characteristices(db.Model):
    __tablename__ = 'Characteristices'
    id                   = db.Column(db.Integer, primary_key=True)
    CharacteristicName   = db.Column(db.String(300), nullable=False, unique=True)


class LanguageDND(db.Model):
    __tablename__ = 'LanguageDND'
    id                      = db.Column(db.Integer, primary_key=True)
    LanguageName            = db.Column(db.String(300), nullable=False, unique=True)
    TypicalRepresentative   = db.Column(db.Text, nullable=True)
    Writing                 = db.Column(db.Text, nullable=True)


class MagicalItemsDND(db.Model):
    __tablename__ = 'MagicalItems'
    id                  = db.Column(db.Integer, primary_key=True)
    MagicalItemsName    = db.Column(db.String(300), nullable=False, unique=True)
    PowerBonus          = db.Column(db.Text, nullable=True)
    ArmorBonus          = db.Column(db.Text, nullable=True)
    Discription         = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=MagicalItems_Characteristices, backref='MagicalItemsCharacteristices')
    Spell               = db.relationship('SpellDND', secondary=SpellDND_MagicalItems, backref='SpellMagicalItemsDND')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=MagicalItems_ArmorTypes, backref='MagicalItemsPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=MagicalItems_Weapoons, backref='MagicalItemsGunOwnership')
    ToolOwnership       = db.relationship('Tools', secondary=MagicalItems_Tools, backref='MagicalItemsToolOwnership')
    DamageResistance    = db.relationship('DamageTypes', secondary=MagicalItems_ResistanceDamageTypes, backref='MagicalItemsResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=MagicalItems_ImmunityDamageTypes, backref='MagicalItemsImmunityDamageTypesDND')
    Skill               = db.relationship('Skills', secondary=MagicalItems_Skills, backref='MagicalItemsSkills')
    Language            = db.relationship('LanguageDND', secondary=MagicalItems_LanguageDND, backref='MagicalItemsLanguageDND')


class RaceDND(db.Model):
    __tablename__ = 'RaceDND'
    id                  = db.Column(db.Integer, primary_key=True)
    RaceName            = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    Speed               = db.Column(db.Integer, nullable=True)
    Climb               = db.Column(db.Integer, nullable=True)
    Fly                 = db.Column(db.Integer, nullable=True)
    Swim                = db.Column(db.Integer, nullable=True)
    Fight               = db.Column(db.Text, nullable=True)
    Armor               = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=RaceDND_Characteristices, backref='RaceDNDCharacteristices')
    DamageResistance    = db.relationship('DamageTypes', secondary=RaceDND_ResistanceDamageTypes, backref='RaceDNDResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=RaceDND_ImmunityDamageTypes, backref='RaceDNDImmunityDamageTypesDND')
    Spell               = db.relationship('SpellDND', secondary=RaceDND_SpellDND, backref='RaceDND')
    Skill               = db.relationship('Skills', secondary=RaceDND_Skills, backref='RaceDNDSkills')
    Language            = db.relationship('LanguageDND', secondary=RaceDND_LanguageDND, backref='LanguageDNDRaceDND')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=RaceDND_ArmorTypes, backref='RaceDNDPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=RaceDND_Weapoons, backref='RaceDNDGunOwnership')
    ToolOwnership       = db.relationship('Tools', secondary=RaceDND_Tools, backref='RaceDNDToolOwnership')


class Skills(db.Model):
    __tablename__ = 'Skills'
    id           = db.Column(db.Integer, primary_key=True)
    SkillsName   = db.Column(db.String(300), nullable=False, unique=True)


class SpellDND(db.Model):
    __tablename__ = 'SpellDND'
    id              = db.Column(db.Integer, primary_key=True)
    SpellName       = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)
    Damage          = db.Column(db.Text, nullable=True)
    Effects         = db.Column(db.Text, nullable=True)
    ApplicationTime = db.Column(db.Text, nullable=True)
    Distance        = db.Column(db.Text, nullable=True)
    Components      = db.Column(db.Text, nullable=True)
    Duration        = db.Column(db.Text, nullable=True)
    LevelSpell      = db.Column(db.Integer, nullable=True)
    Subclasses      = db.Column(db.Integer, nullable=True)
    Ritual          = db.Column(db.Boolean, nullable=True)
    ClassPerson     = db.relationship('ClassPersonDND', secondary=ClassPersonDND_SpellDND, backref='ClassPersonDNDSpellDND')
    Archetype       = db.relationship('Archetypes', secondary=Archetypes_SpellDND, backref='ArchetypesSpellDND')
    TypeDamage      = db.relationship('DamageTypes', secondary=SpellDND_DamageTypes, backref='SpellDamageTypesDND')


class Tools(db.Model):
    __tablename__ = 'Tools'
    id          = db.Column(db.Integer, primary_key=True)
    ToolName    = db.Column(db.String(300), nullable=False, unique=True)
    Cost        = db.Column(db.Integer, nullable=True)
    Weight      = db.Column(db.Integer, nullable=True)
    ToolType    = db.relationship('ToolTypes', secondary=Tool_ToolTypes, backref='ToolToolTypes')


class ToolTypes(db.Model):
    __tablename__ = 'ToolTypes'
    id              = db.Column(db.Integer, primary_key=True)
    ToolTypeName   = db.Column(db.String(300), nullable=False, unique=True)


class Weapoons(db.Model):
    __tablename__ = 'Weapoons'
    id              = db.Column(db.Integer, primary_key=True)
    WeapoonName     = db.Column(db.String(300), nullable=False, unique=True)
    Features        = db.Column(db.Text, nullable=True)
    WeapoonClass    = db.Column(db.Text, nullable=True)
    Cost            = db.Column(db.Integer, nullable=True)
    Damage          = db.Column(db.Text, nullable=True)
    Weight          = db.Column(db.Integer, nullable=True)
    DamageType      = db.relationship('DamageTypes', secondary=Weapoons_DamageTypes, backref='WeapoonsDamageTypes')
    WeapoonType     = db.relationship('WeapoonTypes', secondary=Weapoon_WeapoonTypes, backref='WeapoonsWeapoonTypes')


class WeapoonTypes(db.Model):
    __tablename__ = 'WeapoonTypes'
    id                  = db.Column(db.Integer, primary_key=True)
    WeapoonTypeName     = db.Column(db.String(300), nullable=False, unique=True)


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=Roles_Users, backref='roled')


class Role(db.Model, RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer(), primary_key=True)
    RoleName = db.Column(db.String(80), unique=True)
    name     = db.Column(db.String(80), unique=True)
    NameUser = db.Column(db.String(80), unique=True)


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/CreateArchetype", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArchetype():
    ClassDND         = ClassPersonDND.query.all()
    Languages        = LanguageDND.query.all()
    Spells           = SpellDND.query.all()
    damageTypes      = DamageTypes.query.all()
    armorTypes       = ArmorTypes.query.all()
    skills           = Skills.query.all()
    tools            = Tools.query.all()
    characteristices = Characteristices.query.all()
    weapoons         = Weapoons.query.all()
    if request.method == 'POST':
        ArchetypeName        = request.form['ArchetypeName']
        Discription          = request.form['Discription']
        if 'NotArmorSafe' in request.form:
            NotArmorSafe = True
        else:
            NotArmorSafe = False
        ArmorClass          = request.form["ArmorClass"]
        ClassPersonName     = request.form["ClassPersonName"]

        ArchetypeDND        = Archetypes(ArchetypeName=ArchetypeName, Discription=Discription
                                  , NotArmorSafe=NotArmorSafe, ArmorClass=ArmorClass)
        classDND = ClassPersonDND.query.filter_by(ClassPersonName=ClassPersonName).first()
        ArchetypeDND.ClassPerson.append(classDND)
        TabelsParametrs = [LanguageDND, SpellDND, DamageTypes, ArmorTypes, Skills, Tools, Weapoons, Characteristices]
        res = parametrsoutput(request.form, ArchetypeDND, TabelsParametrs)
        if res:
            try:
                db.session.add(ArchetypeDND)
                db.session.commit()
                return render_template("CreatePosts/CreateArchetype.html", ClassDND=ClassDND, languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills, Tools=tools, Weapoons=weapoons, Characteristices=characteristices)
            except:
                return render_template("CreatePosts/CreateArchetype.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateArchetype.html", ClassDND=ClassDND, languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills, Tools=tools, Weapoons=weapoons, Characteristices=characteristices)


@app.route("/CreateArmor", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmor():
    armortypes = ArmorTypes.query.all()
    if request.method == 'POST':
        ArmorName   = request.form['ArmorName']
        armortype   = request.form['ArmorType']
        Weight      = request.form['Weight']
        Power       = request.form['Power']
        Cost        = request.form['Cost']
        ArmorClass  = request.form['ArmorClass']
        if Weight == '':
            Weight=0
        else:
            Weight=int(Weight)
        if Cost == '':
            Cost=0
        else:
            Cost=int(Cost)
        if "Hindrance" in request.form:
            hindrance=True
        else:
            hindrance=False
        Armor = Armors(ArmorName=ArmorName, Weight=Weight
                                     , Power=Power, Cost=Cost, ArmorClass=ArmorClass, Hindrance=hindrance)
        armorType = ArmorTypes.query.filter_by(ArmorTypeName=armortype).first()
        Armor.ArmorType.append(armorType)
        try:
            db.session.add(Armor)
            db.session.commit()
            return render_template("CreatePosts/CreateArmor.html",ArmorTypes=armortypes)
        except:
            return render_template("CreatePosts/CreateArmor.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateArmor.html",ArmorTypes=armortypes)


@app.route("/CreateArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmorTypes():
    if request.method == 'POST':
        ArmorTypeName = request.form["ArmorTypeName"]
        ArmorType = ArmorTypes(ArmorTypeName=ArmorTypeName)
        try:
            db.session.add(ArmorType)
            db.session.commit()
            return render_template("CreatePosts/CreateArmorTypes.html")
        except:
            return render_template("CreatePosts/CreateArmorTypes.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateArmorTypes.html")


@app.route("/CreateAttribute", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateAttribute():
    Languages        = LanguageDND.query.all()
    Spells           = SpellDND.query.all()
    damageTypes      = DamageTypes.query.all()
    armorTypes       = ArmorTypes.query.all()
    skills           = Skills.query.all()
    tools            = Tools.query.all()
    characteristices = Characteristices.query.all()
    weapoons         = Weapoons.query.all()
    if request.method == 'POST':
        AttributeName        = request.form['AttributeName']
        Discription          = request.form['Discription']
        AttributeDND        = Attributes(AttributeName=AttributeName, Discription=Discription)
        TabelsParametrs = [LanguageDND, SpellDND, DamageTypes, ArmorTypes, Skills, Tools, Weapoons, Characteristices]
        res = parametrsoutput(request.form, AttributeDND, TabelsParametrs)
        if res:
            try:
                db.session.add(AttributeDND)
                db.session.commit()
                return render_template("CreatePosts/CreateAttribute.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)
            except:
                return render_template("CreatePosts/CreateAttribute.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateAttribute.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)


@app.route("/CreateBackground", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateBackground():
    Languages        = LanguageDND.query.all()
    Spells           = SpellDND.query.all()
    damageTypes      = DamageTypes.query.all()
    armorTypes       = ArmorTypes.query.all()
    skills           = Skills.query.all()
    tools            = Tools.query.all()
    weapoons         = Weapoons.query.all()
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        BackgroundName = request.form['BackgroundName']
        Discription = request.form['Discription']
        Background = BackgroundDND(BackgroundName=BackgroundName, Discription=Discription)
        TabelsParametrs = [LanguageDND, SpellDND, DamageTypes, ArmorTypes, Skills, Tools, Weapoons, Characteristices]
        res = parametrsoutput(request.form, Background, TabelsParametrs)
        if res:
            try:
                db.session.add(Background)
                db.session.commit()
                return render_template("CreatePosts/CreateBackground.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)
            except:
                return render_template("CreatePosts/CreateBackground.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateBackground.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)


@app.route("/CreateClass", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateClass():
    Languages        = LanguageDND.query.all()
    Spells           = SpellDND.query.all()
    damageTypes      = DamageTypes.query.all()
    armorTypes       = ArmorTypes.query.all()
    skills           = Skills.query.all()
    tools            = Tools.query.all()
    weapoons         = Weapoons.query.all()
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        ClassPersonName = request.form['ClassPersonName']
        Discription = request.form['Discription']
        if 'NotArmorSafe' in request.form:
            NotArmorSafe = True
        else:
            NotArmorSafe = False
        ArmorClass = request.form["ArmorClass"]
        ClassDND = ClassPersonDND(ClassPersonName=ClassPersonName, Discription=Discription
                                  , NotArmorSafe=NotArmorSafe, ArmorClass=ArmorClass)
        TabelsParametrs = [LanguageDND, SpellDND, DamageTypes, ArmorTypes, Skills, Tools, Weapoons, Characteristices]
        res             = parametrsoutput(request.form, ClassDND,TabelsParametrs)
        if res:
            try:
                db.session.add(ClassDND)
                db.session.commit()
                return render_template("CreatePosts/CreateClass.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)
            except:
                return render_template("CreatePosts/CreateClass.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateClass.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)


@app.route("/CreateDamageType", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateDamageType():
    if request.method == 'POST':
        DamageTypeName = request.form['DamageTypeName']
        DamageType = DamageTypes(DamageTypeName=DamageTypeName)
        try:
            db.session.add(DamageType)
            db.session.commit()
            return render_template("CreatePosts/CreateDamageType.html")
        except:
            return render_template("CreatePosts/CreateDamageType.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateDamageType.html")


@app.route("/CreateEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipments():
    equipmenttypes = ArmorTypes.query.all()
    if request.method == 'POST':
        EquipmentName   = request.form['EquipmentName']
        EquipmentType   = request.form['EquipmentType']
        Weight          = request.form['Weight']
        Cost            = request.form['Cost']
        if Weight == '':
            Weight = 0
        else:
            Weight = int(Weight)
        if Cost == '':
            Cost = 0
        else:
            Cost = int(Cost)
        equipments  = Equipments(EquipmentName=EquipmentName, Weight=Weight, Cost=Cost)
        EquipmentType = EquipmentTypes.query.filter_by(EquipmentTypeName=EquipmentType).first()
        equipments.EquipmentType.append(EquipmentType)
        try:
            db.session.add(equipments)
            db.session.commit()
            return render_template("CreatePosts/CreateEquipments.html",equipmenttypes=equipmenttypes)
        except:
            return render_template("CreatePosts/CreateEquipments.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateEquipments.html",equipmenttypes=equipmenttypes)


@app.route("/CreateEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipmentTypes():
    if request.method == 'POST':
        EquipmentTypeName   = request.form['EquipmentTypeName']
        EquipmentType          = EquipmentTypes(EquipmentTypeName=EquipmentTypeName)
        try:
            db.session.add(EquipmentType)
            db.session.commit()
            return render_template("CreatePosts/CreateEquipmentTypes.html")
        except:
            return render_template("CreatePosts/CreateEquipmentTypes.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateEquipmentTypes.html")


@app.route("/CreateCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateCharacteristices():
    if request.method == 'POST':
        CharacteristicName   = request.form['CharacteristicName']
        Characteristic       = Characteristices(CharacteristicName=CharacteristicName)
        try:
            db.session.add(Characteristic)
            db.session.commit()
            return render_template("CreatePosts/CreateCharacteristices.html")
        except:
            return render_template("CreatePosts/CreateCharacteristices.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateCharacteristices.html")


@app.route("/CreateLanguage", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateLanguage():
    if request.method == 'POST':
        LanguageName = request.form['LanguageName']
        TypicalRepresentative = request.form['TypicalRepresentative']
        Writing = request.form['Writing']
        languageDND = LanguageDND(LanguageName=LanguageName, TypicalRepresentative=TypicalRepresentative, Writing=Writing)
        try:
            db.session.add(languageDND)
            db.session.commit()
            return render_template("CreatePosts/CreateLanguage.html")
        except:
            return render_template("CreatePosts/CreateLanguage.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateLanguage.html")


@app.route("/CreateMagicalItems", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateMagicalItems():
    Spells           = SpellDND.query.all()
    damageTypes      = DamageTypes.query.all()
    armorTypes       = ArmorTypes.query.all()
    skills           = Skills.query.all()
    tools            = Tools.query.all()
    weapoons         = Weapoons.query.all()
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        MagicalItemsName = request.form['MagicalItemsName']
        Discription = request.form['Discription']
        PowerBonus  = request.form["PowerBonus"]
        ArmorBonus = request.form["ArmorBonus"]
        MagicalItem = MagicalItemsDND(MagicalItemsName=MagicalItemsName, Discription=Discription
                                   , PowerBonus=PowerBonus, ArmorBonus=ArmorBonus)
        TabelsParametrs = [LanguageDND, SpellDND, DamageTypes, ArmorTypes, Skills, Tools, Weapoons, Characteristices]
        res             = parametrsoutput(request.form, MagicalItem,TabelsParametrs)
        if res:
            try:
                db.session.add(MagicalItem)
                db.session.commit()
                return render_template("CreatePosts/CreateMagicalItems.html", Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)
            except:
                return render_template("CreatePosts/CreateMagicalItems.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateMagicalItems.html", Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)


@app.route("/CreateRace", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateRace():
    Languages        = LanguageDND.query.all()
    Spells           = SpellDND.query.all()
    damageTypes      = DamageTypes.query.all()
    armorTypes       = ArmorTypes.query.all()
    skills           = Skills.query.all()
    tools            = Tools.query.all()
    weapoons         = Weapoons.query.all()
    characteristices = Characteristices.query.all()
    if request.method == 'POST':
        RaceName = request.form['RaceName']
        Discription = request.form['Discription']
        Armor   = request.form["Armor"]
        Fight   = request.form["Fight"]
        Speed   = request.form["Speed"]
        if Speed == '':
            Speed = 0
        Fly = request.form["Fly"]
        if Fly == '':
            Fly = 0
        Climb = request.form["Climb"]
        if Climb == '':
            Climb = 0
        Swim = request.form["Swim"]
        if Swim == '':
            Swim = 0
        Race = RaceDND(RaceName=RaceName, Discription=Discription, Speed=Speed, Swim=Swim
                                   , Climb=Climb, Fly=Fly, Armor=Armor, Fight=Fight)
        TabelsParametrs = [LanguageDND, SpellDND, DamageTypes, ArmorTypes, Skills, Tools, Weapoons, Characteristices]
        res             = parametrsoutput(request.form, Race,TabelsParametrs)
        if res:
            try:
                db.session.add(Race)
                db.session.commit()
                return render_template("CreatePosts/CreateRace.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)
            except:
                return render_template("CreatePosts/CreateRace.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateRace.html", languages=Languages, Spells=Spells
                               ,damageTypes=damageTypes, armorTypes=armorTypes, skills=skills
                               , Tools=tools, Weapoons=weapoons, Characteristices=characteristices)


@app.route("/CreateSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSkills():
    if request.method == 'POST':
        SkillName = request.form["SkillName"]
        Skill = Skills(SkillName=SkillName)
        try:
            db.session.add(Skill)
            db.session.commit()
            return render_template("CreatePosts/CreateSkills.html")
        except:
            return render_template("CreatePosts/CreateSkills.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateSkills.html")


@app.route("/CreateSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateSpells():
    classPersonDND  = ClassPersonDND.query.all()
    archetypes      = Archetypes.query.all()
    damageTypes     = DamageTypes.query.all()
    if request.method == 'POST':
        SpellName       = request.form['SpellName']
        Discription     = request.form['Discription']
        LevelSpell      = request.form['LevelSpell']
        Damage          = request.form['Damage']
        Effects         = request.form['Effects']
        ApplicationTime = request.form['ApplicationTime']
        Distance        = request.form['Distance']
        Components      = request.form['Components']
        Duration       = request.form['Duration']
        ClassPersons    = request.form['ClassPerson']
        if ClassPersons == '' or ClassPersons == None:
            Classes = []
        else:
            Classes = ClassPersons.split(sep=',')
        SubclassesName = request.form['Subclasses']
        if SubclassesName == '' or SubclassesName == None:
            Subclasses = []
        else:
            Subclasses = SubclassesName.split(sep=',')
        ArmorClass  = request.form["ArmorClass"]
        Spell = SpellDND(SpellName=SpellName, Discription=Discription
                                   , ArmorClass=ArmorClass, LevelSpell=LevelSpell
                                    , Damage=Damage, Effects=Effects, ApplicationTime=ApplicationTime
                                    , Distance=Distance, Components=Components, Duration=Duration)
        for Class in Classes:
            Classdnd = SpellDND.query.filter_by(ClassPerson=Class).first()
            Spell.Skill.append(Classdnd)
        for Archetype in Subclasses:
            Subclass = SpellDND.query.filter_by(Archetype=Archetype).first()
            Spell.Spell.append(Subclass)
        try:
            db.session.add(Spell)
            db.session.commit()
            return render_template("CreatePosts/CreateSpells.html",ClassPersonDND=classPersonDND
                               , Archetypes=archetypes, DamageTypes=damageTypes)
        except:
            return render_template("CreatePosts/CreateSpells.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateSpells.html",ClassPersonDND=classPersonDND
                               , Archetypes=archetypes, DamageTypes=damageTypes)


@app.route("/CreateTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateTools():
    toolTypes = ToolTypes.query.all()
    if request.method == 'POST':
        ToolName = request.form["ToolName"]
        ToolType = request.form["ToolType"]
        Weight = request.form["Weight"]
        Cost = request.form["Cost"]
        if Weight == '':
            Weight=0
        else:
            Weight=int(Weight)
        if Cost == '':
            Cost=0
        else:
            Cost=int(Cost)
        Tool = Tools(ToolName=ToolName, Weight=Weight,
                                     Cost=Cost)

        toolType = ToolTypes.query.filter_by(ToolTypeName=ToolType).first()
        Tool.ToolType.append(toolType)
        try:
            db.session.add(Tool)
            db.session.commit()
            return render_template("CreatePosts/CreateTools.html",ToolTypes=toolTypes)
        except:
            return render_template("CreatePosts/CreateTools.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateTools.html",ToolTypes=toolTypes)


@app.route("/CreateToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateToolTypes():
    if request.method == 'POST':
        ToolTypeName = request.form["ToolTypeName"]
        ToolType = ToolTypes(ToolTypeName=ToolTypeName)
        try:
            db.session.add(ToolType)
            db.session.commit()
            return render_template("CreatePosts/CreateToolTypes.html")
        except:
            return render_template("CreatePosts/CreateToolTypes.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateToolTypes.html")


@app.route("/CreateWeapon", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapon():
    weapoontypes = WeapoonTypes.query.all()
    damageTypes  = DamageTypes.query.all()
    if request.method == 'POST':
        WeapoonName     = request.form['WeapoonName']
        Weight          = request.form['Weight']
        Cost            = request.form['Cost']
        WeapoonClass    = request.form['WeapoonClass']
        damageType      = request.form['DamageType']
        Damage          = request.form['Damage']
        if Weight == '':
            Weight=0
        else:
            Weight=int(Weight)
        if Cost == '':
            Cost=0
        else:
            Cost=int(Cost)
        if Damage == None:
            Damage=0
        weapoon = Weapoons(WeapoonName=WeapoonName, Weight=Weight
                            , Cost=Cost, Damage=Damage)
        if WeapoonClass != None and WeapoonClass != "":
            weapoontype = WeapoonTypes.query.filter_by(WeapoonTypeName=WeapoonClass).first()
            weapoon.WeapoonType.append(weapoontype)
        if damageType != None and damageType != "":
            damagetype = DamageTypes.query.filter_by(DamageTypeName=damageType).first()
            weapoon.DamageType.append(damagetype)
        try:
            db.session.add(weapoon)
            db.session.commit()
            return render_template("CreatePosts/CreateWeapoon.html",Weapoontypes=weapoontypes, DamageTypes=damageTypes)
        except:
            return render_template("CreatePosts/CreateWeapoon.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateWeapoon.html",Weapoontypes=weapoontypes, DamageTypes=damageTypes)


@app.route("/CreateWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoonTypes():
    if request.method == 'POST':
        WeapoonTypeName = request.form["WeapoonTypeName"]
        WeapoonType = WeapoonTypes(WeapoonTypeName=WeapoonTypeName)
        try:
            db.session.add(WeapoonType)
            db.session.commit()
            return render_template("CreatePosts/CreateWeapoonTypes.html")
        except:
            return render_template("CreatePosts/CreateWeapoonTypes.html",msg='При добавлении правила произошла ошибка')
    else:
        return render_template("CreatePosts/CreateWeapoonTypes.html")


@app.route("/CreateMaterial", methods=['POST','GET'])
@roles_accepted('Admin', 'Master')
def CreateMaterial():
    return render_template("CreateMaterial.html")


@app.route("/Index")
@app.route("/")
def Index():
    roles = Role.query.all()
    if len(roles) == 0:
        role1 = Role(RoleName='Gamer', name='Gamer', NameUser='Игрок')
        role2 = Role(RoleName='Master', name='Master', NameUser='Мастер')
        role3 = Role(RoleName='Admin', name='Admin', NameUser='Администратор')
        db.session.add(role1)
        db.session.add(role2)
        db.session.add(role3)
        db.session.commit()
    return render_template("Index.html")


@app.route("/AdminPanel")
@roles_accepted('Admin')
def AdminPanel():
    return render_template("AdminPanel.html")


@app.route("/Posts", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def Posts():
    return render_template("Posts.html")


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

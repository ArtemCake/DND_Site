from flask import (Flask, render_template, request, redirect)
from flask_login import login_user, login_required, logout_user, LoginManager
from flask_security import (roles_accepted, Security, SQLAlchemySessionUserDatastore, UserMixin, RoleMixin)
from functions.functions import appenddatas, parametrsoutput

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


Archetypes_Characteristices = db.Table('Archetypes_Characteristices',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


Archetypes_ResistanceDamageTypes = db.Table('Archetypes_ResistanceDamageTypes',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('ResistanceDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Archetypes_ImmunityDamageTypes = db.Table('Archetypes_ImmunityDamageTypes',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('ImmunityDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Archetypes_EffectsResistance = db.Table('Archetypes_EffectsResistance',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('EffectsResistance', db.Integer, db.ForeignKey('Effects.id')))


Archetypes_Classes = db.Table('Archetypes_Classes',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')))


Archetypes_Spells = db.Table('Archetypes_Spells',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')))


Archetypes_Skills = db.Table('Archetypes_Skills',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Archetypes_PossessionArmor = db.Table('Archetypes_PossessionArmor',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('PossessionArmor_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Archetypes_GunOwnership = db.Table('Archetypes_GunOwnership',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('GunOwnership_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Archetypes_ToolOwnership = db.Table('Archetypes_ToolOwnership',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('ToolOwnership_id', db.Integer(), db.ForeignKey('Tools.id')))


Archetypes_Languages = db.Table('Archetypes_Languages',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


Archetypes_Abilities = db.Table('Archetypes_Abilities',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Abilities_id', db.Integer(), db.ForeignKey('Abilities.id')))


Armors_ArmorTypes = db.Table('Armors_Abilities',
        db.Column('Armors_id', db.Integer(), db.ForeignKey('Armors.id')),
        db.Column('ArmorTypes_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Atributes_Characteristices = db.Table('Atributes_Characteristices',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


Atributes_ResistanceDamageTypes = db.Table('Atributes_ResistanceDamageTypes',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('ResistanceDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Atributes_ImmunityDamageTypes = db.Table('Atributes_ImmunityDamageTypes',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('ImmunityDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Atributes_EffectsResistance = db.Table('Atributes_EffectsResistance',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('EffectsResistance_id', db.Integer(), db.ForeignKey('Effects.id')))


Atributes_Spells = db.Table('Atributes_Spells',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')))


Atributes_Skills = db.Table('Atributes_Skills',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Atributes_PossessionArmor = db.Table('Atributes_PossessionArmor',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('PossessionArmor_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Atributes_GunOwnership = db.Table('Atributes_GunOwnership',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('GunOwnership_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Atributes_ToolOwnership = db.Table('Atributes_ToolOwnership',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('ToolOwnership_id', db.Integer(), db.ForeignKey('Tools.id')))


Atributes_Languages = db.Table('Atributes_Languages',
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


Atributes_Abilities = db.Table('Atributes_Abilities',
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
        db.Column('Abilities_id', db.Integer(), db.ForeignKey('Abilities.id')))


Backgrounds_Characteristices = db.Table('Backgrounds_Characteristices',
        db.Column('Backgrounds_id', db.Integer(), db.ForeignKey('Backgrounds.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


Backgrounds_Languages = db.Table('Backgrounds_Languages',
        db.Column('Backgrounds_id', db.Integer(), db.ForeignKey('Backgrounds.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


Backgrounds_Skills = db.Table('Backgrounds_Skills',
        db.Column('Backgrounds_id', db.Integer(), db.ForeignKey('Backgrounds.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Backgrounds_ToolOwnership = db.Table('Backgrounds_ToolOwnership',
        db.Column('Backgrounds_id', db.Integer(), db.ForeignKey('Backgrounds.id')),
        db.Column('ToolOwnership_id', db.Integer(), db.ForeignKey('Tools.id')))


Backgrounds_Spells = db.Table('Backgrounds_Spells',
        db.Column('Backgrounds_id', db.Integer(), db.ForeignKey('Backgrounds.id')),
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')))


Classes_Characteristices = db.Table('Classes_Characteristices',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


Classes_PossessionArmor = db.Table('Classes_PossessionArmor',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('PossessionArmor_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Classes_GunOwnership = db.Table('Classes_GunOwnership',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('GunOwnership_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Classes_ToolOwnership = db.Table('Classes_ToolOwnership',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('ToolOwnership_id', db.Integer(), db.ForeignKey('Tools.id')))


Classes_Skills = db.Table('Classes_Skills',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Classes_Spells = db.Table('Classes_Spells',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')))


Classes_Languages = db.Table('Classes_Languages',
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


Equipments_EquipmentTypes = db.Table('Equipments_EquipmentTypes',
        db.Column('Equipments_id', db.Integer(), db.ForeignKey('Equipments.id')),
        db.Column('EquipmentTypes_id', db.Integer(), db.ForeignKey('EquipmentTypes.id')))


Characteristices_Skills = db.Table('Characteristices_Skills',
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


MagicalItems_Characteristices = db.Table('MagicalItems_Characteristices',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


MagicalItems_Spells = db.Table('MagicalItems_Spells',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')))


MagicalItems_PossessionArmor = db.Table('MagicalItems_PossessionArmor',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('PossessionArmor_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


MagicalItems_GunOwnership = db.Table('MagicalItems_GunOwnership',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('GunOwnership_id', db.Integer(), db.ForeignKey('Weapoons.id')))


MagicalItems_ToolOwnership = db.Table('MagicalItems_ToolOwnership',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('ToolOwnership_id', db.Integer(), db.ForeignKey('Tools.id')))


MagicalItems_ResistanceDamageTypes = db.Table('MagicalItems_ResistanceDamageTypes',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('ResistanceDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


MagicalItems_ImmunityDamageTypes = db.Table('MagicalItems_ImmunityDamageTypes',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('ImmunityDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


MagicalItems_Skills = db.Table('MagicalItems_Skills',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


MagicalItems_Languages = db.Table('MagicalItems_Languages',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


MagicalItems_EffectsResistance = db.Table('MagicalItems_EffectsResistance',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('EffectsResistance_id', db.Integer(), db.ForeignKey('Effects.id')))


MagicalItems_Effects = db.Table('MagicalItems_Effects',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Effects_id', db.Integer(), db.ForeignKey('Effects.id')))


MagicalItems_Abilities = db.Table('MagicalItems_Abilities',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Abilities_id', db.Integer(), db.ForeignKey('Abilities.id')))


MagicalItems_MagicalItemsTypes = db.Table('MagicalItems_MagicalItemsTypes',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('MagicalItemsTypes_id', db.Integer(), db.ForeignKey('MagicalItemsTypes.id')))


MagicalItems_Armors = db.Table('MagicalItems_Armors',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Armors_id', db.Integer(), db.ForeignKey('Armors.id')))


MagicalItems_Weapoons = db.Table('MagicalItems_Weapoons',
        db.Column('MagicalItems_id', db.Integer(), db.ForeignKey('MagicalItems.id')),
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Races_Characteristices = db.Table('Races_Characteristices',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('Characteristices_id', db.Integer(), db.ForeignKey('Characteristices.id')))


Races_ResistanceDamageTypes = db.Table('Races_ResistanceDamageTypes',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('ResistanceDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Races_ImmunityDamageTypes = db.Table('Races_ImmunityDamageTypes',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('ImmunityDamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Races_Spells = db.Table('Races_Spells',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')))


Races_Skills = db.Table('Races_Skills',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('Skills_id', db.Integer(), db.ForeignKey('Skills.id')))


Races_Languages = db.Table('Races_Languages',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


Races_PossessionArmor = db.Table('Races_PossessionArmor',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('PossessionArmor_id', db.Integer(), db.ForeignKey('ArmorTypes.id')))


Races_GunOwnership = db.Table('Races_GunOwnership',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('GunOwnership_id', db.Integer(), db.ForeignKey('Weapoons.id')))


Races_ToolOwnership = db.Table('Races_ToolOwnership',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('ToolOwnership_id', db.Integer(), db.ForeignKey('Tools.id')))


Races_EffectsResistance = db.Table('Races_EffectsResistance',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('EffectsResistance_id', db.Integer(), db.ForeignKey('Effects.id')))


Races_Abilities = db.Table('Races_Abilities',
        db.Column('Races_id', db.Integer(), db.ForeignKey('Races.id')),
        db.Column('Abilities_id', db.Integer(), db.ForeignKey('Abilities.id')))


Spells_Classes = db.Table('Spells_Classes',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('Classes_id', db.Integer(), db.ForeignKey('Classes.id')))


Spells_Archetypes = db.Table('Spells_Archetypes',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('Archetypes_id', db.Integer(), db.ForeignKey('Archetypes.id')))


Spells_DamageTypes = db.Table('Spells_DamageTypes',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Spells_EffectsResistance = db.Table('Spells_EffectsResistance',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('EffectsResistance_id', db.Integer(), db.ForeignKey('Effects.id')))


Spells_Effects = db.Table('Spells_Effects',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('Effects_id', db.Integer(), db.ForeignKey('Effects.id')))


Spells_Languages = db.Table('Spells_Languages',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('Languages_id', db.Integer(), db.ForeignKey('Languages.id')))


Spells_Abilities = db.Table('Spells_Abilities',
        db.Column('Spells_id', db.Integer(), db.ForeignKey('Spells.id')),
        db.Column('Abilities_id', db.Integer(), db.ForeignKey('Abilities.id')))


Tools_ToolTypes = db.Table('Tools_ToolTypes',
        db.Column('Tools_id', db.Integer(), db.ForeignKey('Tools.id')),
        db.Column('ToolTypes_id', db.Integer(), db.ForeignKey('ToolTypes.id')))


Weapoons_DamageTypes = db.Table('Weapoons_DamageTypes',
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')),
        db.Column('DamageTypes_id', db.Integer(), db.ForeignKey('DamageTypes.id')))


Weapoon_WeapoonTypes = db.Table('Weapoon_WeapoonTypes',
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')),
        db.Column('WeapoonTypes_id', db.Integer(), db.ForeignKey('WeapoonTypes.id')))


class Abilities(db.Model):
        __tablename__ = 'Abilities'
        id           = db.Column(db.Integer, primary_key=True)
        AbilitieName = db.Column(db.String(300), nullable=False, unique=True)
        Discription  = db.Column(db.Text, nullable=True)


class Archetypes(db.Model):
    __tablename__ = 'Archetypes'
    id                  = db.Column(db.Integer, primary_key=True)
    ArchetypeName       = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    ArmorClass          = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Archetypes_Characteristices, backref='ArchetypesCharacteristices')
    DamageResistance    = db.relationship('DamageTypes', secondary=Archetypes_ResistanceDamageTypes, backref='ArchetypesResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=Archetypes_ImmunityDamageTypes, backref='ArchetypesImmunityDamageTypes')
    EffectsResistance   = db.relationship('Effects', secondary=Archetypes_EffectsResistance, backref='ArchetypesEffectsResistance')
    Class               = db.relationship('Classes', secondary=Archetypes_Classes, backref='ArchetypesClasses')
    Spell               = db.relationship('Spells', secondary=Archetypes_Spells, backref='ArchetypesSpells')
    Skill               = db.relationship('Skills', secondary=Archetypes_Skills, backref='ArchetypesSkills')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=Archetypes_PossessionArmor, backref='ArchetypesPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=Archetypes_GunOwnership, backref='ArchetypesWeapoons')
    ToolOwnership       = db.relationship('Tools', secondary=Archetypes_ToolOwnership, backref='ArchetypesTools')
    Language            = db.relationship('Languages', secondary=Archetypes_Languages, backref='ArchetypesLanguages')
    Abilities           = db.relationship('Abilities', secondary=Archetypes_Abilities, backref='ArchetypesAbilities')


class Armors(db.Model):
    __tablename__ = 'Armors'
    id          = db.Column(db.Integer, primary_key=True)
    ArmorName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription = db.Column(db.Text, nullable=True)
    Hindrance   = db.Column(db.Boolean)
    ArmorClass  = db.Column(db.Text, nullable=True)
    Cost        = db.Column(db.Integer, nullable=True)
    Power       = db.Column(db.Text, nullable=True)
    Weight      = db.Column(db.Integer, nullable=True)
    ArmorType   = db.relationship('ArmorTypes', secondary=Armors_ArmorTypes, backref='ArmorsArmorTypes')


class ArmorTypes(db.Model):
    __tablename__ = 'ArmorTypes'
    id              = db.Column(db.Integer, primary_key=True)
    ArmorTypeName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Atributes(db.Model):
    __tablename__ = 'Atributes'
    id                = db.Column(db.Integer, primary_key=True)
    AttributeName     = db.Column(db.String(300), nullable=False, unique=True)
    Discription       = db.Column(db.Text, nullable=True)
    Characteristic    = db.relationship('Characteristices', secondary=Atributes_Characteristices, backref='AtributesCharacteristices')
    DamageResistance  = db.relationship('DamageTypes', secondary=Atributes_ResistanceDamageTypes, backref='AtributesResistanceDamageTypes')
    DamageImmunity    = db.relationship('DamageTypes', secondary=Atributes_ImmunityDamageTypes, backref='AtributesImmunityDamageTypes')
    Language          = db.relationship('Languages', secondary=Atributes_Languages, backref='AtributesLanguages')
    Spell             = db.relationship('Spells', secondary=Atributes_Spells, backref='AtributesSpells')
    Skill             = db.relationship('Skills', secondary=Atributes_Skills, backref='Atributeskills')
    PossessionArmor   = db.relationship('ArmorTypes', secondary=Atributes_PossessionArmor, backref='AtributesPossessionArmor')
    GunOwnership      = db.relationship('Weapoons', secondary=Atributes_GunOwnership, backref='AtributesWeapoons')
    ToolOwnership     = db.relationship('Tools', secondary=Atributes_ToolOwnership, backref='AtributesTools')
    EffectsResistance = db.relationship('Effects', secondary=Atributes_EffectsResistance, backref='AtributesEffectsResistance')
    Abilities         = db.relationship('Abilities', secondary=Atributes_Abilities, backref='AtributesAbilities')


class Backgrounds(db.Model):
    __tablename__ = 'Backgrounds'
    id               = db.Column(db.Integer, primary_key=True)
    BackgroundName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription      = db.Column(db.Text, nullable=True)
    Characteristic   = db.relationship('Characteristices', secondary=Backgrounds_Characteristices, backref='BackgroundsCharacteristices')
    Language         = db.relationship('Languages', secondary=Backgrounds_Languages, backref='BackgroundsLanguages')
    Skill            = db.relationship('Skills', secondary=Backgrounds_Skills, backref='BackgroundsSkills')
    ToolOwnership    = db.relationship('Tools', secondary=Backgrounds_ToolOwnership, backref='BackgroundsTools')
    Spell            = db.relationship('Spells', secondary=Backgrounds_Spells, backref='BackgroundsSpells')


class Characteristices(db.Model):
    __tablename__ = 'Characteristices'
    id                   = db.Column(db.Integer, primary_key=True)
    CharacteristicName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription          = db.Column(db.Text, nullable=True)
    Skill                = db.relationship('Skills', secondary=Characteristices_Skills, backref='CharacteristicesSkills')


class Classes(db.Model):
    __tablename__ = 'Classes'
    id                  = db.Column(db.Integer, primary_key=True)
    ClassName           = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    ArmorClass          = db.Column(db.Text, nullable=True)
    NotArmorSafe        = db.Column(db.Boolean, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Classes_Characteristices, backref='ClassesCharacteristices')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=Classes_PossessionArmor, backref='ClassesPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=Classes_GunOwnership, backref='ClassesGunOwnership')
    ToolOwnership       = db.relationship('Tools', secondary=Classes_ToolOwnership, backref='ClassesToolOwnership')
    Skill               = db.relationship('Skills', secondary=Classes_Skills, backref='ClassesSkills')
    Spell               = db.relationship('Spells', secondary=Classes_Spells, backref='ClassesSpells')
    Language            = db.relationship('Languages', secondary=Classes_Languages, backref='ClassesLanguages')


class DamageTypes(db.Model):
    __tablename__ = 'DamageTypes'
    id              = db.Column(db.Integer, primary_key=True)
    DamageTypeName  = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Effects(db.Model):
    __tablename__ = ' Effects'
    id           = db.Column(db.Integer, primary_key=True)
    EffectName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription  = db.Column(db.Text, nullable=True)


class Equipments(db.Model):
    __tablename__ = 'Equipments'
    id              = db.Column(db.Integer, primary_key=True)
    EquipmentName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)
    Cost            = db.Column(db.Integer, nullable=True)
    Weight          = db.Column(db.Integer, nullable=True)
    EquipmentType   = db.relationship('EquipmentTypes', secondary=Equipments_EquipmentTypes, backref='EquipmentsEquipmentTypes')


class EquipmentTypes(db.Model):
    __tablename__ = 'EquipmentTypes'
    id                  = db.Column(db.Integer, primary_key=True)
    EquipmentTypeName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)


class Languages(db.Model):
    __tablename__ = 'Languages'
    id                      = db.Column(db.Integer, primary_key=True)
    LanguageName            = db.Column(db.String(300), nullable=False, unique=True)
    Discription             = db.Column(db.Text, nullable=True)
    TypicalRepresentative   = db.Column(db.Text, nullable=True)
    Writing                 = db.Column(db.Text, nullable=True)


class MagicalItems(db.Model):
    __tablename__ = 'MagicalItems'
    id                  = db.Column(db.Integer, primary_key=True)
    MagicalItemsName    = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    PowerBonus          = db.Column(db.Text, nullable=True)
    ArmorBonus          = db.Column(db.Text, nullable=True)
    MagicalItemType     = db.relationship('MagicalItemsTypes', secondary=MagicalItems_MagicalItemsTypes, backref='MagicalItemsMagicalItemsTypes')
    Characteristic      = db.relationship('Characteristices', secondary=MagicalItems_Characteristices, backref='MagicalItemsCharacteristices')
    Spell               = db.relationship('Spells', secondary=MagicalItems_Spells, backref='MagicalItemsSpells')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=MagicalItems_PossessionArmor, backref='MagicalItemsPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=MagicalItems_GunOwnership, backref='MagicalItemsGunOwnership')
    ToolOwnership       = db.relationship('Tools', secondary=MagicalItems_ToolOwnership, backref='MagicalItemsToolOwnership')
    DamageResistance    = db.relationship('DamageTypes', secondary=MagicalItems_ResistanceDamageTypes, backref='MagicalItemsResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=MagicalItems_ImmunityDamageTypes, backref='MagicalItemsImmunityDamageTypesDND')
    Skill               = db.relationship('Skills', secondary=MagicalItems_Skills, backref='MagicalItemsSkills')
    Language            = db.relationship('Languages', secondary=MagicalItems_Languages, backref='MagicalItemsLanguages')
    EffectsResistance   = db.relationship('Effects', secondary=MagicalItems_EffectsResistance, backref='MagicalItemsEffectsResistance')
    Effects             = db.relationship('Effects', secondary=MagicalItems_Effects, backref='MagicalItemsEffects')
    Abilities           = db.relationship('Abilities', secondary=MagicalItems_Abilities, backref='MagicalItemsAbilities')
    ArmorType           = db.relationship('Armors', secondary=MagicalItems_Armors, backref='MagicalItemsArmors')
    WeapoonType         = db.relationship('Weapoons', secondary=MagicalItems_Weapoons, backref='MagicalItemsWeapoons')


class MagicalItemsTypes(db.Model):
    __tablename__ = 'MagicalItemsTypes'
    id                  = db.Column(db.Integer, primary_key=True)
    MagicalItemTypeName = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)


class Races(db.Model):
    __tablename__ = 'Races'
    id                  = db.Column(db.Integer, primary_key=True)
    RaceName            = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    Speed               = db.Column(db.Integer, nullable=True)
    Climb               = db.Column(db.Integer, nullable=True)
    Fly                 = db.Column(db.Integer, nullable=True)
    Swim                = db.Column(db.Integer, nullable=True)
    Fight               = db.Column(db.Text, nullable=True)
    Armor               = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Races_Characteristices, backref='RacesCharacteristices')
    DamageResistance    = db.relationship('DamageTypes', secondary=Races_ResistanceDamageTypes, backref='RacesResistanceDamageTypesDND')
    DamageImmunity      = db.relationship('DamageTypes', secondary=Races_ImmunityDamageTypes, backref='RacesImmunityDamageTypesDND')
    Spell               = db.relationship('Spells', secondary=Races_Spells, backref='RacesSpells')
    Skill               = db.relationship('Skills', secondary=Races_Skills, backref='RacesSkills')
    Language            = db.relationship('Languages', secondary=Races_Languages, backref='RacesLanguages')
    PossessionArmor     = db.relationship('ArmorTypes', secondary=Races_PossessionArmor, backref='RacesPossessionArmor')
    GunOwnership        = db.relationship('Weapoons', secondary=Races_GunOwnership, backref='RacesGunOwnership')
    ToolOwnership       = db.relationship('Tools', secondary=Races_ToolOwnership, backref='RacesToolOwnership')
    EffectsResistance   = db.relationship('Effects', secondary=Races_EffectsResistance, backref='RacesEffectsResistance')
    Abilities           = db.relationship('Abilities', secondary=Races_Abilities, backref='RacesAbilities')


class Skills(db.Model):
    __tablename__ = 'Skills'
    id           = db.Column(db.Integer, primary_key=True)
    SkillsName   = db.Column(db.String(300), nullable=False, unique=True)
    Discription  = db.Column(db.Text, nullable=True)


class Spells(db.Model):
    __tablename__ = 'Spells'
    id                = db.Column(db.Integer, primary_key=True)
    SpellName         = db.Column(db.String(300), nullable=False, unique=True)
    Discription       = db.Column(db.Text, nullable=True)
    Damage            = db.Column(db.Text, nullable=True)
    ApplicationTime   = db.Column(db.Text, nullable=True)
    Distance          = db.Column(db.Text, nullable=True)
    Components        = db.Column(db.Text, nullable=True)
    Duration          = db.Column(db.Text, nullable=True)
    LevelSpell        = db.Column(db.Integer, nullable=True)
    Subclasses        = db.Column(db.Integer, nullable=True)
    Ritual            = db.Column(db.Boolean, nullable=True)
    Class             = db.relationship('Classes', secondary=Spells_Classes, backref='SpellsClasses')
    Archetype         = db.relationship('Archetypes', secondary=Spells_Archetypes, backref='SpellsArchetypes')
    DamageType        = db.relationship('DamageTypes', secondary=Spells_DamageTypes, backref='SpellsDamageTypes')
    EffectsResistance = db.relationship('Effects', secondary=Spells_EffectsResistance, backref='SpellsEffectsResistance')
    Effects           = db.relationship('Effects', secondary=Spells_Effects, backref='SpellsEffects')
    Language          = db.relationship('Languages', secondary=Spells_Languages, backref='SpellsLanguages')
    Abilities         = db.relationship('Abilities', secondary=Spells_Abilities, backref='SpellsAbilities')


class Tools(db.Model):
    __tablename__ = 'Tools'
    id          = db.Column(db.Integer, primary_key=True)
    ToolName    = db.Column(db.String(300), nullable=False, unique=True)
    Discription = db.Column(db.Text, nullable=True)
    Cost        = db.Column(db.Integer, nullable=True)
    Weight      = db.Column(db.Integer, nullable=True)
    ToolType    = db.relationship('ToolTypes', secondary=Tools_ToolTypes, backref='ToolsToolTypes')


class ToolTypes(db.Model):
    __tablename__ = 'ToolTypes'
    id              = db.Column(db.Integer, primary_key=True)
    ToolTypeName    = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Weapoons(db.Model):
    __tablename__ = 'Weapoons'
    id              = db.Column(db.Integer, primary_key=True)
    WeapoonName     = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)
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
    Discription         = db.Column(db.Text, nullable=True)


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


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)


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
        magicalItemsType1 = MagicalItemsTypes(MagicalItemTypeName='Доспех', Discription='')
        magicalItemsType2 = MagicalItemsTypes(MagicalItemTypeName='Оружие', Discription='')
        db.session.add(magicalItemsType1)
        db.session.add(magicalItemsType2)
        db.session.commit()


@app.route("/CreateAbilities", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateAbilities():
    if request.method == 'POST':
        AbilitiesName   = request.form['AbilitieName']
        Discription     = request.form['Discription']
        abilities       = Abilities(AbilitiesName=AbilitiesName, Discription=Discription)
        try:
            db.session.add(abilities)
            db.session.commit()
            return render_template("CreatePosts/CreateAbilities.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        ClassName       = request.form['ClassName']
        if 'NotArmorSafe' in request.form:
            NotArmorSafe=True
        else:
            NotArmorSafe=False
        archetypes = Archetypes(ArchetypeName=ArchetypeName, Discription=Discription, NotArmorSafe=NotArmorSafe
                                , ArmorClass=ArmorClass)
        MassivClasses               = parametrsoutput(request.form['ClassName'])
        MassivClassApd              = [MassivClasses, Classes, archetypes.Class]
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        armors = Armors(ArmorName=ArmorName, Discription=Discription, Weight=Weight, Power=Power
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateArmors.html", ArmorTypes=armorTypes)


@app.route("/CreateArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateArmorTypes():
    if request.method == 'POST':
        ArmorTypeName   = request.form['ArmorTypeName']
        Discription     = request.form['Discription']
        ArmorType       = ArmorTypes(ArmorTypeName=ArmorTypeName, Discription=Discription)
        try:
            db.session.add(ArmorType)
            db.session.commit()
            return render_template("CreatePosts/CreateArmorTypes.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateArmorTypes.html")


@app.route("/CreateAttributes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateAttributes():
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
        Attribute                   = Atributes(AttributeName=AttributeName, Discription=Discription)
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
                return render_template("CreatePosts/CreateAttributes.html", Characteristices=characteristices
                                           , DamageTypes=damageTypes, Effects=effects, Spells=spells, Skills=skills, ArmorTypes=PossessionArmor
                                           , Weapoons=GunOwnership, Tools=ToolOwnership, Languages=languages, Abilities=abilities)
            except:
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateAttributes.html", Characteristices=characteristices
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
        Background                   = Backgrounds(BackgroundName=BackgroundName, Discription=Discription)
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Characteristic       = Characteristices(CharacteristicName=CharacteristicName, Discription=Discription)
        MassivSkills         = parametrsoutput(request.form['Skills'])
        MassivSkillsApd      = [MassivSkills, Characteristic, Characteristic.Skill]
        MassivDates          = [MassivSkillsApd]
        res = appenddatas(MassivDates)
        if res:
            try:
                db.session.add(Characteristic)
                db.session.commit()
                return render_template("CreatePosts/CreateCharacteristices.html", Skills=skills)
            except:
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Class = Classes(ClassName=ClassName, Discription=Discription, NotArmorSafe=NotArmorSafe
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        DamageType      = DamageTypes(DamageTypeName=DamageTypeName, Discription=Discription)
        try:
            db.session.add(DamageType)
            db.session.commit()
            return render_template("CreatePosts/CreateDamageTypes.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateDamageTypes.html")


@app.route("/CreateEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEffects():
    if request.method == 'POST':
        EffectName  = request.form['EffectName']
        Discription = request.form['Discription']
        Effect      = Effects(EffectName=EffectName, Discription=Discription)
        try:
            db.session.add(Effect)
            db.session.commit()
            return render_template("CreatePosts/CreateEffects.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Equipment = Equipments(EquipmentName=EquipmentName, Discription=Discription, Weight=Weight, Cost=Cost)
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateEquipments.html", EquipmentTypes=equipmentTypes)


@app.route("/CreateEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateEquipmentTypes():
    if request.method == 'POST':
        EquipmentTypeName   = request.form['EquipmentTypeName']
        Discription         = request.form['Discription']
        EquipmentType       = EquipmentTypes(EquipmentTypeName=EquipmentTypeName, Discription=Discription)
        try:
            db.session.add(EquipmentType)
            db.session.commit()
            return render_template("CreatePosts/CreateEquipmentTypes.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateEquipmentTypes.html")


@app.route("/CreateLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateLanguages():
    if request.method == 'POST':
        LanguageName            = request.form['LanguageName']
        Discription             = request.form['Discription']
        TypicalRepresentative   = request.form['TypicalRepresentative']
        Writing                 = request.form['Writing']
        Language                = Languages(LanguageName=LanguageName, Discription=Discription
                                             , TypicalRepresentative=TypicalRepresentative, Writing=Writing)
        try:
            db.session.add(Language)
            db.session.commit()
            return render_template("CreatePosts/CreateLanguages.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        MagicalItem         = MagicalItems(MagicalItemsName=MagicalItemsName, Discription=Discription, ArmorBonus=ArmorBonus
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
        MassivArmorTypesApd         = [MassivArmorTypes, Armors, MagicalItem.ArmorType]
        MassivWeapoonTypes          = parametrsoutput(request.form['WeapoonTypes'])
        MassivWeapoonTypesApd       = [MassivWeapoonTypes, Weapoons, MagicalItem.WeapoonType]
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        MagicalItemsType    = MagicalItemsTypes(MagicalItemTypeName=MagicalItemTypeName, Discription=Discription)
        try:
            db.session.add(MagicalItemsType)
            db.session.commit()
            return render_template("CreatePosts/CreateMagicalItemTypes.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Race            = Races(RaceName=RaceName, Discription=Discription
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Skill       = Skills(SkillName=SkillName, Discription=Discription)
        try:
            db.session.add(Skill)
            db.session.commit()
            return render_template("CreatePosts/CreateSkills.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Spell               = Spells(SpellName=SpellName, Discription=Discription, Damage=Damage
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
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
        Tool        = Tools(ToolName=ToolName, Discription=Discription, Weight=Weight, Cost=Cost)
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
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateTools.html", ToolTypes=toolTypes)


@app.route("/CreateToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateToolTypes():
    if request.method == 'POST':
        ToolTypeName  = request.form['ToolTypeName']
        Discription   = request.form['Discription']
        ToolType      = ToolTypes(ToolTypeName=ToolTypeName, Discription=Discription)
        try:
            db.session.add(ToolType)
            db.session.commit()
            return render_template("CreatePosts/CreateToolTypes.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateToolTypes.html")


@app.route("/CreateWeapons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapons():
    toolTypes   = ToolTypes.query.all()
    damageTypes = DamageTypes.query.all()
    if request.method == 'POST':
        WeapoonName    = request.form['WeapoonName']
        Discription = request.form['Discription']
        Weight      = request.form['Weight']
        Cost        = request.form['Cost']
        Damage      = request.form['Damage']
        Weapoon               = Weapoons(WeapoonName=WeapoonName, Discription=Discription, Weight=Weight
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
                return render_template("CreatePosts/CreateWeapons.html", ToolTypes=toolTypes, DamageTypes=damageTypes)
            except:
                return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
        else:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateWeapons.html", ToolTypes=toolTypes, DamageTypes=damageTypes)


@app.route("/CreateWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def CreateWeapoonTypes():
    if request.method == 'POST':
        WeapoonTypeName  = request.form['WeapoonTypeName']
        Discription      = request.form['Discription']
        WeapoonType      = WeapoonTypes(WeapoonTypeName=WeapoonTypeName, Discription=Discription)
        try:
            db.session.add(WeapoonType)
            db.session.commit()
            return render_template("CreatePosts/CreateWeapoonTypes.html")
        except:
            return render_template("CreatePosts/CreateMaterial.html", msg='Ошибка загрузки данных')
    else:
        return render_template("CreatePosts/CreateWeapoonTypes.html")


@app.route("/VeiwAbilities", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwAbilities():
    abilities = Abilities.query.all()
    return render_template("CreatePosts/VeiwAbilities.html", Abilities=abilities)


@app.route("/VeiwArchetypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwArchetypes():
    archetypes = Archetypes.query.all()
    return render_template("CreatePosts/VeiwArchetypes.html", Archetypes=archetypes)


@app.route("/VeiwArmors", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwArmors():
    armors = Armors.query.all()
    return render_template("CreatePosts/VeiwArmors.html", Armors=armors)


@app.route("/VeiwArmorTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwArmorTypes():
    armorTypes = ArmorTypes.query.all()
    return render_template("CreatePosts/VeiwArmorTypes.html", ArmorTypes=armorTypes)


@app.route("/VeiwAttributes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwAttributes():
    atributes = Atributes.query.all()
    return render_template("CreatePosts/VeiwAttributes.html", Atributes=atributes)


@app.route("/VeiwBackgrounds", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwBackgrounds():
    backgrounds = Backgrounds.query.all()
    return render_template("CreatePosts/VeiwBackgrounds.html", Backgrounds=backgrounds)


@app.route("/VeiwCharacteristices", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwCharacteristices():
    characteristices = Characteristices.query.all()
    return render_template("CreatePosts/VeiwCharacteristices.html", Characteristices=characteristices)


@app.route("/VeiwClasses", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwClasses():
    classes = Classes.query.all()
    return render_template("CreatePosts/VeiwClasses.html", Classes=classes)


@app.route("/VeiwDamageTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwDamageTypes():
    damageTypes = DamageTypes.query.all()
    return render_template("CreatePosts/VeiwDamageTypes.html", DamageTypes=damageTypes)


@app.route("/VeiwEffects", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwEffects():
    effects = Effects.query.all()
    return render_template("CreatePosts/VeiwEffects.html", Effects=effects)


@app.route("/VeiwEquipments", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwEquipments():
    equipments = Equipments.query.all()
    return render_template("CreatePosts/VeiwEquipments.html", Equipments=equipments)


@app.route("/VeiwEquipmentTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwEquipmentTypes():
    equipmentTypes = EquipmentTypes.query.all()
    return render_template("CreatePosts/VeiwEquipmentTypes.html", EquipmentTypes=equipmentTypes)


@app.route("/VeiwLanguages", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwLanguages():
    languages = Languages.query.all()
    return render_template("CreatePosts/VeiwLanguages.html", Languages=languages)


@app.route("/VeiwMagicalItems", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwMagicalItems():
    magicalItems = MagicalItems.query.all()
    return render_template("CreatePosts/VeiwMagicalItems.html", MagicalItems=magicalItems)


@app.route("/VeiwMagicalItemTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwMagicalItemTypes():
    magicalItemsTypes = MagicalItemsTypes.query.all()
    return render_template("CreatePosts/VeiwMagicalItemTypes.html", MagicalItemsTypes=magicalItemsTypes)


@app.route("/VeiwRaces", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwRaces():
    races = Races.query.all()
    return render_template("CreatePosts/VeiwRaces.html", Races=races)


@app.route("/VeiwSkills", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwSkills():
    skills = Skills.query.all()
    return render_template("CreatePosts/VeiwSkills.html", Skills=skills)


@app.route("/VeiwSpells", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwSpells():
    spells = Spells.query.all()
    return render_template("CreatePosts/VeiwSpells.html", Spells=spells)


@app.route("/VeiwTools", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwTools():
    tools = Tools.query.all()
    return render_template("CreatePosts/VeiwTools.html", Tools=tools)


@app.route("/VeiwToolTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwToolTypes():
    toolTypes = ToolTypes.query.all()
    return render_template("CreatePosts/VeiwToolTypes.html", ToolTypes=toolTypes)


@app.route("/VeiwWeapons", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwWeapons():
    weapoons = Weapoons.query.all()
    return render_template("CreatePosts/VeiwWeapons.html", Weapoons=weapoons)


@app.route("/VeiwWeapoonTypes", methods=['GET', 'POST'])
@roles_accepted('Admin', 'Master')
def VeiwWeapoonTypes():
    weapoonTypes = WeapoonTypes.query.all()
    return render_template("CreatePosts/VeiwWeapoonTypes.html", WeapoonTypes=weapoonTypes)


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
@roles_accepted('Admin', 'Master')
def VeiwMaterial():
    return render_template("VeiwMaterial.html")


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

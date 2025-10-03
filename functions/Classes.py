from flask_sqlalchemy import SQLAlchemy
from flask_security import (UserMixin, RoleMixin)

db = SQLAlchemy()

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
        db.Column('Atributes_id', db.Integer(), db.ForeignKey('Atributes.id')),
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


Weapoons_WeapoonTypes = db.Table('Weapoons_WeapoonTypes',
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')),
        db.Column('WeapoonTypes_id', db.Integer(), db.ForeignKey('WeapoonTypes.id')))


Weapoons_Features = db.Table('Weapoons_Features',
        db.Column('Weapoons_id', db.Integer(), db.ForeignKey('Weapoons.id')),
        db.Column('Features_id', db.Integer(), db.ForeignKey('Features.id')))


Roles_Users = db.Table('Roles_Users',
        db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('Role.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id          = db.Column(db.Integer, autoincrement=True, primary_key=True)
    login       = db.Column(db.String, unique=True)
    password    = db.Column(db.String(255), nullable=False, server_default='')
    active      = db.Column(db.Boolean())
    roles       = db.relationship('Role'  , secondary=Roles_Users
                                                , backref=db.backref("roled", cascade='all,delete',single_parent=True, passive_deletes=True)
                                                , cascade='all,delete'      , single_parent=True)


class Role(db.Model, RoleMixin):
    __tablename__ = 'Role'
    id       = db.Column(db.Integer(), primary_key=True)
    RoleName = db.Column(db.String(80), unique=True)
    name     = db.Column(db.String(80), unique=True)
    NameUser = db.Column(db.String(80), unique=True)


class Abilities(db.Model):
        __tablename__ = 'Abilities'
        id            = db.Column(db.Integer, primary_key=True)
        Name          = db.Column(db.String(300), nullable=False, unique=True)
        Discription   = db.Column(db.Text, nullable=True)


class Archetypes(db.Model):
    __tablename__ = 'Archetypes'
    id                  = db.Column(db.Integer, primary_key=True)
    Name                = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    ArmorClass          = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Archetypes_Characteristices
                                            , backref=db.backref("ArchetypesCharacteristices"        , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageResistance    = db.relationship('DamageTypes'     , secondary=Archetypes_ResistanceDamageTypes
                                            , backref=db.backref("ArchetypesResistanceDamageTypes"   , cascade='all,delete', single_parent=True,  passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageImmunity      = db.relationship('DamageTypes'     , secondary=Archetypes_ImmunityDamageTypes
                                            , backref=db.backref("ArchetypesImmunityDamageTypes"     , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    EffectsResistance   = db.relationship('Effects'         , secondary=Archetypes_EffectsResistance
                                            , backref=db.backref("ArchetypesEffectsResistance"       , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete',  single_parent=True)
    Class               = db.relationship('Classes'         , secondary=Archetypes_Classes
                                            , backref=db.backref("ArchetypesClasses"                 , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Spell               = db.relationship('Spells'          , secondary=Archetypes_Spells
                                            , backref=db.backref("ArchetypesSpells"                  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Skill               = db.relationship('Skills'          , secondary=Archetypes_Skills
                                            , backref=db.backref("ArchetypesSkills"                  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    PossessionArmor     = db.relationship('ArmorTypes'      , secondary=Archetypes_PossessionArmor
                                            , backref=db.backref("ArchetypesPossessionArmor"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    GunOwnership        = db.relationship('Weapoons'        , secondary=Archetypes_GunOwnership
                                            , backref=db.backref("ArchetypesWeapoons"                , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ToolOwnership       = db.relationship('Tools'           , secondary=Archetypes_ToolOwnership
                                            , backref=db.backref("ArchetypesTools"                   , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language            = db.relationship('Languages'       , secondary=Archetypes_Languages
                                            , backref=db.backref("ArchetypesLanguages"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Abilities           = db.relationship('Abilities'       , secondary=Archetypes_Abilities
                                            , backref=db.backref("ArchetypesAbilities"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class Armors(db.Model):
    __tablename__ = 'Armors'
    id          = db.Column(db.Integer, primary_key=True)
    Name        = db.Column(db.String(300), nullable=False, unique=True)
    Discription = db.Column(db.Text, nullable=True)
    Hindrance   = db.Column(db.Boolean)
    ArmorClass  = db.Column(db.Text, nullable=True)
    Cost        = db.Column(db.Integer, nullable=True)
    Power       = db.Column(db.Text, nullable=True)
    Weight      = db.Column(db.Integer, nullable=True)
    ArmorType   = db.relationship('ArmorTypes'              , secondary=Armors_ArmorTypes
                                            , backref=db.backref("ArmorsArmorTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class ArmorTypes(db.Model):
    __tablename__ = 'ArmorTypes'
    id              = db.Column(db.Integer, primary_key=True)
    Name            = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Atributes(db.Model):
    __tablename__ = 'Atributes'
    id                = db.Column(db.Integer, primary_key=True)
    Name              = db.Column(db.String(300), nullable=False, unique=True)
    Discription       = db.Column(db.Text, nullable=True)
    Characteristic    = db.relationship('Characteristices'  , secondary=Atributes_Characteristices
                                            , backref=db.backref("AtributesCharacteristices"     , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageResistance  = db.relationship('DamageTypes'       , secondary=Atributes_ResistanceDamageTypes
                                            , backref=db.backref("AtributesResistanceDamageTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageImmunity    = db.relationship('DamageTypes'       , secondary=Atributes_ImmunityDamageTypes
                                            , backref=db.backref("AtributesImmunityDamageTypes"  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language          = db.relationship('Languages'         , secondary=Atributes_Languages
                                            , backref=db.backref("AtributesLanguages"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Spell             = db.relationship('Spells'            , secondary=Atributes_Spells
                                            , backref=db.backref("AtributesSpells"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Skill             = db.relationship('Skills'            , secondary=Atributes_Skills
                                            , backref=db.backref("Atributeskills"                , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    PossessionArmor   = db.relationship('ArmorTypes'        , secondary=Atributes_PossessionArmor
                                            , backref=db.backref("AtributesPossessionArmor"      , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    GunOwnership      = db.relationship('Weapoons'          , secondary=Atributes_GunOwnership
                                            , backref=db.backref("AtributesGunOwnership"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ToolOwnership     = db.relationship('Tools'             , secondary=Atributes_ToolOwnership
                                            , backref=db.backref("AtributesToolOwnership"        , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    EffectsResistance = db.relationship('Effects'           , secondary=Atributes_EffectsResistance
                                            , backref=db.backref("AtributesEffectsResistance"    , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Abilities         = db.relationship('Abilities'         , secondary=Atributes_Abilities
                                            , backref=db.backref("AtributesAbilities"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class Backgrounds(db.Model):
    __tablename__ = 'Backgrounds'
    id               = db.Column(db.Integer, primary_key=True)
    Name             = db.Column(db.String(300), nullable=False, unique=True)
    Discription      = db.Column(db.Text, nullable=True)
    Characteristic   = db.relationship('Characteristices'   , secondary=Backgrounds_Characteristices
                                            , backref=db.backref("BackgroundsCharacteristices"  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language         = db.relationship('Languages'          , secondary=Backgrounds_Languages
                                            , backref=db.backref("BackgroundsLanguages"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Skill            = db.relationship('Skills'             , secondary=Backgrounds_Skills
                                            , backref=db.backref("BackgroundsSkills"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ToolOwnership    = db.relationship('Tools'              , secondary=Backgrounds_ToolOwnership
                                            , backref=db.backref("BackgroundsToolOwnership"     , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Spell            = db.relationship('Spells'             , secondary=Backgrounds_Spells
                                            , backref=db.backref("BackgroundsSpells"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class Characteristices(db.Model):
    __tablename__ = 'Characteristices'
    id                   = db.Column(db.Integer, primary_key=True)
    Name                 = db.Column(db.String(300), nullable=False, unique=True)
    Discription          = db.Column(db.Text, nullable=True)
    Skill                = db.relationship('Skills'        , secondary=Characteristices_Skills
                                           , backref=db.backref("CharacteristicesSkills", cascade='all,delete', single_parent=True, passive_deletes=True)
                                           , cascade='all,delete', single_parent=True)


class Classes(db.Model):
    __tablename__ = 'Classes'
    id                  = db.Column(db.Integer, primary_key=True)
    Name                = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    ArmorClass          = db.Column(db.Text, nullable=True)
    NotArmorSafe        = db.Column(db.Boolean, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Classes_Characteristices
                                            , backref=db.backref("ClassesCharacteristices"  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    PossessionArmor     = db.relationship('ArmorTypes'      , secondary=Classes_PossessionArmor
                                            , backref=db.backref("ClassesPossessionArmor"   , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    GunOwnership        = db.relationship('Weapoons'        , secondary=Classes_GunOwnership
                                            , backref=db.backref("ClassesGunOwnership"      , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ToolOwnership       = db.relationship('Tools'           , secondary=Classes_ToolOwnership
                                            , backref=db.backref("ClassesToolOwnership"     , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete',  single_parent=True)
    Skill               = db.relationship('Skills'          , secondary=Classes_Skills
                                            , backref=db.backref("ClassesSkills"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Spell               = db.relationship('Spells'          , secondary=Classes_Spells
                                            , backref=db.backref("ClassesSpells"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language            = db.relationship('Languages'       , secondary=Classes_Languages
                                            , backref=db.backref("ClassesLanguages"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class DamageTypes(db.Model):
    __tablename__ = 'DamageTypes'
    id              = db.Column(db.Integer, primary_key=True)
    Name            = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Effects(db.Model):
    __tablename__ = 'Effects'
    id           = db.Column(db.Integer, primary_key=True)
    Name         = db.Column(db.String(300), nullable=False, unique=True)
    Discription  = db.Column(db.Text, nullable=True)


class Equipments(db.Model):
    __tablename__ = 'Equipments'
    id              = db.Column(db.Integer, primary_key=True)
    Name            = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)
    Cost            = db.Column(db.Integer, nullable=True)
    Weight          = db.Column(db.Integer, nullable=True)
    EquipmentType   = db.relationship('EquipmentTypes'      , secondary=Equipments_EquipmentTypes
                                            , backref=db.backref("EquipmentsEquipmentTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class EquipmentTypes(db.Model):
    __tablename__ = 'EquipmentTypes'
    id                  = db.Column(db.Integer, primary_key=True)
    Name                = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)


class Features(db.Model):
    __tablename__ = 'Features'
    id              = db.Column(db.Integer, primary_key=True)
    Name            = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Languages(db.Model):
    __tablename__ = 'Languages'
    id                      = db.Column(db.Integer, primary_key=True)
    Name                    = db.Column(db.String(300), nullable=False, unique=True)
    Discription             = db.Column(db.Text, nullable=True)
    TypicalRepresentative   = db.Column(db.Text, nullable=True)
    Writing                 = db.Column(db.Text, nullable=True)


class MagicalItems(db.Model):
    __tablename__ = 'MagicalItems'
    id                  = db.Column(db.Integer, primary_key=True)
    Name                = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    PowerBonus          = db.Column(db.Text, nullable=True)
    ArmorBonus          = db.Column(db.Text, nullable=True)
    MagicalItemType     = db.relationship('MagicalItemsTypes', secondary=MagicalItems_MagicalItemsTypes
                                            , backref=db.backref("MagicalItemsMagicalItemsTypes"    , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Characteristic      = db.relationship('Characteristices', secondary=MagicalItems_Characteristices
                                            , backref=db.backref("MagicalItemsCharacteristices"     , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Spell               = db.relationship('Spells'          , secondary=MagicalItems_Spells
                                            , backref=db.backref("MagicalItemsSpells"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    PossessionArmor     = db.relationship('ArmorTypes'      , secondary=MagicalItems_PossessionArmor
                                            , backref=db.backref("MagicalItemsPossessionArmor"      , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    GunOwnership        = db.relationship('Weapoons'        , secondary=MagicalItems_GunOwnership
                                            , backref=db.backref("MagicalItemsGunOwnership"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ToolOwnership       = db.relationship('Tools'           , secondary=MagicalItems_ToolOwnership
                                            , backref=db.backref("MagicalItemsToolOwnership"        , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete',  single_parent=True)
    DamageResistance    = db.relationship('DamageTypes'     , secondary=MagicalItems_ResistanceDamageTypes
                                            , backref=db.backref("MagicalItemsResistanceDamageTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageImmunity      = db.relationship('DamageTypes'     , secondary=MagicalItems_ImmunityDamageTypes
                                            , backref=db.backref("MagicalItemsImmunityDamageTypes"  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Skill               = db.relationship('Skills'          , secondary=MagicalItems_Skills
                                            , backref=db.backref("MagicalItemsSkills"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language            = db.relationship('Languages'       , secondary=MagicalItems_Languages
                                            , backref=db.backref("MagicalItemsLanguages"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    EffectsResistance   = db.relationship('Effects'         , secondary=MagicalItems_EffectsResistance
                                            , backref=db.backref("MagicalItemsEffectsResistance"    , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Effects             = db.relationship('Effects'         , secondary=MagicalItems_Effects
                                            , backref=db.backref("MagicalItemsEffects"              , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Abilities           = db.relationship('Abilities'       , secondary=MagicalItems_Abilities
                                            , backref=db.backref("MagicalItemsAbilities"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ArmorTypeItem       = db.relationship('Armors'          , secondary=MagicalItems_Armors
                                            , backref=db.backref("MagicalItemsArmors"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    WeapoonTypeItem     = db.relationship('Weapoons'        , secondary=MagicalItems_Weapoons
                                            , backref=db.backref("MagicalItemsWeapoons"             , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class MagicalItemsTypes(db.Model):
    __tablename__ = 'MagicalItemsTypes'
    id                      = db.Column(db.Integer, primary_key=True)
    Name                    = db.Column(db.String(300), nullable=False, unique=True)
    Discription             = db.Column(db.Text, nullable=True)


class Races(db.Model):
    __tablename__ = 'Races'
    id                  = db.Column(db.Integer, primary_key=True)
    Name                = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
    Speed               = db.Column(db.Integer, nullable=True)
    Climb               = db.Column(db.Integer, nullable=True)
    Fly                 = db.Column(db.Integer, nullable=True)
    Swim                = db.Column(db.Integer, nullable=True)
    Fight               = db.Column(db.Text, nullable=True)
    Armor               = db.Column(db.Text, nullable=True)
    Characteristic      = db.relationship('Characteristices', secondary=Races_Characteristices
                                            , backref=db.backref("RacesCharacteristices"        , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageResistance    = db.relationship('DamageTypes'     , secondary=Races_ResistanceDamageTypes
                                            , backref=db.backref("RacesResistanceDamageTypes"   , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageImmunity      = db.relationship('DamageTypes'     , secondary=Races_ImmunityDamageTypes
                                            , backref=db.backref("RacesImmunityDamageTypes"     , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Spell               = db.relationship('Spells'          , secondary=Races_Spells
                                            , backref=db.backref("RacesSpells"                  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Skill               = db.relationship('Skills'          , secondary=Races_Skills
                                            , backref=db.backref("RacesSkills"                  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language            = db.relationship('Languages'       , secondary=Races_Languages
                                            , backref=db.backref("RacesLanguages"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    PossessionArmor     = db.relationship('ArmorTypes'      , secondary=Races_PossessionArmor
                                            , backref=db.backref("RacesPossessionArmor"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    GunOwnership        = db.relationship('Weapoons'        , secondary=Races_GunOwnership
                                            , backref=db.backref("RacesGunOwnership"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    ToolOwnership       = db.relationship('Tools'           , secondary=Races_ToolOwnership
                                            , backref=db.backref("RacesToolOwnership"           , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    EffectsResistance   = db.relationship('Effects'         , secondary=Races_EffectsResistance
                                            , backref=db.backref("RacesEffectsResistance"       , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Abilities           = db.relationship('Abilities'       , secondary=Races_Abilities
                                            , backref=db.backref("RacesAbilities"               , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class Skills(db.Model):
    __tablename__ = 'Skills'
    id           = db.Column(db.Integer, primary_key=True)
    Name         = db.Column(db.String(300), nullable=False, unique=True)
    Discription  = db.Column(db.Text, nullable=True)


class Spells(db.Model):
    __tablename__ = 'Spells'
    id                = db.Column(db.Integer, primary_key=True)
    Name              = db.Column(db.String(300), nullable=False, unique=True)
    Discription       = db.Column(db.Text, nullable=True)
    Damage            = db.Column(db.Text, nullable=True)
    ApplicationTime   = db.Column(db.Text, nullable=True)
    Distance          = db.Column(db.Text, nullable=True)
    Components        = db.Column(db.Text, nullable=True)
    Duration          = db.Column(db.Text, nullable=True)
    LevelSpell        = db.Column(db.Integer, nullable=True)
    Ritual            = db.Column(db.Boolean, nullable=True)
    Class             = db.relationship('Classes'           , secondary=Spells_Classes
                                            , backref=db.backref("SpellsClasses"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Archetype         = db.relationship('Archetypes'        , secondary=Spells_Archetypes
                                            , backref=db.backref("SpellsArchetypes"         , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageType        = db.relationship('DamageTypes'       , secondary=Spells_DamageTypes
                                            , backref=db.backref("SpellsDamageTypes"        , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    EffectsResistance = db.relationship('Effects'           , secondary=Spells_EffectsResistance
                                            , backref=db.backref("SpellsEffectsResistance"  , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Effects           = db.relationship('Effects'           , secondary=Spells_Effects
                                            , backref=db.backref("SpellsEffects"            , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Language          = db.relationship('Languages'         , secondary=Spells_Languages
                                            , backref=db.backref("SpellsLanguages"          , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    Abilities         = db.relationship('Abilities'         , secondary=Spells_Abilities
                                            , backref=db.backref("SpellsAbilities"          , cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class Tools(db.Model):
    __tablename__ = 'Tools'
    id          = db.Column(db.Integer, primary_key=True)
    Name        = db.Column(db.String(300), nullable=False, unique=True)
    Discription = db.Column(db.Text, nullable=True)
    Cost        = db.Column(db.Integer, nullable=True)
    Weight      = db.Column(db.Integer, nullable=True)
    ToolType    = db.relationship('ToolTypes'               , secondary=Tools_ToolTypes
                                            , backref=db.backref("ToolsToolTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class ToolTypes(db.Model):
    __tablename__ = 'ToolTypes'
    id              = db.Column(db.Integer, primary_key=True)
    Name            = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)


class Weapoons(db.Model):
    __tablename__ = 'Weapoons'
    id              = db.Column(db.Integer, primary_key=True)
    Name            = db.Column(db.String(300), nullable=False, unique=True)
    Discription     = db.Column(db.Text, nullable=True)
    Cost            = db.Column(db.Integer, nullable=True)
    Damage          = db.Column(db.Text, nullable=True)
    Weight          = db.Column(db.Integer, nullable=True)
    Features        = db.relationship('Features'            , secondary=Weapoons_Features
                                            , backref=db.backref("WeapoonsFeatures", cascade='all,delete'   , single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    DamageType      = db.relationship('DamageTypes'         , secondary=Weapoons_DamageTypes
                                            , backref=db.backref("WeapoonsDamageTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)
    WeapoonType     = db.relationship('WeapoonTypes'        , secondary=Weapoons_WeapoonTypes
                                            , backref=db.backref("WeapoonsWeapoonTypes", cascade='all,delete', single_parent=True, passive_deletes=True)
                                            , cascade='all,delete', single_parent=True)


class WeapoonTypes(db.Model):
    __tablename__ = 'WeapoonTypes'
    id                  = db.Column(db.Integer, primary_key=True)
    Name                = db.Column(db.String(300), nullable=False, unique=True)
    Discription         = db.Column(db.Text, nullable=True)
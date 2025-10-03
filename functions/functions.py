from flask import (render_template)
from .Classes import *

def parametrsoutput(Resultrequest):
    ParamDate = Resultrequest
    if ParamDate == None:
        ParamMassiv = []
    else:
        ParamMassiv = ParamDate.split(sep=',')

    return ParamMassiv


def appenddatas(MassivDates):
    for MassivDate in MassivDates:
        Dates           = MassivDate[0]
        TabelsParametrs = MassivDate[1]
        ParametrTabls   = MassivDate[2]
        try:
            for Date in Dates:
                date = TabelsParametrs.query.filter_by(id=Date).first()
                ParametrTabls.append(date)
            return True
        except:
            return False


def ParamNameRepresentationValue(ParamName):
    representationList = RepresentationList()
    ResultArray = list(filter(lambda x: ParamName in x, representationList))
    if len(ResultArray) > 0:
        Result = ResultArray[0]
    else:
        Result = []
    return Result


def RepresentationList():
    RepresentationList = [['Discription','Описание']
                          , ['ArmorClass','Класс брони']
                          , ['Characteristic','Характеристики']
                          , ['DamageResistance','Сопротивление к типу урона']
                          , ['DamageImmunity','Иммунитет к типу урона']
                          , ['EffectsResistance','Сопротивление к эффектам']
                          , ['R_Class','Класс']
                          , ['Spell','Заклинания']
                          , ['Skill','Навыки']
                          , ['PossessionArmor','Владение доспехами']
                          , ['GunOwnership','Владение оружием']
                          , ['ToolOwnership','Владение языками']
                          , ['Language','Знание языков']
                          , ['Abilities','Способности']
                          , ['Hindrance','Помеха']
                          , ['Cost','Стоимость']
                          , ['Power','Сила']
                          , ['Weight','Вес']
                          , ['ArmorType','Тип доспеха']
                          , ['NotArmorSafe','Владение защитой без доспех']
                          , ['EquipmentType','тип снаряжения']
                          , ['TypicalRepresentative','Типичные представители']
                          , ['Writing','Письменность']
                          , ['PowerBonus','Бонус атаки']
                          , ['ArmorBonus','Бонус защиты']
                          , ['MagicalItemType','Тип магического предмета']
                          , ['Effects','Эффекты']
                          , ['WeapoonTypeItem','Оружие основа магического предмета']
                          , ['ArmorTypeItem','Доспех основа магического предмета']
                          , ['Speed','Скорость движения']
                          , ['Climb','Скорость лазания']
                          , ['Fly','Скорость полёта']
                          , ['Swim','Скорость плавания']
                          , ['Fight','Урон от атаки']
                          , ['Armor','Класс брони']
                          , ['Damage','Урон']
                          , ['ApplicationTime','Время накладывания']
                          , ['Distance','Дистанция']
                          , ['Components','Компоненты']
                          , ['Duration','Продолжительность действия']
                          , ['LevelSpell','Уровень заклинания']
                          , ['Archetype','Подклассы']
                          , ['Ritual','Ритуал']
                          , ['Class','Классы']
                          , ['Features','Свойства оружия']
                          , ['Name','']]

    return RepresentationList


def OpenVeiwPost(Parametrs):
    tableName           = Parametrs[0]
    Date_id             = Parametrs[1]
    ClassDate           = get_class(tableName)
    PostDate            = ClassDate.query.filter_by(id=Date_id).first()
    DateName            = getattr(PostDate, 'Name')
    PostDates           = [['', DateName, 'Name']]
    for variables in dir(PostDate):
        parametr = getattr(PostDate, variables)
        if not callable(parametr) and not variables.startswith("__"):
            if variables != 'id' and variables != 'Name':
                if not (isinstance(parametr, list) and len(parametr) == 0):
                    if isinstance(parametr, (int, str, list)):
                        RepresentationValueArray = ParamNameRepresentationValue(variables)
                        if len(RepresentationValueArray) > 1:
                            representationValue = RepresentationValueArray[1]
                        else:
                            representationValue = ''
                        PostDates.append([representationValue, parametr, variables])
    return render_template("VeiwPost.html", tableName=tableName, DateName=DateName, PostDates=PostDates)


def OpenEditPost(Parametrs):
    tableName           = Parametrs[0]
    Date_id             = Parametrs[1]
    OnlyvalueTablesName = Parametrs[2]
    ClassDate           = get_class(tableName)
    PostDate            = ClassDate.query.filter_by(id=Date_id).first()
    DateName            = getattr(PostDate, 'Name')
    PostDates           = [['', DateName, 'Name']]
    variablesClassDate  = []
    inputvalue          = ''
    TableOnly           = False
    for variables in dir(PostDate):
        parametr = getattr(PostDate, variables)
        if not callable(parametr) and not variables.startswith("__"):
            if variables != 'id' and variables != 'Name':
                if not (isinstance(parametr, list) and len(parametr) == 0):
                    if isinstance(parametr, list):
                        for param in parametr:
                            inputvalue = inputvalue+str(param.id)+','
                        if inputvalue != '':
                            inputvalue = inputvalue[:-1]
                        if variables in OnlyvalueTablesName:
                            TableOnly = True
                        variablesClassDate = type(parametr[0]).query.all()
                    if isinstance(parametr, (int, str, list)):
                        RepresentationValueArray = ParamNameRepresentationValue(variables)
                        if len(RepresentationValueArray) > 1:
                            representationValue = RepresentationValueArray[1]
                        else:
                            representationValue = ''
                        PostDates.append([representationValue, parametr, variables, variablesClassDate, inputvalue, TableOnly])
    return render_template("EditPost.html",Date_id=Date_id, tableName=tableName, DateName=DateName, PostDates=PostDates)


def UpdateTable(Parametrs):
    ClassDate = get_class(Parametrs['tableName'])
    PostDate = ClassDate.query.filter_by(id=Parametrs['Date_id']).first()
    try:
        for variables in dir(PostDate):
            parametr = getattr(PostDate, variables)
            if not callable(parametr) and (not variables.startswith("__") or variables.startswith("_sa_") ):
                if variables != 'id':
                    if not (isinstance(parametr, list) and len(parametr) == 0):
                        if isinstance(parametr, list):
                            classparam = type(parametr[0])
                            if parametr is not None:
                                parametr.clear()
                                for date_id in Parametrs[variables].split(sep=','):
                                    parametr.append(classparam.query.filter_by(id=date_id).first())
                        else:
                            if Parametrs.get(variables) is not None:
                                setattr(PostDate, variables, Parametrs[variables])
        return PostDate
    except:
        return False


def RemoveTable(Parametrs):
    ClassDate = get_class(Parametrs['tableName'])
    try:
        PostDate = ClassDate.query.filter_by(id=Parametrs['Date_id']).first()
        for variables in dir(PostDate):
            parametr = getattr(PostDate, variables)
            if not callable(parametr) and (not variables.startswith("__") or variables.startswith("_sa_")):
                if variables != 'id':
                    if not (isinstance(parametr, list) and len(parametr) == 0):
                        if isinstance(parametr, list):
                            if parametr is not None:
                                parametr.clear()
        ClassDate.query.filter_by(id=Parametrs['Date_id']).delete()
        return True
    except:
        return False


def get_class(className):
    return globals()[className]

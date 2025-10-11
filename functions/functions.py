from flask import render_template, request
from .Classes import *
import os

def parametrsoutput(Resultrequest):
    ParamDate = Resultrequest
    if ParamDate == None:
        ParamMassiv = []
    else:
        ParamMassiv = ParamDate.split(sep=',')
    if 'on' in ParamMassiv:
        ParamMassiv.remove('on')
    return ParamMassiv


def appenddatas(Parametrs):
    Dates = Parametrs[0]
    TabelsParametrs = Parametrs[1]
    ParametrTabls = Parametrs[2]
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
        , ['imageName', 'Картинка']
        , ['image', 'Картинка']
                          , ['Name','']]

    return RepresentationList


def OpenVeiwPost(Parametrs):
    AllFilesDelete()
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
                    if isinstance(parametr, (int, str, list, bytes)):
                        RepresentationValueArray = ParamNameRepresentationValue(variables)
                        if isinstance(parametr, bytes):
                            FileDonload([parametr, PostDate.imageName])
                        if len(RepresentationValueArray) > 1:
                            representationValue = RepresentationValueArray[1]
                        else:
                            representationValue = ''
                        PostDates.append([representationValue, parametr, variables])
    return render_template("VeiwPost.html", tableName=tableName, DateName=DateName, PostDates=PostDates)


def OpenEditPost(Parametrs):
    AllFilesDelete()
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
                    if isinstance(parametr, (int, str, list, bytes)):
                        RepresentationValueArray = ParamNameRepresentationValue(variables)
                        if isinstance(parametr, (bytes)):
                            FileDonload([parametr, PostDate.imageName])
                        if len(RepresentationValueArray) > 1:
                            representationValue = RepresentationValueArray[1]
                        else:
                            representationValue = ''
                        PostDates.append([representationValue, parametr, variables, variablesClassDate, inputvalue, TableOnly])
    return render_template("EditPost.html",DatesMassiv=[Date_id, tableName, DateName, PostDates])


def CreateDate(Parametrs):
    Object = Parametrs[0]
    requestDate = Parametrs[1]
    Dateslist = Parametrs[2]
    dates = requestDate.form
    filles = requestDate.files
    for variables in dir(Object):
        parametr = getattr(Object, variables)
        if not callable(parametr) and not variables.startswith("__"):
            if variables != 'id':
                if variables in dates:
                    setattr(Object, variables, dates[variables])
                else:
                    for Datelist in Dateslist:
                        if isinstance(Datelist, (list)):
                            if Datelist[1] == variables:
                                appenddatas([parametrsoutput(dates[Datelist[0]]), get_class(Datelist[0]), parametr])
    if len(filles) > 0:
        Object.image = filles['image_uploads'].read()
        Object.imageName = filles['image_uploads'].filename

    return Object


def FileDonload(Parametrs):
    fileBinaryDate = Parametrs[0]
    fileNames = Parametrs[1]
    if fileNames != '':
        fileName = 'static/image/' + fileNames
        with open(fileName, 'wb') as file:
            file.write(fileBinaryDate)


def FileDelete(Parametrs):
    fileName = 'static/image/' + Parametrs[0]
    os.remove(fileName)


def AllFilesDelete():
    folder = 'static/image'
    for filename in os.listdir(folder):
        print(filename)
        if filename != '':
            os.remove(folder + '/' + filename)


def UpdateTable(Parametrs):
    DateForm = Parametrs[0]
    FileDate = Parametrs[1]
    ClassDate = get_class(DateForm['tableName'])
    PostDate = ClassDate.query.filter_by(id=DateForm['Date_id']).first()
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
                                for date_id in DateForm[variables].split(sep=','):
                                    parametr.append(classparam.query.filter_by(id=date_id).first())
                        else:
                            if DateForm.get(variables) is not None:
                                setattr(PostDate, variables, DateForm[variables])
                    if variables == 'image':
                        PostDate.image = FileDate.read()
                        PostDate.imageName = FileDate.filename
        return PostDate
    except:
        return False


def RemoveTable(Parametrs):
    PaaramDelete = Parametrs[0]
    ClassDate = get_class(PaaramDelete['tableName'])
    try:
        PostDate = ClassDate.query.filter_by(id=PaaramDelete['Date_id']).first()
        for variables in dir(PostDate):
            parametr = getattr(PostDate, variables)
            if not callable(parametr) and (not variables.startswith("__") or variables.startswith("_sa_")):
                if variables != 'id':
                    if not (isinstance(parametr, list) and len(parametr) == 0):
                        if isinstance(parametr, list):
                            if parametr is not None:
                                parametr.clear()
        ClassDate.query.filter_by(id=PaaramDelete['Date_id']).delete()
        return True
    except:
        return False


def get_class(className):
    return globals()[className]

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


from datetime import datetime
from dateutil.relativedelta import relativedelta

def obEdad(birth_date):
    fecha_nac = datetime.strptime(birth_date, '%Y-%m-%d')
    edad = relativedelta(datetime.now(), fecha_nac)
    return edad
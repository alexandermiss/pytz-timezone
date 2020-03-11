from datetime import datetime
import pytz
import textwrap

zonahoraria_utc = pytz.timezone('UTC')
zonahoraria_cdmx = pytz.timezone('America/Mexico_City')
zonahoraria_bogota = pytz.timezone('America/Bogota')
zonahoraria_moscu = pytz.timezone('Europe/Moscow')

hora_actual = datetime.now()

hora_cdmx = zonahoraria_cdmx.localize(hora_actual)
hora_utc = hora_cdmx.astimezone(zonahoraria_utc)
hora_moscu = hora_cdmx.astimezone(zonahoraria_moscu)
hora_bogota = hora_cdmx.astimezone(zonahoraria_bogota)


log = textwrap.dedent(('\n'
                       '	Hora UTC:   		{0}\n'
                       '	Mexico:		        {1}\n'
                       '	Bogota:		        {2}\n'
                       '	Rusia:		        {3}\n')
                      .format(
    hora_utc, hora_cdmx, hora_bogota, hora_moscu)
)

print(log)

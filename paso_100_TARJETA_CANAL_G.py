''' este programa se encarga de generar las grabaciones de Canales '''
import os
import boto
import uuid
import subprocess
import time
import datetime
import shutil

from clsGrabacion import clsGrabacion
from clsGrabacion import clsParametros
from clsGrabacion import clsUtilidades

# formatos de fecha
format_date = "%Y%m%d"
format_time ="%H%M%S"
format_datetime =format_date + format_time
format_dateU = "%Y-%m-%d"
format_timeU ="%H:%M"
format_datetimeU =format_dateU + " " + format_timeU
NombrePrograma ='paso_grabacion_v2'


# variables de Canal y tarjeta
# son obtenidas del mismo nombre del archivo
# el archivo debe venir en el formato paso_100_TARJETA_Canal_Medio_G.py
NombreScript = os.path.basename(__file__)
detalles = NombreScript.split('_')
Canal=detalles[3]
NombreTarjeta='/dev/video' + detalles[2]
Medio = detalles[4]
DirectorioGrabacion="/home/sarv/SERVER_SARV_MONO/VideosBase"

print 'Este script procesara el Canal ' + Canal
print 'En la tarjeta ' + NombreTarjeta
print 'El Directorio de Grabacion sera ' + DirectorioGrabacion

#establezcamos la tarjeta al Canal
cmd = 'v4l2-ctl -i0 -d ' + NombreTarjeta
os.system(cmd)
cmd = 'ivtv-tune -c' + Canal + ' -d ' + NombreTarjeta
os.system(cmd)



hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute

    
#grabamos
Duracion=3590
NombreArchivo = Medio + "_" + datetime.datetime.now().strftime(format_datetime) + ".mpg"
NombreArchivo = os.path.join(DirectorioGrabacion,NombreArchivo)

print 'Si hay proceso de grabacion activo en vlc , lo eliminaremos para evitar posibles conflicos'
util = clsUtilidades()
cadena = "v4l2:///dev/video" + str(detalles[2])
util.killProcess(cadena)

time.sleep(3)

print 'Grabaremos el archivo ' + NombreArchivo + ' por una duracion de ' + str(Duracion)
HoraGrabacion = datetime.datetime.now().strftime(format_datetimeU)
HoraI = datetime.datetime.now()

cmd = 'cvlc pvr://{0} :norm=ntsc :size=720x480 :bitrate=3000000 :maxbitrate=4000000 :run-time={1} --cr-average 1000 --sout=file/ps://{2} vlc://quit'.format(NombreTarjeta,Duracion,NombreArchivo)

cmd = 'cvlc \'v4l2c://{0}:audio-method=0:controls-reset:set-ctrls={{video_bitrate_mode=1,video_bitrate=4000000,video_peak_bitrate=4000000}}:width=720:height=480\' --run-time={1}  --sout=file/ps://{2} vlc://quit'.format(NombreTarjeta,Duracion,NombreArchivo)

print cmd
subprocess.call(cmd, shell=True)
print 'Grabacion finalizada'
tDiff= datetime.datetime.now() - HoraI


# este script inicia un proceso , si y solo si , esta apagado
# ideal para colocar los pasos en el cron
# y que el cron lo ejecute, asi, si no ha terminado la instancia anterior, pues no la ejecuta
# el cron debe mandar el parametro

import os
import boto
import uuid
import subprocess
import time
import datetime
import shutil
import zipfile
import sys
import psutil


from clsGrabacion import clsGrabacion
from clsGrabacion import clsParametros
from clsGrabacion import clsUtilidades

num_paso=0
if len(sys.argv)<2:
    num_paso = raw_input('Que paso desea reset ?  ')
else:
    num_paso = sys.argv[1]
#print 'Procedemos a apagar el paso ' + str(num_paso) + ' independientemente de su estado'

util = clsUtilidades()
nombrePaso = 'paso-' + str(num_paso)
isON = util.is_process_running(nombrePaso)
if isON==True:
    print 'El proceso esta trabajando, lo vamos a parar'
    util.killProcess(nombrePaso)
else:
    print 'El Proceso ' + str(num_paso) + ' no esta trabajando , no hay nada que hacer'
    
    
print 'Finalizado'    

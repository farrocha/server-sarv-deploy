import datetime
import time
import os
import urllib
import urllib2
import subprocess, signal
from subprocess import Popen, PIPE


def killProcess(paso):
        print 'Intentando para el proceso ' + paso
        x=0
        process = Popen(['ps', '-eo' ,'pid,args'], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
            pid, cmdline = line.strip().split(' ', 1)
            if paso in cmdline:
                #detalle = cmdline.split(' ')
                print 'Proceso ' + cmdline + ' encontrado, procedemos a eliminarlo.'
                os.kill(int(pid), signal.SIGKILL)
                x= x+1
        if x==0:
            print 'No encontre procesos con ese nombre corriendo actualmente'
        return x

var = raw_input('Que proceso desea parar ?  ')
killProcess(var)
    
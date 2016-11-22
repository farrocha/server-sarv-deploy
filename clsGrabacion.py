# el formato de los archivos de vlc es 100_20140117180000
import datetime
import time
import os
import urllib
import urllib2
import subprocess, signal
from subprocess import Popen, PIPE




class clsGrabacion:
    IDPais=0
    canal=0
    anio=0
    mes=0
    dia=0
    hora=0
    minuto=0
    IDRegistro=0

        
    def get_ObjectFromFileName(self,FileName, _IDPais):
        try:
            self.IDPais=_IDPais
            separados =FileName.split('_')
            self.canal = int(separados[0])
            self.anio = int(separados[1][0:4])
            self.mes = int(separados[1][4:6])
            self.dia = int(separados[1][6:8])
            self.hora = int(separados[1][8:10])
            self.minuto = int(separados[1][10:12])
            self.FechaHora = datetime.datetime(year=self.anio,day=self.dia, month= self.mes, hour=self.hora, minute = self.minuto)
            day_of_year = self.FechaHora.timetuple().tm_yday
            self.IDRegistro = int(str(self.IDPais) + str(str(self.anio-2000).zfill(2)) + str(str(day_of_year).zfill(3)) + str(self.hora).zfill(2) + str(self.minuto).zfill(2) + str(self.canal).zfill(3))
        except:
            self.IDRegistro=0
                
        
    def get_ObjectFromIDRegistro(self,_IDRegistro):
        self.IDRegistro = _IDRegistro
        self.IDPais = int(str(_IDRegistro)[0:3])
        self.anio = int(str(_IDRegistro)[3:5]) + 2000
        day_of_year = int(str(_IDRegistro)[5:8])
        self.hora = int(str(_IDRegistro)[8:10])
        self.minuto = int(str(_IDRegistro)[10:12])
        self.canal = int(str(_IDRegistro)[12:15])
        self.FechaHora = datetime.datetime(year=self.anio,day=1,month=1) + datetime.timedelta(days=(day_of_year-1))
        
        self.FechaHora = self.FechaHora + datetime.timedelta(hours=self.hora, minutes=self.minuto)
        
        self.dia = self.FechaHora.day
        self.mes = self.FechaHora.month
        #print str(self.dia) + "/" + str(self.mes) 
        #print "minuto: " + str(self.minuto)
        #print "hora: " + str(self.hora)
        print self.FechaHora
        
        
        
class clsParametros:
        
        dirVideos =""
        dirTrabajo=""
        IDPais=0;
        IDComputadora=""
        dirUpload =""
        dirBackUp =""
        dirFinalizados=""
        dirYaCargados=""
        LLaveS3=""
        ClaveS3=""
            
                    
        def get_ObjectFromFile(self,FileName):
            f=open(FileName)
            parametros = f.readlines()
            self.dirVideos=parametros[0].strip()
            self.dirTrabajo=parametros[1].strip()
            self.IDPais=int(parametros[3].strip())
            self.IDComputadora=int(parametros[6].strip())
            self.FechaInicio = datetime.datetime.strptime(parametros[4].strip(),  '%Y/%m/%d %H:%M')
            self.dirBackUp = parametros[2].strip()
            self.LLaveS3 = parametros[7].strip()
            self.ClaveS3 = parametros[8].strip()
            self.dirUpload = os.path.join(self.dirBackUp,"UploadData")
            self.dirFinalizados = os.path.join(self.dirBackUp,"Finalizados")
            self.dirYaCargados = os.path.join(self.dirBackUp,"YaCargados")
            
            if not os.path.exists(self.dirVideos):
                os.makedirs(self.dirVideos)
            if not os.path.exists(self.dirBackUp):
                os.makedirs(self.dirBackUp)
            if not os.path.exists(self.dirFinalizados):
                os.makedirs(self.dirFinalizados)
            if not os.path.exists(self.dirTrabajo):
                os.makedirs(self.dirTrabajo)
            if not os.path.exists(self.dirUpload):
                os.makedirs(self.dirUpload)            
            if not os.path.exists(self.dirYaCargados):
                os.makedirs(self.dirYaCargados)            
            
            
class clsUtilidades:
    
    def ReportStatus(self,Mensaje, IDComputadora,NombrePrograma,IDPais,IDCanal,Metodo,Tiempo,FechaHoraArchivo,Codigo,IDRegistro):
        resp=''
        #print 'recibiendo comandos...'
        url = 'http://health.publisearch.info/UpdateStatus/ReportToLog?Mensaje={0}&IDComputadora={1}&NombrePrograma={2}&IDPais={3}&IDCanal={4}&Metodo={5}&Tiempo={6}&FechaHoraArchivo={7}&Codigo={8}&IDRegistro={9}'.format( Mensaje, IDComputadora, NombrePrograma, IDPais, IDCanal,
                                               Metodo, Tiempo, FechaHoraArchivo, Codigo, IDRegistro)
        #print url
        try:
            wc = urllib.urlopen(url)
            lineas = wc.readlines()
            for row in lineas:
                resp = resp + row
            wc.close()
        except:
            print 'no pudimos conectarnos con el web server'
            resp='False'    
        return resp
    
    def ReportEndLocal(self,Codigo,IDRegistro,dirFinalizado):
        #este archivo se encarga de escribir localmente, en la carpeta /home/sarv/Documents/Videos/Finalizados/
        #que el paso para este archivo esta finalizado
        # los codigos de finalizados sera Extraer Imagenes : 205, HuellasP : 215, HuellasC : 225, Cortes : 235
        ArchivoFinal = os.path.join(dirFinalizado,str(IDRegistro) + "_" + str(Codigo) + ".txt")
        if os.path.exists(ArchivoFinal)==False:
            with open(ArchivoFinal,'w+') as f:
                f.write(str(datetime.datetime.now()))
        return ArchivoFinal    
    def isProcessDone(self,Codigo,IDRegistro,dirFinalizado):
        #este archivo se encarga de escribir localmente, en la carpeta /home/sarv/Documents/Videos/Finalizados/
        #que el paso para este archivo esta finalizado
        # los codigos de finalizados sera Extraer Imagenes : 190, HuellasP : 215, HuellasC : 225, Cortes : 235
        ArchivoFinal = os.path.join(dirFinalizado,str(IDRegistro) + "_" + str(Codigo) + ".txt")
        resp= os.path.exists(ArchivoFinal)
        return resp 
    
    def wget(self,url, dirDestino):
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(os.path.join(dirDestino,file_name), 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        os.system('clear')
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
    
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,
    
        f.close()   
        
    def killProcess(self,paso):
        print 'Intentando para el proceso ' + paso
        x=0;
        process = Popen(['ps', '-eo' ,'pid,args'], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
            pid, cmdline = line.strip().split(' ', 1)
            #print pid + "-->" + cmdline
            if paso in cmdline:
                #detalle = cmdline.split(' ')
                print 'Proceso ' + cmdline + ' encontrado, procedemos a eliminarlo.'
                os.kill(int(pid), signal.SIGKILL)
                x= x+1
        if x==0:
            print 'No encontre procesos con ese nombre corriendo actualmente'
        return x
     
    def ListaProcess(self):
        paso='paso_'
        process = Popen(['ps', '-eo' ,'pid,args'], stdout=PIPE, stderr=PIPE)
        stdout, notused = process.communicate()
        for line in stdout.splitlines():
            pid, cmdline = line.strip().split(' ', 1)
            if paso in cmdline:
                print 'Proceso ' + cmdline + ' encontrado.'
                
    def print_ListProcessByString(self, filtro):
       process = Popen(['ps', '-eo' ,'pid,args'], stdout=PIPE, stderr=PIPE)
       stdout, notused = process.communicate()
       for line in stdout.splitlines():
           pid, cmdline = line.strip().split(' ', 1)
           if filtro in cmdline:
               print 'Proceso ' + cmdline + ' encontrado:' + str(pid)   
   
        
        
        
        


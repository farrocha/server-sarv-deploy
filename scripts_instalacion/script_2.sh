echo "Inicio de instalacion de librerias..."
sudo apt-get update

sudo apt-get --yes install mono-complete
sudo apt-get --yes install build-essential libavformat-dev libmpg123-dev libsamplerate-dev libsndfile-dev cimg-dev libavcodec-dev  libswscale-dev
sudo apt-get --yes install libpng-dev libjpeg-dev libopencv-dev git unzip libargtable2-dev libmagickwand-dev imagemagick vlc python-dev python-pip 
sudo apt-get --yes install patchutils libproc-processtable-perl
sudo apt-get --yes install v4l-utils
sudo apt-get --yes install ivtv-utils
sudo apt-get --yes install mplayer
sudo apt-get --yes install filezilla
sudo apt-get --yes install vsftpd
sudo apt-get --yes install libx264-dev
sudo apt-get --yes install libmp3lame-dev
sudo apt-get --yes install libxcb-xfixes0-dev
sudo apt-get --yes  install ffmpeg

sudo apt-get update

sudo apt-get --yes install apache2
sudo apt-get --yes install php7.0-mysql php7.0-curl php7.0-json php7.0-cgi  php7.0 
sudo apt-get --yes install libapache2-mod-php





echo "******************"
echo "******************"
echo "INSTALANDO PIPS..."
echo ""

pip install boto
pip install psutil
pip install python-openstackclient
pip install python-swiftclient
pip install django
pip install --upgrade watson-developer-cloud


echo "PROGRAMAS PARA RADIO"
sudo apt-get --yes install python-matplotlib

sudo apt-get --yes install python-pip 
sudo apt-get --yes install python-dev 
sudo apt-get --yes install libmysqlclient-dev
pip install PyAudio
pip install pydub
sudo apt-get install python-pip python-dev libmysqlclient-dev
pip install mysql-python
pip install scipy
pip install numpy
sudo apt-get install python-pyaudio

echo "Creando usuarios en MYSQL Local"
mysql -uroot -ppublisearch Create


echo "Fin de instalacion de librerias"

echo "AHORA usted DEBE EDITAR EL ARCHIVO DE vsftpd : /etc/vsftpd.conf "




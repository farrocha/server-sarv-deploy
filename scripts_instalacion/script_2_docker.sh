echo "Inicio de instalacion de librerias..."
apt-get update


apt-get --yes install build-essential libavformat-dev libmpg123-dev libsamplerate-dev libsndfile-dev cimg-dev libavcodec-dev  libswscale-dev
apt-get --yes install libpng-dev libjpeg-dev libopencv-dev git unzip libargtable2-dev libmagickwand-dev imagemagick vlc python-dev python-pip 
apt-get --yes install patchutils libproc-processtable-perl
apt-get --yes install vsftpd
apt-get --yes install libx264-dev
apt-get --yes install libmp3lame-dev
apt-get --yes install libxcb-xfixes0-dev
apt-get --yes install ffmpeg
apt-get --yes install software-properties-common

apt-get update




echo "******************"
echo "******************"
echo "INSTALANDO PIPS..."
echo ""

pip install boto
pip install psutil
echo "PROGRAMAS PARA RADIO"
apt-get --yes install python-matplotlib

apt-get --yes install python-pip 
apt-get --yes install python-dev 
apt-get --yes install libmysqlclient-dev
pip install PyAudio
pip install pydub
apt-get install python-pip python-dev libmysqlclient-dev
pip install mysql-python
pip install scipy
pip install numpy
apt-get install python-pyaudio

echo "Creando usuarios en MYSQL Local"
mysql -uroot -ppublisearch Create

wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
add-apt-repository universe
apt-get install apt-transport-https
apt-get update
apt-get --yes install dotnet-sdk-2.2

echo "Fin de instalacion de librerias"

echo "AHORA usted DEBE EDITAR EL ARCHIVO DE vsftpd : /etc/vsftpd.conf "




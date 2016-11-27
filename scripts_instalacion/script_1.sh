echo "Inicio de instalacion de librerias..."
sudo apt-get update

sudo apt-get --yes install mono-complete
sudo apt-get --yes install build-essential libavformat-dev libmpg123-dev libsamplerate-dev libsndfile-dev cimg-dev libavcodec-dev  libswscale-dev
sudo apt-get --yes libpng-dev libjpeg-dev libopencv-dev git unzip libargtable2-dev libmagickwand-dev imagemagick vlc python-dev python-pip 
sudo pip install boto
sudo pip install psutil
sudo apt-get --yes install patchutils libproc-processtable-perl build-essential
sudo apt-get --yes install v4l-utils
sudo apt-get --yes install ivtv-utils
sudo apt-get --yes install mplayer
sudo apt-get --yes install filezilla
sudo apt-get --yes install vsftpd
sudo apt-get --yes install libx264-dev
sudo apt-get --yes install libmp3lame-dev
sudo apt-get --yes install libxcb-xfixes0-dev
sudo apt-get --yes  install ffmpeg
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get --yes install oracle-java8-installer
wget https://s3.amazonaws.com/sarv/openrc.sh
source openrc.sh
sudo pip install python-openstackclient
sudo pip install python-swiftclient


echo "******************"
echo "******************"
echo "PROBANDO CONEXIONES..."
echo ""
swift list
echo ""
echo ""
echo "******************"
echo "******************"

echo "Fin de instalacion de librerias"

echo "AHORA usted DEBE EDITAR EL ARCHIVO DE vsftpd : /etc/vsftpd.conf "




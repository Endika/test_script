#!bin/bash
RASPI_USER=pi
RASPI_IP=raspberrypi
RASPI_SSH=22
UBUNTU_USER=ubuntu
UBUNTU_IP=192.168.1.37
UBUNTU_MAC=00:00:00:00:00:00
UBUNTU_SSH=22
UBUNTU_VINAGRE=5900
UBUNTU_SSH_VIRTUAL=2222

ssh $RASPI_USER@$RASPI_IP:$RASPI_SSH
wakeonlan $UBUNTU_MAC
simpleproxy -L $UBUNTU_SSH_VIRTUAL -R $UBUNTU_IP:$UBUNTU_SSH &
simpleproxy -L $UBUNTU_VIANGRE -R $UBUNTU_IP:$UBUNTU_VINAGRE &
sleep 60
ssh -Y $UBUNTU_USER@$UBUNTU_IP
vino-prefences
sudo -s
export DISPLAY=:0.0
xhost +
/usr/lib/vino/vino-server &
exit #exit root
exit #exit ubuntu
exit #exit raspi
ssh -L $UBUNTU_VIANGRE:localhost:$UBUNTU_VINAGRE $UBUNTU_USER@$UBUNTU_IP

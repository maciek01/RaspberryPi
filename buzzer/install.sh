
sudo apt-get install python-pip
sudo pip install httplib2
sudo pip install pyserial
sudo ln -s /home/pi/examples/buzzer/alarmd.sh /etc/init.d/pyalarmd

sudo update-rc.d pyalarmd defaults

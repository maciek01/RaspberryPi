#!/bin/bash
# /etc/init.d/pyalarmd

### BEGIN INIT INFO
# Provides:          alarm
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Example initscript
# Description:       This service is used to buzz at specified hour
### END INIT INFO


case "$1" in 
    start)
        echo "Starting pyalarmd"
        sudo -u pi /home/pi/examples/buzzer/run.sh
        ;;
    stop)
        echo "Stopping pyalarmd"
        #sudo -u pi killall /usr/bin/python
        ;;
    *)
        echo "Usage: /etc/init.d/pyalarmd start|stop"
        exit 1
        ;;
esac

exit 0


#!/bin/bash

start()
{
    echo 'start...'
    cd djapps && nohup python djapps/wsgi.py &
    cd tflask && nohup python app.py &
    cd ttornado && nohup python app.py &
}

stop()
{
    echo 'stop...'
    fuser -k -n tcp 8099
    fuser -k -n tcp 5000
    fuser -k -n tcp 6001
}

restart()
{
    stop
    start
}


[ -z $1 ] || {
    $@
}

[ $# -eq 0 ] && {
    echo "Usage: $0 <start|stop|restart>"
    exit 1
}

exit 0

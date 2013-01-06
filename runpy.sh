#!/bin/bash

start()
{
    echo 'start...'
    cd djapps && nohup python djapps/wsgi.py &
    cd tflask && nohup python app.py &
}

stop()
{
    echo 'stop...'
    fuser -k -n tcp 8099
    fuser -k -n tcp 5000
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

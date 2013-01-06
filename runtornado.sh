#!/bin/bash

start()
{
    echo 'start...'
    cd djapps && gunicorn -k tornado -w 8 --worker-connections 1500 -b 0.0.0.0:8097 -D djapps.wsgi

    cd ..
    cd tflask && gunicorn -k tornado -w 8 --worker-connections 1500 -b 0.0.0.0:5002 -D app:app
}

stop()
{
    echo 'stop...'
    fuser -k -n tcp 8097
    fuser -k -n tcp 5002
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

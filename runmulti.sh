#!/bin/bash

start()
{
    echo 'start...'
    echo 'start django + gunicorn + gevent 8 worker'
    cd djapps && gunicorn -k gevent -w 8 --worker-connections 1500 -b 0.0.0.0:8021 -D djapps.wsgi

    cd ..
    echo 'start tflask + gunicorn + gevent 8 worker'
    cd tflask && gunicorn -k gevent -w 8 --worker-connections 1500 -b 0.0.0.0:8031 -D app:app
    echo 'start ok'
}

stop()
{
    echo 'stop...'
    fuser -k -n tcp 8021
    fuser -k -n tcp 8031
    echo 'stop ok'
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

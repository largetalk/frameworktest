#!/bin/bash

start()
{
    echo 'start...'
    echo 'start django + gunicorn at pypy 8 worker'
    cd djapps && gunicorn -w 8 --worker-connections 1500 -b 0.0.0.0:8042 -D djapps.pypy_wsgi
    echo 'start ok'
}

stop()
{
    echo 'stop...'
    fuser -k -n tcp 8042
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

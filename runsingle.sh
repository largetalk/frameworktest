#!/bin/bash

start()
{
    echo 'start...'
    echo 'start django + gevent'
    cd djapps && nohup python djapps/wsgi.py --port 8020 &
    echo 'start flask + gevent'
    cd tflask && nohup python app.py --port 8030 &
    echo 'start tornado'
    cd ttornado && nohup python app.py --port 8040 &
    echo 'start ok'
}

stop()
{
    echo 'stop...'
    fuser -k -n tcp 8020
    fuser -k -n tcp 8030
    fuser -k -n tcp 8040
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

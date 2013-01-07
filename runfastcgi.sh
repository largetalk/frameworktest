#!/bin/bash

start()
{
    echo 'django + nginx +fastcgi'
    echo 'start...'
    cd djapps && nohup python djapps/wsgi.py &

    rundir=$PWD/djapps
    cd $rundir && python manage.py runfcgi protocol=fcgi method=prefork \
        socket=$rundir/app.sock maxrequests=9999 maxspare=20 maxchildren=500 \
        daemonize=false pidfile=$rundir/app.pid outlog=$rundir/app_out.log \
        errlog=$rundir/app_err.log & >/dev/null 2>&1

    sleep 3
    chmod 666 $rundir/app.sock
    #chgrp www-data $rundir/app.sock
    echo 'start ok'
}

stop()
{
    echo 'stop...'
    pidfile="$PWD/djapps/app.pid"
    if [ -f "$pidfile" ]; then
        cat $pidfile | xargs kill -9 
        rm $pidfile
    fi
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

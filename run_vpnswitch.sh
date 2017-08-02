#!/bin/sh
cd $( cd "$(dirname "$0")" ; pwd -P )
export GUNICORN_BIND=${GUNICORN_BIND:-0.0.0.0:9911}
gunicorn --config gunicorn.conf --log-config logging.conf vpnswitch:vpnswitch &

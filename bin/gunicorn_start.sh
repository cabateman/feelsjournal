#!/bin/bash

NAME="feelsjournal"                                  # Name of the application
DIR=/root/feelsjournal             # project directory
#SOCKFILE=/home/ec2-user/metricboard-server/run/gunicorn.sock  # we will communicte using this unix socket
USER=root                                        # the user to run as
GROUP=root                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
#FLASK_SETTINGS_MODULE=hello.settings             # which settings file should Django use
WSGI_MODULE=server                     # WSGI module name
TIMEOUT=200                            # Timeout is set to 10 minutes

echo "Starting $NAME as `whoami`"

echo "getting latest code"
cd $DIR
git pull origin master

# Activate the virtual environment
#cd $DIR
source /root/.virtualenvs/feelsjournal/bin/activate
export PYTHONPATH=$DIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /root/.virtualenvs/feelsjournal/bin/gunicorn ${WSGI_MODULE}:app \
  --name $NAME \
  --workers $NUM_WORKERS \
  --timeout $TIMEOUT \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=info \
  --log-file=-

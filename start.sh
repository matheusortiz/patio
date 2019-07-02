#!/bin/bash
# Diretorio e arquivo de log
set -e
LOGFILE=/home/ortiz/www/patio/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
# Numero de processo simultaneo, modifique de acordo com seu processador
NUM_WORKERS=2
# Usuario/Grupo que vai rodar o gunicorn
USER=ortiz
#GROUP=root
# Endereço local que o gunicorn irá rodar
ADDRESS=127.0.0.1:8000
# Ativando ambiente virtual e executando o gunicorn para este projeto
source /home/ortiz/env/patio/bin/activate
cd /home/ortiz/www/patio/patio/
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS --bind=$ADDRESS --user=$USER --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE patio.wsgi:application

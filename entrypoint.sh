#!/bin/bash
# this script is used to boot the Docker container

mkdir -p logs
touch /logs/error.log
touch /logs/info.log
chmod -R 777 logs

exec gunicorn wolproxypyapi.main:app \
    --bind=0.0.0.0:8000 \
    --workers=2 \
    --worker-class=uvicorn.workers.UvicornWorker \
    --log-level=info \
    --error-logfile=/logs/error.log \
    --access-logfile=/logs/info.log

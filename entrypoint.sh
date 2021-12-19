#!/bin/bash
# this script is used to boot the Docker container

touch /logs/error.log
touch /logs/info.log

exec gunicorn wolproxypyapi.main:app \
    --bind=0.0.0.0:80 \
    --workers=2 \
    --worker-class=uvicorn.workers.UvicornWorker \
    --log-level=info \
    --error-logfile=/logs/error.log \
    --access-logfile=/logs/info.log

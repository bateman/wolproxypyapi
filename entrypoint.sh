#!/bin/bash
# this script is used to boot the Docker container

touch /logs/server.log
touch /logs/app.log

exec gunicorn wolproxypyapi.main:app \
    --bind=0.0.0.0:8000 \
    --workers=2 \
    --worker-class=uvicorn.workers.UvicornWorker \
    --log-level=info \
    --log-file=/logs/server.log \
    --access-logfile=/logs/app.log

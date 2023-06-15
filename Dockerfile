# Base image
FROM python:3.11.4-slim-bullseye

# Label docker image
LABEL maintainer="Fabio Calefato <fabio.calefato@uniba.it>"
LABEL org.label-schema.license="MIT"

# Install dependencies
COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get dist-upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip setuptools wheel build
RUN pip install -r requirements.txt

# Copy app files
COPY wolproxypyapi wolproxypyapi
COPY config config
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# Export ports
EXPOSE 8000

# Run start script
ENTRYPOINT ["./entrypoint.sh"]

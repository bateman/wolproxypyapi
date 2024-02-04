# Base image
FROM python:3.12-slim-bookworm

# Label docker image
LABEL maintainer="Fabio Calefato <fabio.calefato@uniba.it>"
LABEL org.label-schema.license="MIT"

# Install dependencies
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY wolproxypyapi wolproxypyapi
COPY config config
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# Export ports
EXPOSE 8000

# Run start script
ENTRYPOINT ["./entrypoint.sh"]

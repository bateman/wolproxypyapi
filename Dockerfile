# Base image
FROM python:3.9-slim

# Label docker image
LABEL maintainer="Fabio Calefato <fabio.calefato@uniba.it>"
LABEL org.label-schema.license="MIT"

# Install dependencies
COPY Makefile Makefile
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN python -m pip install --upgrade pip
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && make production \
    && apt-get purge -y --auto-remove gcc build-essential

# Copy
COPY wolproxypyapi wolproxypyapi
COPY config config

RUN mkdir -p logs \
    && chmod -R 777 logs

# Export ports
EXPOSE 80

# Start app, overrides config/uvicorn.config
CMD ["uvicorn", "wolproxypyapi.main:app", "--host", "0.0.0.0", "--port", "80"]
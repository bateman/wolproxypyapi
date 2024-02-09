# wolproxypyapi
[![CI_CD](https://github.com/bateman/wolproxypyapi/actions/workflows/CI_CD.yml/badge.svg)](https://github.com/bateman/wolproxypyapi/actions/workflows/CI_CD.yml)
[![Documentation Status](https://readthedocs.org/projects/wolproxypyapi/badge/?version=latest)](https://wolproxypyapi.readthedocs.io/en/latest/?badge=latest)
![Docker Pulls](https://img.shields.io/docker/pulls/bateman/wolproxypyapi)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/bateman/wolproxypyapi)
![GitHub](https://img.shields.io/github/license/bateman/wolproxypyapi)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/bateman/wolproxypyapi)
[![Known Vulnerabilities](https://snyk.io/test/github/bateman/wolproxypyapi/badge.svg)](https://snyk.io/test/github/bateman/wolproxypyapi)

A FastAPI RESTful web service for routing Wake-On-LAN packets via Internet.

This is a simple package for sending Wake-On-LAN packets to other hosts in a local network.
However, wolproxypyapi also offers a fully-dockerized web app (built on Flask) and an API (built on FastAPI) that act as proxy for routing magic WOL packets via the Internet.

## Installation

1. `git clone https://github.com/bateman/wolproxypyapi` - Clone the project from GitHub.
2. `make install` - Install all dependencies via [poetry](https://python-poetry.org/).
3. `make docs` - Build the documentation site via [mkdocs](https://www.mkdocs.org/).

## Usage

To launch the web application, run `poetry run wolproxypyapi` and connect to <http://127.0.0.0:8000>. You can change the port by editing the file `config/api.config`.

### Docker

Assuming that you have Docker installed on your system and that you have cloned the GitHub repository locally as per the [Installation](#installation) step 1 above, to build and execute the image locally, run
`docker-compose up -d --build`.

The app will be available at <http://127.0.0.0:8000>. To change the port, edit the file `docker-compose.yml` accordingly and rebuild the image.

You can stop it by executing `docker-compose stop`.

Alternatively, if you don't want to clone the repository, just download the latest image from [DockerHub](https://hub.docker.com/r/bateman/wolproxypyapi), run:

```bash
docker pull bateman/wolproxypyapi:latest
docker start bateman/wolproxypyapi
```

The app will be again accessible at <http://127.0.0.0:8000>.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

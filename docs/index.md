# wolproxypyapi

This is a simple package for sending Wake-On-LAN packets to other host in a local network. This started as a pet-project to put together and test a series of technologies I'm interested in.
The all WOL packet sending is managed by the Python package [wakeonlan](https://pypi.org/project/wakeonlan/), for which wolproxypy act as a wrapper.

However, wolproxypy also offers a fully-dockerized web app (built on Flask) and an API (built on FastAPI) that act as proxy for routing magic WOL packets via the Internet.

## Installation

1. `git clone https://github.com/bateman/wolproxypyapi` - Clone the project from GitHub.
2. `make install` - Install all dependencies via [poetry](https://python-poetry.org/).
3. `make docs` - Build the documentation site via [mkdocs](https://www.mkdocs.org/).

## Usage

To launch the web application, run `poetry run wolproxypyapi` and connect to <http://127.0.0.0:8000>. You can change the port by editing the file `config/api.config`.

### Docker

Assuming that you have Docker installed on your system and that you have cloned the GitHub repository locally as per the [Installation](#installation) step 1 above, to build and executed the image locally, run:

`docker-compose up -d --build`

The app will be available at <http://127.0.0.0:8000>. To change the port, edit the file `docker-compose.yml` accordingly and rebuild the image.

You can stop it by executing `docker-compose stop`.

Alternatively, if you don't want to clone the repository, just download the latest image from [DockerHub](https://hub.docker.com/r/bateman/wolproxypy), run:

`docker pull bateman/wolproxypyapi:latest`

`docker start bateman/wolproxypyapi`

The app will be again accessible at <http://127.0.0.0:8000>.

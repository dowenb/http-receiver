# http-receiver/API

## Active python virtual environment

Instructions depend on platform:

bash/zsh: `source virtual-environment/bin/activate`

See: <https://docs.python.org/3/library/venv.html>

## Install requirements

`pip install -r requirements.txt`

Note: Depending on your installation of python this may be pip3

## Starting the API

`uvicorn main:app --reload`

## API Docs

<http://localhost:8000/docs>

## Docker

### Build docker

`docker build -t http-receiver .`

### Run docker

docker run -d --name http-receiver -p 80:80 http-receiver

## Docker stop

`docker stop http-receiver`

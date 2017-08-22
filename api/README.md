# Fantasy Football ML Api

This repo contains the source code for our FF ML Api as well as the dockerfile for running a container to serve our flask application.

### Prerequisites

* Python 2.7
* Docker
* Kitematic (optional)

## Local Dev

Run ```python app.py``` to serve the api
Navigate to localhost:5000

## Using Docker

Run ```docker build -t nflapi .``` to build the docker image

Run ```docker run -d -p 5000:5000 nflapi``` to run the docker container

The docker run command sets up port forwarding for port 5000, so you can still use the api via localhost:5000

## Helpful Hints

If you have issues building the image after making changes to the app, occasionally run ```docker rmi $(docker images -q -f dangling=true)``` to get rid of dangling containers

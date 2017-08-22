# Fantasy Football ML

This repo contains the source code for our FF ML project

### Prerequisites

* Python 2.7
* Postgres Client (e.g. DBeaver)
* Docker
* Kitematic (optional)

## Using Docker

Run ```docker-compose up``` to start up the api and db docker containers

The docker-compose settings exposes postgres at port 5432 - use this to set up a connection from your Postgres client

## Helpful Hints

Run ```docker-compose down``` to stop and remove all containers created by ```docker-compose up```

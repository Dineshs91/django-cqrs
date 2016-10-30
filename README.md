# django-cqrs

A demo application to show how cqrs can be implemented in Django

## Bring up the services.

cd into the project root. (After cloning this repo)

Bring up the services up.

`docker-compose up -d --build`

Shutdown the containers.

`docker-compose down`

**NOTE:**
For docker commands refer [this](https://github.com/Dineshs91/init/blob/master/docker/README.md)

## Test events replay

`docker exec -it 9a599402487f blog/demo/replay_three.sh`

`docker exec -it 9a599402487f blog/demo/replay_all.sh`

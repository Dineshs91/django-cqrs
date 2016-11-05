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

`docker exec -it cqrs_web_1 blog/demo/replay_three.sh`

`docker exec -it cqrs_web_1 blog/demo/replay_all.sh`

## Architecture

Currently there is only one event `PostCreatedEvent`.

I tried to replicate the concepts from this [video](https://www.youtube.com/watch?v=A0goyZ9F4bg&t=2160s)
I did not implement the `command` part. 

If anybody wants to help out or interested about this, please open a PR or start a discussion in the issues section.

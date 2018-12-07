# django-cqrs

A demo application to show how cqrs can be implemented in Django

## Bring up the services.

cd into the project root. (After cloning this repo)

Bring up the services up.

`docker-compose up -d --build`

Visit `http://localhost:8000/posts/`

Shutdown the containers.

`docker-compose down`

**NOTE:**
For docker commands refer [this](https://github.com/Dineshs91/init/blob/master/docker/README.md)

## Test events replay

`docker exec -it cqrs_web_1 blog/demo/replay_three.sh`

`docker exec -it cqrs_web_1 blog/demo/replay_all.sh`

## Architecture

Currently there are only two events `PostCreatedEvent` and `PostUpdatedEvent`.

I tried to replicate the concepts from this [video](https://www.youtube.com/watch?v=A0goyZ9F4bg&t=2160s)
I did not implement the `command` part. 

There are 2 types of data, 
1. event data
2. entity data 

Event data captures every change to the system, whereas entity data has only the recent state.

Any state change to the application is captured through an event
`(PostCreatedEvent, PostUpdatedEvent)`. For storing event data I've used MongoDB and for storing entity data PostgresDB.

Creation of event data is handled in django forms. Forms `save` method is overloaded with the [code](https://github.com/Dineshs91/django-cqrs/blob/master/blog/posts/forms.py) which creates the events and makes a call
to event handler. Event handler creates the application state, which in turn gets stored in postgres. 

So all the writes go through `Events` and `EventHandler` and reads happen on the entity data which is stored in postgres.

If anybody wants to help out or interested about this, please open a PR or start a discussion in the issues section.

#! /bin/bash

cd blog
export DJANGO_SETTINGS_MODULE=blog.settings
python -c "from demo.replay import *; replay_first_three_events()"

import django

django.setup()

from posts.models import Post
from events.models import Event
from events.event_handler import EventHandler


def _remove_application_state():
    Post.objects.all().delete()


def replay_all_events():
    _remove_application_state()

    events = Event.objects.all().order_by('event_time')
    event_handler = EventHandler(events)
    event_handler.process()


def replay_first_three_events():
    from pycallgraph import PyCallGraph
    from pycallgraph import Config
    from pycallgraph import GlobbingFilter
    from pycallgraph.output import GraphvizOutput

    config = Config()
    config.trace_filter = GlobbingFilter(exclude=[
        'django.*',
        'mongoengine.*',
        'pymongo.*'
    ])

    graphviz_output = GraphvizOutput()
    graphviz_output.output_file = 'replay_three_events.png'

    with PyCallGraph(config=config, output=graphviz_output):
        _remove_application_state()

        events = Event.objects.all().order_by('event_time')[:3]
        event_handler = EventHandler(events)
        event_handler.process()

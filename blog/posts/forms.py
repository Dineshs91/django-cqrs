import uuid
import datetime

from django.forms import ModelForm

from posts.models import Post
from events.models import Event, EventData
from events.event_types import EventTypes
from events.event_handler import EventHandler


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def save(self, commit=True):
        # TODO(dineshs91) Create a decorator for this.
        from pycallgraph import PyCallGraph
        from pycallgraph import Config
        from pycallgraph import GlobbingFilter
        from pycallgraph.output import GraphvizOutput

        config = Config()
        config.trace_filter = GlobbingFilter(exclude=[
            'django.*',
        ])

        graphviz_output = GraphvizOutput()
        graphviz_output.output_file = 'create_post.png'

        with PyCallGraph(config=config, output=graphviz_output):
            self.save_form()

    def save_form(self):
        # This is where the write model separates.
        # Use event handler.
        event_data = EventData(
            title=self.cleaned_data['title'],
            content=self.cleaned_data['content']
        )

        event = Event(
            event_id=uuid.uuid4(),
            event_time=datetime.datetime.now(),
            event_type=EventTypes.post_created_event,
            event_data=event_data
        )
        event_handler = EventHandler([event])

        event_handler.process()

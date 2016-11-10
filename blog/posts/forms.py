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

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input-field'})
        self.fields['content'].widget.attrs.update({'class': 'materialize-textarea'})

    def save(self, commit=True, action=None):
        # This is where the write model separates.
        # Use event handler.
        event_data = EventData(
            title=self.cleaned_data['title'],
            content=self.cleaned_data['content']
        )

        if action == 'update':
            # this is an update
            event = Event(
                event_id=uuid.uuid4(),
                event_time=datetime.datetime.now(),
                event_type=EventTypes.post_updated_event,
                event_data=event_data,
                post_id=self.instance.id
            )
        else:
            event = Event(
                event_id=uuid.uuid4(),
                event_time=datetime.datetime.now(),
                event_type=EventTypes.post_created_event,
                event_data=event_data,
                post_id=uuid.uuid4()
            )
        event_handler = EventHandler([event])

        event_handler.process()

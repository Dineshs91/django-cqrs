from events.models import Event
from posts.models import Post


class EventHandler:
    def __init__(self, event):
        self.event = event

    def process(self):
        # Update the event store.
        # Update the application state.
        # This should be a transaction.

        # Event store update.
        self.event.save()

        # Create the application state
        Post.objects.create(
            title=self.event.event_data.title,
            content=self.event.event_data.content
        )

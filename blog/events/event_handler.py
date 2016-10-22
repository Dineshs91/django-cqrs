from events.models import Event
from posts.models import Post


class EventHandler:
    def __init__(self, events):
        self.events = events

    def process(self):
        # Update the event store.
        # Update the application state.
        # This should be a transaction.

        for event in self.events:
            # Event store update.
            event.save()

            # Create the application state
            Post.objects.create(
                title=event.event_data.title,
                content=event.event_data.content,
                datetime=event.event_time
            )

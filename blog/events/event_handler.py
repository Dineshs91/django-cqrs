from events.models import Event
from events.event_types import EventTypes
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

            if event.event_type == EventTypes.post_created_event:
                # Create the application state
                Post.objects.create(
                    id=event.post_id,
                    title=event.event_data.title,
                    content=event.event_data.content,
                    datetime=event.event_time
                )
            elif event.event_type == EventTypes.post_updated_event:
                # Get the post and update it.
                post = Post.objects.get(id=event.post_id)
                post.title = event.event_data.title
                post.content = event.event_data.content
                post.datetime = event.event_time

                post.save()

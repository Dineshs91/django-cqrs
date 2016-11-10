from mongoengine import *


class EventData(EmbeddedDocument):
    # Store the event data.
    # In this case the post title and content.
    title = StringField()
    content = StringField()


class Event(Document):
    event_id = UUIDField()
    event_time = DateTimeField(required=True)
    event_type = StringField(required=True)
    event_data = EmbeddedDocumentField(EventData)
    post_id = UUIDField()

    def update(self):
        # Don't allow updates. Events should be immutable.
        pass

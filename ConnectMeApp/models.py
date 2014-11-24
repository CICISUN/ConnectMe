from django.db import models

# Create your models here.
from mongoengine import *
import datetime

connect('ConnectMe')

class User(Document):    
    name = StringField()
    email = EmailField()
    password = StringField()
    salt = StringField()
    email_alerts = BooleanField(default=True)
    alert_frequency = StringField(default='Weekly')
    friends = ListField(ReferenceField('self'))
    friend_requests = ListField(ReferenceField('self'))
    pending_friend_requests = ListField(ReferenceField('self'))
    validate_url = StringField()
    is_validated = BooleanField(default=False)
    validate_set_date = LongField()

class Calendar(Document):
    user_id = ReferenceField('User')
    events = ListField(ReferenceField('Event'))
    invited_events = ListField(ReferenceField('Event'))

class Event(Document):
    creator = ReferenceField('User')
    name = StringField()
    description = StringField()
    location = StringField()
    start_time = DateTimeField()
    end_time = DateTimeField
    tags = ListField(StringField())
    is_private = BooleanField(default=False)
    invite_list = ListField(ReferenceField('User'))
    attending_list = ListField(ReferenceField('User'))
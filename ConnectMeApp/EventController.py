from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from ConnectMeApp import CalendarController
from ConnectMeApp import System
from models import Event


System=System

CalendarController=CalendarController


class EventController:
    def __init__(self):
        pass
    
    @staticmethod
    def createEvent(user_id, name, description, location, start_time, end_time, tags, is_private, invite_list):
        event = Event(user_id, name, description, location, start_time, end_time, tags, is_private, invite_list)
        new_event = event.save()
        event_id = new_event['_id']
        for invitee in invite_list:
            EventController.sendInvite(event_id, invitee)
        CalendarController.addEvent(event_id, user_id)
    
    @staticmethod
    def sendInvite(event_id, user_id): #both IDs are ObjectIds - no need to cast
        CalendarController.addEvent(event_id, user_id, True)
        
    #remove event from invitees, people who have joined, and the creator's calendars
    @staticmethod
    def deleteEvent(event_id):
        event_id = ObjectId(event_id)
        client = MongoClient(System.URI)
        db = client.app
        events = db.event
        
        event = events.find_one({"_id": event_id})
        for user in event['invite_list']:
            CalendarController.removeEvent(str(event_id), str(user))
        for user in event['attending_list']:
            CalendarController.removeEvent(str(event_id), str(user))
        CalendarController.removeEvent(str(event_id), str(event['creator']))
        events.remove({"_id": event_id})
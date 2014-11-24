from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from ConnectMeApp import System
from models import Calendar

System=System

class CalendarController:
    def __init__(self):
        pass
    
    @staticmethod
    def createCalendar(user_id):
        user_id = ObjectId(user_id)
        calendar = Calendar(user_id)
        cal = calendar.save()
        return dumps(cal)
    
    @staticmethod
    def delete(user_id):
        user_id = ObjectId(user_id)
        client = MongoClient(System.URI)
        db = client.db
        calendars = db.calendar
        calendars.remove({"user_id": user_id})
    
    @staticmethod
    def getCalendar(user_id):
        user_id = ObjectId(user_id)
        client = MongoClient(System.URI)
        db = client.db
        calendars = db.calendar
        calendar = calendars.find_one({"user_id": user_id})
        #print calendar
        if not calendar:
            return None
        return dumps(calendar)
    
    @staticmethod
    def addEvent(event_id, user_id, is_invite=False):
        event_id = ObjectId(event_id)
        user_id = ObjectId(user_id)
        client = MongoClient(System.URI)
        db = client.db
        calendars = db.calendar
        
        calendar = calendars.find_one({"user_id": user_id})
        if not calendar:
            return None
        if is_invite and event_id not in calendar['invited_events']:
            calendar['invited_events'].append(event_id)
        elif not is_invite and event_id not in calendar['events']:
            calendar['events'].append(event_id)
            if event_id in calendar['invited_events']:
                calendar['invited_events'].remove(event_id)
        calendars.save(calendar)
        return dumps(calendar)
        
    @staticmethod
    def removeEvent(event_id, user_id):
        user_id = ObjectId(user_id)
        event_id = ObjectId(event_id)
        client = MongoClient(System.URI)
        db = client.db
        calendars = db.calendar
        calendar = calendars.find_one({"user_id": user_id})
        if not calendar:
            return None
        if event_id in calendar['events']:
            calendar['events'].remove(event_id)
        if event_id in calendar['invited_events']:
            calendar['invited_events'].remove(event_id)
        calendars.save(calendar)
        return dumps(calendar)
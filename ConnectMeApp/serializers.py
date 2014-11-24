from models import *
from rest_framework_mongoengine.serializers import MongoEngineModelSerializer

class UserSerializer(MongoEngineModelSerializer):
	class Meta:
		model = User
		depth = 2

class CalendarSerializer(MongoEngineModelSerializer):
	class Meta:
		model = Calendar
		depth = 2

class EventSerializer(MongoEngineModelSerializer):
	class Meta:
		model = Event
		depth = 2

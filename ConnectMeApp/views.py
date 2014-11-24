from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.context import RequestContext
from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ConnectMeApp import UserController
from ConnectMeApp.serializers import *
import urllib2
import json
from django.shortcuts import redirect
from decorators import render_to

UserController=UserController
#from CalendarController import CalendarController
# class UserList(ListCreateAPIView):
#     print "GET /api/users"
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     

 
  
def home(request):
    if request.user.is_authenticated():
        print ('haha')
        return render_to_response(Getfriends(request))
    context = RequestContext(request,
                            {'request': request,
                             'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)
  
             

# @login_required
# @render_to('home.html')   
def Getfriends(request):
    print 'haha?'
    if request.user.is_authenticated():
                print 'haha??'
                social_user = request.user.social_auth.filter(
                    provider='facebook',
                ).first()
                
    else : print 'not logged in'
    if social_user:
        url = u'https://graph.facebook.com/{0}/' \
              u'friends?fields=id,name,location,picture' \
              u'&access_token={1}'.format(
                  social_user.uid,
                  social_user.extra_data['access_token'],
              )
        request = urllib2.Request(url)
        friends = json.loads(urllib2.urlopen(request).read()).get('data')
        for friend in friends:
            print friend
            
            HttpResponse('ok!')
        
            
        
    # ...
     
#     def get_context_data(self, **kwargs):
#         context = super(FlightDetail, self).get_context_data(**kwargs)
#         friends_in_city = []
#         
#             if social_user:
#                 url = u'https://graph.facebook.com/{0}/' \
#                       u'friends?fields=id,name,location,picture' \
#                       u'&amp;access_token={1}'.format(
#                           social_user.uid,
#                           social_user.extra_data['access_token'],
#                       )
#                 request = urllib2.Request(url)
#                 friends = json.loads(urllib2.urlopen(request).read()).get('data')
#                 for friend in friends:
#                     if (
#                         friend.get('location')
#                         and flight.arrival_airport.city
#                         and flight.arrival_airport.city.name
#                         in friend['location']['name']
#                     ):
#                         friends_in_city.append({
#                             'name': friend['name'],
#                             'photo': friend['picture']['data']['url'],
#                             'profile_url':
#                             'https://www.facebook.com/{0}'.format(friend['id']),
#                         })
#         context.update({
#             'friends_in_city': friends_in_city,
#         })
#         return context    
        
    
# class Login(RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#  
#     def post(self, request):
#         print "POST /api/login"
#         email = request.DATA['email']
#         password = request.DATA['password']       
#         user_id = UserController.login(email, password)
#  
#         print user_id
#         if not user_id:
#             return Response(401)
#         return HttpResponse(user_id)
# Create your views here.

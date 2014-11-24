from django.conf.urls import patterns, url, include
from ConnectMeApp import views
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	
    # Core Routes
    url('^login/$', TemplateView.as_view(template_name='login.html')),
    url('^signup/$', TemplateView.as_view(template_name='signup.html')),
	#url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'ConnectMeApp.views.home', name='home'),
 	url('listf', 'ConnectMeApp.views.Getfriends'),
	
	#url(r'^$', 'socialauth.views.signin_complete'),
	#url(r'^$', TemplateView.as_view(template_name='home.html')),
	
    # GET
    #url(r'^api/users/$', views.UserList.as_view()),
    
	# POST
   # url(r'^api/login/$', views.Login.as_view()),
    
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
   
    url(r'', include('jqmobile.urls'))
)

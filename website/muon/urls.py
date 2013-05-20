from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',  
    (r'^login/$', 'website.muon.views.loginRequest'),
    (r'^register/$', 'website.muon.views.register'),
		(r'^addUser/$', 'website.muon.views.addUser'),
    (r'^home/$', 'website.muon.views.home'),
    (r'^logout/$', 'website.muon.views.logoutRequest'),
    (r'^listUsers/$', 'website.muon.views.listUsers'),
		(r'^deleteUser/(?P<username>\w+)/$', 'website.muon.views.deleteUser')	
)


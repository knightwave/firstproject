from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',  
    (r'^list/$', 'website.ebooks.views.list'),
    (r'^compile/$', 'website.ebooks.views.compile'),
    (r'^problems/(?P<problem>\w+)/$', 'website.ebooks.views.problems'),
)


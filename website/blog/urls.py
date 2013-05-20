from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',  
    (r'^post/$', 'website.blog.views.post'),
    (r'^comment/$', 'website.blog.views.comment'),
    (r'^problems/(?P<problem>\w+)/$', 'website.ebooks.views.problems'),
)


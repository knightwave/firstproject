from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',  
    (r'^post/$', 'website.blog.views.post'),
    (r'^comment/$', 'website.blog.views.comment'),
    (r'^tags/(?P<tag>\w+)/$', 'website.blog.views.with_tag'),
)


from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',  
    (r'^sendMail/$', 'website.mailserver.views.sendMail'),
    (r'^comment/$', 'website.blog.views.comment'),
    (r'^problems/(?P<problem>\w+)/$', 'website.ebooks.views.problems'),
)




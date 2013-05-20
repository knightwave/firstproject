from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
		
		#App Urls Begin
		(r'^muon/',include('website.muon.urls')),
		(r'^ebooks/',include('website.ebooks.urls')),
		(r'^blog/',include('website.blog.urls')),
		(r'^mailserver/',include('website.mailserver.urls')),
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		        {'document_root': '/home/knightwave/django_projects/website/website/static/', 'show_indexes': True}),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		        {'document_root': '/home/knightwave/django_projects/website/website/media/', 'show_indexes': True}),
)

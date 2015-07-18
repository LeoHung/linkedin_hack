from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'around-be.views.home_page'),
    url(r'^hello-world$', 'around-be.views.hello_world'),
    url(r'^hello-world-with-template$', 'around-be.views.hello_world_with_template'),
    url(r'^greet$', 'around-be.views.greet'),
)

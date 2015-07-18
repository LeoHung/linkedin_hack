from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'around-be.views.home_page'),
    url(r'^hello-world$', 'around-be.views.hello_world'),
    url(r'^hello-world-with-template$', 'around-be.views.hello_world_with_template'),
    url(r'^greet$', 'around-be.views.greet'),
)
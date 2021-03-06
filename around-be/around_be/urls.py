from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', 'around_be.views.home_page'),
    url(r'^hello-world$', 'around_be.views.hello_world'),
    url(r'^hello-world-with-template$', 'around_be.views.hello_world_with_template'),
    url(r'^greet$', 'around_be.views.greet'),
    url(r'^search$', 'around_be.views.search_api', name="search_api"),
    url(r'^message/(?P<mid>[0-9]+)/$', 'around_be.views.message_api', name='message_api'),
    url(r'^message-upload$', 'around_be.views.message_upload', name='message_upload'),
    url(r'^mock-message$', 'around_be.views.generate_mock_message', name="generate_mock_message"),


    # Web Endpoints
    url(r'^test-base$', 'around_be.views.base_test', name='base_test'),
    url(r'^spots$', 'around_be.views.spots', name='spots'),
    url(r'^spot/(?P<mid>[0-9]+)/$', 'around_be.views.spot', name='spot'),
    url(r'^create-spot$', 'around_be.views.create_spot', name='create_spot'),
    url(r'^add-spot$', 'around_be.views.add_spot', name='add_spot'),
    url(r'^map$', 'around_be.views.map', name='map')
)

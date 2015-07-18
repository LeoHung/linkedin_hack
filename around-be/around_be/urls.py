from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'around_be.views.home_page'),
    url(r'^hello-world$', 'around_be-be.views.hello_world'),
    url(r'^hello-world-with-template$', 'around_be.views.hello_world_with_template'),
    url(r'^greet$', 'around_be.views.greet'),
    url(r'^search$', 'around_be.views.search_api', name="search_api"),
    url(r'^message/(?P<mid>[0-9]+)/$', 'around_be.views.message_api', name='message_api'),
    url(r'^message-upload$', 'around_be.views.message_upload', name='message_upload'),
    url(r'^mock-message$', 'around_be.views.generate_mock_message', name="generate_mock_message"),
)
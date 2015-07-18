from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'around_be.views.home_page'),
    url(r'^hello-world$', 'around_be-be.views.hello_world'),
    url(r'^hello-world-with-template$', 'around_be.views.hello_world_with_template'),
    url(r'^greet$', 'around_be.views.greet'),
    url(r'^search$', 'around_be.views.search_api', name="search_api"),
    url(r'^mock-message$', 'around_be.views.generate_mock_message', name="generate_mock_message"),
)
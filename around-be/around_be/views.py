from django.http import HttpResponse
from django.shortcuts import render
from mock_message_generator import *
from around_be.models import *

import json

def home_page(request):
  # render takes: (1) the request,
  #               (2) the name of the view to generate, and
  #               (3) a dictionary of name-value pairs of data to be
  #                   available to the view.
  return render(request, 'around_be/index.html', {})

def hello_world(request):
  # Just return an HttpResponse object with the HTML we want to send
  html="""
    <!DOCTYPE HTML>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Hello World</title>
      </head>
      <body>
        <h1>Hello World!</h1>
      </body>
    </html>
  """
  return HttpResponse(html)


def hello_world_with_template(request):
  # render takes: (1) the request,
  #               (2) the name of the view to generate, and
  #               (3) a dictionary of name-value pairs of data to be
  #                   available to the view.
  return render(request, 'around_be/hello-world.html', {})


# The action for the 'intro/hello.html' route.
def greet(request):
  # Creates a context dictionary (map) to send data to the templated HTML file
  context = {}

  # Retrieve the 'name' parameter, if present, and add it to the context
  if 'name' in request.GET:
    context['person_name'] = request.GET['name']

  # Pass the context to the templated HTML file (aka the "view")
  return render(request, 'around_be/greet.html', context)

def search_api(request):
  if request.method != 'GET':
    raise Http404

  context = [
    {
      "mid": 1,
      "title": "Pokemon !! ",
      "img_url": "https://raw.githubusercontent.com/LeoHung/linkedin_hack/master/pseudo_api/img/11.png",
      "lat": 37.4253498,
      "lng": -122.0765002,
      "time": 1437190740,
      "lock": False,
      "unlock_type": None,
      "category": "pokemon"
    },
    {
        "mid": 2,
        "title": "Pokemon !! ",
        "img_url": "https://raw.githubusercontent.com/LeoHung/linkedin_hack/master/pseudo_api/img/12.png",
        "lat": 37.5253498,
        "lng": -122.0165002,
        "time": 1437190740,
        "lock": False,
        "unlock_type": None,
        "category": "pokemon"
    }
  ]

  response_text = json.dumps(context)
  return HttpResponse(response_text, content_type='application/json')

def message_api(request, mid=None):
  if not mid:
    return HttpResponseNotFound('<h1>mid is null.</h1>')

  response_text = 'Hello mid = %s' % mid
  return HttpResponse(response_text, content_type='application/json')


def message_upload(request):
  pass

# def generate_mock_message(request):
#   mock_objects = get_all()

#   for obj in mock_objects:
#     message = Messsage(
#       msg_type = obj['msg_type'],
#       title = obj['title'],
#       doc = obj['doc'],
#       url = obj['url'],
#       img_url = obj['img_url'],
#       start_time = obj['start_time'],
#       end_time = obj['end_time'],
#       category = obj['category'],
#       unlock_type = obj['unlock_type'],
#       lat = obj['lat'],
#       lng = obj['lng'])
#   return HttpResponse("mocking succeeded")

from django.http import HttpResponse
from django.shortcuts import render
from mock_message_generator import *
from around_be.models import Message

import json
import datetime
import time

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

  messages = Message.objects.all()
  context = []
  print len(messages)

  for m in messages:
    print m
    res = {
      'id': m.id,
      'msg_type': m.msg_type,
      'title': m.title,
      'doc': m.doc,
      'url': m.url,
      'img_url': m.img_url,
      'start_time': long(time.mktime(m.start_time.timetuple())*1000),
      'end_time': long(time.mktime(m.end_time.timetuple())*1000),
      'category': m.category,
      'lat': float(m.lat),
      'lng': float(m.lng)
    }
    context.append(res)
  response_text = json.dumps(context)
  return HttpResponse(response_text, content_type='application/json')

def message_api(request):
  pass

def message_upload(request):
  pass

def generate_mock_message(request):
  mock_objects = get_all()
  
  for obj in mock_objects:
    message = Message(
      msg_type = obj['msg_type'],
      title = obj['title'],
      doc = obj['doc'],
      url = obj['url'],
      img_url = obj['img_url'],
      start_time = datetime.datetime.fromtimestamp(obj['start_time']).strftime('%Y-%m-%dT%H:%M:%S'),
      end_time = datetime.datetime.fromtimestamp(obj['end_time']).strftime('%Y-%m-%dT%H:%M:%S'),
      category = obj['category'],
      unlock_type = obj['unlock_type'],
      lat = obj['lat'],
      lng = obj['lng']
    )
    message.save()

  return HttpResponse("mocking succeeded")

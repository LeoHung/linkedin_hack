from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import Http404
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
  LAT_RANGE = 0.1
  LNG_RANGE = 0.1

  if request.method != 'GET':
    raise Http404

  lat = request.GET.get("lat")
  lng = request.GET.get("lng")

  if lat and lng:
    lat = float(lat)
    lng = float(lng)
    messages = Message.objects.filter(
        lat__gte=lat - LAT_RANGE,
        lat__lte=lat + LAT_RANGE,
        lng__gte=lng - LNG_RANGE,
        lng__lte=lng + LNG_RANGE)
  else:
    print "No lat lng"
    raise Http404

  category = request.GET.getlist('category')

  context = []
  for m in messages:
    if category and m.category not in category:
      continue
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
      'lng': float(m.lng),
      'unlock_type': m.unlock_type,
      'lock': m.lock
    }
    context.append(res)
  response_text = json.dumps(context)
  return HttpResponse(response_text, content_type='application/json')

def message_api(request, mid=None):
  if not mid:
    return HttpResponseNotFound('<h1>mid is null.</h1>')

  try:
    m = Message.objects.get(id=int(mid))
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
      'lng': float(m.lng),
      'unlock_type': m.unlock_type,
      'lock': m.lock
    }
    return HttpResponse(json.dumps(res), content_type='application/json')
  except Exception as e:
    print e
    return HttpResponseNotFound('<h1>Not Found %s. </h1>' % mid)

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
      lock = obj['lock'],
      unlock_type = obj['unlock_type'],
      lat = obj['lat'],
      lng = obj['lng']
    )
    message.save()

  return HttpResponse("mocking succeeded")

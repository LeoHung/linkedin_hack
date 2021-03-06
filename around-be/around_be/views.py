import json
import datetime
import time
import math

from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse


from around_be.models import Message
from mock_message_generator import *

from around_be.s3 import s3_upload

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

def search(lat, lng, category):
  MAX_RANGE = 0.1
  messages = Message.objects.all()
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
      'category': m.category,
      'lat': float(m.lat),
      'lng': float(m.lng),
      'unlock_type': m.unlock_type,
      'lock': m.lock,
      'dist': math.sqrt((float(m.lat) - lat) ** 2 +
                        (float(m.lng) - lng) ** 2)
    }
    if m.start_time != None:
      res['start_time'] = long(time.mktime(m.start_time.timetuple())*1000)
    if m.end_time != None:
      res['end_time'] = long(time.mktime(m.end_time.timetuple())*1000)

    context.append(res)

  context = filter(lambda x: x['dist'] <= MAX_RANGE, context)
  context = sorted(context, key=lambda x: x['dist'])
  return context

def search_api(request):
  MAX_RANGE = 0.1

  if request.method != 'GET':
    raise Http404

  lat = request.GET.get("lat")
  lng = request.GET.get("lng")

  if lat and lng:
    lat = float(lat)
    lng = float(lng)
    messages = Message.objects.all()
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
      'category': m.category,
      'lat': float(m.lat),
      'lng': float(m.lng),
      'unlock_type': m.unlock_type,
      'lock': m.lock,
      'dist': math.sqrt((float(m.lat) - lat) ** 2 +
                        (float(m.lng) - lng) ** 2)
    }
    if m.start_time != None:
      res['start_time'] = long(time.mktime(m.start_time.timetuple())*1000)
    if m.end_time != None:
      res['end_time'] = long(time.mktime(m.end_time.timetuple())*1000)
    context.append(res)

  context = filter(lambda x: x['dist'] <= MAX_RANGE, context)
  context = sorted(context, key=lambda x: x['dist'])
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
      'category': m.category,
      'lat': float(m.lat),
      'lng': float(m.lng),
      'unlock_type': m.unlock_type,
      'lock': m.lock
    }
    
    if m.start_time != None:
      res['start_time'] = long(time.mktime(m.start_time.timetuple())*1000)
    if m.end_time != None:
      res['end_time'] = long(time.mktime(m.end_time.timetuple())*1000)

    return HttpResponse(json.dumps(res), content_type='application/json')
  except Exception as e:
    print e
    return HttpResponseNotFound('<h1>Not Found %s. </h1>' % mid)


# http://localhost:8000/message-upload?msg_type=pokemon&title=Pokemon151&doc=whatever&url=test&img_url=test&start_time=1437199878000&end_time=1437286278000&category=pokemon&lat=37.4253498&lng=-122.0765002&lock=True&unlock_type=upload_pic
@csrf_exempt
def message_upload(request):
  if request.method != 'POST':
    raise Http404

  message = Message(
    msg_type = request.POST['msg_type'],
    title = request.POST['title'],
    doc = request.POST['doc'],
    url = request.POST['url'],
    img_url = request.POST['img_url'],
    start_time = datetime.datetime.fromtimestamp(long(request.POST['start_time'])/1000).strftime('%Y-%m-%dT%H:%M:%S'),
    end_time = datetime.datetime.fromtimestamp(long(request.POST['end_time'])/1000).strftime('%Y-%m-%dT%H:%M:%S'),
    category = request.POST['category'],
    lock = bool(request.POST['lock']),
    unlock_type = request.POST['unlock_type'],
    lat = float(request.POST['lat']),
    lng = float(request.POST['lng'])
  )
  message.save()

  return HttpResponse("message upload succeeded")

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

def base_test(request):
  return render(request, 'around_be/base.html', {})

def spots(request):
  lat = 37.4253498
  lng = -122.0765002
  messages = search(lat, lng, [])
  context = {}
  # context['messages'] = messages
  return render(request, 'around_be/spots.html', context)  

def spot(request, mid=None):
  if not mid:
    return HttpResponseNotFound('<h1>mid is null.</h1>')
  
  m = Message.objects.get(id=int(mid))
  context = {}
  context['message'] = m
  return render(request, 'around_be/spot.html', context)  

def map(request):
  return render(request, 'around_be/map.html', {})

def create_spot(request):
  return render(request, 'around_be/create-spot.html', {})

@csrf_exempt
def add_spot(request):
  if request.method != "POST":
    raise Http404

  print request.FILES['fileField'].name
  img_url = s3_upload(request.FILES['fileField'], request.FILES['fileField'].name)
  print img_url

  message = Message(
    msg_type = request.POST['msg_type'],
    title = request.POST['title'],
    doc = request.POST['doc'],
    url = request.POST['url'],
    img_url = img_url,
    # start_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S'),
    # end_time = datetime.datetime.fromtimestamp(time.time() + 100000000).strftime('%Y-%m-%dT%H:%M:%S'),
    # category = request.POST['category'],
    # lock = bool(request.POST['lock']),
    # unlock_type = request.POST['unlock_type'],
    lat = float(request.POST['lat']),
    lng = float(request.POST['lng'])
  )
  message.save()

  return redirect(reverse('map'))

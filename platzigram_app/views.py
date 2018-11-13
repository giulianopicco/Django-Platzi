#Django
from django.http import HttpResponse
from django.http import JsonResponse
import json

#Utilities
from datetime import datetime

def hello_world(request):
  """Return a greeting"""
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse('Hi, current server time is: {now}'.format(now=now))


def sort_int(request):
  """Returns a JSON response with sorted integers"""
  """Debugger"""
  # import pdb; pdb.set_trace()
  args = (request.GET['numbers']).split(',')
  args = list(map(int, args))
  print(args)
  sorted_args = sorted(args)
  response = json.dumps(sorted_args, indent=4)

  data = {
    'status' : 'ok',
    'numbers' : sorted_args,
    'message' : 'Integers sorted succesfully',
  }
  
  return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
  # return JsonResponse({'Numbers':response})

def say_hi(request, name, age):
  """Return a greeting"""
  message = ''
  if age < 12 : message = 'sorry {} you are not allowed here'.format(name)
  else: message = "welcome {}".format(name)
  return HttpResponse(message)
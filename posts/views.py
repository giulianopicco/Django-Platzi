from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

#Utilities
from datetime import datetime

posts = [
  {
    'title': "Mont Blac",
    'user': {
      'name': 'Yesica Cortez',
      'picture': 'https://picsum.photos/60/60/?1027'
    },
    'timestamp': str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')),
    'photo': 'https://picsum.photos/200/200/?132',
  },
  {
    'title': "Via Lactea",
    'user': {
      'name': 'C. Vander',
      'picture': 'https://picsum.photos/60/60/?1005'
    },
    'timestamp': str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')),
    'photo': 'https://picsum.photos/200/200/?234',
  },
  {
    'title': "Nuevo Auditorio",
    'user': {
      'name': 'Thespianartist',
      'picture': 'https://picsum.photos/60/60/?883'
    },
    'timestamp': str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')),
    'photo': 'https://picsum.photos/200/200/?345',
  }
]


# render from list
# def list_posts(request):
#   content = []
#   for post in posts:
#     content.append("""
#       <p><strong>{name}</strong></p>
#       <p><small>{user} - {timestamp}</small></p>
#       <figure><img src="{picture}"/></figure>
#     """.format(**post))
#   # return HttpResponse(content)
#   return HttpResponse('<br>'.join(content)) #here <br> is the separator of the list to be joined

# render from template

@login_required
def list_posts(request):
  return render(request, 'posts/feed.html', {'posts':posts})


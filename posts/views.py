from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

#Utilities
from datetime import datetime # not being used anymore

#Models
from posts.models import Post

#Forms
from posts.forms import PostForm

# posts = [
#   {
#     'title': "Mont Blac",
#     'user': {
#       'name': 'Yesica Cortez',
#       'picture': 'https://picsum.photos/60/60/?1027'
#     },
#     'timestamp': str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')),
#     'photo': 'https://picsum.photos/200/200/?132',
#   },
#   {
#     'title': "Via Lactea",
#     'user': {
#       'name': 'C. Vander',
#       'picture': 'https://picsum.photos/60/60/?1005'
#     },
#     'timestamp': str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')),
#     'photo': 'https://picsum.photos/200/200/?234',
#   },
#   {
#     'title': "Nuevo Auditorio",
#     'user': {
#       'name': 'Thespianartist',
#       'picture': 'https://picsum.photos/60/60/?883'
#     },
#     'timestamp': str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs')),
#     'photo': 'https://picsum.photos/200/200/?345',
#   }
# ]


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
  posts = Post.objects.all().order_by('-created')
  return render(request, 'posts/feed.html', {'posts':posts})

@login_required
def create_post(request):
  """Create new post view."""
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('feed')

  else:
    form = PostForm()

  return render(
    request=request,
    template_name='posts/new.html',
    context={
      'form': form,
      'user': request.user,
      'profile': request.user.profile
    } 
  )
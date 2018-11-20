#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#exceptions
from django.db.utils import IntegrityError

#models
from django.contrib.auth.models import User
from users.models import Profile

#forms
from users.forms import ProfileForm


def update_profile(request):
  # update a user's profile view
  profile = request.user.profile

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data

      profile.website = data['website']
      profile.phone_number = data['phone_number']
      profile.biography = data['biography']
      profile.picture = data['picture']
      profile.save()

      return redirect('update_profile')
      
  else:
    form = ProfileForm()
  
  return render(
    request,
    "users/update-profile.html",
    context={
      'profile': profile,
      'user': request.user,
      'form': form,
    }
  )



def login_view(request):
  # import pdb; pdb.set_trace()
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    print(username,':',password)

    user = authenticate(request, username=username, password=password)
    if user:
      print('you are logged in')
      login(request, user)
      return redirect('feed')
    else:
      print('wrong username or password')
      return render (request, 'users/login.html', {'error':'invalid username and password'})
     

  return render(request, 'users/login.html')

def signup_view(request):
  # import pdb; pdb.set_trace()
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    password_confirmation = request.POST['password_confirmation']
    #validate password
    if password == password_confirmation: return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})

    try:
      user = User.objects.create_user(username=username, password=password)
    except IntegrityError:
      return render(request, 'users/signup.html', {'error':'User name is already taken'})
      
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()

    profile = Profile(user=user)
    profile.save()

    return redirect('login')

  return render(request, 'users/signup.html')
  

@login_required
def logout_view(request):
  logout(request)
  return redirect ('login')




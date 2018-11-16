#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#models
from django.contrib.auth.models import User
from users.models import Profile


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
    except:
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




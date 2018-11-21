"""Users forms"""

from django import forms

# models
from django.contrib.auth.models import User
from users.models import Profile


# class SignupForm(forms.Form):
#   """Sign up form"""

#   username = forms.CharField(min_length=4 ,max_length=50)
#   password = forms.CharField(max_length=70, widget=forms.PasswordInput())
#   password_confimation = forms.CharField(max_length=70, widget=forms.PasswordInput())

#   first_name = forms.CharField(min_length=2, max_length=50)
#   last_name = forms.CharField(min_length=2, max_length=50)

#   email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput)

#   def clean_username(self):
#     """Username must be unique"""
#     username = self.cleaned_data['username']
#     username_taken = User.objects.filter(username=username).exists()
#     if username_taken:
#       raise forms.ValidationError('Username is already in use.')
#     return username

#   def clean(self):
#     """Verify password confirmation match"""
#     data = super().clean()

#     password = data['password']
#     password_confimation = data['password_confirmation']

#     if password != password_confimation:
#       raise forms.ValidationError('Passwords do not match')
#     return data

#   def save(self):
#     """Create User and profile"""
#     # data = self.cleaned_data
#     username = self.cleaned_data['username']
#     password = self.cleaned_data['password']
#     password = self.cleaned_data['password']
#     first_name = self.cleaned_data['first_name']
#     last_name = self.cleaned_data['last_name']
#     email = self.cleaned_data['email']

#     data.pop('password_confimation') #removes unnecessary field

#     # user = User.objects.create_user(**data)
#     user = User.objects.create_user(
#       username=data['username'],
#       password=data['password'],
#       first_name=data['first_name'],
#       last_name=data['last_name'],
#       email=data['email'],
#     )
#     profile = Profile(user=user)
#     profile.save()


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.data
        # creamos usuario
        user = User.objects.create(
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email')
        )
        # guardamos el pass
        user.set_password(data.get('password'))
        user.save()
        # creamos el perfil
        profile = Profile(user=user)
        profile.save()
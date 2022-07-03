from attr import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# This class is using a built-in form.
class  SignupForm(UserCreationForm):
      class Meta:
            model = User
            fields = ('username', 'password1', 'password2')
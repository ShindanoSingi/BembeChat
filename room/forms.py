from django import forms
from .models import Room, Message


class RoomForm(forms.ModelForm):

    # name: forms.CharField(widget=forms.TextInput(attrs={'class': 'room-name'}))
    # slug: forms.SlugField(widget=forms.TextInput(attrs={'class': 'room-slug'}))

    class Meta:
        model = Room
        fields = ['name', 'slug',]

# This class is using a built-in form.
# class  SignUpForm(UserCreationForm):
#       class Meta:
#             model = User
#             fields = ['username', 'password1', 'password2',]


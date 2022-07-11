from django import forms
from .models import Room


class RoomForm(forms.ModelForm):

    name: forms.CharField(widget=forms.TextInput(attrs={'class': 'room-name'}))
    slug: forms.SlugField(widget=forms.TextInput(attrs={'class': 'room-slug'}))

    class Meta:
        model = Room
        fields = "__all__"







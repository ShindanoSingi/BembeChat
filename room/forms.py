from django import forms
from .models import Room


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'slug',)


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('author', 'body')

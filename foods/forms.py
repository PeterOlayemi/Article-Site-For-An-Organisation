from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Comment

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=99, help_text='Enter your Username')
    first_name=forms.CharField(max_length=30, required=True, help_text='Enter your First Name')
    last_name=forms.CharField(max_length=30, required=True, help_text='Enter your Last Name')
    email=forms.EmailField(max_length=50, help_text='Enter a valid email address', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    text=forms.Textarea()

    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment'}

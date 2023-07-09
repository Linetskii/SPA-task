from django import forms
from django.core import validators
from django.core.files.images import get_image_dimensions


class MessageForm(forms.Form):
    template_name = "spa/form_snippet.html"
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'value': 'Avatar'}))  # , validators=[validators.val])
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    homepage = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder': 'Homepage'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))  # attrs={'name':'title'}
    attachment = forms.FileField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
"""SPA forms"""
from django import forms
from django.core.validators import FileExtensionValidator



class MessageForm(forms.Form):
    """Message sending form"""
    # template_name = "spa/form_snippet.html"
    avatar = forms.ImageField(
        # required=False,
        widget=forms.ClearableFileInput(
            attrs={'value': 'Avatar'}
        ),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'gif', 'png', ])
        ]
    )
    username = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        )
    )
    email = forms.EmailField(
        min_length=3,
        max_length=50,
        widget=forms.EmailInput(
            attrs={'placeholder': 'e-mail'}
        )
    )
    homepage = forms.URLField(
        min_length=8,
        max_length=50,
        required=False,
        widget=forms.URLInput(
            attrs={'placeholder': 'Homepage'}
        )
    )
    text = forms.CharField(
        min_length=2,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message'}
        )
    )
    attachment = forms.FileField(
        required=False,
        max_length=800 * 1024,
        validators=[
            FileExtensionValidator(allowed_extensions=['txt', 'jpg', 'jpeg', 'gif', 'png',])
        ]
    )
    password = forms.CharField(
        min_length=8,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )
    prev_post = forms.CharField(
        widget=forms.HiddenInput(
        )
    )

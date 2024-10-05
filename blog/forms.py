from .models import Comment
from django import forms
# blog/forms.py
from allauth.account.forms import LoginForm, SignupForm
from django import forms
from .models import Comment 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control custom-class'})
        self.fields['password'].widget.attrs.update({'class': 'form-control custom-class'})

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control custom-class'})
        self.fields['email'].widget.attrs.update({'class': 'form-control custom-class'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control custom-class'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control custom-class'})
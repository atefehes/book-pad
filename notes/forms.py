from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


READ_STATUS = (('0', 'not added'),
                ('1', 'added'),
                )

class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=READ_STATUS, widget=forms.Select(attrs={'onchange': 'submit();'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})

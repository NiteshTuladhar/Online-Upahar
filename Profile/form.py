from django import forms
from .models import Profile,gender_list


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile

        exclude = ['user']
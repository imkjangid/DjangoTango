from django import forms
from basics.models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'message']
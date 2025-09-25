from django import forms
from signals.models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email']
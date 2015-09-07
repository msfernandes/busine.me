from django import forms
from .models import BusinemeUser


class BusinemeUserForm(forms.ModelForm):

    class Meta:
        model = BusinemeUser
        fields = ('first_name', 'username', 'email', 'password')

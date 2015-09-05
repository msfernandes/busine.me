from django.forms import ModelForm
from .models import BusinemeUser


class BusinemeUserForm(ModelForm):
    class Meta:
        model = BusinemeUser
        fields = ('first_name', 'username', 'email', 'password')

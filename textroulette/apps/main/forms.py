from django.forms import ModelForm
from textroulette.apps.main.models import UserNumber


class UserForm(ModelForm):
    class Meta:
        model = UserNumber
        fields = ['phone_number'] 

    def is_valid(self, *args, **kwargs):
        super(UserForm, self).is_valid()


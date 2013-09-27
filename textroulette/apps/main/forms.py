from django.forms import ModelForm
from textroulette.apps.main.models import UserNumber
import re


class UserForm(ModelForm):
    class Meta:
        model = UserNumber
        fields = ['phone_number']


    def is_valid(self, *args, **kwargs):
        super(UserForm, self).is_valid()
        pattern = re.compile('(\d{3})-?(\d{3})-?(\d{4})$')
        result = pattern.match(self.cleaned_data.get('phone_number'))
        return result

from django.views.generic.edit import FormView
from textroulette.apps.main.forms import UserForm

class Home(FormView):
    form_class = UserForm
    template_name = "main/home.html"
    



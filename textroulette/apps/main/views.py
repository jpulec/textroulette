from django.views.generic.edit import FormView
from textroulette.apps.main.forms import UserForm

class Home(FormView):
    form_class = UserForm
    template_name = "main/home.html"
    success_url = "/success/"

class Success(TemplateView):
    template_name = "main/success.html"

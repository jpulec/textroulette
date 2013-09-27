from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from textroulette.apps.main.forms import UserForm
from textroulette.apps.main.models import UserNumber

class Home(FormView):
    form_class = UserForm
    template_name = "main/home.html"
    success_url = "/success/"

    def form_valid(self, form):
        self.object = form.save()
        if UserNumber.objects.count() > 1:
            self.object.connected = UserNumber.objects.exclude(id=self.object).order_by('?')[0]
        return super(Home, self).form_valid(form)

class Success(TemplateView):
    template_name = "main/success.html"

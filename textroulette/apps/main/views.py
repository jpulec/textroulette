from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from textroulette.apps.main.forms import UserForm
from textroulette.apps.main.models import UserNumber

class Home(FormView):
    form_class = UserForm
    template_name = "main/home.html"
    success_url = "/success/"

    def form_valid(self, form):
        try:
            UserNumber.objects.get(phone_number=form.instance.phone_number)
            return HttpResponseRedirect("/duplicate/")
        except ObjectDoesNotExist:
            self.object = form.save()
            if UserNumber.objects.count() > 1:
                connectee = UserNumber.objects.exclude(id=self.object.id).order_by('?')[0]
                self.object.connected = connectee
                connectee.connected = self.object
                connectee.save()
                self.object.save()

        return super(Home, self).form_valid(form)

class Success(TemplateView):
    template_name = "main/success.html"

class Duplicate(TemplateView):
    template_name = "main/duplicate.html"

from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

class Twilio(View):

    def post(self, request, *args, **kwargs):
        if request.POST:
            if request.POST['Body'].startswith("STOP"):
                connected = UserNumber.objects.get(phone_number=request.POST['From'][2:]).connected
                UserNumber.objects.get(phone_number=request.POST['From'][2:]).delete()
                if UserNumber.objects.count() > 1:
                    connectee = UserNumber.objects.exclude(id=connected.id).order_by('?')[0]
                    connected.connected = connectee
                    connected.save()
            if request.POST['Body'].startswith("NEXT"):
                connected = UserNumber.objects.get(phone_number=request.POST['From'][2:]).connected
                from_user = UserNumber.objects.get(phone_number=request.POST['From'][2:])
                from_user.connected = UserNumber.objects.exclude(id=from_user.id).order_by('?')[0]
                from_user.save()
                connected.connected = UserNumber.objects.exclude(id=connected.id).order_by('?')[0]
                connected.save()
            xml = '<?xml version="1.0" encoding="UTF-8" ?><Response><Message to="' + "+1" + UserNumber.objects.get(phone_number=request.POST['From'][2:]).connected.phone_number + '">' + request.POST['Body'] + '</Message></Response>'
            return HttpResponse(xml, content_type="text/xml")


    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Twilio, self).dispatch(*args, **kwargs)

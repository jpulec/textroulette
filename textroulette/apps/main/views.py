from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "main/home.html"
    success_url = "/success/"

class Success(TemplateView):
    template_name = "main/success.html"

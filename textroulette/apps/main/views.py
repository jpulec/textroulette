from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "main/home.html"
    success_url = "main/success.html"


    def form_valid(self, form):


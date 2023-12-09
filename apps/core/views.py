from django.shortcuts import HttpResponse
from django.http import HttpRequest
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request: HttpRequest):
        return HttpResponse("Bienvenido a la pagina bro!")
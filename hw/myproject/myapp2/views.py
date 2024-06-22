from django.views import View
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")

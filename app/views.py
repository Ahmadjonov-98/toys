from django.http import HttpResponse


def dashboard(request):
    return HttpResponse('<h1>Hello World </h1>')

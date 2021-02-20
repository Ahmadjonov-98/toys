from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('<h1> Welcome to dashboard </h1>')

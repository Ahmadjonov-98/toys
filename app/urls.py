from django.urls import path
from .views import dashboard

app_name= 'app'
urlpatterns = {
    path('', dashboard, name='dashboard'),
}

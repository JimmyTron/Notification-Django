from django.urls import path
from . import views

urlpatterns = [
    path('mpesa', views.mpesa_payment, name='mpesa'),
    path('response', views.response_view, name='response')
]
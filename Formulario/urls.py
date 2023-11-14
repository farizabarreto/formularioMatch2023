from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('processamento_form/', views.processamento_form, name='processamento_form'),
    path('sucesso/', views.sucesso, name='sucesso')
    ]

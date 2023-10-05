from django.urls import path
from Receita import views


urlpatterns = [
    path('', views.home, name="home"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="calificami-index"),
    path('about/', views.aboutus, name="calificami-about"),
    path('login/', views.login, name='calificami-login'),
]
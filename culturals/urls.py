
from django.urls import path
from . import views


urlpatterns = [
    path('', views.culturals, name='cultural'),
    path('signup', views.ghanekar, name='signup'),
    

]
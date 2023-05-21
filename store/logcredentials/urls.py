from django.urls import path
from.import views

urlpatterns = [

     path('computer', views.computer, name='computer'),
     path('commerce', views.commerce, name='commerce'),
     path('chemistry', views.chemistry, name='chemistry'),
     path('zoology', views.zoology, name='zoology'),
     path('english', views.english, name='english'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]
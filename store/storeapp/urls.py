from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('logout', views.logout, name='logout'),

    path('add/', views.order_create_view, name='order_add'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
]

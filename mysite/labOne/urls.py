from django.urls import path

from . import views

urlpatterns = [
    path('', views.forms, name='index'),
    path('mplimage/', views.mplimage, name='forms'),
    path('dyhotomia/', views.dyhotomia, name='forms'),
    path('newton/', views.dyhotomia, name='forms')
]
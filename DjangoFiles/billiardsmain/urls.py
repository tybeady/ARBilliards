from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calibrationValues/', views.calibrationValues, name='calibrationValues'),
]
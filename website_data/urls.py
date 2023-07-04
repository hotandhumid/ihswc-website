
from . import views
from django.urls import path

urlpatterns = [
    path('', views.send_to_home),
    path('about/', views.about),
    path('awards/', views.awards),
    path('submit/', views.form, name="form"),
    path('index/', views.index),
    path('process/', views.process),
    path('rules/', views.rules),
    path('submissions/', views.submissions),
    path('test/', views.test, name="test")
]

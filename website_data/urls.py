
from . import views
from django.urls import path

urlpatterns = [
    path('submit/', views.submit),
    path('awards/', views.awards)
]


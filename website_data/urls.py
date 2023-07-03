
from . import views
from django.urls import path

urlpatterns = [
    path('form/', views.form, name="form"),
    path('submit/', views.submit),
    path('awards/', views.awards)
]


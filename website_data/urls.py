
from . import views
from django.urls import path

urlpatterns = [
    path('', views.send_to_home),
    path('about/', views.about),
    path('awards/', views.awards),
    path('submit/', views.submit),
    path('form/', views.form, name="form"),
    path('home/', views.home),
    path('process/', views.process),
    path('rules/', views.rules),
    path('test/', views.test, name="test"),
    path('sign-in/', views.sign_in),
    path('admin-page/', views.admin_page),
    path('admin-page/submission/', views.submission),
    path('donate/', views.donate)
]

from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloAPI.as_view()),
]

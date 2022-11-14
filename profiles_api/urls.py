from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewsets, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloAPI.as_view()),
    path('', include(router.urls))
]

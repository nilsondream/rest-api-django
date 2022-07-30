from django.urls import path
from profiles_api import views

urlpatterns = [
    path('helloview/', views.HelloApiView.as_view()),
]
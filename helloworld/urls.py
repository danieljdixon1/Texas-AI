from django.urls import path
from .views import helloView

urlpatterns = [
    path("", helloView, name="home"),
]
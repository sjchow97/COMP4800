from django.urls import path
# from .feeds import RssSource

from . import views

urlpatterns = [
    path("", views.index, name="index"),
  
]
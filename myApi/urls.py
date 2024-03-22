from django.urls import path
from myApi import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data", views.dataBack)
]
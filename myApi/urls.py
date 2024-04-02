from django.urls import path
from myApi import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data", views.dataBack),
    path("lw", views.leaveWord),
    path("gw", views.getWord),
]
from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("bakeshophome", views.bakeshophome),
    path("giftshophome", views.giftshophome),
    path("printshophome", views.printshophome)
]
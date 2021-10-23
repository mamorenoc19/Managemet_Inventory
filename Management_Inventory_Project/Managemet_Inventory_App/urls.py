from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("search/", views.add_product, name="search"),
    path("add/", views.add_product, name="add"),
    path("edit/", views.edit_product, name="edit"),
    path("remove/", views.remove_product, name="remove")
]

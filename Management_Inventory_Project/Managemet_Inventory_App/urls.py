from django.urls import path
from Managemet_Inventory_App.views import home,producto_view,search,add_product,edit_product,remove_product

app_name = 'Managemet_Inventory_App'

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("productos/", views.producto_view, name="productos"),
    path("search/", views.search, name="search"),
    path("add/", views.add_product, name="add"),
    path("edit/", views.edit_product, name="edit"),
    path("remove/", views.remove_product, name="remove")
]

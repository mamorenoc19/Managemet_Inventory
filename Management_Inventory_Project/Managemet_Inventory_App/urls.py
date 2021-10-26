from django.urls import path
from Managemet_Inventory_App.views import home,producto_view,search,add_product,edit_product,remove_product

app_name = 'Managemet_Inventory_App'

urlpatterns = [
    path("home/", home, name = "home"),
    path("productos/", producto_view, name="productos"),
    path("search/", search, name="search"),
    path("add/", add_product, name="add"),
    path("edit/", edit_product, name="edit"),
    path("remove/", remove_product, name="remove")
]

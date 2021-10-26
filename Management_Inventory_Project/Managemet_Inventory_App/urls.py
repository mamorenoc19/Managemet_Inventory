from django.urls import path
from Managemet_Inventory_App.views import home,search,add_product,edit_product,remove_product,inventory

app_name = 'Managemet_Inventory_App'

urlpatterns = [
    path("home/", home, name = "home"),
    path("inventory/",inventory,name = "inventory"),
    path("search/", search, name="search"),
    path("add/", add_product, name="add"),
    path("edit/", edit_product, name="edit"),
    path("remove/", remove_product, name="remove")
]

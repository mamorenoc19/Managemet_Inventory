from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "Managemet_Inventory_App/home.html")

def home(request):
    return render(request, "Managemet_Inventory_App/search.html")

def add_product(request):
    return render(request, "Managemet_Inventory_App/inventory_add.html")

def edit_product(request):
    return render(request, "Managemet_Inventory_App/inventory_edit.html")

def remove_product(request):
    return render(request, "Managemet_Inventory_App/inventory_remove.html")

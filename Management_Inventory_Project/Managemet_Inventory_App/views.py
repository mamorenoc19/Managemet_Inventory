from django.shortcuts import render, redirect
from django.http import HttpResponse
from Managemet_Inventory_App.forms import productoForm

# Create your views here.
def home(request):
    return render(request, "Managemet_Inventory_App/home.html")

def search(request):
    return render(request, "Managemet_Inventory_App/search.html")

def inventory(request):
    return render(request, "Managemet_Inventory_App/inventory.html")

def add_product(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Managemet_Inventory_App:inventory')
    else:
        form = productoForm()
    
    return render(request, "Managemet_Inventory_App/add.html", {'form':form})

def edit_product(request):
    return render(request, "Managemet_Inventory_App/inventory_edit.html")

def remove_product(request):
    return render(request, "Managemet_Inventory_App/inventory_remove.html")
    

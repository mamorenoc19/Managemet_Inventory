from django.shortcuts import render, redirect
from django.http import HttpResponse
from Managemet_Inventory_App.forms import productoForm

# Create your views here.
def home(request):
    return render(request, "Managemet_Inventory_App/home.html")

def producto_view(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Managemet_Inventory_App:productos')
    else:
        form = productoForm()
    
    return render(request, "Managemet_Inventory_App/productos.html", {'form':form})

def home(request):
    return render(request, "Managemet_Inventory_App/search.html")

def add_product(request):
    return render(request, "Managemet_Inventory_App/inventory_add.html")

def edit_product(request):
    return render(request, "Managemet_Inventory_App/inventory_edit.html")

def remove_product(request):
    return render(request, "Managemet_Inventory_App/inventory_remove.html")

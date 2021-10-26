from django import forms
from Managemet_Inventory_App.models import producto

class productoForm(forms.ModelForm):
    
    class Meta:
        
        model = producto
    
        fields = [
            'nombre',
            'categoria',
            'marca',
            'sede',
            'proveedor',
            'cantidad',
        ]

        labels = {
            'nombre':'Nombre',
            'categoria':'Categoria',
            'marca':'Marca',
            'sede':'Sede',
            'proveedor':'Proveedor',
            'cantidad':'Cantidad', 
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'sede':forms.TextInput(attrs={'class':'form-control'}),
            'proveedor':forms.TextInput(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'})
        }

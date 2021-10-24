from django import forms
from Managemet_Inventory_App.models import Producto

class productoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'etiqueta', 'cantidad']
        labels = {'nombre: Nombre', 'etiqueta:Etiqueta', 'cantidad:Cantidad'}
        widgets = {'nombre':forms.TextInput(attrs={'class':'form-control'}),
                   'etuqueta': forms.TextInput(attrs={'class': 'form-control'}),
                   'cantidad': forms.NumberInput(attrs={'class': 'form-control'})
        }


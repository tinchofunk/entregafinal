from django import forms

class ProductosFormulario(forms.Form):
    producto = forms.CharField()
    categoria = forms.CharField()

class ClienteFormulario(forms.Form):
    usuario = forms.CharField()
    fecha_alta = forms.DateField()

class StockFormulario(forms.Form):
    precio = forms.IntegerField()
    codigo = forms.IntegerField()

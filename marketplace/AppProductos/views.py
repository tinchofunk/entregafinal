from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

from AppProductos.models import Productos, Cliente, Stock
from django.core import serializers

from AppProductos.forms import ProductosFormulario
from AppProductos.forms import ClienteFormulario
from AppProductos.forms import StockFormulario

# Create your views here.
# BUSCAR


def buscar(request):  
    Productos_views = request.GET ['producto']
    Productos_todos = Productos.objects.filter(producto = Productos_views)
    return render(request, "AppProductos/resultadoproducto.html", {"producto": Productos_views , "productos": Productos_todos})
def buscarproducto(request):
    return render(request, "AppProductos/buscarproducto.html")

def buscarc(request):
    Usuarios_views = request.GET ['usuario']
    Usuarios_todos = Cliente.objects.filter(usuario = Usuarios_views)
    return render(request, "AppProductos/resultadocliente.html", {"usuario": Usuarios_views , "usuarios": Usuarios_todos})
def buscarcliente(request):
    return render(request, "AppProductos/buscarcliente.html")

def buscars(request):
    Codigos_views = request.GET ['codigo']
    Codigos_todos = Stock.objects.filter(codigo = Codigos_views)
    return render(request, "AppProductos/resultadostock.html", {"codigo": Codigos_views , "codigos": Codigos_todos})
def buscarstock(request):
    return render(request, "AppProductos/buscarstock.html")

def inicio(request):
    return render(request, "AppProductos/inicio.html")


def productos(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            productos = Productos(
                producto=informacion["producto"], categoria=informacion["categoria"])
            productos.save()
            return render(request, "AppProductos/productos_list.html")
    else:
        miFormulario = ProductosFormulario()

    return render(request, "AppProductos/productos.html", {"miFormulario": miFormulario})


def cliente(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)
            usuario = Cliente(
                usuario=informacion["usuario"], fecha_alta=informacion["fecha_alta"])
            usuario.save()
            return render(request, "AppProductos/inicio.html")
    else:
        miFormulario = ClienteFormulario()

    return render(request, "AppProductos/cliente.html", {"miFormulario": miFormulario})


def stock(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = StockFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)
            precio = Stock(
                precio=informacion["precio"], codigo=informacion["codigo"])
            precio.save()
            return render(request, "AppProductos/inicio.html")
    else:
        miFormulario = StockFormulario()

    return render(request, "AppProductos/stock.html", {"miFormulario": miFormulario})


def productosapi(request):
    productos_todos = Productos.objects.all()
    return HttpResponse(serializers.serialize("json", productos_todos))


def leer_producto(request):
    producto = Productos.objects.all()
    return HttpResponse(serializers.serialize('json', producto))


def leer_cliente(request):
    cliente = Cliente.objects.all()
    return HttpResponse(serializers.serialize('json', cliente))


def leer_stock(request):
    stock = Stock.objects.all()
    return HttpResponse(serializers.serialize('json', stock))


def crear_producto(request):
    productos = Productos(id=5, producto='LedHd', categoria='Tv_Lcd')
    productos.save()
    return HttpResponse(f'El producto  {productos.producto} ah sido creado')


def crear_cliente(request):
    cliente = Cliente(id=5, usuario='Fravega', fecha_alta="1881-10-25")
    cliente.save()
    return HttpResponse(f'EL cliente {cliente.usuario} ah sido creado')


def crear_stock(request):
    stock = Stock(id='125', precio=10000, codigo=15)
    stock.save()
    return HttpResponse(f'El Numero  {stock.codigo} del stock ah sido creado')

# Editar#


def editar_producto(request):
    nombre_consulta = 'LedHd'
    Productos.objects.filter(producto=nombre_consulta).update(
        producto='Led 60 pulgaras')
    return HttpResponse(f'EL producto {nombre_consulta} ah sido modificado')


def editar_cliente(request):
    nombre_consulta = 'Fravega'
    Cliente.objects.filter(usuario=nombre_consulta).update(usuario='Musimundo')
    return HttpResponse(f'el cliente {nombre_consulta} ah sido modificado')


def editar_Stock(request):
    nombre_consulta = 15
    Stock.objects.filter(codigo=nombre_consulta).update(codigo=20)
    return HttpResponse(f'el numero  {nombre_consulta} del stock ah sido modificado')

# Eliminar


def eliminar_producto(request):
    producto = 'LedHd'
    producto_d = Productos.objects.get(producto=producto)
    producto_d.delete()
    return HttpResponse(f'El producto {producto} ah sido eliminado')


def eliminar_cliente(request):
    nombre_nuevo = 'Musimundo'
    cliente = Cliente.objects.get(usuario=nombre_nuevo)
    cliente.delete()
    return HttpResponse(f'EL cliente {nombre_nuevo} ah sido eliminado')


def eliminar_stock(request):
    nombre_nuevo = 20
    stock = Stock.objects.get(codigo = nombre_nuevo)
    stock.delete()
    return HttpResponse(f'El numero {nombre_nuevo} del codigo ah sido eliminado')


# Class


class ProductosList(ListView):
    model = Productos
    template_name = "AppProductos/productos_list.html"


class ClienteList(ListView):
    model = Cliente
    template_name = "AppProductos/cliente_list.html"


class StockList(ListView):
    model = Stock
    template_name = "AppProductos/stock_list.html"


# Class Create

class ProductosCreate(CreateView):
    model = Productos
    fields = '__all__'
    success_url = "/productos/list/"


class Clientecreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = "/cliente/list/"


class Stockcreate(CreateView):
    model = Stock
    fields = '__all__'
    success_url = "/stock/list/"

# Class edit


class ProductoEdit(UpdateView):
    model = Productos
    fields = '__all__'
    success_url = '/productos/list'


class ClienteEdit(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = '/cliente/list'


class StockEdit(UpdateView):
    model = Stock
    fields = '__all__'
    success_url = '/stock/list'


# Detalle


class ProductoDetail(DetailView):
    model = Productos
    template_name = "AppProductos/productos_detail.html"


class ClienteDetail(DetailView):
    model = Cliente
    template_name = "AppProductos/cliente_detail.html"


class StockDetail(DetailView):
    model = Stock
    template_name = "AppProductos/stock_detail.html"


# Borrar
class ProductoDelete(DeleteView):
    model = Productos
    #fields= '__all__'
    success_url = '/productos/list'


class ClienteDelete(DeleteView):
    model = Cliente
    #fields= '__all__'
    success_url = '/cliente/list'


class StockDelete(DeleteView):
    model = Stock
    #fields= '__all__'
    success_url = '/stock/list'

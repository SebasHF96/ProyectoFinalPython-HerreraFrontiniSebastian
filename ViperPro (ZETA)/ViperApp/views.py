from django.shortcuts import render, redirect
from django.http import HttpResponse
from ViperApp.models import Usuario, Producto, Proveedor
from ViperApp.forms import UsuarioForm, ProductoForm, ProveedorForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "ViperApp/inicio.html")

#LOGIN------------------------------------------------------------
def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
           usuario = form.cleaned_data.get("username")
           contra = form.cleaned_data.get("password")
           user = authenticate(username=usuario, password=contra)
           if user:
               login(request, user)
               return render(request, "ViperApp/inicio.html", {"mensaje":f"Bienvenido {user}"})
        else:
            return render(request, "ViperApp/login_error.html")
    else:
        form = AuthenticationForm()
    return render(request, "ViperApp/login.html", {"formulario":form})

#LOGIN ERROR
def inicioError(request):
    return render(request, "ViperApp/login.html")

#LOGOUT------------------------------------------------------------
@login_required
def cerrarSesion(request):
    logout(request)
    return render(request, "ViperApp/logout.html")

#REGISTRO---------------------------------------------------------
def registro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "ViperApp/inicio.html", {"mensaje":"Usuario Creado"})
    else:
        form = UsuarioForm()
    return render(request, "ViperApp/registro.html", {"formulario":form})


#FUNCIONALES------------------------------------------------------
def carrito(request):
    return render(request, "ViperApp/carrito.html")

def nosotros(request):
    return render(request, "ViperApp/nosotros.html")

def buscarProducto(request):
    return render(request, "ViperApp/buscar_producto.html")

def resultado(request):
    if request.GET["producto"]:
       producto = request.GET["producto"]
       resultado = Producto.objects.filter(nombre__iexact=producto)
       return render(request, "ViperApp/resultado.html", {"resultado":resultado})
    else:
       respuesta = "No se enciaron los datos."
    return HttpResponse(respuesta)

#LISTAS DE CONSULTAS----------------------------------------------
def usuario(request):   
    return render(request, "ViperApp/usuarios.html")

def producto(request):    
    return render(request, "ViperApp/productos.html")

def proveedor(request):    
    return render(request, "ViperApp/proveedores.html")

#CRUDS------------------------------------------------------------
def listaUsuario(request):
    usuarios = Usuario.objects.all()
    contexto = {"user": usuarios}
    return render(request, "ViperApp/lista_usuarios.html", contexto)

def listaProducto(request):
    productos = Producto.objects.all() 
    contexto = {"products": productos}
    return render(request, "ViperApp/lista_productos.html", contexto)

def listaProveedor(request):    
    proveedores = Proveedor.objects.all()
    contexto = {"proveedor": proveedores}
    return render(request, "ViperApp/lista_proveedores.html", contexto)

#ALTA----------------------------------------------
#ALTA USUARIO:
@login_required
def usuarioForm(request):
    if request.method == "POST":
        formularioUser = UsuarioForm(request.POST)
        if formularioUser.is_valid():
            info = formularioUser.cleaned_data
            usuario = Usuario(user=info["user"], password=info["password"], email=info["email"],)
            usuario.save()
            return render(request, "ViperApp/alta_exitosa.html")
    else:
        formularioUser = UsuarioForm()
    return render(request, "ViperApp/alta_usuario.html", {"formUser":formularioUser}) 

#ALTA PRODUCTO:
@login_required
def productoForm(request):
    if request.method == "POST":
        formularioProd = ProductoForm(request.POST)
        if formularioProd.is_valid():
            info = formularioProd.cleaned_data
            producto = Producto(nombre=info["nombre"], sku=info["sku"], 
                            marca=info["marca"], descripcion=info["descripcion"], 
                            precio=info["precio"], imagen=info["imagen"])
            producto.save()
            return render(request, "ViperApp/alta_exitosa.html")
    else:
        formularioProd = ProductoForm()
    return render(request, "ViperApp/alta_producto.html", {"formProd":formularioProd})


#ALTA PROVEEDOR:
@login_required
def proveedorForm(request):
    if request.method == "POST":
        formularioProv = ProveedorForm(request.POST)
        if formularioProv.is_valid():
            info = formularioProv.cleaned_data
            proveedor = Proveedor(nombre=info["nombre"], direccion=info["direccion"], email=info["email"],)
            proveedor.save()
            return render(request, "ViperApp/alta_exitosa.html")
    else:
        formularioProv = ProveedorForm()
    return render(request, "ViperApp/alta_proveedor.html", {"formProv":formularioProv}) 
    
#BAJA-----------------------------------------------
#BAJA USUARIO:
@login_required
def bajaUsuario(request, nombreUsuario):
    usuario = Usuario.objects.get(user=nombreUsuario)
    usuario.delete()
    usuarios = Usuario.objects.all()
    contexto = {"user":usuarios}
    return render(request, "ViperApp/lista_usuarios.html", contexto)

#BAJA PRODUCTO:
@login_required
def bajaProducto(request, nombreProducto):
    producto = Producto.objects.get(nombre=nombreProducto)
    producto.delete()
    productos = Producto.objects.all()
    contexto = {"user":productos}
    return render(request, "ViperApp/lista_productos.html", contexto)

#BAJA PROVEEDOR:
@login_required
def bajaProveedor(request, nombreProveedor):
    proveedor = Proveedor.objects.get(nombre=nombreProveedor)
    proveedor.delete()
    proveedores = Proveedor.objects.all()
    contexto = {"proveedor":proveedores}
    return render(request, "ViperApp/lista_proveedores.html", contexto)

#MODIFICACION----------------------------------------
#MODIFICAR USUARIO:
@login_required
def modificaUsuario(request, nombreUsuario):
    usuario = Usuario.objects.get(user=nombreUsuario)
    if request.method == "POST":
        formularioUser = UsuarioForm(request.POST)
        if formularioUser.is_valid():
            info = formularioUser.cleaned_data
            usuario.user = info["user"]
            usuario.password = info["password"]
            usuario.email = info["email"]
            usuario.save()
            return render(request, "ViperApp/alta_exitosa.html")
    else:
        formularioUser = UsuarioForm(initial={"user":usuario.user,"password":usuario.password, "email":usuario.email})
    return render(request, "ViperApp/modifica_usuario.html", {"formUser":formularioUser, "user":nombreUsuario})

#MODIFICAR PRODUCTO:
@login_required
def modificaProducto(request, nombreProducto):
    producto = Producto.objects.get(nombre=nombreProducto)
    if request.method == "POST":
        formularioProd = ProductoForm(request.POST)
        if formularioProd.is_valid():
            info = formularioProd.cleaned_data
            producto.nombre = info["nombre"]
            producto.sku = info["sku"]
            producto.marca = info["marca"]
            producto.descripcion = info["descripcion"]
            producto.precio = info["precio"]
            producto.imagen = info["imagen"]
            producto.save()
            return render(request, "ViperApp/alta_exitosa.html")
    else:
        formularioProd = ProductoForm(initial={"nombre":producto.nombre,"sku":producto.sku,"marca":producto.marca,
                                               "descripcion":producto.descripcion,"precio":producto.precio,"imagen":producto.imagen })
    return render(request, "ViperApp/modifica_producto.html", {"formProd":formularioProd, "nombre":nombreProducto})

#MODIFICAR PROVEEDOR:
@login_required
def modificaProveedor(request, nombreProveedor):
    proveedor = Proveedor.objects.get(nombre=nombreProveedor)
    if request.method == "POST":
        formularioProv = ProveedorForm(request.POST)
        if formularioProv.is_valid():
            info = formularioProv.cleaned_data
            proveedor.nombre = info["nombre"]
            proveedor.direccion = info["direccion"]
            proveedor.email = info["email"]
            proveedor.save()
            return render(request, "ViperApp/alta_exitosa.html")
    else:
        formularioProv = ProveedorForm(initial={"nombre":proveedor.nombre,"direccion":proveedor.direccion,"email":proveedor.email})
    return render(request, "ViperApp/modifica_proveedor.html", {"formProv":formularioProv, "nombre":nombreProveedor}) 
    


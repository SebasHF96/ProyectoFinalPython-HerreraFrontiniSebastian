from django.urls import path
from ViperApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', inicioSesion, name="Login"),
    path('logout/', cerrarSesion, name="Logout"),
    path('registro/', registro, name="Registro"),
    path('login_error/', inicioError, name="Login_Error"),
    path('usuarios/', usuario, name="Usuarios"),
    path('productos/', producto, name="Productos"),
    path('proveedores/', proveedor, name="Proveedores"),    
    path('alta_usuario/', usuarioForm, name="Alta_Usuarios"),
    path('alta_producto/', productoForm, name="Alta_Productos"),
    path('alta_proveedor/', proveedorForm, name="Alta_Proveedores"),
    path('carrito/', carrito, name="Carrito"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('buscar_producto/', buscarProducto, name="Buscar_Producto"),
    path('resultado/', resultado, name="Resultados"),
    path('lista_productos/', listaProducto, name="Lista_Productos"),
    path('lista_usuarios/', listaUsuario, name="Lista_Usuarios"),
    path('lista_proveedores/', listaProveedor, name="Lista_Proveedores"),
    path('baja_usuario/<nombreUsuario>', bajaUsuario, name="Baja_Usuarios"),
    path('baja_producto/<nombreProducto>', bajaProducto, name="Baja_Productos"),
    path('baja_proveedor/<nombreProveedor>', bajaProveedor, name="Baja_Proveedores"),
    path('modifica_usuario/<nombreUsuario>', modificaUsuario, name="Modifica_Usuarios"),
    path('modifica_producto/<nombreProducto>', modificaProducto, name="Modifica_Productos"),
    path('modifica_proveedor/<nombreProveedor>', modificaProveedor, name="Modifica_Proveedores"),

]
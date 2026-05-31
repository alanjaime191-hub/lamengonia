#main file
import random
from files import Utils
from files.Zonas import bosque
from files import Users

nombre = input("Ingrese su nombre de usuario: ") #logica de usuarios
usuario = Users.cargar_usuario(nombre)

while True:
    eleccion = input("Tome una opcion\n" #prueba crota de exploracion/inv/crafteos y caliadades en proceso
    "1) ingresar a madera1 \n"
    "2) ingresar a madera2 \n"
    "3) mirar el inventario")
    if eleccion == "1":
        drop = Utils.explorar(bosque["bosque1"]) #devuelve drop madera1
        Utils.agregar_item(usuario, drop, random.randint(1, 3))
    elif eleccion == "2":
        Utils.explorar(bosque["bosque2"]) #devuelve drop madera2
        Utils.agregar_item(usuario,drop,random.randint(1, 3))
    elif eleccion == "3":
        Utils.mostrar_inv(usuario)
    else:
        print("No implementado")
    Users.guardar_usuario(usuario)
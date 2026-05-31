#main file
import random
from files import Utils
from files.Zonas import zonas
from files import Users

nombre = input("Ingrese su nombre de usuario: ") #logica de usuarios
usuario = Users.cargar_usuario(nombre)

while True:
    tipo, dato = Utils.menu() #da el menu de opciones segun files.zonas y agrega acciones tipo inventario y crafteos
    if tipo == "zona":
        item = Utils.explorar(zonas[dato])
        Utils.agregar_item(usuario, item, random.randint(1,3) )

    elif tipo == "inventario":
        Utils.mostrar_inv(usuario)

    elif tipo == "crafteo":
        print("No implementado")
    
    Users.guardar_usuario(usuario)

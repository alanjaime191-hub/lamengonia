import random
from files.Items import items
from files import Zonas

ORDEN_CATEGORIAS = [
    "Material",
    "Comida",
    "Herramienta"
]

def explorar(zona):
    drop_id = random.choice(zona["drops"])
    item = items[drop_id]
    print(f"Encontraste {item['nombre']}")

    return drop_id


def mostrar_inv(usuario):

    categorias = {}

    for clave, cantidad in usuario["inventario"].items():

        item_id, calidad = clave.rsplit("_", 1)

        categoria = items[item_id]["tipo"]

        if categoria not in categorias:
            categorias[categoria] = []

        categorias[categoria].append(
            (item_id, calidad, cantidad)
        )

    for categoria in categorias:

        print(f"\n=== {categoria} ===")

        lista = sorted(
        categorias[categoria],
        key=lambda x: (
        int(x[1]),
        items[x[0]]["nombre"]
        ))

        for item_id, calidad, cantidad in lista:

            print(
                f"{items[item_id]['nombre']} "
                f"(calidad {calidad}) "
                f"x{cantidad}"
            )

def agregar_item(usuario, item_id, calidad, cantidad=1):
    clave = f"{item_id}_{calidad}"

    if clave not in usuario["inventario"]:
        usuario["inventario"][clave] = 0

    usuario["inventario"][clave] += cantidad

def menu():
    
    opciones = list(Zonas.zonas.keys())

    for i, zona_id in enumerate(opciones, start=1):

        print(f"{i}) {Zonas.zonas[zona_id]['nombre']}")

    print(f"{len(opciones)+1}) Ver inventario")
    print(f"{len(opciones)+2}) Crafteo")
    try:
        eleccion = int(input("Opción: "))

        if 1 <= eleccion <= len(opciones):
            return ("zona", opciones[eleccion-1])

        elif eleccion == len(opciones)+1:
            return ("inventario", None)

        elif eleccion == len(opciones)+2:
            return ("crafteo", None)

        return ("error", None)
    
    except: 
        print("Donde eso fue una opcion???? panflin")
        input("(enter para re lanzar el menu)\n")
        return(None, None)
    

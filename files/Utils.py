import random
from files.Items import items

def explorar(zona):
    drop_id = random.choice(zona["drops"])
    item = items[drop_id]
    print(f"Encontraste {item['nombre']}")

    return drop_id

def mostrar_inv(usuario):

    for clave, cantidad in usuario["inventario"].items():

        item_id, calidad = clave.rsplit("_", 1)

        nombre = items[item_id]["nombre"]

        print(
            f"{nombre} (calidad {calidad}) x{cantidad}"
        )

def agregar_item(usuario, item_id, calidad, cantidad=1):
    clave = f"{item_id}_{calidad}"

    if clave not in usuario["inventario"]:
        usuario["inventario"][clave] = 0

    usuario["inventario"][clave] += cantidad
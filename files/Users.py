#para guardar users
#files.user
# User.py

import json
import os

def crear_usuario(nombre):

    return {
        "nombre": nombre,

        "inventario": {
        },
        "habilidades": {
            "exploracion": 1,
            "carpinteria": 1,
            "mineria": 1
        },
        "experiencia": {
            "xp_exploracion": 0,
            "xp_carpinteria": 0,
            "xp_mineria": 0
        }
    }

def guardar_usuario(usuario):

    ruta = f"saves/{usuario['nombre']}.json"

    with open(ruta, "w") as f:
        json.dump(usuario, f, indent=4)

def cargar_usuario(nombre):

    ruta = f"saves/{nombre}.json"

    if os.path.exists(ruta):

        with open(ruta, "r") as f:
            return json.load(f)

    usuario = crear_usuario(nombre)

    guardar_usuario(usuario)

    return usuario


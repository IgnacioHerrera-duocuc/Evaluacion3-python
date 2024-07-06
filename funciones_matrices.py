#funciones matrices#
import numpy as np
import json
import os


def cargar_datos():
    try:
        with open('mascotas.json', 'r') as file:
            data = json.load(file)
            mascotas = np.array(data)
    except FileNotFoundError:
        mascotas = np.empty((0, 8), dtype=object)
    return mascotas

def guardar_datos(mascotas):
    with open('mascotas.json', 'w') as file:
        json.dump(mascotas.tolist(), file)

def ingresar_ficha():
    nombre_mascota = input("Nombre de la mascota: ")
    codigo_mascota = input("codigo de la mascota: ")
    edad_mascota = input("Edad de la mascota: ")
    peso_mascota = input("edad de la mascota: ")
    raza_mascota = input("raza de la mascota: ")
    especie_mascota = input("especie de la mascota: ")
    diagnostico_mascota = input("diagnostico para la mascota: ")
    medicamentos_mascota = input("Medicamentos para la mascota")

    nueva_ficha = np.array([[nombre_mascota, codigo_mascota, edad_mascota, peso_mascota, raza_mascota, especie_mascota, medicamentos_mascota, diagnostico_mascota]])
    return nueva_ficha

def buscar_por_codigo(mascotas, codigo_mascota):
    mascotas_encontrado = None
    for mascotas in mascotas:
        if mascotas[1] == codigo_mascota:
            mascotas_encontrado = mascotas
            break
    return mascotas_encontrado


def eliminar_ficha(mascotas, codigo_mascota):
    mascotas_actualizados = [mascotas for mascotas in mascotas if mascotas[1] != codigo_mascota]
    return np.array(mascotas_actualizados)

def listar_mascotas(mascotas):
    for i, mascotas in enumerate(mascotas, start=1):
        print(f"mascotas {i}:")
        print(f"Nombre: {mascotas[0]}")
        print(f"Codigo mascota: {mascotas[1]}")
        print(f"Edad: {mascotas[2]}")
        print(f"peso: {mascotas[3]}")
        print(f"Raza: {mascotas[4]}")
        print(f"Especie : {mascotas[5]}")
        print(f"diagnostico mascota: {mascotas[6]}")
        print(f"medicamentos recetados: {mascotas[7]}")

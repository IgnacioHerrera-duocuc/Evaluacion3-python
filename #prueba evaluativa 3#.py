#prueba3#
import numpy as np
from funciones_matrices import cargar_datos, guardar_datos, ingresar_ficha, buscar_por_codigo, eliminar_ficha, listar_mascotas

listado_mascotas = cargar_datos()

while True:
    print("Menú:")
    print("1. Crear ficha mascota")
    print("2. Buscar por codigo de mascota")
    print("3. Eliminar por codigo de mascota")
    print("4. Listar mascotas")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción deseada (1-5): ")
    if opcion == '1':
        nueva_ficha = ingresar_ficha()
        listado_mascotas = np.concatenate((listado_mascotas, nueva_ficha), axis=0)
        print("¡Ficha ingresada correctamente!")
    elif opcion == '2':
        codigo_mascota = input("Ingrese el codigo de la mascota a buscar: ")
        mascotas_encontrado = buscar_por_codigo(listado_mascotas, codigo_mascota)
        if mascotas_encontrado is not None:
            print("Paciente encontrado:")
            print(f"Nombre: {mascotas_encontrado[0]}")
            print(f"codigo: {mascotas_encontrado[1]}")
            print(f"edad: {mascotas_encontrado[2]}")
            print(f"peso: {mascotas_encontrado[3]}")
            print(f"raza: {mascotas_encontrado[4]}")
            print(f"especie: {mascotas_encontrado[5]}")
            print(f"diagnostico mascota: {mascotas_encontrado[6]}")
            print(f"medicamentos recetados {mascotas_encontrado[7]}")
        else:
            print("No se encontró ningúna mascota con ese codigo.")
    elif opcion == '3':
        rut = input("Ingrese el codigo de la ficha a eliminar: ")
        listado_mascotas = eliminar_ficha(listado_mascotas, codigo_mascota)
        print("Ficha eliminada correctamente.")  
    elif opcion == '4':
        if len(listado_mascotas) > 0:
            print("Listado de mascotas atendidas:")
            listar_mascotas(listado_mascotas)
        else:
            print("No hay mascotas registradas.")    
    elif opcion == '5':
        guardar_datos(listado_mascotas)
        break          

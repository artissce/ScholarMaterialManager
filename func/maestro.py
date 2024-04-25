from colorama import init, Fore, Style
import json

# Función para imprimir mensajes con color
def imprimir_mensaje(mensaje, color=Fore.WHITE):
  print(color + mensaje + Style.RESET_ALL)

# Función para cargar los datos de maestros desde el archivo JSON
def cargar_maestros():
    try:
        with open('./jsons/maestros.json', 'r') as file:
            maestros_data = json.load(file)
        return maestros_data
    except FileNotFoundError:
        return []

# Función para guardar los datos de maestros en el archivo JSON
def guardar_maestros(maestros_data):
    with open('./jsons/maestros.json', 'w') as file:
        json.dump(maestros_data, file, indent=4)

# Función para agregar un nuevo maestro
def agregar_maestro():
    nombre = input("Ingrese el nombre del maestro: ")
    ubicacion = input("Ingrese la ubicación del maestro: ")
    maestros_data = cargar_maestros()
    nuevo_maestro = {
        "id": len(maestros_data) + 1,
        "maestro": nombre,
        "ubicacion": ubicacion
    }
    maestros_data.append(nuevo_maestro)
    guardar_maestros(maestros_data)
    print("Maestro agregado correctamente.")

# Función para mostrar la lista de maestros
def mostrar_maestros():
    maestros_data = cargar_maestros()
    if maestros_data:
        print("Lista de maestros:")
        for maestro in maestros_data:
            print(f"ID: {maestro['id']}, Nombre: {maestro['maestro']}, Ubicación: {maestro['ubicacion']}")
    else:
        print("No hay maestros en la lista.")

# Función para actualizar la información de un maestro
def actualizar_maestro():
    maestros_data = cargar_maestros()
    if maestros_data:
        id_maestro = int(input("Ingrese el ID del maestro a actualizar: "))
        for maestro in maestros_data:
            if maestro['id'] == id_maestro:
                nuevo_nombre = input("Ingrese el nuevo nombre del maestro: ")
                nueva_ubicacion = input("Ingrese la nueva ubicación del maestro: ")
                maestro['maestro'] = nuevo_nombre
                maestro['ubicacion'] = nueva_ubicacion
                guardar_maestros(maestros_data)
                print("Información del maestro actualizada correctamente.")
                break
        else:
            print("ID de maestro no encontrado.")
    else:
        print("No hay maestros en la lista.")

# Función para eliminar un maestro
def eliminar_maestro():
    maestros_data = cargar_maestros()
    if maestros_data:
        id_maestro = int(input("Ingrese el ID del maestro a eliminar: "))
        for maestro in maestros_data:
            if maestro['id'] == id_maestro:
                maestros_data.remove(maestro)
                guardar_maestros(maestros_data)
                print("Maestro eliminado correctamente.")
                break
        else:
            print("ID de maestro no encontrado.")
    else:
        print("No hay maestros en la lista.")

# Función principal
def menuM():
    while True:
        print("\n1. Agregar maestro")
        print("2. Mostrar maestros")
        print("3. Actualizar maestro")
        print("4. Eliminar maestro")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_maestro()
        elif opcion == '2':
            mostrar_maestros()
        elif opcion == '3':
            actualizar_maestro()
        elif opcion == '4':
            eliminar_maestro()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

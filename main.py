import json
from datetime import datetime
from colorama import init, Fore, Style


# Función para imprimir mensajes con color
def imprimir_mensaje(mensaje, color=Fore.WHITE):
  print(color + mensaje + Style.RESET_ALL)


# Función para cargar los datos del archivo JSON, LEER
def cargar_datos():
  try:
    with open('./jsons/materials.json', 'r') as file:
      data = json.load(file)
    return data
  except FileNotFoundError:
    return []


# Función para guardar los datos en el archivo JSON
def guardar_datos(data):
  with open('./jsons/materials.json',
            'w') as file:  #el with asegura que se cierre el archivo
    json.dump(data, file, indent=4)  #indent es la sangria


# Función para dar de ALTA un nuevo material
def agregar_material():
  nombre = input("Ingrese el nombre del material: ")
  #estado = input("Ingrese el estado del material: 0-libre 1-ocupado ")
  data = cargar_datos()  #ubicacion,maestro,fecha,hora,fecha
  nuevo_material = {
      "id": len(data) + 1,
      "nombre": nombre,
      "estado": 0,
      "ubicacion": "",
      "maestro": "",
      "fecha_hora_asignacion": ""
  }
  data.append(nuevo_material)
  guardar_datos(data)
  print("material agregado correctamente.")


# Función para mostrar la lista de materials
def mostrar_materials():
  data = cargar_datos()
  if data:
    print("Lista de materials:")
    for material in data:
      if material['estado'] == 0:
        info1 = "Sin asignar"
        info2 = "Sin asignar"
      else:
        info1 = material['ubicacion']
        info2 = material['maestro']
      print(
          f"ID: {material['id']}, Nombre: {material['nombre']}, Estado: {material['estado']}, Ubicacion: {info1}, Maestro: {info2}, Fecha: {material['fecha_hora_asignacion']}"
      )
  else:
    print("No hay materials en la lista.")


# Función para asignar material a un maestro
def asignar_material():
  # Cargar los datos de los maestros desde el archivo "maestros.json"
  try:
    with open('maestros.json', 'r') as maestros_file:
      maestros_data = json.load(maestros_file)
  except FileNotFoundError:
    imprimir_mensaje("Error: No se encontró el archivo de maestros.", Fore.RED)
    return

  # Mostrar la lista de maestros disponibles
  imprimir_mensaje("Lista de maestros disponibles:", Fore.GREEN)
  for maestro in maestros_data:
    print(f"ID: {maestro['id']}, Nombre: {maestro['maestro']}")

  # Solicitar al usuario que seleccione un maestro
  try:
    maestro_id = int(
        input("Ingrese el ID del maestro al cual asignar el material: "))
  except ValueError:
    imprimir_mensaje(
        "Error: Por favor ingrese un número entero para el ID del maestro.",
        Fore.RED)
    return

  # Verificar que el ID del maestro ingresado sea válido
  maestro_encontrado = False
  maestro_ubicacion = ""  # Variable para almacenar la ubicación del maestro
  for maestro in maestros_data:
    if maestro['id'] == maestro_id:
      maestro_encontrado = True
      maestro_ubicacion = maestro[
          'ubicacion']  # Obtener la ubicación del maestro
      break

  if not maestro_encontrado:
    print("Error: ID de maestro no válido.")
    return

  # Cargar los datos de los materiales desde el archivo "materials.json"
  data = cargar_datos()

  # Mostrar la lista de materials disponibles para asignar
  print("Lista de materials disponibles para asignar:")
  for material in data:
    if material['estado'] == 0:
      print(f"ID: {material['id']}, Nombre: {material['nombre']}")

  # Solicitar al usuario que seleccione un material para asignar al maestro
  material_id = input("Ingrese el ID del material a asignar: ")
  material_id = int(material_id)

  # Verificar que el ID del material ingresado sea válido y que esté libre
  material_encontrado = False
  for material in data:
    if material['id'] == material_id and material['estado'] == 0:
      material_encontrado = True
      material['maestro'] = maestro_id  # Asignar el ID del maestro al material
      material['estado'] = 1  # Cambiar el estado del material a "ocupado"
      material[
          'ubicacion'] = maestro_ubicacion  # Asignar la ubicación del maestro al material
      # Obtener la fecha y hora actual
      ahora = datetime.now()
      fecha_hora_asignacion = ahora.strftime("%Y-%m-%d %H:%M:%S")
      material[
          'fecha_hora_asignacion'] = fecha_hora_asignacion  # Agregar fecha y hora de asignación

      print("Material asignado correctamente.")
      break

  if not material_encontrado:
    print("Error: ID de material no válido o material ya asignado.")

  # Guardar los cambios en el archivo "materials.json"
  guardar_datos(data)


#Funcion para liberar
def liberar_material():
  # Cargar los datos de los materiales desde el archivo "materials.json"
  data = cargar_datos()
  # Mostrar la lista de materials disponibles para asignar
  imprimir_mensaje("Lista de materials para liberar:", Fore.GREEN)
  for material in data:
    if material['estado'] == 1:
      print(f"ID: {material['id']}, Nombre: {material['nombre']}")
  # Solicitar al usuario que seleccione un material para liberar
  material_Id = int(input("Ingrese el ID del material a liberar: "))
  material_encontrado = False
  for material in data:
    if material['id'] == material_Id and material['estado'] == 1:
      material_encontrado = True
      material['estado'] = 0
      material['ubicacion'] = ""
      material['maestro'] = ""
      material['fecha_hora_asignacion'] = ""
      imprimir_mensaje("Material liberado correctamente.", Fore.GREEN)
      break
  if not material_encontrado:
    imprimir_mensaje("Error: ID de material no válido o material no asignado.",
                     Fore.RED)
  guardar_datos(data)


# Función principal
def main():
  while True:
    imprimir_mensaje("\tMENU", Fore.GREEN)
    print("\n1. Agregar material")
    print("2. Mostrar materials")
    print("3. Asignar materials")
    print("4. Liberar material")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
      agregar_material()
    elif opcion == '2':
      mostrar_materials()
    elif opcion == '3':
      asignar_material()
    elif opcion == '4':
      print("Pendiente2")
    elif opcion == '0':
      print("¡Hasta luego!")
      break
    else:
      print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
  main()

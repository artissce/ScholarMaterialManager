from colorama import init, Fore, Style
#este es la conexion entre maestro y producto

# Función para imprimir mensajes con color
def imprimir_mensaje(mensaje, color=Fore.WHITE):
  print(color + mensaje + Style.RESET_ALL)
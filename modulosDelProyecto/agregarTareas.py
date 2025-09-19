import os
from datetime import date,datetime
from datosTareas import pedirFechaDeVencimiento, pedirPrioridad
import time
from animaciones import animacionAgregandoTarea
from colorama import Fore,Style
ly = Fore.LIGHTYELLOW_EX
sb = Style.BRIGHT
sr = Style.RESET_ALL

# ********************** Crea un archivo texto con los datos de la tarea agregada ***********************
# *******************************************************************************************************

def agregarTarea():
    time.sleep(0.4) # Espera 0.4 segundos para continuar.
    os.system("clear") # Limpia la pantalla.
    print(f"{sb}{ly}{' Agregar tarea ':*^50}{sr}\n")
    titulo:str = input("Título de la tarea:\n> ")
    descripcion:str = input("Descripción:\n> ")
    fechaDeVencimiento = pedirFechaDeVencimiento()
    prioridad:str = pedirPrioridad()
    categoria:str = input("Categoría (Personal, Trabajo, Mantenimiento, etc): \n> ")
    responsable:str = input("Responsable: \n> ")

    id = 1

    while True:
        try:
            with open(f"Tarea_{id}.txt","x") as tarea: # Crea el archivo Tarea_1..2..3... si no existe.
                tarea.write("------------------------------------------------------------------\n")
                tarea.write(f"| {' ':<63}|\n")
                tarea.write(f"| {'Título:':<15} {titulo:<47}|\n")
                tarea.write(f"| {'Descripción:':<15} {descripcion:<47}|\n")
                tarea.write(f"| {'ID:':<15} {id:<47}|\n")
                tarea.write(f"| {'Fecha límite:':<15} {fechaDeVencimiento:<47}|\n")
                tarea.write(f"| {'Prioridad:':<15} {prioridad:<47}|\n")
                tarea.write(f"| {'Categoría:':<15} {categoria:<47}|\n")
                tarea.write(f"| {'Responsable:':<15} {responsable:<47}|\n")
                estado:str = estadoDeLaTarea(fechaDeVencimiento)
                tarea.write(f"| {'Estado:':<15} {estado:<47}|\n")
                tarea.write(f"| {' ':<63}|\n")
                tarea.write("------------------------------------------------------------------")
        except FileExistsError:
            id += 1 # Si el archivo Tarea_1..2..3.. existe, aumenta +1 ID
            continue
        break
    animacionAgregandoTarea()
    print("\nTarea agregada exitosamente.")
    print(f"\n{sb}{ly}{'':*^50}{sr}")
    continuar = input("\nPresione una tecla para continuar.")


# ****************************    Define el estado de la tarea    ***********************************
# ***************************************************************************************************


#Esta funcion recibe una fecha tipo str y compara si la fecha recibida es mayor o menor que la fecha actual
#para definir el estado de la tarea.

def estadoDeLaTarea(fechaDeVencimiento:str)-> str:
    fecha:object = datetime.strptime(fechaDeVencimiento,"%d/%m/%Y").date()
    fechaActual:object = date.today() # Fecha actual.
    return "En proceso" if fecha >= fechaActual else "Vencida"  
    # Devuelve "En proceso" si la fecha recibida es mayor o igual a la fecha actual y "vencida" si es menor.
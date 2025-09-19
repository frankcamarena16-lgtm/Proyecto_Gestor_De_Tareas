import os
from datetime import datetime,date

# ************* Recorre todos los archivos del directorio y cuanta solo las tareas ***********************
# ********************************************************************************************************

def cantidadTotalDeTareas()-> int:
    contador = 0

    listaDeArchivos = os.listdir() # Hace una lista con los nombres de todos los archivos. 

    for archivo in listaDeArchivos: # Recorre todos los archivos. 
        if archivo.startswith("Tarea_"): # Si el nombre del archivo empieza con "Tarea_".
            contador += 1
    return contador

# ************** Recorre todos los archivos del directorio y cuenta solo las tareas vencidas *************
# ********************************************************************************************************

def cantidadTareasVencidas()-> int:
    contador = 0
    estado = "Vencida"

    listaDeArchivos = os.listdir() # Hace una lista con los nombres de todos los archivos.

    for archivo in listaDeArchivos: # Recorre todos los archivos. 
        if archivo.startswith("Tarea_"):
            with open(archivo,"r") as t:
                contenido = t.read()
            if f"| {'Estado:':<15} {estado:<47}|\n" in contenido: # Si el estado de la tarea es "Vencida" contador +1.
                contador += 1

    return contador

# ******** Recorre todos los archivos del directorio y cuenta solo las tareas en proceso *****************
# ********************************************************************************************************

def cantidadTareasEnProceso()-> int:
    contador = 0
    estado = "En proceso"

    listaDeArchivos = os.listdir() # Hace una lista con los nombres de todos los archivos.

    for archivo in listaDeArchivos: # Recorre todos los archivos. 
        if archivo.startswith("Tarea_"):
            with open(archivo,"r") as t:
                contenido = t.read()
            if f"| {'Estado:':<15} {estado:<47}|\n" in contenido:
                contador += 1

    return contador

# ************* Recorre todos los archivos del directorio y cuenta solo las tareas completadas ***********
# ********************************************************************************************************

def cantidadTareasCompletas()-> int:
    contador = 0
    estado = "Completada"

    listaDeArchivos = os.listdir() # Hace una lista con los nombres de todos los archivos.

    for archivo in listaDeArchivos: # Recorre todos los archivos. 
        if archivo.startswith("Tarea_"):
            with open(archivo,"r") as t:
                contenido = t.read()
            if f"| {'Estado:':<15} {estado:<47}|\n" in contenido:
                contador += 1

    return contador

# ****** Recorre todas las tareas "En proceso" devuelve el nombre de la que esta proxima a vencer ********
# ********************************************************************************************************

def tareaProximaAVencer()-> str:
    id = 1
    fechaAux = date.max
    proximaAVencer = ""
    while True:
        try:
            with open(f"Tarea_{id}.txt","r") as tarea:
                contenido = tarea.read()
                
                if f"| {'Estado:':<15} {'En proceso':<47}|" in contenido:
                    lsContenido:list[str] = contenido.splitlines()
                    recorteDeFecha = lsContenido[5][18:29].strip()

                    fechaDeLaTarea:object = datetime.strptime(recorteDeFecha,"%d/%m/%Y").date()


                    if fechaDeLaTarea <= fechaAux:
                        proximaAVencer = f"-> Tarea ID: {id}"
                        fechaAux = fechaDeLaTarea

                id += 1
        except FileNotFoundError:
            break
    return proximaAVencer if cantidadTareasEnProceso() > 0 else "-> Ninguna."
import os
from funcionesPanel import cantidadTareasCompletas,cantidadTareasEnProceso,\
                           cantidadTareasVencidas,cantidadTotalDeTareas
import time
from colorDeEstado import colorEstado
from colorama import Fore,Style

sb = Style.BRIGHT
sr = Style.RESET_ALL
lb = Fore.LIGHTBLUE_EX
lg = Fore.LIGHTGREEN_EX
lr = Fore.LIGHTRED_EX
lm = Fore.LIGHTMAGENTA_EX
ly = Fore.LIGHTYELLOW_EX
blc = Fore.LIGHTBLACK_EX
lc = Fore.LIGHTCYAN_EX
lw = Fore.LIGHTWHITE_EX



# ************************* Muestra la tarea que tenga el ID introducido por el usuario ******************
#*********************************************************************************************************

def mostrarTareaPorID()-> None:
    os.system("clear")
    print(f"{blc}{sb}{' Tareas por ID ':*^66}{sr}")
    totalDeTareas = cantidadTotalDeTareas()

    if totalDeTareas > 0:
        while True:
            try:
                idTarea:int= int(input("Ingresa el ID de la tarea: \n> "))

                with open(f"Tarea_{idTarea}.txt","r") as t:
                    os.system("clear")
                    print(f"{' Tareas por ID ':*^66}")
                    print(f"\n{'Tarea: ':>35}{idTarea:<40}")

                    colorEstado(f"Tarea_{idTarea}.txt")

            except ValueError:
                print("Error, dato incorrecto.")
                print("Intente de nuevo.")
                continue
            except FileNotFoundError:
                print("No existe una tarea con ese ID.")
                time.sleep(1)
                break
            print(f"\n{'':*^66}\n")
            continuar = input("Presione una tecla para continuar.")
            break
    else:
        print("\nNo hay tareas disponibles.\n")
        print(f"\n{blc}{sb}{'':*^66}{sr}")
        continuar = input("Presione una tecla para continuar.")

# ************************* Mostra la lista completa de las tareas ***************************************
# ********************************************************************************************************

def mostrarTodasLasTareas():
    os.system("clear")
    print(f"{sb}{' Todas Las Tareas Creadas ':*^66}{sr}")
    id = 1

    listaDeArchivos = os.listdir()

    for archivo in listaDeArchivos:
        if archivo.startswith("Tarea_"):
            with open(archivo,"r") as t:
                print(f"\n{'Tarea: ':>35}{id:<40}")
                colorEstado(archivo)

            id += 1

    print(f"\n{' Fin ':^66}")
    print(f"\n{sb}{'':*^66}{sr}")
    continuar = input("Presione una tecla para continuar.")
            

# ********************* Imprime las tareas con PRIORIDAD introducida por el usuario **********************
# ********************************************************************************************************

def mostrarTareasPorPrioridad():
    os.system("clear")
    print(f"{sb}{' Prioridad ':*^66}{sr}")
    id = 1
    prioridades:dict[str,int] = pAltaMediaBaja()
    sumPrioridades = 0
    for c,v in prioridades.items():
        print(f"{c}: {v}")
        sumPrioridades += v

    if sumPrioridades > 0:
        while True:
            prioridad:str = input("\nAlta, Media o Baja:\n> ").lower().capitalize()
            if prioridad != "Alta" and prioridad != "Media" and prioridad != "Baja":
                print("Intente de nuevo.")
                continue
            break

        listaDeArchivos = os.listdir()

        for archivo in listaDeArchivos:

            if archivo.startswith("Tarea_"):
                with open(archivo,"r") as t:
                    contenido = t.read()

                lsContenido:list[str] = contenido.splitlines()
                priori = lsContenido[6][18:24].strip()

                if prioridad == priori:
                    print(f"\n{'Tarea: ':>35}{id:<40}")
                    colorEstado(archivo)
            id += 1

        print(f"\n{' Fin ':^66}")
        print(f"\n{sb}{'':*^66}{sr}")
        continuar = input("Presione una tecla para continuar.")

    else:
        print("\nLa lista de prioridades esta vacia.")
        print(f"\n{'':*^66}")
        continuar = input("\nPresione una tecla para continuar.")


# *********** Imprime las tareas que son RESPONSABILIDAD del nombre introducido por el usuario ***********
# ********************************************************************************************************

def mostrarTareasPorResposable():
    os.system("clear")
    print(f"{sb}{' Responsabilidad ':*^66}{sr}")
    lsResposables = listaResponsables()

    if not lsResposables:
        print("\nLa lista esta vacia.\n")
        print(f"\n{sb}{'':*^66}{sr}")
        continuar = input("\nPresione una tecla para continuar.")
    else:
        print("\n-- Lista De Responsables --\n")

        for personaResponsable in lsResposables:
            print(f" {sb}{lm}⏺  {personaResponsable}{sr}")
        print()
        print("---------------------------\n")
        responsable:str = input("Ingresa el nombre del resposable de la tarea:\n> ")

        id = 1
        listaDeArchivos = os.listdir()

        for archivo in listaDeArchivos:

            if archivo.startswith("Tarea_"):
                with open(archivo,"r") as t:
                    contenido = t.read()

                lsContenido:list[str] = contenido.splitlines()
                respon = lsContenido[8][18:55].strip()

                if responsable == respon:
                    print(f"\n{'Tarea: ':>35}{id:<40}")
                    colorEstado(archivo)
                id += 1

        print(f"\n{' Fin ':^66}")
        print(f"\n{sb}{'':*^66}{sr}")
        continuar = input("\nPresione una tecla para continuar.")

# ***************** Muetra las tareas con el ESTADO introducido por el usuario ***************************
# ********************************************************************************************************

def mostrarTareasPorEstado():
    tareasCompletas = cantidadTareasCompletas()
    tareasVencidas = cantidadTareasVencidas()
    tareasEnProceso = cantidadTareasEnProceso()
    os.system("clear")
    print(f"{sb}{' Mostrar Tareas Por Estado ':*^66}{sr}")
    print(f"\n{lg}{sb}Completadas: {sr}{tareasCompletas}")
    print(f"{lr}{sb}Vencidas: {sr}{tareasVencidas}")
    print(f"{lb}{sb}En proceso: {sr}{tareasEnProceso}\n")
    sumTareas = tareasCompletas + tareasVencidas + tareasEnProceso

    if sumTareas > 0:
        while True:
            estadoTarea = input("Estado (Vencida, En proceso, Completada)\n> ").lower().capitalize()

            if estadoTarea != "Vencida" and estadoTarea != "En proceso" and estadoTarea != "Completada":
                print("Ingrese el estado correctamente.")
                continue
            break

        id = 1
        listaDeArchivos = os.listdir()

        for archivo in listaDeArchivos:

            if archivo.startswith("Tarea_"):
                with open(archivo,"r") as t:
                    contenido = t.read()

                lsContenido:list[str] = contenido.splitlines()
                status = lsContenido[9][18:30].strip()                

                if estadoTarea == status:
                    if estadoTarea == "Completada":
                        print(f"\n{'Tarea: ':>35}{id:<40}")
                        colorEstado(archivo)

                    elif estadoTarea == "En proceso":
                        print(f"\n{'Tarea: ':>35}{id:<40}")
                        colorEstado(archivo)

                    else:
                         print(f"\n{'Tarea: ':>35}{id:<40}")
                         colorEstado(archivo)
                id += 1

        print(f"\n{' Fin ':^66}")
        print(f"\n{'':*^66}")
        continuar = input("Presione una tecla para continuar.")

    else:
        print("\nNo hay tareas disponibles")
        print(f"\n{'':*^66}")
        continuar = input("\nPresione una tecla para continuar.")

# ****************** Elimina la tarea que con el ID introducido por el usuario ***************************
# ********************************************************************************************************

def eliminarTarea():
    os.system("clear")
    print(f"{sb}{' Eliminar Tarea ':*^66}{sr}\n")

    totalDeTareas = cantidadTotalDeTareas()

    if totalDeTareas > 0:
        idEliminarTarea:str = input("Ingresa el ID de la tarea que quieres eliminar:\n> ")

        if os.path.exists(f"Tarea_{idEliminarTarea}.txt"):
            with open(f"Tarea_{idEliminarTarea}.txt","r") as t: # Muestra la tarea antes de borrarla
                    tarea = t.read()
                    print(f"\n{'Tarea: ':>35}{idEliminarTarea:<40}")
                    colorEstado(f"Tarea_{idEliminarTarea}.txt")
            while True:
                r = input("¿Seguro que quieres eliminar ésta tarea (si/no):\n> ").lower().replace("sí","si")
                if r == "si":
                    print("Eliminando...")
                    time.sleep(1)
                    os.remove(f"Tarea_{idEliminarTarea}.txt")
                    print("Tarea eliminada.")
                    continuar = input("Presiona una tecla para continuar.")
                    break
                elif r == "no":
                    print("Volviendo al menú principal...")
                    time.sleep(1.7)
                    break
                else:
                    print("Ingrese (si/no).")
                    time.sleep(1.2)

        else:
            print("Esa tarea no existe.")
            time.sleep(0.5)
            print("Volviendo al menú principal...")
            time.sleep(1.3)
    else:
        print("\nNo hay tareas disponibles.\n")
        continuar = input("Presione una tecla para continuar.")

# ************************* Lista los nombres de los responsables disponibles ****************************
# ********************************************************************************************************

def listaResponsables()-> list[str]:
    lsresponsables = []

    listaDeArchivos = os.listdir()

    for archivo in listaDeArchivos:

        if archivo.startswith("Tarea_"):
            with open(archivo,"r") as t:
                contenido = t.read()

            lsContenido:list[str] = contenido.splitlines()
            responsable = lsContenido[8][18:55].strip()

            if responsable not in lsresponsables:
                lsresponsables.append(responsable)

    return lsresponsables


# ************************* Cuenta las tareas por prioridad disponibles **********************************
# ********************************************************************************************************

def pAltaMediaBaja()-> dict[str,int]:
    prioridadAlta = 0
    prioridadMedia = 0
    prioridadBaja = 0
    prioridades = {}

    listaDeArchivos = os.listdir()

    for archivo in listaDeArchivos:

        if archivo.startswith("Tarea_"):
            with open(archivo,"r") as t:
                contenido = t.read()

            lsContenido:list[str] = contenido.splitlines()
            prioridad = lsContenido[6][18:24].strip()

            if prioridad == "Alta":
                prioridadAlta += 1

            elif prioridad == "Media":
                prioridadMedia += 1
                
            else: 
                prioridadBaja += 1
    
    prioridades = {"Alta": prioridadAlta,"Media": prioridadMedia,"Baja": prioridadBaja}
    return prioridades

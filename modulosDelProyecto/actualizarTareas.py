import os
from menusDinamicos import menuModificarTareas
from agregarTareas import pedirFechaDeVencimiento,estadoDeLaTarea
from funcionesPanel import cantidadTotalDeTareas
import time
from colorDeEstado import colorEstado
from colorama import Fore,Style
from animaciones import animacionDeCarga

lm = Fore.LIGHTMAGENTA_EX
sb = Style.BRIGHT
sr = Style.RESET_ALL

# Permitir al usuario modificar la descripción, fecha límite,
# prioridad u otros detalles de una tarea existente.

def actualizarTarea():
    os.system("clear")
    print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")
    totalDeTareas = cantidadTotalDeTareas()

    if totalDeTareas > 0:
        while True:
            try:
                idTarea:int= int(input("\nIngresa el ID de la tarea que quieres modificar: \n> "))
                os.system("clear")
                print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")

                with open(f"Tarea_{idTarea}.txt","r") as t:
                    print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                    colorEstado(f"Tarea_{idTarea}.txt")

            except ValueError:
                print("Error, dato incorrecto.")
                continue
            except FileNotFoundError:
                print("No existe una tarea con ese ID.")
                continuar = input("Presione un tecla para continuar.")
                continue
            break

        opcion:int = menuModificarTareas()
         
        if opcion == 1:# ----------------> Cambia el "titulo" de la tarea <----------------
            os.system("clear")
            print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")

            with open(f"Tarea_{idTarea}.txt","r") as t: # Muestra la tarea antes de actutalizarla
                print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                colorEstado(f"Tarea_{idTarea}.txt")

            with open(f"Tarea_{idTarea}.txt","r") as t:
                contenido = t.read()
                lsLineas  = contenido.splitlines()
                tituloNuevo  = input("Ingresa el nuevo título:\n> ")
                lsLineas[2] = f"| {'Título:':<15} {tituloNuevo:<47}|"
                contenido = "\n".join(lsLineas)

            with open(f"Tarea_{idTarea}.txt","w") as t:# sobreescribe la tarea con los nuevos cambios.
                t.write(contenido)
            animacionDeCarga("Espere"," .")
            time.sleep(0.3)
            print("\nNuevo título agregado.")
            print(f"\n{lm}{sb}{'':*^66}{sr}")
            continuar = input("\nPresione una tecla para continuar.")

        elif opcion == 2:# ----------------> Cambia la "descripción" de la tarea <----------------
            os.system("clear")
            print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")

            with open(f"Tarea_{idTarea}.txt","r") as t: # Muestra la tarea antes de actutalizarla
                print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                colorEstado(f"Tarea_{idTarea}.txt")

            with open(f"Tarea_{idTarea}.txt","r") as t:
                contenido:str = t.read()
                lsLineas:list[str] = contenido.splitlines()
                nuevaDescripcion:str = input("Ingresa la nueva descripción:\n> ")
                lsLineas[3] = f"| {'Descripción:':<15} {nuevaDescripcion:<47}|"
                contenido = "\n".join(lsLineas)

            with open(f"Tarea_{idTarea}.txt","w") as t:# sobreescribe la tarea con los nuevos cambios.
                t.write(contenido)
                animacionDeCarga("Procesando"," .")
                time.sleep(0.3)
                print("\nNueva descripción agregada.")
                print(f"\n{lm}{sb}{'':*^66}{sr}")
                continuar = input("\nPresione una tecla para continuar.")

        elif opcion == 3:# ----------------> Cambia la "fecha límite" de la tarea <----------------
            os.system("clear")
            print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")

            with open(f"Tarea_{idTarea}.txt","r") as t: # Muestra la tarea antes de actutalizarla
                print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                colorEstado(f"Tarea_{idTarea}.txt")

            with open(f"Tarea_{idTarea}.txt","r") as t:
                contenido:str = t.read()
                lsLineas = contenido.splitlines()
                nuevaFechaLimite = pedirFechaDeVencimiento()
                nuevoEstado = estadoDeLaTarea(nuevaFechaLimite)
                lsLineas[5] = f"| {'Fecha límite:':<15} {nuevaFechaLimite:<47}|"
                lsLineas[9] = f"| {'Estado:':<15} {nuevoEstado:<47}|"
                contenido = "\n".join(lsLineas)

            with open(f"Tarea_{idTarea}.txt","w") as t:# sobreescribe la tarea con los nuevos cambios.
                t.write(contenido)
            animacionDeCarga("Cambiando"," .")
            time.sleep(0.5)
            print("\nNueva fecha límite agregada.")
            print(f"\n{lm}{sb}{'':*^66}{sr}")
            continuar = input("\nPresione una tecla para continuar.")

        elif opcion == 4:# ----------------> Cambia la "prioridad" de la tarea <----------------
            os.system("clear")
            print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")
            with open(f"Tarea_{idTarea}.txt","r") as t: # Muestra la tarea antes de actutalizarla
                print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                colorEstado(f"Tarea_{idTarea}.txt")

            with open(f"Tarea_{idTarea}.txt","r") as t:
                contenido = t.read()
                lsLineas = contenido.splitlines()

            while True:
                nuevaPrioridad = input("Nueva prioridad (Alta, Media o Baja):\n> ").lower().capitalize()

                if nuevaPrioridad != "Alta" and nuevaPrioridad != "Media" and nuevaPrioridad != "Baja":
                    print("Ingrese la prioridad correctamente.")
                    print("Intente de nuevo.")
                    continue

                else:
                    lsLineas[6] = f"| {'Prioridad:':<15} {nuevaPrioridad:<47}|"
                    contenido = "\n".join(lsLineas)
                    with open(f"Tarea_{idTarea}.txt","w") as t:# sobreescribe la tarea con los nuevos cambios.
                        t.write(contenido)
                    animacionDeCarga("Agregando"," .")
                    time.sleep(0.2)
                    print("\nNueva prioridad agregada.")
                    print(f"\n{lm}{sb}{'':*^66}{sr}")
                    continuar = input("\nPresione una tecla para continuar.")
                break

        elif opcion == 5:# ----------------> Cambia el "estado" a tarea completada  <----
            os.system("clear")
            print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")
            with open(f"Tarea_{idTarea}.txt","r") as t: # Muestra la tarea antes de actutalizarla
                print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                colorEstado(f"Tarea_{idTarea}.txt")

            with open(f"Tarea_{idTarea}.txt","r") as t:
                contenido = t.read()
                lsLineas = contenido.splitlines()

                while True:
                    respuesta = input("¿Has completado la tarea (si/no)?:\n> ").lower().replace("sí","si")

                    if respuesta == "si":
                        lsLineas[9] = f"| {'Estado:':<15} {'Completada':<47}|"
                        contenido = "\n".join(lsLineas)

                        with open(f"Tarea_{idTarea}.txt","w") as t:# sobreescribe la tarea con los nuevos cambios.
                            t.write(contenido)
                        animacionDeCarga("Agregando estado"," .")
                        time.sleep(0.4)
                        print("\nNuevo estado agregado tarea 'Completada'.")
                        print(f"\n{lm}{sb}{'':*^66}{sr}")
                        continuar = input("\nPresione una tecla para continuar.")
                        break
                    elif respuesta == "no":
                        print("El estado de la tarea ha sido definido segun su fecha límite.")
                        time.sleep(2.5)
                        break
                    else:
                        print("Ingrese (si/no).")

        elif opcion == 6:# ----------------> Cambia el nombre del "RESPONSABLE" de la tarea <----------------
            os.system("clear")
            print(f"{lm}{sb}{' Actualizar Tarea ':*^66}{sr}")

            with open(f"Tarea_{idTarea}.txt","r") as t: # Muestra la tarea antes de actutalizarla
                tarea = t.read()
                print(f"\n{'Tarea: ':>35}{idTarea:<40}")
                colorEstado(f"Tarea_{idTarea}.txt")

            with open(f"Tarea_{idTarea}.txt","r") as t:
                contenido = t.read()
                lsLineas = contenido.splitlines()
                nuevoResponsable:str = input("Ingresa el nuevo responsable:\n> ")
                lsLineas[8] = f"| {'Responsable:':<15} {nuevoResponsable:<47}|"
                contenido = "\n".join(lsLineas)

            with open(f"Tarea_{idTarea}.txt","w") as t:# sobreescribe la tarea con los nuevos cambios.
                t.write(contenido)
            animacionDeCarga("Agregando"," .")
            time.sleep(1)
            print("\nNuevo responsable agregado.")
            print(f"\n{lm}{sb}{'':*^66}{sr}")
            continuar = input("\nPresione una tecla para continuar.")

        else:# ----------------> Sale de la función <----------------
            animacionDeCarga("Saliendo", " .")
    else:
        print("\nNo hay tareas disponibles.\n")
        continuar = input("\nPresione una tecla para continuar.")


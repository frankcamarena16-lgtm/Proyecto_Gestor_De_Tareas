from agregarTareas import agregarTarea
from actualizarTareas import actualizarTarea
from menusDinamicos import *
from verTareas import *
from animaciones import animacionCargaAplicacion

#animacionCargaAplicacion()

while True:   
    if panelPrincipal() == 1:# Se muestra el Panel Principal y sus opciones.
        while True:
            opcionMenu:int = mostrarMenu()

            if opcionMenu == 1:
                agregarTarea()# Agrega una tarea.

            elif opcionMenu == 2:
                opcionMenuLista:int = menuListaDeTarea()

                if opcionMenuLista == 1:
                    mostrarTareaPorID()# Muestra la tarea segun su ID.

                elif opcionMenuLista == 2:
                    mostrarTodasLasTareas() # Muestra todas las tareas de la disponibles.

                elif opcionMenuLista == 3:
                    mostrarTareasPorPrioridad()# Muestra las tareas segun su PRIORIDAD.

                elif opcionMenuLista == 4:
                    mostrarTareasPorResposable()# Muestra las tareas segun el RESPONSABLE.

                elif opcionMenuLista == 5:
                    mostrarTareasPorEstado()# Muestra las tareas segun su ESTADO.
                else:
                    print("Volviendo al Menú principal")

            elif opcionMenu == 3:
                actualizarTarea()# Actualiza una tarea segun su ID.

            elif opcionMenu == 4:
                eliminarTarea()# Elimina una tarea segun su ID.
            else:
                break
    else:
        #Salir del panel principal
        print("Saliendo...")
        break



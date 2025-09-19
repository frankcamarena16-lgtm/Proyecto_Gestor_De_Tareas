import os
from datetime import date
import funcionesPanel as fp
import time
from animaciones import animacionDeCarga
from colorama import init,Fore,Style

# init(autoreset=True) ---> solo se usa cuando usas Windows

sb = Style.BRIGHT # Pone la letra en formato negrita.
sr = Style.RESET_ALL # Se usa para volver al color original.
fa = Fore.YELLOW # Pone la letra color amarilla.
fc = Fore.CYAN # Pone la letra color cyan.
lb = Fore.LIGHTBLUE_EX # Pone la letra color azul brillante.
ly = Fore.LIGHTYELLOW_EX # Pone la letra color amarilla brillante.

# ************************************* Muestra el menu principal ****************************************
# ********************************************************************************************************

def mostrarMenu()-> int:
    os.system("clear")
    print("---------------------------------------------------------")
    print(f"|{sb}{'>>> Gestor De Tareas <<<':^55}{sr}|")
    print(f"|{fa}{sb}{'Menú Principal':^55}{sr}|")
    print(f"|{'             ➖➖➖➖➖➖➖➖              ':^47}|")
    print(f"|{' ':<55}|")
    print(f"|{' ':<55}|")
    print(f"|{sb}{' (1) ➕ Agregar tarea.          (2) 👀 Ver tareas.':<53}{sr}|")
    print(f"|{' ':^55}|")
    print(f"|{' ':^55}|")
    print(f"|{sb}{' (3) ✏️  Actualizar tarea.       (4) 🗑️  Eliminar tarea.':<55}{sr} |")
    print(f"|{' ':^55}|")
    print(f"|{' ':^55}|")
    print(f"|{sb}{' (5)  ◀ Volver atras.':<55}{sr}|")
    print(f"|{' ':^55}|")
    print(f"|{' ':^55}|")
    print(f"|{' ':^55}|")
    print("---------------------------------------------------------")
    print("Elige una opcion:")
    while(True):
        try:
            opcion:int = int(input("> "))
            if opcion > 0 and opcion < 6:
                return opcion
            else:
                print("Esa opcion no existe.")
                print("Introduce un numero del 1 al 5.")
        except ValueError:
            print("Error, dato incorrecto.")
            print("debes introducir un numero del 1 al 5.")

# *********************************** Muestra el menú lista de tareas ************************************
# ********************************************************************************************************

def menuListaDeTarea()-> int:
    os.system("clear")
    print("---------------------------------------------------------")
    print(f"|{ly}{sb}{'>>> Menu Lista De Tareas <<<':^55}{sr}|")
    print(f"|{sb}{'✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴':^55}{sr}|")
    print(f"|{' ':<55}|")
    print(f"|{sb}{' (1) Ver tareas por ID.':<55}{sr}|")
    print(f"|{sb}{' (2) Ver todas las tareas.':<55}{sr}|")
    print(f"|{' ':^55}|")
    print(f"|{lb}{sb}{' --> "Filtro" <--':<55}{sr}|")
    print(f"|{' ':^55}|")
    print(f"|{sb}{' (3) Prioridad: ':<15}{sr}{'(Alta, Media, Baja.)':<39}|")
    print(f"|{' ':^55}|")
    print(f"|{sb}{' (4) Responsable: ':<15}{sr}{'(Nombre del encargado de la tarea.)':<37}|")
    print(f"|{' ':^55}|")
    print(f"|{sb}{' (5) Estado: '}{sr}{'(vencidas, en proceso, completadas).':<42}|")
    print(f"|{' ':^55}|")
    print(f"|{sb}{' (6) Volver atras.':<55}{sr}|")
    print(f"|{' ':<55}|")
    print("---------------------------------------------------------")
    print("Elige una opcion:")
    while(True):
        try:
            opcion:int = int(input("> "))
            if opcion > 0 and opcion < 7:
                return opcion
            else:
                print("Esa opcion no existe.")
                print("Introduce un numero del 1 al 6.")
        except ValueError:
            print("Error, dato incorrecto.")
            print("debes introducir un numero del 1 al 6.")

# ******************** Muestra el menú con las opciones para actualizar las tareas ***********************
# ********************************************************************************************************

def menuModificarTareas()-> int:
    print("------------------------------------------------------------------")
    print(f"| {sb}{ly}{'¿Que dato quieres modificar?':^63}{sr}|")
    print(f"| {' ':^63}|")
    print(f"|{sb} {'(1) Título.                         (2) Descripcíon. ':<63}{sr}|")
    print(f"| {' ':^63}|")
    print(f"|{sb} {'(3) Fecha límite.                   (4) Prioridad. ':<63}{sr}|")
    print(f"| {' ':^63}|")
    print(f"|{sb} {'(5) Estado.                         (6) Responsable. ':<63}{sr}|")
    print(f"| {' ':^63}|")
    print(f"|{sb} {'(7) Salir. ':<63}{sr}|")
    print("------------------------------------------------------------------")
    print("Elige una opción.")
    while True:
        try:
            opcion:int = int(input("> "))
            if opcion > 0 and opcion < 8:
                return opcion
            else:
                 print("Esa opcion no existe.")
                 print("introduce un número del 1 al 7.")
        except ValueError:
                print("Error, dato incorrecto.")
                print("debes introducir un número del 1 al 7.")

# ************************************* Panel principal **************************************************
# ********************************************************************************************************

def panelPrincipal():
    fecha = date.today() # Fecha actual
    fecha = fecha.strftime("%d/%m/%Y") # Le da formato a la (dia/mes/anio) a la fecha.
    numTareas:int = fp.cantidadTotalDeTareas()
    tareasVencidas:int = fp.cantidadTareasVencidas()
    tareasEnProceso:int = fp.cantidadTareasEnProceso()
    tareascompletas:int = fp.cantidadTareasCompletas()
    proximaAVencer:str = fp.tareaProximaAVencer()

    while True:
        os.system("clear")
        print("---------------------------------------------------------------------")
        print(f"|{sb}{'*** Gestor De Tareas *** ':^67}{sr}|")
        print(f"|{sb}{'Fecha: ':>56}{fecha}{sr} |")
        print(f"|{sb}{fa}{'>> Estadísticas <<':^20}{sr}{'':>46} |")
        print(f"|{'____________________':<20}{'':^26}{'_____________________':>21}|")
        print(f"|{sb}{'Tareas completas':^20}{sr}|{'':^24}|{sb}{fa}{' >> Recordatorio << ':>21}{sr}|")
        print(f"|{tareascompletas:^20}|{'':^24}|{'':^21}|")
        print(f"|{'                    |':<20}{sb}{fc}{' -- Elige una opción -- ':<20}{sr}|{sb}{'Próxima a vencer ❗':>20}{sr}|")
        print(f"|{'                    |':<20}{'    ➖➖➖➖➖➖➖➖':^}    |  {proximaAVencer:<19}|")
        print(f"|{sb}{'Tareas en proceso':^20}{sr}|{'   |_____________________':>46}|")
        print(f"|{tareasEnProceso:^20}|{'   |':^46}|")
        print(f"|{'                    |':<20}{sb}{'(1) Menú.':^24}{sr}|{'':^21}|")
        print(f"|{'                    |':<20}{'':^24}|{'':^21}|")
        print(f"|{sb}{'Tareas vencidas':^20}{sr}|{'':^24}|{'':^21}|")
        print(f"|{tareasVencidas:^20}|{'':^24}|{'':^21}|")
        print(f"|{'                    |':<20}{sb}{'(2) Salir.':^24}{sr}|{'':^21}|")
        print(f"|{'':^20}|{'':^24}|{'':^21}|")
        print(f"|{sb}{'Tareas en total':^20}{sr}|{'':^24}|{'':^21}|")
        print(f"|{numTareas:^20}|{'':^24}|{'':^21}|")
        print(f"|{'':^20}|{'':^24}|{'':^21}|")
        print("---------------------------------------------------------------------")
    
        try:
            opcion:int = int(input("> "))
            if opcion == 1:
                animacionDeCarga("Cargando menú principal"," .") # Funcion que simula una carga imprimiendo un mensaje y el un caracter.
                return opcion
            elif opcion == 2:
                return opcion
            else:
                print("Esa opcion no existe.")
                time.sleep(2) # Espera 2 segundos antes de seguir con el flujo del programa.
        except ValueError:
                print("Error, dato incorrecto.")
                time.sleep(2) # Espera 2 segundos antes de seguir con el flujo del programa.

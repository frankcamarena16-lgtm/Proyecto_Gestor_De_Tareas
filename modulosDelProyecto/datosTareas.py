# ************ Pide y verifica que la fecha introducida por el usuario sea válida ************************
# ********************************************************************************************************
import time
  
def pedirFechaDeVencimiento()-> str:
    print("Fecha límite (DD/MM/AA):")
    while True:
        try:
            fecha:list[str] = input("> ").split("/")
            if len(fecha) == 3:
                dia,mes,anio = fecha
                if len(anio) != 4:
                    print("El año debe tener 4 cifras Ej: '2025'.")
                    time.sleep(1)
                    continue
            else:
                print("Formato incorrecto.")
                print("Intente de nuevo.")
                continue
            dia = int(dia)
            mes = int(mes)
            anio = int(anio)
            fecha:str = f"{dia}/{mes}/{anio}"
        except ValueError:
            print("Error, dato inválido.")
            print("Intente de nuevo.")
            continue
        if mes == 2 and dia > 29: 
            print("Ese día no existe.")
            print("Intente de nuevo.")
            continue
        if (dia <= 0 or dia > 31 or mes <= 0 or mes > 12 or anio <= 0):
            print(f'La fecha "{fecha}" no es válida.')
            print("Intente de nuevo.")
            continue
        if mes == 9 and dia > 30: 
            print("Ese día de septiembre no existe.")
            print("Intente de nuevo.")
            continue
        if mes == 4 and dia > 30: 
            print("Ese día de abril no existe.")
            print("Intente de nuevo.")
            continue
        if mes == 6 and dia > 30: 
            print("Ese día de junio no existe.")
            print("Intente de nuevo.")
            continue
        if mes == 11 and dia > 30: 
            print("Ese día de noviembre no existe.")
            print("Intente de nuevo.")
            continue
        return fecha
    
# ************* Pide y verifica que la prioridad introducida por el usuario sea válida *******************
# ********************************************************************************************************

def pedirPrioridad()-> str:
    while True:
        prioridad:str = input("Prioridad (Alta, Media o Baja) \n> ").lower().capitalize()
        if prioridad != "Alta" and prioridad != "Media" and prioridad != "Baja":
            print("Intente de nuevo.")
            continue
        return prioridad

from colorama import Fore,Style

sb = Style.BRIGHT
sr = Style.RESET_ALL

lb = Fore.LIGHTBLUE_EX
lg = Fore.LIGHTGREEN_EX
lr = Fore.LIGHTRED_EX

# *********************************************** Colorea el estado de la tarea **************************************************
# ********************************************************************************************************************************

def colorEstado(archivo:str):
        
        with open(archivo,"r") as t:
            contenido = t.read()

            lsContenido = contenido.splitlines()
            estado = lsContenido[9][18:30].strip()

            if estado == "Completada":
                estado = "Completada ✔"
                lsContenido[9] = f"| {'Estado:':<15} {lg}{estado:<47}{sr}{sb}|{sr}"
                for linea in lsContenido:
                    print(f"{sb}{linea}")

            if estado == "Vencida":
                estado = "Vencida ✖"
                lsContenido[9] = f"| {'Estado:':<15} {lr}{estado:<47}{sr}{sb}|{sr}"
                for linea in lsContenido:
                    print(f"{sb}{linea}")
                    
            if estado == "En proceso":
                estado = "En proceso ⏺"
                lsContenido[9] = f"| {'Estado:':<15} {lb}{estado:<47}{sr}{sb}|{sr}"
                for linea in lsContenido:
                    print(f"{sb}{linea}")
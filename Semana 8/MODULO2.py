#Nathaly Sarai Rodriguez Silva
def DUI():
     DUI_1 = input("Ingrese su numero de DUI: ")
     if DUI_1.isdigit():
        if len(DUI_1) == 9:
            return("EL DUI INGRESADO ES VALIDO")
        else:
            return("EL DUI INGRESADO ES INVALIDO")
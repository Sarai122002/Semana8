#Nathaly Sarai Rodriguez Silva
def AÑOS():
    while True:
        try:
           AÑO = int(input("Ingrese su año de nacimiento: "))
        except ValueError:
            print("La Fecha ingresada es invalida")
            continue
        años_1 = 2022 - AÑO
        if años_1 >= 18:
            print("Segun la fecha, eres mayor de edad")
            break
        elif años_1 >= 0:
            print("Segun la fecha, eres menor de edad")
            break  
        elif años_1 < 0:
            print("La Fecha ingresada es invalida")
            break
            
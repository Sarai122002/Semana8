#Nathaly Sarai Rodriguez Silva
import MODULO1
import MODULO2
Start = int(input("Seleccione:\n-Opcion 1 para calcular su edad\n"
"-Opcion 2 para validar su DUI\n"))

if Start == 1:
    age_C = MODULO1.AÑOS()
    print(age_C)

elif Start == 2:
    DUI_C = MODULO2.DUI()
    print(DUI_C)

else:
    print("No existe esa opcion")
    

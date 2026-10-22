sexo = input("si eres mujer introduce una m y si eres hombre introduce una h ")
sexo = sexo.lower()
nombre = input("introduce tu nombre ")
nombre = nombre.lower()

if sexo == "m" and nombre < "n" or sexo == "h"  and nombre > "n":
    print("perteneces al grupo A")
else:
   
    print("perteneces al grupo B")
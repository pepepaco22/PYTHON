cantidad = float(input("Dime la cantidad que quieres invertir: "))
interes = float(input("dime cuál es el interés anual?: "))
años = int(input("Dime cuántos años quieres invertirlo: "))

for x in range(1, años + 1):
    cantidad += cantidad * (interes / 100)
    print("El capital obtenido en ", x, "año es de ", round(cantidad, 2))


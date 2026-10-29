puntos = float(input("introduce tu puntuacion"))
sueldo = 2400
if puntos == 0.0:
    print("vas a cobrar", sueldo, "euros")
elif puntos == 0.4:
    print("vas a cobrar", sueldo * 2, "euros")
elif puntos <= 0.6:
    print("vas a cobrar", sueldo * 3, "euros")
else:
    print("introduce un valor correcto")

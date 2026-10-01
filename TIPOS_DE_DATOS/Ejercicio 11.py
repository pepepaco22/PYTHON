d = float(input("¿cuanto dinero quieres invertir?"))
año1 = round(d * (1 + 0.04),2)
año2 = round( año1 * (1 + 0.04),2)
año3 = round( año2 * (1 + 0.04),2)

print(f"Ahorros tras el primer año: {año1} $")
print(f"Ahorros tras el segundo año: {año2} $")
print(f"Ahorros tras el tercer año: {año3} $")
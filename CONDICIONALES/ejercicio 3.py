nu = int(input("introduce un numero"))
nu_1 = int(input("introduce otro numero"))

if nu_1 == 0:
    print("el divisor no puede ser cero")
else:
    ca = nu / nu_1
    print(f"la division de estos numeros da {ca}")
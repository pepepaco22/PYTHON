ob = input("escriba el producto ")
pr = float(input("escriba el precio de ese producto "))
ca = int(input("escriba la cantidad de un mismo objeto que se va a llevar "))
pr_t = precio * unidades
print(f"{ob}: {pr:09.2f}€ x {unidades:03d} ca = {pr_t:011.2f}€")
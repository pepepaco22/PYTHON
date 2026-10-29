pizza =input("si quieres una pizza vegetariana escribe si y si la quieres normal escribe no ")
pizza = pizza.lower()
if pizza == "si" :
 ingredientes=input("elija uno de nuestros ingredientes Ingredientes vegetarianos: Pimiento y tofu.")
 print(f"tu pizza es vegetariana y lleva mozzarella, tomate y", ingredientes)
else :
 ingredientes=input("elija uno de nuestros ingredientes Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
 print(f"tu pizza es vegetariana y lleva mozzarella, tomate y", ingredientes)
 
 

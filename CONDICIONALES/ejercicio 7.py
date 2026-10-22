renta = int(input("introduce tu renta anual"))

if renta <= 10000:
    print("te corresponde un impositivo del 5%")
elif renta <= 20000:
    print("te corresponde un impositivo del 15%")
elif renta <= 35000:
    print("te corresponde un impositivo del 20%")
elif renta <= 60000:
     print("te corresponde un impositivo del 30%")
else:
        print("te corresponde un impositivo del 45%")

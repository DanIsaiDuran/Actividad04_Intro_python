from area import Area
from zodiaco import Zodiaco
from euler import Euler


print("1. Calcular areas")
print("2. Saber signo Zodiacal")
print("3. Numero e")
opc = input("Elige una opcion: ")

while True:
    if opc == "1":
        a = Area()
        while True:
            print("\n1. Area cuadrado")
            print("2. Area triangulo")
            print("3. Area circulo")
            op = input("Elige una opcion: ")

        
            if op == "1":
                a.areaCuadrado()
            elif op == "2":
                a.areaTriangulo()
            elif op == "3":
                a.areaCirculo()
            elif op == "0":
                break

    elif opc == "2":
        print("\n")
        z = Zodiaco()
        z.signo()

    elif opc == "3":
        e = Euler()
        print("\n")
        limite = int(input("Limite: "))
        n = e.numeroe(limite)
        print("e: ", n)
    else:
        break
    



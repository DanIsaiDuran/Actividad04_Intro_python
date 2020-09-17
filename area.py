class Area:

    def areaCuadrado(self):
        lado = float(input("Lado: "))
        print("Area: ", lado * lado)

    def areaTriangulo(self):
        base = float(input("Base: "))
        altura = float(input("Altura: "))

        print("Area: ", (base * altura)/2 )

    def areaCirculo(self):
        radio = float(input("Radio: "))
        pi = 3.1416

        print("Area: ", pi * (radio * radio))
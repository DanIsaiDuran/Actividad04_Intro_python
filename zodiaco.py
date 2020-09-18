class Zodiaco:

    def __init__(self):
        self.__dia = 0
        self.__mes = ''

    def signo(self):

        dia = int(input("Dia: "))
        mes = input("Mes: ")

        if mes == "Enero":
            if dia >= 20:
                print("Acuario")
            else:
                print("Capricornio")
        elif mes == "Febrero":
            if dia <= 18:
                print("Acuario")
            else:
                print("Piscis")
        elif mes == "Marzo":
            if dia <= 21:
                print("Piscis")
            else:
                print("Aries")
        elif mes == "Abril":
            if dia <= 19:
                print("Aries")
            else:
                print("Tauro")
        elif mes == "Mayo":
            if dia <= 20:
                print("Tauro")
            else:
                print("Geminis")
        elif mes == "Junio":
            if dia <= 20:
                print("Geminis")
            else:
                print("Cancer")
        elif mes == "Julio":
            if dia <= 22:
                print("Cancer")
            else:
                print("Leo")
        elif mes == "Agosto":
            if dia <= 22:
                print("Leo")
            else:
                print("Virgo")
        elif mes == "Septiembre":
            if dia <= 22:
                print("Virgo")
            else:
                print("Libra")
        elif mes == "Octubre":
            if dia <= 22:
                print("Libra")
            else:
                print("Escorpio")
        elif mes == "Noviembre":
            if dia <= 21:
                print("Escorpio")
            else:
                print("Sagitario")
        elif mes == "Diciembre":
            if dia <= 21:
                print("Sagitario")









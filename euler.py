class Euler:
    
    def factorial(self, numero):       
        if numero == 1 or numero == 0:
            return 1
        else:
            return numero * self.factorial(numero-1)

    def numeroe(self, limite):
        n = 0
        e = 0.0
        while n < limite:
            e += 1/self.factorial(n)
            n = n+1
        return e


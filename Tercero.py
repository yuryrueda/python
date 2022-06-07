class Calculadora:
    
    def __init__(self):
        self.num1=int(input("Ingrese un numero: "))
        self.num2=int(input("Ingrese otro numero: "))
      
    def suma(self):
        suma = self.num1 + self.num2
        print("La suma queda asi : ", suma)

    def resta(self):
        resta = self.num1 - self.num2
        print("La resta queda asi: ", resta)

    def multi(self):
        multi = self.num1 * self.num2
        print("La multiplicacion queda asi: ", multi)

    def divi(self):
        divi = self.num1 / self.num2
        print("La division queda asi: ", divi)

calculadora1=Calculadora()
calculadora1.suma()
calculadora1.resta()
calculadora1.multi()
calculadora1.divi()

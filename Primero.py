class Persona:
    
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
 
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
 
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
    def pagar_impuestos(self):
        if self.sueldo > 3600000:
            print("Se le hara un descuento del 3,5% a su salario.")
            porce = self.sueldo * 0.035
            descuen = self.sueldo - porce
            print("Se le desconto un valor de : ",porce)
            print("Quedando asi su salario con el descuento en: ", descuen)
      
        else:
            print("No se le descontara nada.")


persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()

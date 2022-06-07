class Alumno:
    
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.nota=int(input("Ingrese su nota: "))

    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Su nota es: ",self.nota)


    def final(self):
        if self.nota >= 3:
            print("Usted aprobo.")
        else:
            print("Usted repreobo.")
 
alumno1=Alumno()
alumno1.mostrar()
alumno1.final()

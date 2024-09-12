print("Ejemplo de Funciones")
# Declarando Funciones
def hola():
    print("Alguien uso la funcion hola")
def chos(mensa):
    print(f"chat {mensa}")
def ellacontesta(mensa):
    print(f"chat ella: {mensa}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es:{n} {ap}")
def suma(a,b):
    s=a+b
    return s
def resta(a,b):
    r=a-b
    return r
def mult(a,b):
    mul=a*b
    return mul
def division(a,b):
    div=a/b
    return div
#llamadas a 
hola()
chos("que bonita estas")
ellacontesta("gracias")
escribenombre(" Esquivel", "Adrian")
print("Operaciones basicas")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
Resuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {Resuma}")
print("Operacion Resta")
c3=int(input("ingresa un numero"))
c4=int(input("ingresa un numero"))
Rresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} ={Rresta}")
print("Operacion Multiplicacion")
c5=int(input("Ingresa un numero"))
c6=int(input("Ingresa u numero"))
Rmul=mult(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {Rmul}")
print("Operacion Division")
c7=int(input("Ingresa un numero"))
c8=int(input("Ingresa u numero"))
Rdiv=division(c7,c8)
print(f"La Division de  {c7} / {c8} = {Rdiv}")

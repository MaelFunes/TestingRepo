a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

def mayor(num1, num2):
    if num1>num2:
        may=num1
    else:
        may=num2
    return may
#subrutinas...
#sub problema 1 mayor entre A y B
may1 = mayor(a, b)

#sub problema 2 mayor entre C y D
may2 = mayor(c, d)

#diferencia
resta = may1-may2

#mostrar resultado...
print("el primer mayor es: ", may1)
print("el segundo mayor es: ", may2)
print("el resto es: ",resta)
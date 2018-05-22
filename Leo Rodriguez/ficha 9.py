#Titulo del ejercicio...
print("Encontrar el menor de los datos, y sacar su cuadrado y cubo. ")

#Calcular el menor de 3 variables ...
def menor(a,b,c):

    if a < b and a < c:
        men = a
    elif b < c:
        men = b
    else:
        men = c
    return men

#Calcular el cuadrado y cubo de un número...
def cua_cub(num):
    cuadrado = num**2
    cubo = num**3
    return cuadrado, cubo

#Carga de datos...
a = int(input("\nIngresar el valor de A: "))
b = int(input("Ingresar el valor de B: "))
c = int(input("Ingresar el valor de C: "))

#Procesos...
men = menor(a,b,c)
cuad, cub = cua_cub(men)

#Mostrar el resultado...
print("\nEl menor de los tres valores ingresado es: ",men)
print("El cuadrado del menor es: ", cuad)
print("El cubo del menor es: ", cub)

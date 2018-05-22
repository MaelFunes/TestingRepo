
def comparar():
    if a > p:
        print('El valor', a, 'es mayor...' )

    if b > p:
        print('El valor', b, 'es mayor...')

    if c > p:
        print('El valor', c, 'es mayor...')


def promedio():
    global p
    p = (a + b + c) / 3


a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

promedio()
comparar()

print('Programa terminado...')
max(1,2,key=3,)
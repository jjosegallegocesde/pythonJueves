import math
#menu de opciones
opcion=1

print("Empanadas el machetico")
print("******")
print("0. Salir")
print("1. Encontrar multiplo 2")
print("2. Encontrar raiz cuadrada")
print("3. sumar +100")
print("4. elevar a la 2")

while(opcion != 0):
    opcion=int(input("Bienvenido, digita una opcion: "))
    if(opcion == 1):
        numero=int(input('Digite un número entero: '))
        if(numero % 2 == 0):
            print(f'El número {numero} es multiplo de 2')
        else:
            print(f'El número {numero} no es multiplo de 2')
    elif(opcion == 2):
        numero=int(input('Digite un número entero: '))
        print(f'La razi cuadrada de {numero} es :{math.sqrt(numero)}')
    elif(opcion ==3):
        numero=int(input('Digite un número entero: '))
        print(f'La suma de {numero} + 100 es: {numero + 100}')
    elif(opcion ==4):
        numero=int(input('Digite un numero entero:'))
        print(f'el cuadrado de {numero} es: {numero * numero}')
    elif(opcion == 0):
        break
    else:
        print("Digita una opcion valida")
else:
    print("PARA AHI")
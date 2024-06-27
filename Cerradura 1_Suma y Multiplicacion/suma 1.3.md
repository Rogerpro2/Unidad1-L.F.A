#   Ingresa el primer numero
num1 = float(input("Ingrese el primer número: "))

#   Ingresa el segundo numero
num2 = float(input("Ingrese el segundo número: "))

#   Comparacion para determinar cual es mayor
if num1>num2:
    print("El primer numero ({}) es mayor que el segundo numero ({})".
    format(num1,num2))
elif num1<num2:
    print("El segundo numero ({}) es mayor que el primer numero ({})".
    format(num2,num1))
else:
    print("Ambos numeros son iguales.")

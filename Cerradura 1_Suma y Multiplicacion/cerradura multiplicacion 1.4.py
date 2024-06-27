#   Desarrollo del programa con cerradura de operacion de multiplicacion
print("Cerradura: La suma de dos numeros reales simepre da como resultado otro numero real")
print("a * b pertenece a R ")
print() #  Linea en blanco para separar la introduccion de la siguiente seccion

#   Imprime el mensaje  que indica que el programa demostrara la propiedad de cerradura de multiplicacion
print("El siguiente programa realiza la propiedad de cerradura")
print() #  Linea en blanco para separar la introduccion de la siguiente seccion

#   Solicita al usuario que ingrese dos numeros
num1= int(input("Ingrese el primer numero: ")) #input:Meter datos
num2= int(input("Ingrese el segundo numero: "))

#   Operacion de la multiplicacion de estos dos numeros
multiplicacion = num1 * num2

#   Verificar si la suma es un entero o un numero racional
if multiplicacion.is_integer():
    resultado = "entero"
else:
    resultado = "racional"

#   Mostrar el resultado de la suma y su tipo de resultado
print() # Linea en blanco para separar la introduccion de la siguiente seccion
print("El resultado de la suma es:", multiplicacion)
print("El resultado es un numero:", resultado)

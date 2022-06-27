import os
def comienz(numerouno, segundo, tercero):
    #ciclo repetitivo para ordenar si el numero es mayor o menor
    #en los elif se compara si el numero ingresado por panttalla es menor intermedio o menor
    if numerouno>tercero and numerouno>segundo:
        print("El numero mayor es: ", numerouno) # imprimir el numero mayor
        if tercero>segundo:
            print("El numero intermedio es: ", tercero)
            print("El numero menor es: ", segundo)

        elif segundo>tercero:
            print("El numero intermedio es: ", segundo) # imprimo el numero intermedio
            print("El numero menor es: ", tercero)

    elif segundo>numerouno and segundo>tercero:
        print("El numero mayor es: ", segundo)# imprimo el numero mayor
        # compara el primer numero si es mayor al tercer numero
        if numerouno>tercero:
            print("El numero intermedio es: ", numerouno)# imprimo el numero intermedio
            print("El numero menor es: ", tercero)# imprimo el numero menor
        # compara si el tercer numero es mayor que el primer numero
        elif tercero>numerouno:
            print("El numero intermedio es: ", tercero)
            print("El numero menor es: ", numerouno)

    elif tercero>numerouno and tercero>segundo:
        print("El numero mayor es: ", tercero)

        if numerouno>segundo:
            print("El numero intermedio es: ", numerouno)
            print("El numero menor es: ", segundo)

        elif segundo>numerouno:
            print("El numero intermedio es: ", segundo)
            print("El numero menor es: ", numerouno)
    else:
        # es caso de que haya numero iguales imprimimos lo siguiente
        print("Hay numeros iguales")

# mostrar por pantalla un mensaje pidiendo los numeros
primerN=int(input("ingre un numero: "))
segundoN=int(input("ingrese otro numero: "))
terceroN=int(input("Ingrese otro numero: "))
comienz(primerN, segundoN, terceroN)
#terminar el programa
os.system("pause")
# vacales-de-una-frase
ejemplo de cuantas vocales hay en una frase paython 
def frase_ingresadas():
    #DECLARAMOS Variable GLOBAL
    global texto
    #EL LOWER NOS PERMITE QUE LAS PALABRAS SALGAN EN MINUSCULAS, NO AFECTA EN NADA LA PROGRAMACION SI LO RETIRAS.
    texto=(input("***** INGRESE UNA FRASE O PALABRA: *****")).lower()
    #definir las vocales
def vocales_ingresadas():
    vocal=["a","e","i","o","u","á","é","í","ó","ú"]
    cont=0
    #BUCLE REPETITIVO DE FOR: PARA EL CONTEO DE CUANTAS VOCALES HAY EN LA FRASE INGRESADA POR TECLADO.
    for i in vocal:
        for j in texto:
            if (i==j):
                cont+=1
    #PRESENTAR POR MENSAJE EL RESULTAO DE CUANTAS VOCALES HAY EN LA FRASE INGRESADA,
    print("--EL NUMERO DE VOCALES QUE TIENE LA FRASE:--",texto,"--ES DE:--",cont)
frase_ingresadas()
vocales_ingresadas()

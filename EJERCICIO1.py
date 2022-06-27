import os
def impr_comun(INICI):

	print('>', INICI)

def Nprimo(NUM):
	#BUCLE REPETITIVO PARA HACER LA OPERACION SI ES PRIMO O NO
	if NUM < 2:
		return False
	for Y in range(2, NUM):

		if NUM % Y == 0:
			return False
	return True

def INICIO():
	COMIENZ = True
	#BUCE REPETITIVO WHILE PARA MOSTAR POR PANTALLA LOS MENSAJES RESPECTIVO
	while COMIENZ:
		try:
            #MENSAJE POR PANTALLA PARA INGRESAR EL PRIMER NUMERO
			num = int(input('INGRESE UN NUMERO: '))

			while not(Nprimo(num)):

            #MENSAJE PARA PEDIR OTRO NUMERO
				num = int(input('INGRESE OTRO NUMERO: '))

            #MENSAJE POR PANTALLA CUANDO DECTETE QUE EL NUMERO INGRESADO ES PRIMO
			impr_comun("EL NUMERO QUE USTED HA INGRESADO ES PRIMO")
			COMIENZ = False
		except ValueError:
			print("NO INGRESE LETRAS SOLO NUMEROS POR FAVOR")
INICIO()
#FINALIZAR
os.system("pause")
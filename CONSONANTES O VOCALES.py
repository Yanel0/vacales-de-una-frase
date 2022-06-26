print('*GRUPO 12', '\nRAPHAEL ANDRES CARBO ESPIN', '\nDIEGO ELIAS PIGUAVE LAJE', '\nRIKY JHOEL RONQUILLO CRESPIN',
      '\nYANELA CRISTINA BENALCAZAR DOMINGUEZ', '\nRICARDO JEREMY VERA RECALDE')
import datetime
import os


class Persona:
    def declarar(self):
        self.nombre = input("INGRESE EL NOMBRE DE LA PERSONA")
        self.apellido = input("INGRESE EL APELLIDO")

        año = int(input("INGRESE EL AÑO DE NACIMIENTO"))
        while (año > 2022 and año < 1000):
            año = int(input("INGRESE UN AÑO VALIDO MAYOR A 2022 Y MENOR A 1000"))

        mes = int(input("INGRESE EL MES DE NACIMIENTO (NUMERICO)"))
        while (mes > 12 or mes < 1):
            mes = int(input("INGRESE UN MES VALIDO"))

        dia = int(input("INGRESE EL DIA DE NACIMIENTO"))
        while (dia > 31 or dia < 1):
            dia = int(input("INGRESE UN DIA VALIDO (DEL 1 HASTA EL 31)"))

        self.nacimiento = datetime.date(año, mes, dia)
        self.Cal_edad()

    def Cal_edad(self):
        self.edad = 0
        hoy = datetime.date.today()
        naci = self.nacimiento.year
        while (naci < hoy.year):
            self.edad += 1
            naci += 1
        if (self.nacimiento.month > hoy.month):
            self.edad -= 1
        elif (self.nacimiento.month == hoy.month):
            if (self.nacimiento.day > hoy.day):
                self.edad -= 1

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Fecha de Nacimiento: ", self.nacimiento)
        print("Edad: ", self.edad)


class medico(Persona):
    def __init__(self):
        self.declarar()
        self.especialidad = input("INGRESE SU ESPECIALIDAD ")
        self.celular = input("INGRESE SU NUMERO TELEFONICO")
        self.codigo = input("INGRESE EL CODIGO DE REGISTRO PROFESIONAL")
        self.sueldo = int(input("INGRESE EL SUELDO MENSUAL"))

    def mostrardatos(self):
        self.mostrar()
        print("Especialidad: ", self.esp)
        print("Celular: ", self.cel)
        print("Codigo: ", self.cod)
        self.sueldoAnual = self.sueldo * 12
        print("Sueldo Anual sin Impuestos: ", self.sueldoAnual)
        if (self.sueldoAnual > 48000):
            self.impuestos = self.sueldoAnual * 0.10
        elif (self.sueldoAnual >= 30000):
            self.impuestos = self.sueldoAnual * 0.045
        else:
            self.impuestos = self.sueldoAnual * 0.025
        print("Impuestos: ", self.impuestos)
        print("Sueldo Anual: ", self.sueldoAnual - self.impuestos)

    @property
    def esp(self):
        return self.especialidad

    @esp.setter
    def esp(self, esp2):
        self.especialidad = esp2

    @property
    def cel(self):
        return self.celular

    @cel.setter
    def cel(self, cel2):
        self.celular = cel2

    @property
    def cod(self):
        return self.codigo

    @cod.setter
    def cod(self, cod2):
        self.codigo = cod2

    @property
    def suel(self):
        return self.sueldo

    @suel.setter
    def suel(self, suel2):
        self.sueldo = suel2


class enfermero(Persona):
    def __init__(self):
        self.declarar()
        self.especialidad = input("INGdef bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
def bubbleSort( array ):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array [ j + 1]:
                auxi = array[j]
                array[j] = array[ j + 1]
                array[ j + 1] = auxi

    return array


scores = [2, 9, 5, 8, 12, 4, 7, 25]
print("antes de ordenar: ")
print(scores)
print("ordenado: ")
print( bubbleSort(scores))
RESE SU ESPECIALIDAS su especialidad")
        self.experencia = input("ESCRIBA SU EXPERIENCIA PROFESIONAL")


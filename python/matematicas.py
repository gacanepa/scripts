# Nombre del archivo: matematicas.py
# Propósito: Generar ejercicios matemáticos (suma y resta con dificultad, ordenar números de menor a mayor, etc) aleatorios.
# Licencia: GPL v3 (http://www.gnu.org/licenses/gpl.html)

# Autor: Gabriel Alejandro Cánepa
# Facebook / Skype / G+ / Twitter / Github: gacanepa

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# HISTORIAL DE REVISIONES
# FECHA	      VERSIÓN  AUTOR 	         DESCRIPCIÓN
# ----------  -------  --------------  ------------------
# 2017-05-13  1.0      Gabriel Cánepa  Versión inicial	

# Importar librerías
import random, sys

# Saludo inicial
print('¡Hola! ¿Cómo es tu nombre?')

# Variable para guardar el nombre
nombre = input()

# Segundo saludo
print('¡Vamos a practicar matemáticas, ', nombre + '!')

# Presentación del menú
print('Para elegir una operación, ingresá el número correspondiente:')
print('1 - Suma')
print('2 - Resta')
print('3 - Ordenar números de menor a mayor')
print('4 - Armar números')
print('5 - Desarmar números')
operacion = input()

# Números aleatorios para las operaciones de suma y resta
primerNumero = random.randrange(1, 2500)
segundoNumero = random.randrange(1, 2500)

# Función suma
def suma(numero1, numero2):
    print('¿Cuál es el resultado de la suma de', primerNumero, 'más ' + str(segundoNumero) + '?')
    respuesta = input()
    resultadoSuma = primerNumero + segundoNumero
    if int(respuesta) == resultadoSuma:
        input('¡Felicitaciones! La respuesta es correcta.')
    else:
        input('La respuesta correcta era ' + str(resultadoSuma) + '. Volvé a intentarlo.')

# Función resta
def resta(numero1, numero2):
    if numero1 >= numero2:
        resultadoResta = numero1 - numero2
        print('¿Cuál es el resultado de la resta de', numero1, 'menos ' + str(numero2) + '?')
    else:
        resultadoResta = numero2 - numero1
        print('¿Cuál es el resultado de la resta de', numero2, 'menos ' + str(numero1) + '?')
    respuesta = input()  
    if int(respuesta) == resultadoResta:
        input('¡Felicitaciones! La respuesta es correcta.')
    else:
        input('La respuesta correcta era ' + str(resultadoResta) + '. Volvé a intentarlo.')

# Función para generar números para ordenar
def ordenarNumeros(cantNumeros, desdeNumero, hastaNumero):
    listaNumeros = []
    listaOrdenada = []
    i = 0
    while i < int(cantNumeros):
        listaNumeros.append(random.randrange(int(desdeNumero), int(hastaNumero)))
        i = i + 1
    print('Ordená los siguientes números de menor a mayor:')
    for j in range(0, len(listaNumeros)):
        print(listaNumeros[j])
    input('Cuando hayas terminado, presioná Enter para verificar la respuesta.')
    for i in sorted(listaNumeros):
        print(i)
    input('Presiona Enter para salir')

# Función para armar números (recomposición)
def armarNumero(numero):
    numeroALista = list(str(numero))
    print('Vamos a armar el número compuesto por: ')
    for i in range(1, len(numeroALista)+1):
        numeroActual = str(numeroALista[i-1])+'0'*(len(numeroALista)-i)
        print(numeroActual.rjust(len(numeroALista)))
    print('Ahora ingresá el resultado:')
    resultado = input()
    if numero == int(resultado):
        input('¡Felicitaciones! La respuesta es correcta.')
    else:
        input('La respuesta correcta era ' + str(numero) + '. Volvé a intentarlo.')

# Función para desarmar números (descomposición)
def desarmarNumero(numero):
    numeroALista = list(str(numero))
    print('Vamos a descomponer el siguiente número: ' + str(numero))
    input('Cuando hayas terminado, presioná Enter para verificar la respuesta.')
    for i in range(1, len(numeroALista)+1):
        numeroActual = str(numeroALista[i-1])+'0'*(len(numeroALista)-i)
        print(numeroActual.rjust(len(numeroALista)))

# Estructura para determinar la operación a realizar
if int(operacion) == 1:
    suma(primerNumero, segundoNumero)
elif int(operacion) == 2:
    resta(primerNumero, segundoNumero)
elif int(operacion) == 3:
    print('¿Cuántos números querés?')
    cuantosNumeros = input()
    print('¿Desde qué número?')
    numeroInicial = input()
    print('¿Hasta qué número?')
    numeroFinal = input()
    ordenarNumeros(cuantosNumeros, numeroInicial, numeroFinal)
elif int(operacion) == 4:
    numeroParaArmar = random.randrange(1000, 9999)
    armarNumero(numeroParaArmar)
elif int(operacion) == 5:
    numeroParaDesarmar = random.randrange(1000, 9999)
    desarmarNumero(numeroParaDesarmar)

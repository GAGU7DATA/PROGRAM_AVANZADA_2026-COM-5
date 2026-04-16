#EJERCICIO 3
# Definir una función denominada retorno_mensaje que retorne siguiente mensaje:
#“Estudiando en la UNAB”.
#A. ¿Cómo hago para mostrar ese mensaje en pantalla?
#B. ¿Qué diferencia encuentra con el ejercicio anterior?
#C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAB“ y
#“Estudiando Python en la UNAB” utilizando la misma función ¿Cómo la modificarías?

def retorno_mensaje():
    return "Estudiando en la UNAB!"
print(retorno_mensaje())

def retorno_mensaje2(materia):
    return f"Estoy estudiando {materia} en la UNAB!"
print(retorno_mensaje2("Programación Avanzada!"))
print(retorno_mensaje2("Paradigma de Programación Orientada a Objetos!!!"))
print(f"\033[91m{'='*60}\033[0m")

# EJERCICIO 4
# Definir una función denominada imprimo_fecha que reciba tres cadenas de caracteres
#como parámetros formales, que representan un día, un mes y un año e imprima la fecha de la
#siguiente manera: “ 21 de septiembre de 2025”.
def imprimo_fecha(dia, mes, año):
    return f"{dia} de {mes} de {año}"   

print(imprimo_fecha("21", "septiembre", "2025"))
print(imprimo_fecha("07", "Mayo", "1978")) 
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 5
# Definir una función denominada cuantos_dias que reciba el número de mes como
#parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1), debería retornar 31.
#Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31], [“febrero”, 28], [“marzo”, 31], [“abril”, 30], [“mayo”, 31], [“junio”, 30], [“julio”, 31], [“agosto”, 31], [“septiembre”, 30], [“octubre”, 31], [“noviembre”, 30], [“diciembre”, 31]].
def cuantos_dias(mes):
    meses = [
        ["Enero", 31], ["Febrero", 28], ["Marzo", 31],
        ["Abril", 30], ["Mayo", 31], ["Junio", 30],
        ["Julio", 31], ["Agosto", 31], ["Septiembre", 30],
        ["Octubre", 31], ["Noviembre", 30], ["Diciembre", 31]
    ]
    
    nombre = meses[mes - 1][0]
    dias = meses[mes - 1][1]
    
    return f"El mes {mes} corresponde a {nombre} y tiene {dias} días"

# Programa principal
n = int(input("Ingrese un número de mes: "))
print(cuantos_dias(n))
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 6
#Definir una función que reciba un número como parámetro y mostrar la tabla de multiplicar de dicho número.

def tabla_multiplicar(numero):
    for i in range(0, 10):
        print(numero, "x", i, "=", numero * i)

n = int(input("Ingrese un número: "))
tabla_multiplicar(n)
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 7
#Definir una función que calcule el área de un círculo, otra que calcule el área de un rectángulo y
#otra que calcule el área de un cuadrado. Analice qué parámetros deberían recibir dichas funciones.

def area_circulo(radio):                                      # para averiguar el área de un círculo, se necesita el radio, por lo tanto la función recibe un parámetro llamado radio.
    import math                                               # se importa la biblioteca math para poder utilizar la constante pi, que es necesaria para calcular el área del círculo.
    return math.pi * radio ** 2

def area_rectangulo(base, altura):                            # para averiguar el área de un rectángulo, se necesita la base y la altura, por lo tanto la función recibe
    return base * altura                                      # dos parámetros llamados base y altura.

def area_cuadrado(lado):                                      # para averiguar el área de un cuadrado, se necesita uno de los lados, por que son los 4 iguales por lo tanto la función recibe un 
    return lado ** 2                                          #parámetro llamado lado.
    
radio = float(input("Ingrese el radio del círculo: "))      
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))     
lado = float(input("Ingrese el lado del cuadrado: "))

print("El área del círculo es:", area_circulo(radio))
print("El área del rectángulo es:", area_rectangulo(base, altura))          
print("El área del cuadrado es:", area_cuadrado(lado))
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 8
#Definir una función llamada calculo_rebaja que reciba dos números, uno con el precio
#anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje rebajado.

def calculo_rebaja(precio_ant, nuevo_precio):
    if nuevo_precio > precio_ant:
        return "Error: el precio rebajado no puede ser mayor al original"
    
    porcentaje_rebaja = (1 - (nuevo_precio / precio_ant)) * 100
    return f"{porcentaje_rebaja:.2f}"

precio_ant= float(input("Ingrese el precio anterior: "))
nuevo_precio = float(input("Ingrese el precio rebajado: "))
print("El porcentaje de rebaja es:", calculo_rebaja(precio_ant, nuevo_precio), "%")
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 9
#Definir una función llamada calculo_nuevo_precio que reciba dos números, uno con el
#precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.

def precio_final(precio_ant, porcentaje_aumento):
    nuevo_precio = precio_ant * (1+(porcentaje_aumento / 100))
    return f"{nuevo_precio:.2f}"
precio_ant = float(input("Ingrese el precio anterior: "))
porcentaje_aumento = float(input("Ingrese el porcentaje a aumentar: ")) 
print("El nuevo precio es:", precio_final(precio_ant, porcentaje_aumento))
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 10
#Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad
#de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del
#transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión
#sabiendo que cada salita es acompañada por tres adultos.

def transp(sal_1, sal_2, sal_3, asientos):
    total_alumnos = sal_1 + sal_2 + sal_3
    total_adultos = 9
    total_personas = total_alumnos + total_adultos
    micros_necesarios = (total_personas + asientos - 1) // asientos
    return micros_necesarios    
sal_1 = int(input("Ingrese la cantidad de alumnos de 1era salita: "))
sal_2 = int(input("Ingrese la cantidad de alumnos de 2da salita: "))            
sal_3 = int(input("Ingrese la cantidad de alumnos de 3er salita: "))
asientos = int(input("Ingrese la cantidad de asientos del transporte escolar: "))
print("La cantidad de micros necesarios para la excursión es:", transp(sal_1, sal_2, sal_3, asientos))
print(f"\033[91m{'='*60}\033[0m")

#EJERCICIO 11
#Definir una función llamada armo_cartel que reciba una cadena de caracteres (para el
#nombre del producto) y dos números (el precio anterior y el otro para el precio rebajado) e imprima
#un cartel de la siguiente forma:
#*************************************
#Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)
#Antes: precio anterior (dato recibido como parámetro)
#Ahora: precio rebajado (dato recibido como parámetro)
print (" ")
red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
cyan = "\033[96m"
nor = "\033[0m"

def cartel(producto, precio_ant, precio_nuevo):
    print(f"{cyan}{'='*60}{nor}")
    print(f"  Atención!!! Gran rebaja para el producto {producto}")
    print(f"                  {red}Antes: $ {precio_ant}{nor}")
    print(f"                  {green}Ahora: $ {precio_nuevo}{nor}")
    print(f"{cyan}{'='*60}{nor}")

producto = input("Ingrese el nombre del producto: ")
precio_ant = float(input("Ingrese el precio anterior: "))       
precio_nuevo = float(input("Ingrese el precio rebajado: "))

cartel(producto, precio_ant, precio_nuevo)
print(f"\033[91m{'='*60}\033[0m")

# EJERCICIO 12
#Definir una función llamada calculo_litros que reciba tres números, el alto, ancho y
#profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.

def calculo_litros(alto, ancho, profundidad):
    volumen_metros_cubicos = alto * ancho * profundidad
    litros = volumen_metros_cubicos * 1000
    return litros   

alto = float(input("Ingrese el alto de la pileta en metros: "))
ancho = float(input("Ingrese el ancho de la pileta en metros: "))       
profundidad = float(input("Ingrese la profundidad de la pileta en metros: "))
print("La cantidad de litros que tiene la pileta es:", calculo_litros(alto, ancho, profundidad), "litros")
print(f"\033[91m{'='*60}\033[0m")

# EJERCICIO 13
#Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el
#monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le
#toca pagar a cada uno.

def a_pagar(personas, bebida, comida, alquiler):
    gasto_total = bebida + comida + alquiler
    pago_indiv = gasto_total  / personas
    return pago_indiv

personas = int(input("Ingrese la cantidad de personas: "))
bebida = float(input("Ingrese el monto gastado en bebida:$ "))
comida = float(input("Ingrese el monto gastado en comida:$ "))
alquiler = float(input("Ingrese el monto del alquiler:$ "))

print("Cada persona debe pagar:$", a_pagar(personas, bebida, comida, alquiler))
print(f"\033[91m{'='*60}\033[0m")   

# EJERCICIO 14 
#Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real.
#Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión
#respectiva.
def dolar(pesos):
    return pesos / 1395
def euro(pesos): 
    return pesos / 1607.01
def real(pesos):
    return pesos / 273.97
pesos = float(input("Ingrese el monto en pesos: $ "))
print("El monto en dólares es: u$s ", dolar(pesos)) 
print("El monto en euros es:    €  ", euro(pesos))
print("El monto en reales es:   R$ ", real(pesos)) 
print(f"\033[91m{'='*60}\033[0m")

# EJERCICIO 15
#Definir una función llamada calculo_dosis que reciba tres números. Uno para la
#cantidad de días que debe suministrar el remedio, el segundo dato para la cantidad de veces por
#día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La
#función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.

red = "\033[91m"
green = "\033[92m"
nor = "\033[0m"
def calculo_dosis(dias, veces_por_dia, comprimidos_por_envase):
    dosis_total = dias * veces_por_dia
    return dosis_total <= comprimidos_por_envase    
dias = int(input("Ingrese la cantidad de días que debe suministrar el remedio: "))
veces_por_dia = int(input("Ingrese la cantidad de veces por día que debe tomarlo: "))
comprimidos_por_envase = int(input("Ingrese la cantidad de comprimidos que trae el envase: "))
if calculo_dosis(dias, veces_por_dia, comprimidos_por_envase):
    print(f"{green}El envase alcanza para el tratamiento.{nor}") 
else:
    print(f"{red}El envase no alcanza para el tratamiento.{nor}")
print(f"\033[91m{'='*60}\033[0m")

# EJERCICIO 16
#Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto dado su precio de venta sin IVA.
def precio_final(precio_bruto):
    iva = precio_bruto * 1.21
    precio_final = iva
    return precio_final
print(f"\033[91m{'='*60}\033[0m")
precio_bruto = float(input("Ingrese el precio de venta sin IVA: $ "))
print("El precio con IVA incluido es: $", precio_final(precio_bruto))   
print(f"\033[91m{'='*60}\033[0m")


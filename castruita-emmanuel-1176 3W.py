
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta 
#1-2 1.- Capturar tu nombre dándole valor a las variables que correspondan por separado y desplegar cada una de las variables que conforman tu nombre Concatenar y desplegarlo empezando por el Apellido Paterno
a=("Castruita")# se definira variable a como castruita 
b=("Soto")# se definira variable b como soto
z=("Emmanuel")# se definira variable z como emmanuel
c = a+" " +" "+ b+" " +z #la variable z se definira como la suma de las otra vriables implimiendo haci el nombre y las " se usan para dejar un espacio entre cad vriable 
print(c)# se implimira la variante c en pntalla
print("")# servira como un espacio cuando el codigo se ejecuta 

#3 3.- Convertir todo ese string en Mayúsculas y desplegarlo
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
w=("Castruita")# se definira variable a como castruita 
q=("Soto")# se definira variable b como soto
r=("Emmanuel")# se definira variable z como emmanuel


print(w.upper())#uppper es una comando que transforma un testo en minuscolas en mayusculas en este casa el testo es la variable w
print(q.upper())#uppper es una comando que transforma un testo en minuscolas en mayusculas en este casa el testo es la variable q
print(r.upper())#uppper es una comando que transforma un testo en minuscolas en mayusculas en este casa el testo es la variable r
print("")# servira como un espacio cuando el codigo se ejecuta 

#4.- Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables: A, B y C respectivamente.
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
print("ingresa valor de a")#se le da una instruccion al usuario mediante el texto impleso por print
a =("ingresa valor de a")#se implimira el mensaje de ingrese valor de a
a= int(input("Ingresa un número: "))#se le solicitara y se leera el tanto que es usuario ingrese por comando imput
print("ingresa valor de b")#se le da una instruccion al usuario mediante el texto impleso por print
b=("ingresa valor de b")#se implimira el mensaje de ingrese valor de b
b= int(input("Ingresa un número: "))#se le solicitara y se leera el tanto que es usuario ingrese por comando imput
print("ingresa valor de c")#se le da una instruccion al usuario mediante el texto impleso por print
c =("ingresa valor de c")#se implimira el mensaje de ingrese valor de c
c= int(input("Ingresa un número: "))#se le solicitara y se leera el tanto que es usuario ingrese por comando imput

if a > b > c:# if es como la condicion a cumplir aqui es si a es mayor b y mayor que se parara la siguiente linea 
    print("a es el mayor y c es el menor")#esta sentencia  se ejecuta 
elif b > c > a:#elif es por si no se se cumple la 1 condicion es como un o sino  si esta se cumple se ejecutara la siguiente linea
     print("b es el mayor y a el menor")#esta sentencia se ejecutara
elif c > a > b:#elif es por si no se se cumple la 2 condicion es como un o sino  si esta se cumple se ejecutara la siguiente linea
     print("c es el mayor y b el menor")#esta sentencia  se ejecuta 
elif c == a == b:#este elif solo se ejecutara si los numeros son iguale y mandara el siguiente mensaje de la proxima linea
     print("los valores son iguales ingrese otros")#esta sentencia se se ejecuta 
print("")# servira como un espacio cuando el codigo se ejecuta

#5 Desarrollar código que lea dos valores que captures, determinar cual de los dos valores es elmenor y escríbalo. Realizar un algoritmo que sume dos números y desplegarlo
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
print("ingresa valor de a")#se solicitara el valor de a en mensaje por print
a=("ingresa valor de a")#se solicitara el valor de b junto con el comando de la proxima linea en mensaje por print
a= int(input("Ingresa un número: "))#se introduce el numero
print("ingresa valor de b")#se solicitara el valor de a en mensaje por print
b =("ingresa valor de b")#se solicitara el valor de b junto con el comando de la proxima linea en mensaje por print
b= int(input("Ingresa un número: "))#se introduce el numero


if a > b  :# if es como la condicion a cumplir aqui es si a es mayor b y mayor que se parara la siguiente linea 
    print(" b es el menor")#esta sentencia  se ejecuta 
elif  b > a:#elif es por si no se se cumple la 2 condicion es como un o sino  si esta se cumple se ejecutara la siguiente linea
     print(" a el menor")#esta sentencia  se ejecuta 
elif a == b:
     print("los valores son iguales ")#esta sentencia se se ejecuta 
print("el resultado de su suma es:")
print(a + b)
print("")# servira como un espacio cuando el codigo se ejecuta 
#6 Hallar el perímetro y el área de un rectángulo ingresando la baseb y la altura h.
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
print("responde lo siguiente para sacar el perimetro rectangulo")#se solicitara dato por medio de comando print
print("ingresa valor de longitud ")#se solicitara dato por medio de comando print
L = int(input("Ingresa longitud: "))#se introduce el numero
print("ingresa valor de lo ancho ")#se solicitara dato por medio de comando print
w = int(input("Ingresa ancho: "))#se introduce el numero
print("perimetro es igual ")#se escribira el mensaje de resultado por medio de print
print(2*L+2*w)#se selecciona la operacion a realizar
print("")# servira como un espacio cuando el codigo se ejecuta
print("responde lo siguiente para sacar el area de un rectangulo")#se solicitara dato por medio de comando print
m = int(input("Ingresa longitud: "))#se introduce el numero
print("ingresa valor de longitud ")#se solicitara dato por medio de comando print
print("ingresa valor de ancho  ")#se solicitara dato por medio de comando print
e = int(input("Ingresa ancho: "))#se introduce el numero
print("area es igual ")#se escribira el mensaje de resultado por medio de print
print(m*w)#se selecciona la operacion a realizar
print("")# servira como un espacio cuando el codigo se ejecuta

#7 Solicitar al usuario un número natural y verificar que el número ingresado se encuentre dentro de la primera docena de números naturales,es decir entre el 1 y el 12.
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
print("ingresa un numero natural de los primeros 12")#se solicita un numero por print con especificacion que sean los primeros 12
a=("ingresa tu numero ")#se solicita un numero por comando print
a= int(input("Ingresa un número: "))#se introduce el numero
if a > 12 :# if es como la condicion a cumplir aqui es si a es mayor b y mayor que se parara la siguiente linea 
    print(" no es el dato solicitado ")#esta sentencia  se ejecuta 
elif  a<=12 :#elif es por si no se se cumple la 1 condicion es como un o sino  si esta se cumple se ejecutara la siguiente linea
     print(" el numero ingresado si es natural entre el 1 y el 12")#esta sentencia  se ejecuta 
print("")# servira como un espacio cuando el codigo se ejecuta

#8 Ingresar un número natural por teclado. Se desea saber y mostrar si es par o impar.
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
# Ingresar un número natural
numero = int(input("Ingresa un número natural: "))  # Solicita al usuario un número y lo convierte a entero

# Verificar si es par o impar
if numero % 2 == 0:  # Si el residuo de la división entre 2 es 0, es par
    print("es par.")  # Imprime que el número es par
else:#sino se cumple condicion una se una esta y se implime lo siguiente
    print("es impar.")  # Imprime que el número es impar
print("")# servira como un espacio cuando el codigo se ejecuta

#9  Ingresar un número entero para saber si es divisible por 7 y es mayor a 40.
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
# Ingresar un número entero
numero = int(input("Ingresa un número entero: "))  # Solicita un número al usuario

# Verificar si es divisible por 7 y mayor a 40
if numero > 40 and numero % 7 == 0:  # Comprueba las dos condiciones
    print(f"{numero} es divisible por 7 y es mayor a 40.")  # Imprime si cumple
else:# sino se cumple uno se usa esta
    print(f"{numero} no cumple con las condiciones.")  # Imprime si no cumple
print("")# servira como un espacio cuando el codigo se ejecuta

#10 El factorial de un número entero se denota de la siguiente manera«n!» y su resultado es n!=n*(n-1)*(n-2)*…*1. Por ejemplo: 5!=5*4*3*2*1siendo el resultado 120. Se pide desarrollar un programa que lee un valor N y determine su factorial.
print("")# servira como un espacio cuando el codigo se ejecuta 
print("Emmanuel Castruita Soto 3W ") #se implira en pantalla el mensaje escrito
print("")# servira como un espacio cuando el codigo se ejecuta
# Ingresar un número entero
numero = int(input("Ingresa un número entero para calcular su factorial: "))  # Solicita un número al usuario

# Inicializar el factorial en 1
factorial = 1  # El factorial se inicia en 1

# Verificar si el número es negativo
if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")  # Mensaje para números negativos
else:#sino se cumple variacion 1 seguira esta
    # Calcular el factorial usando un bucle
    for i in range(1, numero + 1):  # Itera desde 1 hasta el número ingresado (inclusive)
        factorial *= i  # Multiplica el factorial por i

    # Mostrar el resultado
    print("El factorial de", numero, "es", factorial)  # Imprime el resultado final


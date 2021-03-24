import math

i=1

while i<=10:
	print("Ejecucion" + str(i))
	i=i+1

print("Termino la ejecucion")

edad=int(input("Introduce la edad: "))
while edad<0 or edad>100:
	print("Edad incorrecta")
	edad=int(input("Introduce la edad: "))

print("Gracias por colaborar")
print("Edad del aspirante" + str(edad))

#este es otro programa
print("Programa de calculo de raiz cuadrada")
num = int(input("Introduce un numero: "))
intentos=0
while num <0:
	print("No se permite numeros negativos")

	if intentos==2:
		print("Demasiados intentos")
		break;

	num=int(input("Introduce un numero: "))
	if num<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(num)
	print("La raiz cuadrada es: " + str(solucion))

#este es otro programa
for letra in "Python":
	if letra=="h":
		continue

	print("Viendo la letra: " + letra)

#este es otro programa
nombre="karlos Avila"
contador=0

for i in nombre:
	if i == " ":
		continue
	contador+=1

print(contador)
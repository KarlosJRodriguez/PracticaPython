n1 = int(input("Ingrese un numero"));
tablas = [1,2,3,4,5,6,7,8,9,10]

for i in tablas:
	print(" ",n1 * i);


for j in ["Primavera","Verano", "Otoño","Invierno"]:
	print(j); #imprimira la lista de datos

for k in ["Primavera","Verano", "Otoño","Invierno"]:
	print("Hola");#imprimira 4 veces hola

for l in "karlos":
	print("hola");#imprime hola por cada letra del string

email=False;
for i in "karlos@gmail.com":
	if(i == "@"):
		email = True;

if email == True:
	print("Correcto");
else:
	print("incorrecto")

email2=False;
correo = input("Ingresa direccion de correo");
for i in correo:
	if(i == "@"):
		email2 = True;

if email2 == True:
	print("Correcto");
else:
	print("incorrecto")

for i in range(3):
	print("Hola")


	'''
bucle for recorre tuplas listas y cadenas de caracteres
no tienen un contador como vb o c#
	'''
for r in range(5,50,2):
	print(f"valor de la variable {r}")

valido=False
email3=input("Introduce tu email: ")
for h in range(len(email3)):
	if email3[i]=="@":
		valido=True

if valido:
	print("Correcto")
else:
	print("Incorrecto")

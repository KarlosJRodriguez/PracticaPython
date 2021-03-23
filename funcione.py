'''def mensaje(): #funcion
	print("Estamos aprendiendo python");
	print("Estamos aprendiendo instrucciones basicas");
	print("Poco a Poco iremos avanzando");

mensaje(); #llamada de funcion
print("Ejecutando codigo fuera de funcion");
mensaje();'''

def suma(num1, num2):
	suma=num1 + num2;
	resta=num1 - num2;
	multi=num1 * num2;
	print("La suma es: ",suma);
	print("La resta es: ",resta);
	print("La multiplicacion es: ",multi);

def ope(num1,num2):
	suma=num1+num2;
	return suma

suma(8,5);
print(ope(4,8));
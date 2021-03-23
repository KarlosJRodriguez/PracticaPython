'''print("Programa de evaluacion de notas");
n1=input();

def evaluacion(nota):
	valoracion="aprobado"
	if nota < 70:
		valoracion="Reprobado"
	return valoracion

print(evaluacion(int(n1)))'''

def suma(n1,n2):
	sum = n1 + n2;
	return sum;
def resta(n1,n2):
	return n1 - n2;
'''lower y upper son para poner textos en mayusculas o minusculas'''	

print("===========================");
print("Menu");
print("1. SUMA");
print("2. RESTA");
print("?");
op = int(input("Escoje una opcion: "));
if op == 1:
	print("suma");
	n1 = int(input("Ingresa n1: "));
	n2 = int(input("Ingresa n2: "));
	print(suma(n1,n2));
else:
	print("resta");
	n1 = int(input("Introduce n1: "));
	n2 = int(input("Introduce n2: "));
	print(resta(n1,n2));

print("+++++++++++++++++++++++++++++");
print("Segundo programa de condicional");
print("Carros Disponibles");
print("1 Honda");
print("2 Toyota");
print("?");
opc = int(input("Escoja una opcion"));
if opc == 1:
	print("Modelos");
	print("1 CIVIC");
	print("2 ACCORD");
	print("?");
	mod = int(input("Escoja un modelo"));
	if opc == 1 and mod == 1:
		print("Escojiste un Honda CIVIC");
	elif opc == 1 and mod == 2:
		print("Escojiste un Honda ACCORD");
	else:
		print("No escojiste una opcion valida");
elif opc == 2:
	print("Modelos");
	print("1 COROLLA");
	print("2 YARIS");
	print("?");
	mod = int(input("Escoja un modelo"));
	if opc == 2 and mod == 1:
		print("Escojiste un Toyota COROLLA");
	elif opc == 2 and mod == 2:
		print("Escojiste un Toyota YARIS");
	else:
		print("No escojiste una opcion valida");
else:
	print("No escojiste una opcion valida");
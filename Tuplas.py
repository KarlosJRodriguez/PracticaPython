mitupla=(2,5,4,8,9,7)
milista=list(mitupla)#convierte la tupla a una lista
milista2=[2,5,4,8,5,7]
mitupla2=tuple(milista2);
print(milista[:]);
print(mitupla2.count(5));#count cuenta cuantos valores hay del que estoy buscando
print(len(mitupla2));#len cuenta el total dentro de la tupla o lista

mitupla3=("Karlos",7,3,1996)#esto es un
nombre,dia,mes,anio=mitupla3#desempaquetado de tuplas
print(nombre);#y los permite imprimir una tupla
print(dia);#en el orden prestablecido en la tupla
print(mes);
print(anio);
print(mitupla.index(5));
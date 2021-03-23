arreglo=["Juan","Lucas","Mateo","Pedro"]
arreglo2=[1,2,3,4,5,6,7,8,9] 
arreglo2.remove(5);#remove elimina un elemento de la lista
print(arreglo[0:3]);#el primer digito es el inicio y el ultimo excluye ese dato
print(arreglo2[7]);#accede directamente a un dato
arreglo.append("Moises");#apend ingresa un dato a una lista
arreglo.insert(2,"Ester");#insert me da mas control de donde quiero insertar
print(arreglo)
print(arreglo2.index(4));#index busca el indice
print("Mateo" in arreglo);#in busca el dato en la lista

milista=["Sandra","Lucia"]
milista2=["Maria",9,78]
milista3=milista+milista2; #se unen las dos listas en una sola
print(milista3[:]);
milista4=[5,7,9]* 2 #repite las veces la lista
print(milista4[:]);

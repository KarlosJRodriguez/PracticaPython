midiccionario={"Alemania":"Berlin","Francia":"Paris","España":"Barcelona"}
midiccionario["Italia"]="Lisboa";#para agregar un conjunto mas
print(midiccionario["Alemania"]);
print(midiccionario);
midiccionario["Italia"]="Roma";#se sobreescribe el dato lisboa por roma
print(midiccionario);
del midiccionario["Francia"]#del elimina un dato de un diccionario
print(midiccionario);
midiccionario[23]="Michael";
print(midiccionario);

mitupla=["España","Francia","Alemania"]
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"Monaco",mitupla[2]:"Munich"}
print(midiccionario2["Francia"])

midiccionario3={23:"jordan","Nombre":"Michael","anillos":{"Temporadas":[1991,1992,1993,1997,1998]}}
print(midiccionario3["anillos"])

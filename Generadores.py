#esta es una funcion
def generaPares(limite):
	num=1
	milista=[]
	while num<limite:
		milista.append(num*2)

		num= num+1
	return milista

print(generaPares(10))

#este es un generador
def generaPares2(limite):
	num=1
	while num<limite:
		yield num*2

		num= num+1

devuelvepares=generaPares2(10)
for i in devuelvepares:
	print(i)

#otro generador
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		for sub in elemento:
			yield sub
		yield elemento

ciudades_devueltas=devuelve_ciudades("Barcelona","Sevilla","Zaragoza")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
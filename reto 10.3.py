lista1=[]
lista2=[]
lista3=[]

i= int(input("ingresa la cantidad de elementos: "))
for x in range(i):
    valor=int(input("Ingrese el valor para la lista: "))
    if valor!=0:
     lista1.append(valor)
    else:
      lista2.append(valor)


lista3= lista1+lista2
print("la lista resusltante es "+ str(lista3))
lista1=[]
lista2=[]
nuevalista=[]

i= int(input("ingresa la cantidad de elementos: "))
for x in range(i):
    valor=int(input("Ingrese un valor entero de la primera lista: "))
    lista1.append(valor)

for x in range(i):
    valor=int(input("Ingrese un valor entero de la segunda lista: "))
    lista2.append(valor)

def ProductoPunto(lista1, lista2) -> float:
  productoPunto=0
  n=0
  for n in range (i):
    productoPunto += (lista1[n]*lista2[n])
  return productoPunto
    
if __name__ == "__main__":
    punto = ProductoPunto(lista1, lista2)

print(lista1)
print(lista2)
print("el producto punto de las listas es "+ str(punto) )
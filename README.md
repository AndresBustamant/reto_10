# reto_10
1.Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

- el programa desarrollado funciona a apartir de solicitar al usuario dos cosas la longitud de la lista y la lista en si misma, con el fin de sumar a lartir de la funcion sum(lista) y dividir sobre la longitud dada con anterioridad.

```pseudocode
lista=[]
i= int(input("ingresa la cantidad de elementos de la lista: "))
for x in range(i):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
print("el promedio de la lista es:")
print(sum(lista)/i)
```

2.Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

- para desarrollar este punto me base en el programa anterior ya que se solicita la longitud de las listas y las dos listas en si, esto con el fin de definir una funcion que calcule el producto punto a partir de un ciclo que sumara el producto de los numeros en cierta posicion hasta completar las listas dadas.

```pseudocode
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
```

3.Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

- en este programa tambien me base en el mismo inicio de los porgramas anteriores (solicitar la longitud de la lista y la lista en si) para a partir de una condicional ubicar los valores en dos listas diferentes, una lleva los numero y la otra solo los ceros, y posteriormente unir las dos listas de manera que la lista con los numeros quede primero y la de los ceros quede despues.

```pseudocode
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
```
4 Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

- algoritmos de sorting:
Son algoritmos que fueron realizados para ordenar un conjunto de datos. Los algoritmos varían según su facilidad de entendimiento, su eficiencia, cantidad de código necesario para implementarlos, complejidad, requisitos necesarios de los datos.
  algunos son:
  1.Bubble Sort
  2.algoritmo de ordenamiento por Insercion (Insertsort).
  3.Ordenamiento Quicksort
  4.insertion sort
  5.Heapsort

- bubble-sort:
Bubble Sort es un algoritmo de clasificación simple que se usa comúnmente para ordenar elementos en una lista o matriz. Funciona comparando repetidamente elementos adyacentes e intercambiándolos si están en el orden incorrecto. El algoritmo recorre la lista varias veces hasta que no se necesitan más intercambios, lo que da como resultado una secuencia ordenada. Durante cada iteración, el elemento sin clasificar más grande "burbuja" hasta su posición correcta, de ahí el nombre "Clasificación de burbujas".

![image](https://github.com/AndresBustamant/reto_10/assets/141858005/4c97b749-2478-41f7-8d70-d215b1f4f6e5)

Referencias:
- Algoritmos de ordenamiento. (2013, marzo 27). koketxt. https://koketxt.wordpress.com/unidad-i/algoritmos-de-ordenamient/   
  
- Simplilearn. (2021, julio 8). How to use Bubble Sort in C programming? Simplilearn.com; Simplilearn. https://www.simplilearn.com/tutorials/c-tutorial/c-program-for-bubble-sort
gracias por leer has aqui 

#verificar si hay elementos repetidos en una lista

def repes(lista):

    return len(lista)!= len(set(lista))

lista1=["david","andres","raul","david"]
lista2=["david","andres","raul"]

if (repes(lista1))==True:
    print("hay elementos repetidos")
else:
    print("no hay elementos repetidos")

if (repes(lista2))==True:
    print("hay elementos repetidos")
else:
    print("no hay elementos repetidos")
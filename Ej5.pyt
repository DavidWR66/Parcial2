#encontrar la media de un arreglo
def media(arreglo):

    organizado=sorted(arreglo)
    cont=len(arreglo)/2

    return (organizado(cont))

lista=(2,7,5,9,3,6,2,8)

print("la media del arreglo es",media(lista))

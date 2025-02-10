#cadena de caracteres con dos o mas vocales si existe imprima si no imprimir "no existe"

def vocal(plbra):

    vocales= [letra for letra in plbra if((letra=="a")or(letra=="e")or(letra=="i")or(letra=="o")or(letra=="u"))]
    conta= len(vocales)

    return (conta)

def palabras(lista):

    cont=[pal for pal in lista if (vocal(pal)>=2)]

    return (cont)


lista1=["sol","gas","ummm"]

lista2=["casa","sin","patio"]

if not (palabras(lista1)):
    print("no existe")
else:
    print(palabras(lista1))

if not (palabras(lista2)):
    print("no existe")
else:
    print(palabras(lista2))

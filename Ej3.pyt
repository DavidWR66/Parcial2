#determinar si dos listas comparar y solo los elementos unicos de la primera

def comparacion(lista1,lista2):

    elementos= set(lista1)&set(lista2)
    return(elementos)

nombres=["david", "andres", "wilches", "ramirez", "albarado"]
apellidos=["wilches","albarado","carlos", "raul"]
pseudonimos=["carlos","raul","mauricio"]

if not comparacion(nombres,apellidos):
    print("no hay elementos repetidos")
else:
    print(comparacion(nombres,apellidos))
    
if not comparacion(nombres,pseudonimos):
    print("no hay elementos repetidos")
else:
    print(comparacion(nombres,pseudonimos))
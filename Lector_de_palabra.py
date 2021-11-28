print("Bienvenido al contador de palabras por texto")
palabras=[]
with open("Ejemplo.txt") as fname:
    for palabra in fname:
        palabras.extend(palabra.split())
        print("estas son las palbras separadas por comas")
print(palabras)
print("Pasamos a la fase 2 del programa")
print("Ahora se procede al diccionario")

archivo = open('Ejemplo.txt', 'r')
palabraHash = archivo.read()

if palabraHash is not None:
            palabraHash = palabraHash.replace(",", "")
            palabraHash = palabraHash.replace(".", "")

def printFrequency(palabraHash):
    List = {}
    word = ""
    for i in range(len(palabraHash)):
        if (palabraHash[i] == ' '):
            if (word not in List):
                List[word] = 1
                word = ""
            else:
                List[word] += 1
                word = ""
        else:
            word += palabraHash[i]
    if (word not in List):
        List[word] = 1
    else:
        List[word] += 1
    for i in List:
        print(f"{i}->{List[i]}")
printFrequency(palabraHash)
print("Bienvenido al contador de palabras por texto")
palabra=[]
with open("Texto.txt") as fname:
    for linea in fname:
        palabra.extend(linea.split())
print(palabra)
print("Hasta Luego , Vuelva pronto")
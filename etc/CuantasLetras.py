print("Cual es tu nombre?")
Nombre= input()
def CantidadLetras():
    i = 0
    cont = 0
    palabras = 0
    while i < len(Nombre):
        Letra = Nombre[i]
        if Letra == ' ':
            i += 1
            palabras += 1
        else:
            i += 1
            cont += 1
    return cont
def CantidadPalabras():
    i = 0
    cont = 0
    palabras = 0
    while i < len(Nombre):
        Letra = Nombre[i]
        if Letra == ' ':
            if i == 0:
                i += 1
                palabras = 0
            else:
                i += 1
                if palabras >=1:
                    palabras += 1
                else:
                    palabras = 1
                    palabras += 1
        else:
            i += 1
            cont += 1
    return palabras
print("Hola "+Nombre+", tu nombre tiene "+str(CantidadLetras())+" letras dentro de "+str(CantidadPalabras())+" palabras.")
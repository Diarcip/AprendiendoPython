print("Cual es tu nombre?")
Nombre= input()

#CONTAR LETRAS EN LA FRASE INGRESADA

def CantidadLetras():
    i = 0
    contLetras = 0
    while i < len(Nombre):
        Letra = Nombre[i]
        if Letra == ' ':
            i += 1
        else:
            i += 1
            contLetras += 1
    return contLetras

#CONTAR PALABRAS EN LA FRASE INGRESADA
def CantidadPalabras():
    i = 0
    contPalabras = 0
    while i < len(Nombre):
        Letra = Nombre[i]
        if Letra == ' ': #Valida si la letra es un espacio ' '
            if i == 0: #Valida si el espacio es el primer caracter
                i += 1
                contPalabras = 0
            elif Nombre[i-1] == ' ':#Valida si el caracter anteriormente analizado fue un espacio
                i += 1
            else: #Si no hay dos o mas espacios consecutivos...
                i += 1
                contPalabras += 1
        else:
            i += 1
    if Nombre[i-1] != ' ' and Nombre[i-1] == Nombre[-1]:
        #Valida si la ultima letra no es espacio para incrementar en 1 el numero de palabras
        contPalabras += 1
    if contPalabras == 0 and CantidadLetras() > 0:
        #Si en el bucle anterior no encontró 2 o mas palabras, valida que la cantidad de letras de la funcion CantidadLetras sea mayor a 1 y asi asignar el valor de 1 a la variable contPalabras
        contPalabras = 1
    return contPalabras

#IMPRIMIR RESULTADO

print("Hola "+Nombre+", tu nombre tiene "+str(CantidadLetras())+" letras dentro de "+str(CantidadPalabras())+" palabras.")
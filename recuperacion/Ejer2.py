from collections import Counter
#importo libreria que me fue util para el ejercicio

def contfrecuencia():

    #leo cadena de caracteres
    cadena = input("Escriba su cadena de palabras: ")
    #divido la cadena por palabras ej: Hola como estas -> hola/como/estas
    cadenaPar = cadena.split()

    #Uso la funcion de la libreria collection
    #contador = variable que uso para guardar
    #??? = dict counter
    contador = dict(Counter(cadenaPar))

    print (contador)    
    #llamo la funcion para obtener la cantidad de letras
    contletras(cadena)       
    
#llamada de funcion
def contletras(cadena):
    #se guarda la cadena escrita anteriormente en una variable nueva
    #list, divide la cadena por caracter
    cadenaAbc = list(cadena)

    #hago lo mismo
    contadorLetras = dict(Counter(cadenaAbc))

    print (contadorLetras)

contfrecuencia()
def contfrecuencia():

    #leo cadena de caracteres
    cadena = input("Escriba su cadena de palabras: ")
    #divido la cadena por palabras ej: Hola como estas -> hola/como/estas
    cadenaPar = cadena.split()
    #creo un array con las palabras de la cadena ingresada por teclado
    palabras=[""]
    #se crea array de contadores
    Arrcont = []
    cont = 0 
    
    #En este for lo que se hace es guardas las palabras ingresadas por teclado en un array separado
    for i in range(len(cadenaPar)):
        palabras[i]=cadenaPar[i]
        palabras.insert(i, cadenaPar[i])

    #con ese array separado elimino las palabras repetidas con esta funcion
    palabrasSinRep = list(set(palabras))

    """con estos dos for voy comparandos las palabras unicas con las palabras que el usuario ingreso por
    teclado. si una palabra unica es igual a una palabra ingresada por teclado, esta entra a un if
    donde se va  a contabilizar las veces que se repite, para luego guardarlo en un contador""" 
    for i in range(len(palabrasSinRep)):
        for j in range(len(cadenaPar)):
            if palabrasSinRep[i]==cadenaPar[j]:
                cont=cont+1
        Arrcont.insert(i, cont)
        cont = 0

    #For que utilizo printear ambos arrays
    for i in range(len(palabrasSinRep)):
        print("{} se repitio un total de: {} vez/veces".format(palabrasSinRep[i], Arrcont[i]))
  
    #llamo la funcion para obtener la cantidad de letras
    contletras(cadena)  
         
    
"""Cuando se llama la funcion se le pasa anteriormente la cadena  de caracteres escrita por el usuario
esta funcion recibe dicho dato, y luego lo trabaja. En esta funcion se hace algo parecido a lo que 
hicimos anteriormente pero con la diferencia de que primero se divide la cadena en caracteres individuales
para luego eliminar los caracteres repetidos. Luego se hace el uso de los 2 for para comparar un unico
caracter con los caracteres de la cadena, tenes un contador que registre la cantidad de numeros que
se repiten y guardar en un array.
Por ultimo se utiliza el mismo print para mostras los datos"""
def contletras(cadena):
    cadenalis = list(cadena)
    cadenalisClean = list(set(cadenalis))
    ArrcontLetras = []
    contLet= 0

    for i in range(len(cadenalisClean)):
        for j in range(len(cadenalis)):
            if cadenalisClean[i]==cadenalis[j]:
                contLet=contLet+1
        ArrcontLetras.insert(i, contLet)
        contLet = 0

    for i in range(len(cadenalisClean)):
        print("{} se repitio un total de: {} vez/veces".format(cadenalisClean[i], ArrcontLetras[i]))



contfrecuencia()
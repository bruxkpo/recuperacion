def validar(ecu):
    #empieza el verificador
    #divido la funcion que me dan por caracteres 
    ecuPar = list(ecu)
    #creo un boolean
    flag = False
    #hago un for teniendo en cuenta la longitud de la funcion
    for i in range(len(ecuPar)):
        #pregunto si la funcion empieza con una llave
        if ecuPar[i]=="{":
            #si empieza con una llave este pasa a un for para buscar una llave cerrada 
            for j in range(len(ecuPar)):
                #pregunto si esta la llave cerrada
                if ecuPar[j] == "}":
                    #si lo esta el booleano me queda true
                    flag = True
                else:
                    #en cambio, si no se cierra me devuelve false
                    flag=False

        #HAGO LO MISMO CON LOS CORCHETES

        elif ecuPar[i]=="[":
            for j in range(len(ecuPar)):
                if ecuPar[j] == "]":
                    flag = True
                else:
                    flag=False

        #HAGO LO MISMO CON LOS PARENTESIS

        elif ecuPar[i]=="(":
            for j in range(len(ecuPar)):
                if ecuPar[j] == ")":
                    flag = True
                else:
                    flag=False

    return flag


def prueba():
    #EMPIEZA ACA
    #leo una ecuacion
    ecu = input("Escriba su ecuacion de palabras: ")
    #la ecuacion la paso por funcion a un verificador
    boliche = validar(ecu)
    print("La ecuacion {} -> {}".format(ecu, boliche))


prueba()
import random

def dados():

    #Darme una variable entera que indica la cantidad de tiradas que se hacen
    tiradas = int (input("Ingrese la cantidad de tiradas que quiere realizar: "))
    #creo array para guardar tiradas
    ArrTiradas = []
    #creo array para guardar un contador que indica la cantidad de veces que toco un numero en especifico
    Arrcont = []
    #Guardo los valores posibles que me pueden dar los 2 dados
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    #variable para mantener un contador
    cont=0

    for i in range(tiradas):
        #creo dos variables random para obtener una suma
        dado1= random.randint(1,6) 
        dado2= random.randint(1,6)
        #guardo la suma y la asigno en el array de tiradas
        suma = dado1+dado2
        ArrTiradas.insert(i, str(suma))


    for i in range(len(valores)):
        for j in range(len(ArrTiradas)):
            #si la suma de los dados es igual a un numero en especifico de los posibles resultados entra en
            #el if
            if valores[i]==ArrTiradas[j]:
                #asigno la cantidad de veces que se repite un numero
                cont=cont+1
            #inserto la cantidad en el array de cantidad
        Arrcont.insert(i, cont)
        cont = 0

    #for para printear
    for i in range(len(valores)):
        print("El valor {} se repitio un total de: {} vez/veces".format(valores[i], Arrcont[i]))


dados()
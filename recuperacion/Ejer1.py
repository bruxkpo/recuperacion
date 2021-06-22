def codificador():

    #guardo abecedario
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #Leo palabra por teclado y lo paso a miniscula para evitar problemas con las mayusculas
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower()
    #Variable para guardar la palabra nueva
    encriptado = ""
    #Fracciona la palabra en letras ej: Hola -> H, o, l, a
    p=list(palabra)
    #saco la longitud de la palabra para trabajar en el for
    cant = len(p)
    for i in range(cant):
        #si el true queda verdadero se va a sumar el caracter tal cual se leyo ej:1
        cambio = True
        #Verifico si hay espacio entre las palabras, si lo hay dejo un espacio vacio
        if p[i]==" ":
            encriptado = encriptado + " "
        for j in range(25):
            #se fija si el caracter de la palabra se encuentra en el abecedario
            if abc[j] == p[i]:
                cambio = False
                # si se encuentra de la mitad de para adelante del abc se le resta 13 caracteres
                if j>12:
                    encriptado = encriptado + abc[j-13]
                # lo contrario del anterior
                elif j<=12:
                    encriptado = encriptado + abc[j+13]
        #Si el cambio queda true se anota en la palabra codificada
        if cambio:
            encriptado = encriptado + p[i]

    print(encriptado)       





codificador()
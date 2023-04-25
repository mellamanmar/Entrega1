print ("Necesitamos hacer limonada")
paso1= input ("¿Tenemos un vaso? ") .upper()
if paso1 == "SI":
    paso2= input ("¿Tenemos limón? ") .upper()
    if paso2 == "SI":
        print ("Exprimimos el limón")
    elif paso2 == "NO":
        print ("Compramos limón")
        print ("Exprimimos el limón")
    paso3= input ("¿Hay azúcar?")
    if paso3 == "SI":
        print ("Mezclar azúcar con limón y agua")
        paso4= input ("¿Mezclaste bien?") .upper()
        if paso4 == "SI":
            print ("Sirve la limonada")
        elif paso4 == "NO":
            print ("Mezcla de nuevo")
            paso4= input ("¿Mezclaste bien?") .upper()
            if paso4 == "SI":
                print ("Sirve la limonada")
            else:
                print ("Vuelve al paso anterior")
    else:
        print ("Intenta de nuevo")
else:
    print ("Busca un vaso primero")
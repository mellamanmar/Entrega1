print ("Se quiere adoptar un gato gris, maacho, de 3 meses, en un refugio en Bogotá")
print ("¿Es una fundación o refugio?")
fundacion= input () .lower()
if fundacion == "si":
    print ("Se continúa proceso \n¿Está dentro de Bogota?")
    lugar= input () .lower() 
    if lugar == "si":
        print ("¿Está desparasitado?")
        desparasitado= input () .lower()
        if desparasitado == "si":
            print ("¿Es macho?")
            sexo= input () .lower()
            if sexo == "si":
                print ("¿Tiene más de 3 meses?")
                edad= input () .lower()
                if edad == "no":
                    print ("¿Qué color es?")
                    color= input () .lower()
                    if color == "gris":
                        print ("Se adopta el gato")
                    else: print ("No se adopta")
                else: print ("No se adopta")
            else: print ("No se adopta")
        else: print ("No se adopta")
    else: print ("No se adopta")
else: print ("No se adopta")

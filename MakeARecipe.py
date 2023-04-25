print ("Se desea hacer un arroz con leche")

print ("¿Tienes la receta?")
receta= input () .upper()
if receta == "SI":
    print ("¿Hay arroz?")
    arroz= input () .upper()
    if arroz == "SI":
        panela= input ("¿Tienes panela o azúcar? ") .upper()
        
        if panela == "PANELA":
            print ("Continuemos lavando el arroz \n¿La estufa esta encendida?")
            estufa= input () .upper()

            if estufa == "SI":
                print ("Cocinamos el arroz con agua, panela y canela por 15 minutos")
                print ("Luego agregamos la leche, leche condensada y revolvemos 15 minutos más")
                print ("Servimos en vasos y se deja reposar por 2 horas")
                print ("Ahora escogemos la decoración \n¿Que hay para decorar?")
                decoracion= input () .upper()
            elif estufa == "NO":
                print ("Debemos prender la estufa")
                print ("¿La encendiste?")
                estufa= input () .upper()
                if estufa == "SI":
                    print ("Cocinamos el arroz con agua, panela y canela por 15 minutos")
                    print ("Luego agregamos la leche, leche condensada y revolvemos 15 minutos más")
                    print ("Servimos en vasos y se deja reposar por 2 horas")
                    print ("Ahora escogemos la decoración \n¿Que hay para decorar?")
                    decoracion= input () .upper()
                else:
                    print ("La estufa debe estar prendida")
            if decoracion  == "MORA":
                print ("Decoramos con mora y queso rallado")
                print ("Presentamos al comprador el arroz con leche \n¿Método de pago?")
                pago= input () .upper()
            elif decoracion == "CHOCOLATE":
                print ("Decoramos con chocolate y queso")
                print ("Presentamos al comprador el arroz con leche \n¿Método de pago?")
                pago= input () .upper()         
            else:
                print ("Decoramos con queso rallado")
                print ("Presentamos al comprador el arroz con leche \n¿Método de pago?")
                pago= input () .upper()

            if pago == "EFECTIVO":
                print ("Paga en ", pago)
                print ("Entregamos el producto")
            else:
                print ("Paga en", pago)
                print ("Verificamos el pago \n¿Fue exitoso?")
                pagoExitoso= input () .upper()

                if pagoExitoso == "SI":
                    print ("Entregamos el producto")
                else:
                    print ("¿Intenta pago en efectivo?")
                    pagoExitoso= input () .upper()
                    if pagoExitoso == "SI":
                        print ("Entregamos el producto")
                    else: print ("No entregamos el producto")
        else:
            print ("No es posible hacer la receta")   
    else:
        print ("No es posible hacer la receta")  
else:
    print ("Debes buscar la receta")
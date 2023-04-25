print ("Se necesitan comprar unas entradas para un concierto de salsa en Bogotá, asientos en VIP, con un presupuesto máximo de 2 millones, y que incluyan bebidas alcoholicas y no alcoholicas")
print ("Conciertos en Bogotá \nElegir:\n") 
concierto= input () .upper()

if concierto == "FRANKIE RUIZ" or concierto == "OSCAR DE LEON" or concierto == "RUBEN BLADES":
    print ("Escoja su asiento")
    asiento= input () .upper()
    if "VIP" in asiento:
        print ("Continúa con la compra \n¿El precio pasa del presupuesto?")
        precio= int (input())
        if precio <= 2000000:
            print ("Escoja su paquete de bebidas \n1 Bebidas nacionales \n2 Bebidas no alcohólicas \n3 Todas las bebidas alcohólicas y no alcohólicas")
            bebidas= input ()

            if bebidas == "3":
                print ("Elige el método de pago")
                input ()
                print ("Confirmar compra sí o no")
                confirmar= input () .upper()
                if confirmar == "SI":
                    print ("Compra exitosa")
                else:
                    print ("No ha confirmado su compra")
            else:
                print ("No ha seleccionado su paquete de bebidas")
        else:
            print ("Supera el presupuesto")
    else:
        print ("No hay disponibles")
else: 
    print ("No hay disponibles")
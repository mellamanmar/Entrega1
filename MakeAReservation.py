print ("Se necesita hacer una reserva online para un restaurante")
print ("¿Ingresó a la página?")
ingreso= input() .upper()
if ingreso == "SI":
    print ("Para el registro porfavor ingrese sus datos \nNúmero de documento")
    numeroDocumento= input()
    print ("Nombres")
    nombre= input () .upper()
    print ("Apellidos")
    apellido= input() .upper()
    recordar= input ("¿Recordar usuario?") .upper()
    if recordar == "SI":
        print ("Usuario guardado \nEscoja fecha y hora de la reserva")
        fechaYHora= input ()
        print ("La reserva fue escogida para")
        print (fechaYHora)
        print ("¿Confirmar reserva?")
        confirmacion= input() .upper()
    elif recordar == "NO":
        print ("Escoja fecha y hora de la reserva")
        fechaYHora= input ()
        print ("La reserva fue escogida para")
        print (fechaYHora)
        print ("¿Confirmar reserva?")
        confirmacion= input() .upper()
    if confirmacion == "SI":
        print ("Reserva exitosa")
    elif confirmacion == "NO":
        print ("¿Desea confirmar la reserva?")
        confirmacion= input () .upper()
        if confirmacion == "SI":
            print ("Reserva exitosa")    
        else:
            print ("No es posible hacer la reserva")               
    else:
        print ("Seleccione una opción válida")
else:
    print ("No es posible hacer la reserva")
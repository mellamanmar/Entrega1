# Elabora un código sobre una búsqueda del tesoro

print ("Bienvenido a la isla. Tu misión será encontrar el tesoro")
decision1= input ("Elige, izquierda o derecha. ") .lower()

if decision1 == "izquierda":
    decision2= input ("¿Nadar o esperar?. ") .lower()
    
    if decision2 == "esperar":
        decision3= input ("Escoge una puerta: Rojo, Azul ó Amarillo. ") .lower()
        if decision3 == "amarillo":
            print ("¡¡HAS GANADO!!")
        elif decision3 == "rojo":
            print ("Eres quemado. GAME OVER")
        else:
            print ("Devorado por bestias. GAME OVER")

    else:
        print ("Atacado por una tribu. GAME OVER")
else:
    print ("Caíste en agujero. GAME OVER")
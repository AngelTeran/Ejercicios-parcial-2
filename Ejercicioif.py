nombre = ""
edad = 0
nacionalidad = ""

nombre = input("ingresa tu nombre:")
edad = int(input("ingresa tu edad"))
nacionalidad = input("ingresa tu nacionalidad:")

if edad >= 18: # el if va seguido de la condición y dos puntos
    print("Eres mayor de edad")
else: # el esle va seguido de dos puntos para decir que se hace si no se cumple la condición del if
    print("No eres mayor de edad")

if nacionalidad == "N":
    print("Eres de nacionalidad mexicana")
else:
    print("No eres de nacionalidad mexicana")





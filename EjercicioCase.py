name = ""
lastName = "" 
age = 0
birthday = "" 
email = ""
password = ""
confirmPass = ""
gender = ""
opcion = 0

print("Bienvenido al sistema de registro de clientes")
print("--------MENÚ PRINCIPAL--------")
print("1. Registrar cliente")
print("2. Ver información de cliente")
print("3. Borrar información de cliente")
print("4. Modificar información del cliente")
print("5. Salir")
print("--------------------")
opcion = int(input("Selecciona una opción"))

match opcion: #Aqui inicia el match, que es una validación de caso
    case 1:
        name = input("Ingresa tu nombre: ")
        lastName = input("Ingresa tu apellido: ")
        age = int(input("Ingresa tu edad: "))
        birthday = input("Ingresa tu fecha de nacimiento: ")
        email = input("Ingresa tu correo electrónico: ")
        password = input("Ingresa tu contraseña: ")
        confirmPass = input("Confirma tu contraseña: ")
        gender = input ("Ingresa tu género")
    case 2:
        print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electrónico:", email, "Contraseña:", password, "Género:", gender)
    case 3:
        name = ""
        lastName = ""
        age = 0
        birthday = ""
        email = ""
        password = ""
        gender = ""
    case 4:
        name = input("Ingresa tu nombre: ")
        lastName = input("Ingresa tu apellido: ")
        age = int(input("Ingresa tu edad: "))
        birthday = input("Ingresa tu fecha de nacimiento: ")
        email = input("Ingresa tu correo electrónico: ")
        password = input("Ingresa tu contraseña: ")
        gender = input("Ingresa tu género")
    case 5:
        print("¡Hasta luego!")
    case _:
        print("Opción no válida")
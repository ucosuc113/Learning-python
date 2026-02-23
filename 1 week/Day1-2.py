import json

def inicio():
    print("desea iniciar sesion? (s/n)")
    return input().lower()

def sesioniniciar():
    print("inicie sesion, para salir escriba (n)")
    with open("sesion.json", "r") as archivo:
        sesion = json.load(archivo)

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario.lower() == "n" or contraseña.lower() == "n":
        print("sesion cerrada")
        return  # vuelve al menú

    if sesion["username"] == usuario and sesion["password"] == contraseña:
        print("sesion iniciada correctamente")
        return exit()
    else:
        print("usuario o contraseña incorrectos")
        return sesioniniciar()

def registrarse():
    print("registrese para iniciar sesion")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario.lower() == "n" or contraseña.lower() == "n":
        print("volviendo al menu")
        return

    sesion = {
        "username": usuario,
        "password": contraseña
    }

    with open("sesion.json", "w") as archivo:
        json.dump(sesion, archivo, indent=4)

while True:
    opcion = inicio()

    if opcion == "s":
        sesioniniciar()
    elif opcion == "n":
        registrarse()
import json
import os

def inicio():
    print("desea iniciar sesion? (s/n)")
    return input().lower()

def sesioniniciar():
    print("inicie sesion, para salir escriba (n)")
    with open("sesion.json", "r") as archivo:
        sesion = json.load(archivo)

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    encontrado = False

    for s in sesion:
        if s["username"] == usuario and s["password"] == contraseña:
            encontrado = True
            break

    if encontrado:
        print("sesion iniciada correctamente")
        exit()
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

    archivo_path = "sesion.json"

    if not os.path.exists(archivo_path):
        with open(archivo_path, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(archivo_path, "r", encoding="utf-8") as f:
        datos = json.load(f)

    existe = any(s["username"] == usuario for s in datos)

    if not existe:
        datos.append(sesion)

        with open(archivo_path, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        print("Sesión añadida.")
    else:
        print("Ese usuario ya existe.")
        return registrarse()

while True:
    opcion = inicio()

    if opcion == "s":
        sesioniniciar()
    elif opcion == "n":
        registrarse()
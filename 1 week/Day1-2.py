import json
import os

# como funciona?, no se XD, osea si se, pero no lo toquen si no saben lo q hacen XD

def inicio():
    print("desea iniciar sesion? (s/n)")
    return input().lower()

def sesioniniciar():

# por aca, primero envia el mensaje ese, luego abre el json, luego pide el usuario y contraseña, luego recorre el json buscando una coincidencia, si la encuentra, inicia sesion, sino, muestra un mensaje de error y vuelve a pedir los datos ASSAKHDK
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

# aca es similar... pero diferente JAJASKDJH, primero muestra el mensaje, luego pide los datos, luego verifica si el usuario ya existe, si no existe, lo añade al json, sino, muestra un mensaje de error y vuelve a pedir los datos ASSAKHDK
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

# hola while :D, este es el menu principal, aqui se pregunta si quieres iniciar sesion o registrarte, dependiendo de la opcion, se llama a la funcion correspondiente, si la opcion es invalida, se vuelve a mostrar el menu ASSAKHDK
    opcion = inicio()

    if opcion == "s":
        sesioniniciar()
    elif opcion == "n":
        registrarse()
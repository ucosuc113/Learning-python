def pedir_nota(numero):
    nota = float(input(f"ingrese la nota {numero}: "))
    if nota < 1 or nota > 5:
        print("nota no valida, ingrese una nota entre 1 y 5")
        #exit()
        return pedir_nota(numero)
    return nota

nota1 = pedir_nota(1)
nota2 = pedir_nota(2)
nota3 = pedir_nota(3)

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 3.5:
    print("aprobado con ", promedio)
else:
    print("reprobado con ", promedio)
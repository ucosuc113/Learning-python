nota1 = float(input("introduce la primer nota: "))

if nota1 < 1 or nota1 > 5:
    print("la nota debe ser entre 1 y 5")
    exit()
    
nota2 = float(input("introduce la segunda nota: "))

if nota2 < 1 or nota2 > 5:
    print("la nota debe ser entre 1 y 5")
    exit()
    
nota3 = float(input("introduce la tercera nota: "))

if nota3 < 1 or nota3 > 5:
    print("la nota debe ser entre 1 y 5")
    exit()
    

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 3.5:
    print("aprobado con ", promedio)
else:
    print("reprobado con ", promedio)
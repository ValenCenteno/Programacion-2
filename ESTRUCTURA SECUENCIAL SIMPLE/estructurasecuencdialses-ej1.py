nota1 = 0
nota2 = 0
#Se declaran las variables
ingles = 10
musica = 0
lengua = 0
geografia = 0
historia = 0
promedio = 0

#Se solicitan las notas al usuario
for i in range (1, 6) :
    print(f"Ingrese la nota de la materia (i):")
    nota = float(input())
    if nota >= 0 and nota <= 10:
        if i == 1:
            ingles = nota
        elif i == 2:
            musica = nota
        elif i == 3:
            lengua = nota
        elif i == 4:
            geografia = nota
        else:
            historia = nota
    else:
        print("Error: La nota debe estar entre o y 10.")
        i -= 1 #Se repite la solicitud de la nota

#Se calcula el promedio
promedio = (ingles + musica + lengua + geografia + historia) /5

#Se muestra el promedio
print(f"El promedio general es: {promedio:.2f}")

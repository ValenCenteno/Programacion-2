nombres = []
for i in range(10):
    nombre = input("Ingresa un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("el nombre ya ha sido ingresado. intentalo de nuevo.")
print("los nombres ingresados son:", nombres)

if len(nombres) >= 3:
    del nombres[2]
if nombres:
    del nombres[-1]
nombres.sort()
print("después de eliminar y ordenar, la lista queda así:", nombres)

persona = {}
persona["nombre"] = input("ingrese nosmbre: ")
persona["apellido"] = input("ingrese apellido: ")
persona["dni"] = input("ingrese DNI: ")
persona["email"] = input("ingrese email: ")
persona["fecha_nacimiento"] = input("ingrese fecha de nacimiento: ")
print("los datos de la persona son:", persona)

familia = {}
for i in range(4):
    persona = {}
    persona["nombre"] = input("Ingrese nombre de la persona {}: ".format(i+1))
    persona["apellido"] = input("Ingrese apellido de la persona {}: ".format(i+1))
    persona["dni"] = input("Ingrese DNI de la persona {}: ".format(i+1))
    persona["email"] = input("Ingrese email de la persona {}: ".format(i+1))
    persona["fecha_nacimiento"] = input("Ingrese fecha de nacimiento de la persona {}: ".format(i+1))
    familia["persona{}".format(i+1)] = persona
print("Los datos de la familia son:", familia)

n = int(input("Ingrese un número para obtener los primeros números pares: "))
pares = tuple(i for i in range(2, 2*n+1, 2))
print("Los primeros", n, "números pares son:", pares)

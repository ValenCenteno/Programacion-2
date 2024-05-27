partidos_jugados = 0
partidos_ganados = 0
partidos_empatados = 0
partidos_perdidos = 0
puntaje_total= 0 

partidos_jugados = int(input("Ingrese la cantidad de partidos jugados"))
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados"))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados"))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos"))

if partidos_jugados != (partidos_ganados + partidos_empatados + partidos_perdidos):
    print("Error! La suma de partidos ganados, empatados y perdidos no coincide con el total de partidos jugados.")
    exit ()
    
puntaje_total = (partidos_ganados + 3) + partidos_empatados

print(f"El equipo lleva (puntaje_total) puntos acumulados en el campeonato.")

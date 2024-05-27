altura = 0
ancho = 0
superficie = 0
costo_por_metro_cuadrado = 0
costo_por_mano_de_obra = 0

altura = float(input("Ingrese la altura de la pared en metros"))
ancho = float(input("Ingrese el ancho de la pared en metros"))

superficie = altura * ancho

costo_por_metro_cuadrado = float(input("Ingrese el costo por el metro cuadrado de pintura: "))
costo_por_mano_de_obra = superficie * costo_por_metro_cuadrado

print(f"el costo total de la mabo de obra para pintar la pared es de: $(costo_mano_de_obra:.2f)")
#Una despensa de barrio vende la leche de vaca emtera de litro a 1000 pesos la unidad.
#Si el cliente conpra mas de l2 unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. Si compra mas de 24 unidades, el descuento es del 15%. Ademas posee la promocion a los jubilados. La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuetos). Desarrolle una solución algoritmica para saber cuanto debe pagar el cliente,

#Para cada caso hacer:

#Una breve descripcion de la situacion comentada en la cabecera deol archivo.py

#Una solucion implementada em python en el mismo archivo donde se encuentra detallada la descripción

def calcular_costo(cantidad):
    precio_unitario = 1000
    costo_sin_descuento = cantidad * precio_unitario
    
    if cantidad > 24:
        descuento = 0.15
    elif cantidad > 12:
        descuento = 0.10
    else:
        descuento = 0
    
    costo_con_descuento = costo_sin_descuento * (1 - descuento)
    return costo_con_descuento

def aplicar_descuento_jubilado(costo):
    descuento_jubilado = 0.10
    costo_con_descuento_jubilado = costo * (1 - descuento_jubilado)
    return costo_con_descuento_jubilado

cantidad_comprada = int(input("Ingrese la cantidad de unidades de leche compradas: "))
costo_final = calcular_costo(cantidad_comprada)

es_jubilado = input("¿Es usted jubilado? (Sí/No): ").lower()
if es_jubilado == "sí" or es_jubilado == "si":
    costo_final = aplicar_descuento_jubilado(costo_final)

print("El costo final a pagar es: ${:.2f}".format(costo_final))
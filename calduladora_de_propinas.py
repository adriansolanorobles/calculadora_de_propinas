"""
acabo de terminar una deliciosa cena de huevos con jamon. 
Sin embargo, el computador ddel restaurante no funciona; 
asi tendrar que calcular el costo de la cena tu mismo.
Hay que calcular la propina sobre el costo total de la 
comida  incluyendo el impuesto.
"""
comida = 44.50

impuesto = 6.75 / 100

propina = 15 / 100

comida = comida + comida * impuesto

total = comida + comida * propina

print ("%.2f" % total)

# Grupo 11: Galón vs Pinta
# La clase es Medida y requiere de los atributos de nombre medida, valor medida (en el valor de la medida) y valor equivalente (en el valor en Lt).
# La formula es: valorEquivalente = valorMedida/equivalenteA1Lt
# Información equivalente a 1 KM:
# 1 Lt = 0,26 Galones
# 1 Lt = 2,11 Pintas

class Medida():
    def __init__(self, nombreMedida, valorMedida):
        self.nombreMedida = nombreMedida.lower()
        self.valorMedida = float(valorMedida)
        if self.nombreMedida == 'galones':
            self.equivalenteA1Lt = float(0,26)
        elif self.nombreMedida == 'pintas':
            self.equivalenteA1Lt = float(2,11)
        self.valorEquivalente = self.valorMedida/self.equivalenteA1Lt

    def __str__(self):
        resultado = (f'{self.valorEquivalente} Lt')
        return resultado
    
    def comparar(self):
        x1 = 0
        x2 = 0
        if x1 < x2:
            comparacion = (f'{x1} < {x2}')
            return comparacion
        elif x1 > x2:
            comparacion = (f'{x1} > {x2}')
            return comparacion
        elif x1 == x2:
            comparacion = (f'{x1} = {x2}')
            return comparacion
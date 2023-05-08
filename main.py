# Grupo 11: Galón vs Pinta
# La clase es Medida y requiere de los atributos de nombre medida, valor medida (en el valor de la medida) y valor equivalente (en el valor en Lt).
# La formula es: valorEquivalente = valorMedida/equivalenteA1Lt
# Información equivalente a 1 KM:
# 1 Lt = 0,26 Galones
# 1 Lt = 2,11 Pintas

class Medida():
    def __init__(self, nombreMedida, valorMedida):
        self.nombreMedida = nombreMedida.lower()
        self.valorMedida = int(valorMedida)
        if self.nombreMedida == 'galones':
            self.equivalenteA1Lt = int(0,26)
        elif self.nombreMedida == 'pintas':
            self.equivalenteA1Lt = int(2,11)
        self.valorEquivalente = self.valorMedida/self.equivalenteA1Lt

    def __str__(self):
        return f'{self.nombreMedida}: {self.valorMedida} ({self.valorEquivalente} Lt)'
    
    def comparar(self):
        x1 = 0
        x2 = 0
        if x1 < x2:
            print(f'{x1} < {x2}')
        elif x1 > x2:
            print(f'{x1} > {x2}')
        elif x1 == x2:
            print(f'{x1} = {x2}')
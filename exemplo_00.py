# def soma(a, b):
#     return a + b


# resultado = soma(200, 3)
# print(resultado)


from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

resultado = calcular_media([1, 4, 7, 9, 10])
print(resultado) 

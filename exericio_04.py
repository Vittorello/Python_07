from typing import List

def numeros(valores: List[int]) -> List[int]:
    return [num for num in valores if num % 2 == 0]

resultado = numeros([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,])
print(resultado)

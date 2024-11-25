from typing import List

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))


lista = contar_valores_unicos([1,2,1,1,1,4])
print(lista)
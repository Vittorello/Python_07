from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado


resultados = filtrar_acima_de([3, 6, 9, 12], 1)
print(resultados)

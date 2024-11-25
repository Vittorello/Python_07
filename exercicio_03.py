from typing import List

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]


celsius = celsius_para_fahrenheit([26.7])
print(f"A temperatura convertida de celsius é {celsius}")
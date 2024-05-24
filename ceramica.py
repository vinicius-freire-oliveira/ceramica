import math

# Dimensões da parede em metros
comprimento_parede = 5.2
altura_parede = 2.6

# Área da parede em metros quadrados
area_parede = comprimento_parede * altura_parede

# Dimensões do azulejo em metros
lado_azulejo_cm = 20
lado_azulejo_m = lado_azulejo_cm / 100  # convertendo centímetros para metros

# Área do azulejo em metros quadrados
area_azulejo = lado_azulejo_m ** 2

# Calculando o número total de azulejos necessários
numero_azulejos = area_parede / area_azulejo

# Tem a função de exibir a quantidade total de azulejos necessários para cobrir uma determinada área, utilizando a função math.ceil para arredondar o valor para cima
print("Número total de azulejos necessários:", math.ceil(numero_azulejos))

# Considerando 10% de perdas
numero_azulejos_com_perdas = math.ceil(numero_azulejos * 1.1)

# Exibindo o número total de azulejos necessários com perdas
print("Número total de azulejos necessários (com 10% de perdas):", numero_azulejos_com_perdas)

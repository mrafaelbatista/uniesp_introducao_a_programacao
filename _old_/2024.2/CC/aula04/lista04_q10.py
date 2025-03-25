# Contexto: Determinação do tipo de triângulo.
# Questão: Peça ao usuário para inserir três lados
# de um triângulo e determine se é um triângulo
# equilátero, isósceles ou escaleno.

lado_a = float(input('Digite o lado A: '))
lado_b = float(input('Digite o lado B: '))
lado_c = float(input('Digite o lado C: '))


if lado_a == lado_b and lado_b == lado_c:
    print('Equilátero!')

elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    print('Isósceles')

elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
    print('Escaleno!')

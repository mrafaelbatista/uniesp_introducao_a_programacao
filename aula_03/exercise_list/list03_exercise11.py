import math

# Declaração de variáveis
A = 2
B = 7
C = 3.5
L = False

# Descobrindo o resultado das sentenças
print(f'B = A * C e (L ou V) é {(B == A * C and (L or True))}')
print(f'B > A ou B = pot(A, A) é {(B > A or B == A**A)}')
print(f'L e B div A >= C ou não A <= C é {(L and B / A >= C or not A <= C)}')
print(f'não L ou V e rad(A + B) >= C é {(not L or True and math.sqrt(A + B) >= C)}')
print(f'B/A = C ou B/A <> C é {(B/A == C or B/A != C)}')
print(f'L ou pot(B, A) <= C * 10 + A * B é {(L or B**A <= C * 10 + A * B)}')
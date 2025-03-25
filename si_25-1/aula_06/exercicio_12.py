ladoa = float(input('Digite o valor A: '))
ladob = float(input('Digite o valor B: '))
ladoc = float(input('Digite o valor C: '))

if ladoa == ladob == ladoc:
    print('Equilátero')

elif ladoa != ladob and ladob != ladoc and ladoa != ladoc:
    print('Escaleno')

if not (ladoa == ladob == ladoc) and (ladoa == ladob or ladob == ladoc or ladoa == ladoc):
    print('Isóceles')

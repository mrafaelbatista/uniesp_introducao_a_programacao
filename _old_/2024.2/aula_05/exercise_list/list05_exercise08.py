missoes_completas = int(input("Número de missões completadas: "))

if missoes_completas > 10:
    bonus = 100
elif 5 <= missoes_completas <= 10:
    bonus = 50
else:
    bonus = 10

print(f"O cavaleiro receberá {bonus} moedas de ouro de bônus.")

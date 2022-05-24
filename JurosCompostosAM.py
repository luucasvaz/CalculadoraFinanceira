# Juros Compostos com Aportes Mensais

aporte = float(input('Aplicação mensal:'))
tempo = int(input('Período em que ficará aplicado (em meses):'))
taxa = float(input('Taxa de juros mensal:')) * 0.01

montante = round((aporte * (((1 + taxa) ** tempo) - 1) / taxa), 2)
montante_str = str(montante).replace('.', ',')
juros = round(montante - (aporte * tempo), 2)
juros_str = str(juros).replace('.', ',')
print(f'O total acumulado no período será de R$ {montante_str}. Os juros acumulados no período é de R$ {juros_str}.')

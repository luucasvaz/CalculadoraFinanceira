principal = float(input('Montante a ser aplicado:'))
tempo = int(input('Período em que ficará aplicado (em meses):'))
taxa = float(input('Taxa de juros mensal:'))*0.01

montante = round(principal * ((1 + taxa) ** tempo), 2)
montante_str = str(montante).replace('.', ',')
juros = round((montante - principal), 2)
juros_str = str(juros).replace('.', ',')
print(
    'O total acumulado no período será de R$ ' + montante_str + '. Os juros acumulados no período é de R$ ' + juros_str + '.'
)

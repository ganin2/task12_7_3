per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита:"))
per_cent = {k: v for k, v in per_cent.items() if v == max(per_cent.values())}
for key,value in per_cent.items():
    print("Максимальная сумма, которую вы можете заработать- ", key,':',value * money/100)
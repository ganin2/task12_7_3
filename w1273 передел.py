per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита:"))
deposit={}
for k, v in per_cent.items():
    deposit[k] = round(v * money/100,2)
deposit = {k: v for k, v in deposit.items() if v == max(deposit.values())}
for key,value in deposit.items():
    print("Максимальная сумма, которую вы можете заработать- ", key,':',value)


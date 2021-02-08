'''
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

dct = {}
average_profit_dct = {"average_profit": 0}
profit = 0
profit_c = 0
average = 0
list_to_json = []
with open('text_7.txt', encoding='utf-8') as file:
    companies = [comp.split(' ') for comp in [line.split('\n')[0] for line in file.readlines()]]
    for i in companies:
        dct[(i[0].encode('utf-8')).decode('utf-8')] = int(i[2]) - int(i[3])
    for key in dct:
        if dct[key] >= 0:
            profit_c += 1
            profit += dct[key]
    average = profit/profit_c
    average_profit_dct['average_profit'] = average
    list_to_json.append(dct)
    list_to_json.append((average_profit_dct))

with open('text_777.json', 'w', encoding='utf-8') as file:
    json.dump(list_to_json, file, ensure_ascii=False)

'''
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

avg_salary = 0
with open('text_3.txt', encoding='utf-8') as file:
    persons = [(person.split(' ')[0], float((person.replace('\n', ' ')).split(' ')[1])) for person in file]

less20k = [person[0] for person in persons if person[1] < 20000]
for person in persons:
    avg_salary += person[1]
print(f'Сотрудники, с зарплатой меньше 20000: {less20k}')
print(f'Средняя зарплата: {avg_salary/len(persons)}')

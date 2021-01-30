'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
in_month = int(input(f'Введите номер месяца: '))
print('Через list')
LST_YEAR = ['January', 'February', 'March', 'April', 'May', 'June', \
            'Jule', 'August', 'September', 'October', 'November', 'December']
SEASONS_LST = ['Winter', 'Spring', 'Summer', 'Autumn']
if in_month > 0 and in_month<= len(LST_YEAR):
    if in_month in [1,2,12]:
        season = SEASONS_LST[0]
    elif in_month in [3,4,5]:
        season = SEASONS_LST[1]
    elif in_month in [6,7,8]:
        season = SEASONS_LST[2]
    else:
        season = SEASONS_LST[3]
    print(f'{LST_YEAR[in_month-1]} is month of {season}')


print('Через dict')
LST_DICT = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', \
            7: 'Jule', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12:'December'}
SEASONS_DICT = {1: 'Winter', 3: 'Spring', 6: 'Summer', 9: 'Autumn'}
if in_month > 0 and LST_DICT.keys():
    if in_month == 12 or in_month <= 2:
        season = SEASONS_DICT[1]
    elif in_month <= 5:
        season = SEASONS_DICT[3]
    elif in_month <= 8:
        season = SEASONS_DICT[6]
    elif in_month < 12:
        season = SEASONS_DICT[9]
    print(f'{LST_DICT[in_month]} is month of {season}')

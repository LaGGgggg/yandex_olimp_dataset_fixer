from csv import reader, writer

"""
Dataset columns by indexes:
0: id
1: Название игры
2: Разработчики
3: Издатели
4: Дата выхода
5: Поддерживаемые языки
6: Возрастное ограничение
7: Цена
8: Предполагаемое количество владельцев
9: Функции
10: Метки
11: Жанры
12: Тема и атмосфера
13: Визуальный стиль и перспектива
14: Особенности
15: Игроки
16: Оценки
17: Рейтинги
18: Устройства ввода
19: Финансирование
20: Программное обеспечение
21: Позитивные отзывы
22: Негативные отзывы
23: Описание
24: Ссылка на страницу магазина
"""

data = []

with open('input.csv', 'r', encoding='UTF-8') as f:

    first_line = f.readline()

    for line in list(reader(f)):

        if line[0] in ('24043', '24049', '24058', '24085'):

            print(f'Game from ban list founded: {line[0]}, skip it')

            continue

        line[2] = ', '.join(set(line[2].split(', ')))
        line[3] = ', '.join(set(line[3].split(', ')))
        line[5] = ', '.join(set(line[5].split(', ')))
        line[9] = ', '.join(set(line[9].split(', ')))
        line[10] = ', '.join(set(line[10].split(', ')))
        line[11] = ', '.join(set(line[11].split(', ')))
        line[14] = ', '.join(set(line[14].split(', ')))
        line[15] = ', '.join(set(line[15].split(', ')))
        line[16] = ', '.join(set(line[16].split(', ')))
        line[17] = ', '.join(set(line[17].split(', ')))
        line[18] = ', '.join(set(line[18].split(', ')))
        line[20] = ', '.join(set(line[20].split(', ')))

        if 'Для одного игрока' in line[9] and 'Для одного игрока' not in line[15]:

            if line[15] != '':
                line[15] = ', '.join([*line[15].split(', '), 'Для одного игрока'])

            else:
                line[15] = ', '.join(['Для одного игрока'])

        if 'Кооператив (LAN)' in line[9] or 'Кооператив (общий экран)' in line[9]:

            fields_to_add = []

            for i in ('Мультиплеер', 'Кооператив', 'Локальный кооператив', 'Локальный мультиплеер'):
                if i not in line[15]:
                    fields_to_add.append(i)

            if line[15] != '':
                line[15] = ', '.join([*line[15].split(', '), *fields_to_add])

            else:
                line[15] = ', '.join(fields_to_add)

        if 'Кооператив (по сети)' in line[9]:

            fields_to_add = []

            for i in ('Мультиплеер', 'Кооператив', 'Сетевой кооператив'):
                if i not in line[15]:
                    fields_to_add.append(i)

            if line[15] != '':
                line[15] = ', '.join([*line[15].split(', '), *fields_to_add])

            else:
                line[15] = ', '.join(fields_to_add)

        if 'Против игроков (по сети)' in line[9]:

            fields_to_add = []

            if 'Мультиплеер' not in line[15]:
                fields_to_add.append(i)

            if line[15] != '':
                line[15] = ', '.join([*line[15].split(', '), 'Мультиплеер'])

            else:
                line[15] = ', '.join(['Мультиплеер'])

        data.append(line)

with open('output.csv', 'w+', encoding='UTF-8') as f:

    f.write(first_line)

    writer(f, lineterminator='\n').writerows(data)

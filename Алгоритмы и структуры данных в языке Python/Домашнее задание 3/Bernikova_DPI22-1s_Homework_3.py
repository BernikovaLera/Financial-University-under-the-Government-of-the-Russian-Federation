with open("input.csv", "r") as f:
    lines = f.readlines()

preferences = [list(map(int, line.strip().split(","))) for line in lines]  # разделение строк на отдельные элементы
options = list(set([option for preference in preferences for option in preference]))# создание списка вариантов голосования

# Определение победителя
winner = None
while winner is None:
    votes = {option: 0 for option in options} # создание словаря для подсчета голосов
    print(votes)
    for preference in preferences:        # подсчет голосов
        if len(preference) > 0:
            votes[preference[0]] += 1
            #print(votes)
    min_votes = min(votes.values())              # проверка количества голосов за каждый вариант
    if list(votes.values()).count(min_votes) > 1:
        winner = min(votes, key=votes.get)
    else:                                                                                           
        # если есть несколько вариантов с минимальным числом голосов, 
        # то исключаем их из списка вариантов и переходим к следующей итерации
        options = [option for option in options if votes[option] > min_votes] 
        print(options)
        for i in range(len(preferences)):
            preferences[i] = [option for option in preferences[i] if option in options]


# Формирование общественного порядка предпочтений
order = []

while len(options) > 0:
    votes = {option: 0 for option in options}  # создание словаря для подсчета голосов
    for preference in preferences:            # подсчет голосов
        for option in preference:
            if option in options:
                votes[option] += 1
                break
    min_votes = min(votes.values())# Определение варианта голосования,который получил наименьшее количество голосов
    if list(votes.values()).count(min_votes) == 1:
        next_option = min(votes, key=votes.get)
        options.remove(next_option)
        order.append(next_option)
    else:                                                                                           
        # если есть несколько вариантов с минимальным числом голосов,
        # о исключаем их из списка вариантов и добавляем их в общественный порядок
        next_options = [option for option in options if votes[option] == min_votes]
        options = [option for option in options if option not in next_options]
        order.append(next_options)

with open("result.txt", "w+") as f:
    f.write(",".join(map(str, reversed(order))))
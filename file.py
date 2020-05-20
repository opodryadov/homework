cook_book = {}
dish_name = []
with open('recipes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        dish_name.append(line)
    if dish_name[0] and dish_name[6] and dish_name[13] and dish_name[19] not in cook_book.keys():
        cook_book[dish_name[0]] = []
        cook_book[dish_name[6]] = []
        cook_book[dish_name[13]] = []
        cook_book[dish_name[19]] = []
        print(cook_book)

with open('recipes.txt', 'r', encoding='utf-8') as file_work:
    for line in file_work:
        line = line.strip()
        if 'Омлет' in line or 'Утка по-пекински' in line or 'Запеченный картофель' in line or 'Фахитос' in line:
            dish_name = line
        counter = len(file_work.readlines())
        list_of_ingridient = [] #временный список
        # for i in range(counter):
        #     temp_dict = {} #временный словарь
        #     ingridient = file.readline() #вот так перемещаемся по файлу
            #заполняем словарь с ингридиентом
            #добавляем словарь в список
        #записываем в словарь cook_dict наш рецепт
        #file_work.readline() - еще раз спускаемся ниже т.к. пустая строка

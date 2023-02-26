with open(r'C:\Users\DELL\PycharmProjects\pythonProject\open fail and read fail\cook book.txt',
          'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        number_of_ingredients = int(f.readline())
        ingredients = []
        for i in range(number_of_ingredients):
            ing = f.readline().strip()
            ingredient_name, quantity, measure = ing.split(" | ")
            ingredients.append({
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure
            })
        f.readline()
        cook_book[dish_name] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                dict_dishes[ingridient['ingredient_name']] = {'quantity': int(ingridient['quantity']) * person_count,
                                                              'measure': ingridient['measure']}
    print(dict_dishes)
    return


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
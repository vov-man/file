with open(r'C:\Users\DELL\PycharmProjects\pythonProject\open fail and read fail\cook book.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        number_of_ingredients = int(f.readline())
        ingredients = []
        for i in range (number_of_ingredients):
            ing = f.readline().strip()
            ingredient_name, quantity, measure = ing.split(" | ")
            ingredients.append ({
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure
            })
        f.readline()
        cook_book[dish_name] = ingredients
print(cook_book)
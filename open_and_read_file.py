from pprint import pprint


def get_meal(file_name):
    with open(file_name, encoding='utf-8') as file:
        cook_book = dict()
        for line in file:
            name_meal = line.strip()
            counter = int(file.readline())
        
            temporary_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temporary_list.append({'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[name_meal] = temporary_list
            file.readline()

    return cook_book

pprint(get_meal('text.txt'))



def get_shop_list_by_dishes(dishes, person_count):
    list_meal = dict()
    for meal in dishes:
        for ingrd in cook_book[meal]:
          list_meal_item = dict(ingrd)
          list_meal_item['quantity'] *= person_count
          if list_meal_item['ingredient_name'] not in list_meal:
            list_meal[list_meal_item['ingredient_name']] = list_meal_item
          else:
            list_meal[list_meal_item['ingredient_name']]['quantity'] += list_meal_item['quantity']
    return list_meal

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



            





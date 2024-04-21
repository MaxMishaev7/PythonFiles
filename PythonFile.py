import os
from operator import itemgetter

def print_dict(dict):
    for key, value in dict.items():
        if not isinstance(value, list):
            print(key, value)
        else:
            print(key)
            for element in value:
                print(element)

def merge_files(folder):
    files = os.listdir(folder)
    print(os.listdir(folder))
    files_count = {}
    files_content = {}
    for file in files:
        file_path = os.path.join(folder, file)
        print(file_path)
        file_content = []
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.readlines()
            files_count[file] = len(file_content)
            files_content[file] = file_content
            print(file_content, len(file_content))
    sorted_files_count = sorted(files_count.items(), key=itemgetter(1))
    print(sorted_files_count)
    with open("strings.txt", 'w', encoding='utf-8') as f:
        for file in sorted_files_count:
            f.write(f'File: {file[0]}\n')
            f.write(f'Lines: {file[1]}\n')
            f.write('\n')
            for line in files_content[file[0]]:
                f.write(line)
            f.write('\n\n')



def get_cook_book(file_path):
    file_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        file_list = file.readlines()
    new_file_list = []
    for elem in file_list:
        new_file_list.append(elem.strip())
    cook_book = {}
    recipe_name = ''
    for i in range(len(new_file_list)):
        if i == 0 or new_file_list[i - 1] == '':
            recipe_name = new_file_list[i]
            cook_book[recipe_name] = []
        if new_file_list[i].isdigit():
            ingredient_count = int(new_file_list[i])
            ingredient_list = []
            for j in range(ingredient_count):
                ingredient = new_file_list[i + 1 + j].split(' | ')
                ingredient_list.append(
                    {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            cook_book[recipe_name] = ingredient_list
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count=1):
    print(dishes, '\n')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            print(f"\nЕсть такое блюдо: {dish}")
            for ingredient in cook_book[dish]:
                print(ingredient)
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': str(int(ingredient['quantity']) * person_count)
                    }
                else:
                    quantity = int(ingredient['quantity']) * person_count
                    shop_list_quantity = str(int(shop_list[ingredient['ingredient_name']]['quantity']) + quantity)
                    shop_list[ingredient['ingredient_name']]['quantity'] = shop_list_quantity
    return shop_list



cook_book = get_cook_book('recipes.txt')
# print(cook_book)
print_dict(cook_book)

shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 3)
print("\nСписок покупок:\n")
print_dict(shop_list)

print()
merge_files("txt")










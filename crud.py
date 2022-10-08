from datetime import datetime
import json
from json.decoder import JSONDecodeError
from setting import FILE_PATH

# data = [
#     {
#         'id': 1,
#         'name': 'product1',
#         'price': 100,
#         'created_at': '2022.10.08',
#         'update_time': '2022.10.08',
#         'description': 'green',
#         'is_active': True
#     }
# ]



def get_products():
    with open(FILE_PATH) as f:
        try:
            for a in json.load(f):
                b = f'''
                id: {a['id']}
                название: {a['name']}
                цена: {a['price']} $
                дата создания: {a['created_at']}
                дата обновления: {a['update_time']}
                описание: {a['description']}
                статус: {a['is_active']}
                '''
                print(b)
            return json.load(f)
        except JSONDecodeError:
            return []

def get_one_product(id):
    with open(FILE_PATH) as f:
        data = json.loads(f)
        product = [i for i in data if id == i['id']]
        if product:
            return product[0]
        else:
            return('Нет такого товара!')

def post_product():
    with open(FILE_PATH) as f:
        data = json.load(f)
        max_id = max([i['id'] for i in data])
        new_data = {
            'id': max_id + 1,
            'name': input('Введите имя товара: '),
            'price': int(input('Введите цену товара: ')),
            'created_at': datetime.now().strftime('%d.%m.%Y %H:%M'),
            'update_time': datetime.now().strftime('%d.%m.%Y %H:%M'),
            'description': input('Введите описания товара: '),
            'is_active': True
        }
        data.append(new_data)
    with open(FILE_PATH, 'w') as f:
            json_data = json.load(f)
    json_data.append(data)
    with open(FILE_PATH, 'w') as f:
            json.dump(json_data, f)
            return f'Вы добавили новый товар\n{new_data}'

def delete_product(id):
    with open(FILE_PATH) as f:
        data = json.load(f)
        delete_product = [i for i in data if i['id'] == id]
        if delete_product:
            data.remove(delete_product[0])
            json.dump(data, open(FILE_PATH, 'w'))
            return 'Успешно удален! '
        return 'Нет такого продукта! '

def update_product(id):
    with open(FILE_PATH) as f:
        data = json.load(f)
        update_product = [i for i in data if i['id'] == id]
        if update_product:
            index_item = data.index(update_product[0])
            if input('Хотите обновить имя? ') == 'Да':
                data[index_item]['name'] = input('Введите новое имя: ')
            if input('Хотите обновить цену? ') == 'Да':
                data[index_item]['price'] = int(input('Введите новую цену: '))       
            if input('Хотите обновить описание? ') == 'Да':
                data[index_item]['description'] = input('Опишите свой товар ')
            if input('Хотите обновить статус товара? ') == 'Да':
                data[index_item]['is_active'] = bool(input('True/False: '))
            data[index_item]['update_time'] = datetime.now().strftime('%d.%m.%Y %H:%M')
            json.dump(data, open(FILE_PATH, 'w'))
            return 'Удачно обновили'
        return 'Товар не найден'




def main():

    while True:
        try:
            print('Привет вот функционал: \n1 - получить все товары, \n2 - получить определенный товар, \n3 - создать товар, \n4 - удалить товар, \n5 - обновить товар, \n0 - выйти из программы ')
            method = input('Введи число: ')
            if method == '1':
                print(get_products())
            elif method == '2':
                id == int(input('Введи id товара'))
                print(get_one_product(id))
            elif method == '3':
                print(post_product())
            elif method == '4':
                id == int(input('Введите id товара, который хотите удалить '))
                print(delete_product(id))
            elif method == '5':
                id == int(input('Введите id товара, который хотите обновить '))
                print(update_product(id))
            elif method == '0':
                print('До новых встреч ')
                break
            else:
                print('Нет такого функционала ')
        except KeyboardInterrupt:
            print('До встречи')

main()
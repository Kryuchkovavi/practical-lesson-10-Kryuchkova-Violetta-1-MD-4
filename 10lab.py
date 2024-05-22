import json

def z1():
    with open('products.json', encoding='utf-8') as file:
        data = json.load(file)

    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])

        if product['available']:
            print("\nВ наличии\n")
        else:
            print("\nНет в наличии!\n")

def z2():
    product_name = input("Введите название продукта: ")
    product_price = float(input("Введите цену продукта: "))
    product_quantity = int(input("Введите количество продукта: "))

    try:
        with open('products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    new_product = {
        "название": product_name,
        "цена": product_price,
        "количество": product_quantity
    }

    data.append(new_product)

    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Содержимое файла products.json:")
    with open('products.json', 'r', encoding='utf-8') as file:
        print(file.read())

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    ru_en_dict = {}

    for line in lines:
        en_word, ru_translation = line.strip().split(' - ')
        if ru_translation in ru_en_dict:
            ru_en_dict[ru_translation].append(en_word)
        else:
            ru_en_dict[ru_translation] = [en_word]

    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for ru_word in sorted(ru_en_dict.keys()):
            en_words = ', '.join(sorted(ru_en_dict[ru_word]))
            file.write(f"{ru_word} - {en_words}\n")

z3()
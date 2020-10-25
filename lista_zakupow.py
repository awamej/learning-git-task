print('Lista zakupów')
lista_zakupow = {'piekarnia' : ['chleb', 'bułki', 'pączek'], 'warzywniak' : ['marchew', 'seler', 'rukola']}
for store_name,products in lista_zakupow.items():
    store_name_capitalize = store_name.capitalize()
    capitalized_products = []
    for i in products:
        capitalized_products.append(i.capitalize())
    products_to_print = ', '.join(capitalized_products)
    print("Idę do "+ store_name_capitalize +" i kupuję tam: " + products_to_print)
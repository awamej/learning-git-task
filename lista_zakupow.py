print('Lista zakupów')
lista_zakupow = {'piekarnia' : ['chleb', 'bułki', 'pączek'], 'warzywniak' : ['marchew', 'seler', 'rukola']}
for store_name,products in lista_zakupow.items():
    products_to_print = ', '.join(products)
    print("Idę do "+ store_name +" i kupuję tam: " + products_to_print)
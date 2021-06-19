name = str(input('\nWhat is your name: ')).title().strip()
cart = []
total = []


def trolley():
    print(f'\n{name}, you are purchasing the follow items:\n')
    for product in cart:
        for k, v in product.items():
            print(f" {k}: {str(v)} ", end="")
        print(f" = {product.get('valor') * product.get('unit')}")
    print(f'\nTotal to pay = {sum(total)}')


def product_details():
    question = True
    while question:
        product_name = str(input('Product name: ')).capitalize().strip()
        product_valor = float(input('What is the valor: ')).__round__()
        product_unit = int(input('Qtd: '))
        total.append(product_valor * product_unit)
        cart.append({'product': product_name, 'valor': product_valor, 'unit': product_unit})
        question = str(input('\nWould you like to add more products? Y or N: ')).capitalize() == "Y"
    trolley()
    return


product_details()

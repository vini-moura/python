# coding=<utf-8>

"""
COFFEE MACHINE
"""

moedas = [5, 10, 25, 50, 100]

CAFES = [
    {'expresso': {
        'ingredientes': {
            'agua': 50,
            'café': 18,
        },
        "preço": 1.5
    }
    },
    {'latte': {
        'ingredientes': {
            'agua': 200,
            'café': 24,
            'leite': 150
        },
        "preço": 2.5
    }
    },
    {'cappuccino': {
        'ingredientes': {
            'agua': 250,
            'café': 24,
            'leite': 100
        },
        "preço": 3.0
    },
    }
]

estoques = {
    'agua': 300,
    'café': 200,
    'leite': 100,
    'moedas': 0
}

# print(CAFES[1]["latte"]["ingredientes"]['café'])

pedido = input("Selecione uma bebida:(expresso/latte/cappuccino) ")

if pedido == "report":
    print(estoques)

# TODO fazer o report

def tem(usuario):
    """verifica se há recursos para o pedido"""
    if usuario == "expresso":
        if CAFES[0]["expresso"]['ingredientes']['agua'] <= estoques['agua'] and CAFES[0]["expresso"]['ingredientes'][
            'café'] <= estoques['café']:
            return True
        else:
            print('Reabasteça por favor')
            return False
    if usuario == "latte":
        if CAFES[1]["latte"]['ingredientes']['agua'] <= estoques['agua'] and CAFES[1]["latte"]['ingredientes'][
            'café'] <= estoques['café'] and CAFES[1]["latte"]['ingredientes']['leite'] <= estoques['leite']:
            return True
        else:
            print('Reabasteça por favor')
            return False
    if usuario == 'cappuccino':
        if CAFES[2]["cappuccino"]['ingredientes']['agua'] <= estoques['agua'] and \
                CAFES[2]["cappuccino"]['ingredientes']['café'] <= estoques['café'] and \
                CAFES[2]["cappuccino"]['ingredientes']['leite'] <= estoques['leite']:
            return True
        else:
            print('Reabasteça por favor')
            return False


podefazer = tem(pedido)


def pagamento(usuario):
    """verifica se o pagamento foi realizado"""
    a = int(input('Quantas moedas? '))
    coins = 0
    lista = []
    for i in range(a):
        lista.append(float(input('Qual o valor da moeda? ')))
        coins = sum(lista)
    if usuario == "expresso":
        total = CAFES[0]['expresso']['preço']
        if coins > total:
            return f"seu troco é {coins - total}"
        elif coins < total:
            return f"Por favor complete o valor com {total - coins}"
        else:
            return "Seu café está sendo feito"
    elif usuario == "latte":
        total = CAFES[1]['latte']['preço']
        if coins > total:
            return f"seu troco é {coins - total}"
        elif coins < total:
            return f"Por favor complete o valor com {total - coins}"
        else:
            return "Seu café está sendo feito"
    elif usuario == "cappuccino":
        total = CAFES[2]['cappuccino']['preço']
        if coins > total:
            return f"seu troco é {coins - total}"
        elif coins < total:
            return f"Por favor complete o valor com {total - coins}"
        else:
            return "Seu café está sendo feito\n\n\n\n\nAqui está"


print(pagamento(pedido))

# TODO a haburger

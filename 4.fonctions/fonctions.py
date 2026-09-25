def calcul_tva(price):
    print("Price computing...")
    return price * 1.27

print(calcul_tva(120))
print(calcul_tva(75))
print(calcul_tva(230))
print(calcul_tva(500))


def rectangle_area(width, eight):
    area = width * eight
    return area

def double(value):
    # print(value * 2)
    return value * 2

def hello():
    print("hello")

hello()
hello()
hello()
hello()

# Calculer un tarif de livraison à partir du poids, de la distance et d'une option express

def cout_poids(poids):
    cout = 0
    return cout

def cout_distance(distance):
    cout= 0
    return cout

def cout_express(option):
    cout = 0
    return cout

def cout_total(poids, distance, option):
    cout = cout_poids(poids) + cout_distance(distance) + cout_express(option)
    return cout

def imprimer_etiquette_livraison(poids, distance, option):
    cout = cout_total(poids, distance, option)
    # imprimer l'étiquette


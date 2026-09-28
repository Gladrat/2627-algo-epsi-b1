# Une fonction difficile à réutiliser

**Niveau :** intermédiaire  
**Format :** correction de conception

```python
discount = 0.10

def final_price(price):
    price = price * (1 - discount)
    print(price)


result = final_price(100)
print(result)
```

Deux problèmes empêchent cette fonction d'être facilement réutilisable :

1. une dépendance n'apparaît pas dans sa signature ;
2. le résultat du calcul n'est pas réellement renvoyé.

Réécrivez la fonction pour obtenir :

```python
final_price(price, discount)
```

puis ajoutez deux `assert`.

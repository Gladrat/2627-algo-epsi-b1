# Exercice — Limiter un volume

Écrivez une fonction :

```python
limit_volume(volume)
```

qui renvoie :

- 0 si **volume** est inférieur à 0 ;
- 100 s'il est supérieur à 100 ;
- la valeur elle-même sinon.

# Exercice difficile — Valider une date

On veut vérifier qu'une date donnée existe réellement.

Hypothèse : **year est un entier strictement positif**.

Rappels :

- janvier, mars, mai, juillet, août, octobre et décembre ont 31 jours ;
- avril, juin, septembre et novembre ont 30 jours ;
- février a 28 jours, ou 29 lors d'une année bissextile ;
- une année est bissextile si elle est divisible par 4, sauf les années divisibles par 100 qui ne le sont pas, à moins d'être aussi divisibles par 400.

Exemples :

- 29/02/2024 : valide ;
- 29/02/2023 : invalide ;
- 31/04/2025 : invalide ;
- 31/12/2025 : valide.

Décomposez le problème en fonctions. La fonction finale devra être :

```python
is_valid_date(day, month, year)
```

Ajoutez ensuite des tests avec `assert`.

# Exercice bonus - refactorisation

Reprendre le calcul d'heure de la partie 0 et montrer qu'une fonction évite la duplication.

```python
duration = 99999999

hours = duration // 3600
remaining = duration % 3600
minutes = remaining // 60
secondes = remaining % 60

print(hours, minutes, secondes)
```

Comment améliorer encore la fonction si l'on souhaite réutiliser le résultat au lieu de seulement l'afficher.

# Exercice bonus - refactorisation 2

1. réécrivez le programme avec au moins trois fonctions ;
2. ajoutez un test par fonction.

```python
quantity = 4
unit_price = 25
is_member = True
express = True

subtotal = quantity * unit_price

if is_member:
    subtotal = subtotal * 0.90

shipping = 5
if express:
    shipping = shipping + 8

total = subtotal + shipping

print(total)
```
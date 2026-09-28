> 🧠 **À retenir :** une condition produit un booléen et permet au programme de choisir un chemin d'exécution.

# Concepts clés

- Une comparaison produit `True` ou `False`.
- `if` permet d'exécuter un bloc seulement si une condition est vraie.
- `elif` ajoute des cas alternatifs ; `else` traite le cas restant.
- Dans une chaîne `if / elif / else`, **une seule branche** est exécutée.
- Plusieurs `if` indépendants représentent plusieurs décisions successives.
- Les opérateurs booléens permettent de combiner les règles : `and`, `or`, `not`.
- L'**ordre des cas** compte lorsque plusieurs règles peuvent s'appliquer.
- Une règle peut être écrite avec des conditions imbriquées ou une condition composée.
- Les **cas limites** doivent être testés explicitement.

# Syntaxe essentielle

Les opérateurs de comparaison produisent un booléen :

```python
a == b    # égal
a != b    # différent
a < b
a <= b
a > b
a >= b
```

Les opérateurs booléens permettent de combiner des conditions :

- `a and b` est vrai seulement si les deux conditions sont vraies ;
- `a or b` est vrai si au moins une des deux est vraie ;
- `not a` inverse le booléen.

```python
if condition:
    ...

elif autre_condition:
    ...

else:
    ...
```

# Réflexes

- traduire chaque règle métier en condition simple ;
- nommer les sous-conditions lorsqu'une expression devient difficile à lire ;
- tester les valeurs situées exactement sur les seuils ;
- vérifier si deux décisions doivent être indépendantes ou exclusives.

# Pièges à éviter

- utiliser `elif` alors que les deux tests doivent pouvoir s'exécuter ;
- inverser `and` et `or` ;
- oublier qu'une première condition peut modifier l'état utilisé par la suivante ;
- écrire les cas dans un ordre qui rend une règle plus précise inaccessible.

> ✅ **Je sais faire si :** je peux transformer des règles en booléens, choisir entre `if`, `elif` et plusieurs `if`, puis vérifier les cas frontières.

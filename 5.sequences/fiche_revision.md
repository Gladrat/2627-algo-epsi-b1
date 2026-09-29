> 🧠 **À retenir :** une séquence contient plusieurs valeurs dans un ordre ; on peut parcourir ses valeurs, ses indices ou construire une nouvelle séquence.
> 

# Concepts clés

- Une liste est une collection **ordonnée**.
- Un **indice** indique « où ? » ; une **valeur** indique « quoi ? ».
- Les indices positifs commencent à 0.
- `len(sequence)` donne le nombre d'éléments.
- Parcourir les **valeurs** est préférable si la position n'est pas utile.
- Parcourir les **indices** est utile pour connaître ou modifier une position.
- `.append(value)` ajoute un élément à la fin d'une liste.
- Un parcours peut **transformer** ou **filtrer** une collection pour construire un résultat.
- Une chaîne est aussi une séquence, mais elle est **immuable**.
- Une grille peut être représentée par une liste de listes et parcourue avec deux boucles.
- Avant un accès par indice, il faut respecter les bornes.

# Syntaxe essentielle

```python
values = [10, 20, 30]

values[0]       # premier élément
len(values)     # nombre d'éléments
```

```python
for value in values:
    ...
```

```python
for index in range(len(values)):
    print(index, values[index])
```

```python
result = []
result.append(value)
```

```python
text = "ALGO"
text[0]         # "A"

grid[row][column]
```

Une chaîne peut être lue comme une séquence, mais ses caractères ne peuvent pas être modifiés directement.

# Fenêtre sur le C

Un tableau C déclaré avec une taille fixe est plus contraint qu'une liste Python, qui peut grandir dynamiquement. Les principes de parcours restent cependant comparables.

# Réflexes

- choisir parcours par valeur ou par indice selon le besoin ;
- construire progressivement une liste ou une chaîne résultat ;
- pour une grille, raisonner en ligne puis colonne ;
- vérifier les bornes avant d'accéder à une position calculée.

# Pièges à éviter

- accéder à `values[len(values)]` ;
- modifier une chaîne caractère par caractère comme une liste ;
- confondre indice et valeur ;
- oublier les bords et coins d'une grille.

> ✅ **Je sais faire si :** je peux parcourir listes et chaînes, construire une nouvelle collection, utiliser les indices et manipuler une grille sans sortir de ses limites.
>
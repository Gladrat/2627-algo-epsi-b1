# Exercice facile — Inverser un mot

Écrivez une fonction :

```python
reverse_text(text)
```

qui renvoie le texte inversé.

Contraintes :

- construire le résultat avec une boucle ;
- ne pas utiliser de raccourci Python qui inverse directement le texte.

Exemple :

```
ALGO → OGLA
```

# Palier intermédiaire — Parcourir une grille

Sur la grille suivante :

```python
grid = [
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
]
```

Écrire deux fonctions :

```python
count_all(grid)
count_row(grid, row)
```

La première compte tous les **1** de la grille.  

La seconde compte les **1** d'une ligne donnée.

# Exercice difficile — Compter les mines voisines

On représente une grille de démineur avec :

- **1** : une mine ;
- **0** : pas de mine.

```python
grid = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
]
```

Écrivez une fonction :

```python
count_neighbors(grid, row, column)
```

qui compte le nombre de mines dans les huit cases autour de la position donnée.

La case centrale elle-même ne doit pas être comptée.

L'algorithme doit fonctionner aussi sur les bords et dans les coins.

Hypothèse : la grille est **rectangulaire et non vide**.
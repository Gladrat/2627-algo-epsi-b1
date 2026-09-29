# Une grille rectangulaire mal parcourue

**Niveau :** intermédiaire  
**Format :** correction de bug

```python
grid = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
]

for row in range(len(grid)):
    for column in range(len(grid)):
        print(grid[row][column])
```

Le programme ne parcourt pas toutes les cases.

1. Combien de lignes possède la grille ?
2. Combien de colonnes possède chaque ligne ?
3. Quelle expression est incorrecte dans la boucle intérieure ?
4. Corrigez le parcours pour qu'il fonctionne aussi sur une grille rectangulaire.

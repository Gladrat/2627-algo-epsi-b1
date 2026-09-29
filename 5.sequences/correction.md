# Palier intermédiaire — Parcourir une grille

Parcourir :
- chaque ligne
- chaque valeur de cette ligne

```ascii
i = 0
pour chaque ligne
  pour chaque valeur de la ligne
    si valeur == 1
      on incrément count de 1
```

# Exercice difficile — Compter les mines voisines

|   | 0        | 1        | 2        |
|---|----------|----------|----------|
| 0 | (-1, -1) | (-1, 0)  | (-1, +1) |
| 1 | (0, -1)  | X        | (0, +1)  |
| 2 | (+1, -1) | (+1, 0)  | (+1, +1) |

## Vérifier les limites avant l'accès

Calcul de l'endroit (voisin) où on veut se déplacer :

```ascii
neighbor_row = row + row_offset
neighbor_col = col + col_offset
```

Les conditions qui vérifient les limites :

```ascii
0 <= neighbor_row <= row_count
0 <= neighbor_col <= col_count
```

Cette vérification doit évidemment avoir lieu AVANT l'accès à la grille.
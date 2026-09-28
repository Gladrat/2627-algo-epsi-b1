> 🧠 **À retenir :** une fonction donne un nom à un sous-problème et permet de le résoudre, le tester et le réutiliser séparément.

# Concepts clés

- Une fonction est définie avec `def`.
- Les **paramètres** décrivent les informations dont elle a besoin.
- `return` transmet un résultat au code appelant.
- `print` affiche une valeur mais ne la renvoie pas.
- Une fonction sans `return` explicite renvoie `None`.
- Les variables créées dans une fonction servent au calcul local de cette fonction.
- Les dépendances importantes doivent être rendues aussi explicites que possible.
- Décomposer un problème consiste à identifier des sous-problèmes ayant chacun une responsabilité claire.
- Le **contrat** d'une fonction précise ses entrées, sa sortie et ses cas invalides.
- `assert` permet de vérifier simplement un résultat attendu.
- Un `return` termine immédiatement l'appel courant.

# Syntaxe essentielle

```python
def rectangle_area(width, height):
    area = width * height
    return area

result = rectangle_area(4, 3)
```

La définition décrit la fonction ; l'appel `rectangle_area(4, 3)` l'exécute avec des valeurs concrètes et récupère ici son résultat.

```python
assert rectangle_area(4, 3) == 12
```

# Réflexes

- demander : « quelles petites fonctions puis-je tester séparément ? » ;
- définir clairement ce qu'une fonction reçoit et renvoie ;
- tester le cas nominal et les cas limites ;
- préférer plusieurs responsabilités explicites à une fonction monolithique.

# Pièges à éviter

- confondre `print` et `return` ;
- utiliser une dépendance cachée sans comprendre d'où elle vient ;
- oublier qu'un `return` arrête la fonction ;
- décomposer artificiellement sans que les fonctions correspondent à de vrais sous-problèmes.

> ✅ **Je sais faire si :** je peux définir le contrat d'une fonction, la tester, expliquer son résultat et découper un problème plus grand en fonctions cohérentes.

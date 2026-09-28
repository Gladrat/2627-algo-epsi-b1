> 🧠 **À retenir :** une boucle répète un traitement ; il faut toujours savoir ce qui varie et ce qui doit être mémorisé.

# Concepts clés

- `for` convient lorsqu'on sait quels éléments ou quelles valeurs parcourir.
- `range(start, stop)` exclut la borne `stop`.
- Un **compteur** compte des événements.
- Un **accumulateur** conserve une somme ou un résultat construit progressivement.
- `while` convient lorsque le nombre d'itérations n'est pas connu à l'avance.
- Pour comprendre un `while`, identifier :
  1. l'état initial ;
  2. la condition de continuation ;
  3. la manière dont l'état évolue.
- `break` interrompt uniquement la boucle la plus proche.
- Des boucles imbriquées permettent de parcourir plusieurs dimensions ou combinaisons.

# Syntaxe essentielle

```python
range(stop)                # de 0 à stop exclu
range(start, stop)         # de start à stop exclu
range(start, stop, step)   # même principe avec un pas

for value in range(1, 6):
    ...

for value in range(0, 10, 2):
    ...
```

La borne `stop` n'est jamais incluse.

```python
while condition:
    ...
```

```python
break
```

# Réflexes

- faire une trace de quelques tours ;
- vérifier que l'état d'un `while` évolue vers sa condition d'arrêt ;
- distinguer la valeur du tour courant de l'état accumulé ;
- dans des boucles imbriquées, identifier précisément quelle boucle contrôle quoi.

# Pièges à éviter

- boucle infinie ;
- mauvais nombre d'itérations à cause des bornes de `range` ;
- remplacer un accumulateur au lieu de l'incrémenter ;
- croire qu'un `break` sort de toutes les boucles.

> ✅ **Je sais faire si :** je peux choisir entre `for` et `while`, construire compteur et accumulateur, expliquer la terminaison d'une boucle et suivre des boucles imbriquées.

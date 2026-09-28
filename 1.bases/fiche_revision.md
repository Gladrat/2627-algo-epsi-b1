> 🧠 **À retenir :** une variable représente une valeur utile à un instant donné de l'exécution.

# Concepts clés

- L'affectation `=` signifie : **évaluer la droite puis associer le résultat au nom de gauche**.
- Une variable peut changer de valeur au cours du programme : elle représente un **état**.
- Une **expression** combine des valeurs, variables et opérateurs.
- Les parenthèses permettent de rendre l'ordre d'évaluation explicite.
- Il faut distinguer **valeur, type et représentation** : `42` et `"42"` ne sont pas équivalents.
- Une saisie avec `input()` est du texte et doit parfois être convertie.
- Des variables intermédiaires bien nommées rendent le raisonnement plus lisible et plus facile à vérifier.

# Syntaxe essentielle

Les opérateurs arithmétiques vus dans le cours :

- `+` : addition ;
- `-` : soustraction ;
- `*` : multiplication ;
- `/` : division ;
- `//` : quotient entier ;
- `%` : reste de la division ;
- `**` : puissance.

Les multiplications et divisions sont évaluées avant les additions et soustractions. Les parenthèses permettent de rendre l'ordre voulu explicite.

```python
10 / 3      # division
10 // 3     # 3
10 % 3      # 1
2 ** 3      # 8

int("18")           # convertir une chaîne en entier
float("12.50")      # convertir une chaîne en nombre décimal
str(18)             # convertir un nombre en chaîne

raw_age = input("Âge : ")
age = int(raw_age)

type(age)            # inspecter le type d'une valeur
```

# Typage

- Python est **dynamiquement typé**.
- La comparaison avec C montre qu'un autre langage peut rendre le type d'une variable explicite dès sa déclaration.
- L'algorithme reste conceptuellement indépendant de cette différence de syntaxe.

# Réflexes

- tracer chaque réaffectation ;
- utiliser les valeurs **courantes** des variables ;
- décomposer une grosse expression en étapes nommées lorsque cela clarifie le calcul.

# Pièges à éviter

- lire `score = score + 5` comme une égalité mathématique ;
- confondre chaîne et nombre ;
- oublier de convertir une entrée avant un calcul numérique.

> ✅ **Je sais faire si :** je peux suivre l'évolution de variables, évaluer une expression, convertir une donnée et expliquer pourquoi deux représentations visuellement proches peuvent avoir des types différents.

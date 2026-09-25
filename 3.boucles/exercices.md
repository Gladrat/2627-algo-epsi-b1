# Exercice facile — Sauvegardes automatiques

Un programme crée **12 versions** successives d'un projet.

Règle :

- une sauvegarde incrémentale dure **2 secondes** ;
- toutes les **4 versions**, le programme effectue à la place une sauvegarde complète qui dure **8 secondes**.

Écrivez un programme qui :

1. affiche pour chaque version s'il s'agit d'une sauvegarde incrémentale ou complète ;
2. calcule la durée totale des 12 sauvegardes ;
3. compte le nombre de sauvegardes complètes.

# Exercice difficile — Téléchargement par blocs

Un programme télécharge un fichier de **850 Mo**.

À chaque seconde :

- s'il reste plus de **300 Mo**, il télécharge **120 Mo** ;
- sinon, il télécharge **70 Mo** ;
- lors de la dernière seconde, il ne doit jamais télécharger plus que ce qu'il reste.

Écrivez un programme qui :

1. affiche après chaque seconde la quantité restante ;
2. compte le nombre de secondes nécessaires ;
3. affiche la quantité téléchargée pendant la dernière seconde.

Avant de coder, identifiez les états qui doivent évoluer pendant la boucle.

# Lecture de code — 5 min

```python
value = 3
total = 0

while value < 10:
    total = total + value
    value = value + 2

print(value)
print(total)
```

Sans exécuter :

1. combien de fois la boucle s'exécute-t-elle ?
2. quelles valeurs successives prend **value** dans le corps de boucle ?
3. quelles sont les deux valeurs affichées à la fin ?
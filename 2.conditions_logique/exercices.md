# Exercice facile — Consigne automatique

Un casier s'ouvre uniquement si :

- le code PIN est correct ;
- le casier n'est pas bloqué.

Données :

```python
entered_pin = "3812"
expected_pin = "3812"
is_blocked = False
```

1. Construisez un booléen **can_open**.
2. Affichez « ouverture » ou « accès refusé ».
3. Testez au moins trois combinaisons différentes.

# Exercice difficile — Tarif d'un parc

Règles :

- moins de 6 ans : gratuit ;
- de 6 à 17 ans : 12 € ;
- à partir de 18 ans : 20 € ;
- un étudiant majeur paie 16 € ;
- le week-end ajoute 2 € à tous les tarifs non gratuits.

On donne :

```python
age = 21
is_student = True
is_weekend = True
```

Écrivez l'algorithme puis le programme qui calcule le prix.

Avant de coder, listez explicitement les cas.
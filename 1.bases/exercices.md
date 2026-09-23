# Exercice facile — Score d'arcade

Le score d'un joueur sur un jeu vidéo se compose de :

- 120 points de base ;
- un multiplicateur de 1,5 ;
- un bonus final de 40 points.

Avant de coder :

1. nommez les données de départ ;
2. séparez les étapes intermédiaires du calcul ;
3. faites une petite trace avec les valeurs données.

Traduisez ensuite votre raisonnement en Python.

# Exercice difficile — Décomposer une couleur

Une couleur **RGB 24 bits** peut être regroupée dans un seul entier : les trois composantes rouge, verte et bleue sont alors « empaquetées » dans la même valeur.

<aside>
🖼️

**Contexte réel :** ce type de représentation apparaît dans des formats, protocoles ou traitements graphiques de bas niveau. Les bibliothèques d'image haut niveau fournissent souvent directement les composantes RGB, mais le principe reste utile pour comprendre comment une couleur peut être représentée en mémoire.

</aside>

On utilise ici la formule :

```
couleur = rouge × 65536 + vert × 256 + bleu
```

Chaque composante est comprise entre 0 et 255.

On donne :

```python
color = 16744448
```

Retrouvez séparément les composantes **rouge**, **verte** et **bleue**, uniquement avec **//** et **%**.

Indice : commencez par la composante rouge.
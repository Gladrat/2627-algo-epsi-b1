12x sauvegarde

save incrémentale → 2s
complète → 8s / 4 save

2 2 2 8 2 2 2 8 2 2 2 8

incrémentale : 2
incrémentale : 2
incrémentale : 2
complète     : 8
incrémentale : 2
incrémentale : 2
incrémentale : 2
complète     : 8
incrémentale : 2
incrémentale : 2
incrémentale : 2
complète     : 8

42 / 3

---

A chaque tour (tant qu'il reste des trucs à télécharger) :

1. choisir la taille du bloc selon la quantité restante
2. si ce bloc est plus grand que ce qu'il reste → le réduire
3. soustraire le bloc à ce qu'il reste
4. augmenter le temps de téléchargement d'une seconde
5. afficher l'état

Les états :

- remaining : quantité restante à télécharger
- seconds : nb de secondes écoulées
- chunk : quantité téléchargée pendant la seconde courante


```ascii
tant que remaining est inférieur à 0:
  si remaining est supérieur à 300:
    je vais télécharger par morceaux de 120
  sinon:
    je vais télécharger par morceaux de 70

  si chunk > remaining:
    chunk = remaining
  
  remaining = remaining - chunk

  seconds = seconds + 1

  afficher seconds
  afficher remainings

afficher seconds
```
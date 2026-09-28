# Une qualité impossible à atteindre

**Niveau :** intermédiaire  
**Format :** correction de bug

> **Contexte :** la latence est le délai de réponse d'un service, mesuré ici en millisecondes (ms). Plus elle est faible, plus le service répond rapidement. Pour cet exercice, il suffit d'appliquer les seuils donnés.

On veut classer une latence :

- jusqu'à 50 ms : `"excellent"` ;
- de 51 à 100 ms : `"correct"` ;
- au-delà : `"lent"`.

Le programme contient un problème :

```python
latency = 35

if latency <= 100:
    quality = "correct"
elif latency <= 50:
    quality = "excellent"
else:
    quality = "lent"

print(quality)
```

1. Quel résultat obtient-on pour 35 ms ?
2. Pourquoi `"excellent"` ne peut-il jamais être atteint ?
3. Corrigez l'ordre des cas.
4. Testez mentalement 35, 80 et 140 ms.

# Refactoriser un coût de calcul cloud

**Niveau :** avancé  
**Format :** refactorisation

> **Contexte :** on modélise ici un service de calcul facturé selon sa durée d'utilisation. Le mode prioritaire augmente le prix. Un **cache chaud** signifie simplement que l'environnement nécessaire au calcul est déjà prêt ; sinon, un coût de démarrage de 2 € est ajouté. Aucune connaissance du cloud ou des caches n'est nécessaire pour résoudre l'exercice.

Le programme fonctionne, mais mélange plusieurs responsabilités :

```python
minutes = 85
rate_per_minute = 0.04
is_priority = True
has_warm_cache = False

cost = minutes * rate_per_minute

if is_priority:
    cost = cost * 1.5

startup_cost = 0
if not has_warm_cache:
    startup_cost = 2

total = cost + startup_cost
print(total)
```

1. Identifiez les sous-problèmes.
2. Proposez les signatures de fonctions avant de coder.
3. Réécrivez le programme avec au moins trois fonctions courtes.
4. Ajoutez au moins un test par fonction.
